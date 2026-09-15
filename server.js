/**
 * Phoenix Chems — Backend Server
 * Node.js + Express + SQLite
 */
const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const path    = require('path');
const fs      = require('fs');
const crypto  = require('crypto');

const app  = express();
const PORT = process.env.PORT || 3000;
const DB_PATH = path.join(__dirname, 'database', 'phoenixchems.db');

// ── Middleware ────────────────────────────────────────────────────────────────
app.use(express.json({ limit: '1mb' }));
app.use(express.urlencoded({ extended: true }));

// Security headers
app.use(function(req, res, next) {
    res.setHeader('X-Content-Type-Options', 'nosniff');
    res.setHeader('X-Frame-Options', 'SAMEORIGIN');
    res.setHeader('X-XSS-Protection', '1; mode=block');
    res.setHeader('Referrer-Policy', 'strict-origin-when-cross-origin');
    next();
});

// Cache static assets aggressively (images 7 days, fonts 30 days)
app.use('/assets', express.static(path.join(__dirname, 'standalone-preview', 'assets'), {
    maxAge: '7d',
    etag: true,
    lastModified: true,
    setHeaders: function(res, filePath) {
        if (/\.(jpg|jpeg|png|gif|webp|svg|ico)$/i.test(filePath)) {
            res.setHeader('Cache-Control', 'public, max-age=604800, immutable');
        }
        if (/\.(woff|woff2|ttf|eot)$/i.test(filePath)) {
            res.setHeader('Cache-Control', 'public, max-age=2592000, immutable');
        }
    }
}));

// Serve static HTML
app.use(express.static(path.join(__dirname, 'standalone-preview'), { maxAge: '10m', etag: true }));

// ── Database ──────────────────────────────────────────────────────────────────
const dbDir = path.dirname(DB_PATH);
if (!fs.existsSync(dbDir)) fs.mkdirSync(dbDir, { recursive: true });

const db = new sqlite3.Database(DB_PATH, function(err) {
    if (err) { console.error('DB error:', err.message); return; }
    console.log('Connected to database:', DB_PATH);
    db.serialize(function() {
        db.run(`CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL, email TEXT NOT NULL,
            address TEXT, country TEXT, notes TEXT,
            items_json TEXT NOT NULL,
            subtotal REAL NOT NULL, shipping REAL NOT NULL DEFAULT 0, total REAL NOT NULL,
            status TEXT NOT NULL DEFAULT 'pending_payment',
            nowpay_id TEXT, paid_at TEXT,
            created_at TEXT DEFAULT (datetime('now')),
            updated_at TEXT DEFAULT (datetime('now'))
        )`);
        db.run(`CREATE TABLE IF NOT EXISTS subscribers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            source TEXT DEFAULT 'popup',
            created_at TEXT DEFAULT (datetime('now'))
        )`);
        db.run(`CREATE TABLE IF NOT EXISTS analytics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event TEXT NOT NULL, product_id INTEGER,
            meta TEXT, ip_hash TEXT,
            created_at TEXT DEFAULT (datetime('now'))
        )`);
        db.run(`CREATE INDEX IF NOT EXISTS idx_orders_email ON orders(email)`);
        db.run(`CREATE INDEX IF NOT EXISTS idx_orders_status ON orders(status)`);
        console.log('Database tables ready');
    });
});

// ── API ───────────────────────────────────────────────────────────────────────

// Create order
app.post('/api/orders', function(req, res) {
    var b = req.body;
    if (!b.order_id || !b.name || !b.email || !b.total) return res.status(400).json({ error: 'Missing fields' });
    var orderId  = String(b.order_id).replace(/[^A-Z0-9\-]/g,'').slice(0,30);
    var name     = String(b.name).slice(0,120);
    var email    = String(b.email).toLowerCase().slice(0,200);
    var address  = String(b.address||'').slice(0,300);
    var country  = String(b.country||'').slice(0,80);
    var notes    = String(b.notes||'').slice(0,500);
    var items    = JSON.stringify(b.items||[]);
    var subtotal = parseFloat(b.subtotal)||0;
    var shipping = parseFloat(b.shipping)||0;
    var total    = parseFloat(b.total)||0;
    db.run(`INSERT OR IGNORE INTO orders (order_id,name,email,address,country,notes,items_json,subtotal,shipping,total) VALUES (?,?,?,?,?,?,?,?,?,?)`,
        [orderId,name,email,address,country,notes,items,subtotal,shipping,total],
        function(err) {
            if (err) return res.status(500).json({ error: 'Database error' });
            console.log('New order:', orderId, email, '$'+total);
            res.json({ success: true, order_id: orderId });
        });
});

// Get order status
app.get('/api/orders/:id', function(req, res) {
    var id = String(req.params.id).replace(/[^A-Z0-9\-]/g,'').slice(0,30);
    db.get('SELECT order_id,name,email,country,subtotal,shipping,total,status,created_at,paid_at FROM orders WHERE order_id=?',
        [id], function(err, row) {
            if (err) return res.status(500).json({ error: 'Database error' });
            if (!row) return res.status(404).json({ error: 'Order not found' });
            res.json(row);
        });
});

// Email subscribe
app.post('/api/subscribe', function(req, res) {
    var email = String(req.body.email||'').toLowerCase().trim().slice(0,200);
    if (!email || !email.includes('@')) return res.status(400).json({ error: 'Invalid email' });
    db.run('INSERT OR IGNORE INTO subscribers (email,source) VALUES (?,?)',
        [email, req.body.source||'popup'], function(err) {
            if (err) return res.status(500).json({ error: 'Database error' });
            res.json({ success: true });
        });
});

// Analytics event
app.post('/api/analytics', function(req, res) {
    var event = String(req.body.event||'').slice(0,60);
    var pid   = parseInt(req.body.product_id)||null;
    var meta  = req.body.meta ? JSON.stringify(req.body.meta).slice(0,500) : null;
    var ip    = req.headers['x-forwarded-for']||req.connection.remoteAddress||'';
    var hash  = crypto.createHash('sha256').update(ip+'phxsalt2026').digest('hex').slice(0,16);
    db.run('INSERT INTO analytics (event,product_id,meta,ip_hash) VALUES (?,?,?,?)',
        [event,pid,meta,hash], function() { res.json({ ok:true }); });
});

// NOWPayments Webhook IPN
app.post('/api/nowpayments-webhook', function(req, res) {
    var b = req.body;
    var orderId = String(b.order_id||'').replace(/[^A-Z0-9\-]/g,'').slice(0,30);
    var nowStatus = String(b.payment_status||'');
    var nowpayId  = String(b.payment_id||'').slice(0,60);
    var statusMap = { waiting:'pending_payment', confirming:'payment_confirming',
        confirmed:'payment_confirmed', sending:'fulfillment',
        finished:'paid', failed:'failed', expired:'expired', refunded:'refunded' };
    var ourStatus = statusMap[nowStatus] || nowStatus;
    var paidAt = ourStatus === 'paid' ? "datetime('now')" : "paid_at";
    db.run(`UPDATE orders SET status=?, nowpay_id=?, paid_at=CASE WHEN ?='paid' THEN datetime('now') ELSE paid_at END, updated_at=datetime('now') WHERE order_id=?`,
        [ourStatus, nowpayId, ourStatus, orderId], function(err) {
            if (err) return res.status(500).json({ error: 'DB error' });
            console.log('Webhook:', orderId, '->', ourStatus);
            res.json({ ok: true });
        });
});

// Admin orders (requires ADMIN_KEY env var)
app.get('/api/admin/orders', function(req, res) {
    if ((req.headers['x-admin-key']||req.query.key) !== process.env.ADMIN_KEY) return res.status(401).json({ error:'Unauthorized' });
    db.all('SELECT * FROM orders ORDER BY created_at DESC LIMIT 500', function(err,rows) {
        if (err) return res.status(500).json({ error: err.message });
        res.json({ orders: rows, count: rows.length });
    });
});

// Admin subscribers
app.get('/api/admin/subscribers', function(req, res) {
    if ((req.headers['x-admin-key']||req.query.key) !== process.env.ADMIN_KEY) return res.status(401).json({ error:'Unauthorized' });
    db.all('SELECT email,source,created_at FROM subscribers ORDER BY created_at DESC', function(err,rows) {
        if (err) return res.status(500).json({ error: err.message });
        res.json({ subscribers: rows, count: rows.length });
    });
});

// Health check for Render
app.get('/health', function(req, res) {
    res.json({ status: 'ok', time: new Date().toISOString(), version: '2.0.0' });
});

// SPA fallback
app.get('*', function(req, res) {
    res.sendFile(path.join(__dirname, 'standalone-preview', 'index.html'));
});

app.listen(PORT, function() {
    console.log('Phoenix Chems server started on port', PORT);
});

module.exports = app;
