# Phoenics Peptide (`phoenicspeptide.com`) — Platform Master Repository

## 🧬 Project Overview
**Phoenics Peptide** is a specialized international research peptide synthesis and analytical sales gateway engineered for university laboratories, private biotech firms, and clinical research institutions worldwide.

Target Geographic Coverage:
- **North America:** United States, Canada
- **Europe:** United Kingdom, Germany, France, Switzerland, Netherlands, Scandinavia
- **Africa:** Regional Cargo Hubs (Nigeria, South Africa, Kenya, Egypt, Ghana)
- **Asia-Pacific:** Japan, Singapore, South Korea, UAE, India

---

## 📁 Repository Directory Structure

```
phoenicspeptide/
├── brand/
│   ├── logo.svg              # Primary brand vector logo
│   ├── logo-white.svg        # Dark mode inverted vector logo
│   ├── logo.jpg              # High-res master insignia emblem
│   └── brand-guide.md        # Typography, colors, and compliance rules
│
├── phoenics-theme/           # Custom WordPress & WooCommerce Theme
│   ├── style.css             # Theme header & root design variables
│   ├── functions.php         # Theme setup, WooCommerce hooks & asset enqueues
│   ├── header.php            # Announcement ticker, multi-currency switcher & mega-menu
│   ├── footer.php            # Compliance disclaimer, global hubs & payment badges
│   ├── front-page.php        # High-impact biotech homepage template
│   ├── page-research.php     # HPLC/MS protocols & reconstitution laboratory guide
│   ├── page-track-order.php  # Public tracking portal template
│   ├── woocommerce.php       # WooCommerce layout wrapper
│   └── assets/
│       ├── css/main.css      # Theme core CSS
│       ├── css/woocommerce.css # Shop, catalog & product styles
│       ├── js/main.js        # Dynamic currency converter & mobile navigation
│       └── images/           # Brand image assets
│
├── phoenics-shipping/        # Proprietary Shipping & Cold-Chain Tracking Plugin
│   ├── phoenics-shipping.php # Main plugin bootstrap & order status registrations
│   ├── includes/
│   │   ├── order-manager.php # Tracking metabox, carrier URLs & AJAX lookup API
│   │   └── tracking-emails.php # Automated dispatch email triggers
│   ├── admin/
│   │   └── shipping-dashboard.php # Fulfillment queue & tracking assignment console
│   ├── templates/
│   │   └── tracking-page.php # Frontend live satellite tracking interface
│   └── assets/
│       ├── css/tracking.css  # Timeline, temperature gauge & telemetry card styles
│       └── js/tracking.js    # Asynchronous tracking lookup script
│
├── setup/                    # Data & Gateway Deployment Configurations
│   ├── products.csv          # Complete 18-product WooCommerce catalog with 3-image SVG sets
│   ├── generate_all_product_assets.py # Vector SVG generator for 54 custom product perspectives
│   ├── update_products_csv.py # Automated gallery sync tool
│   ├── categories.json       # Product taxonomy & scientific fields
│   ├── shipping-zones.json   # Multi-carrier zone rates & cold-chain fee rules
│   ├── btcpay-server-setup.md # Personal Bitcoin/Lightning direct wallet guide (0% fee)
│   ├── stripe-setup.md       # Stripe Visa/Mastercard/Apple Pay 3D-Secure setup
│   ├── hosting-kinsta-setup.md # High-performance Google Cloud / Kinsta deployment
│   └── plugin-list.md        # Complete plugins ecosystem guide
│
├── emails/                   # Transactional HTML Email Templates
│   ├── order-confirmed.html  # Immediate purchase confirmation
│   ├── order-shipped.html    # Carrier AWB dispatch notice
│   └── delivered.html        # Final delivery & laboratory storage protocol
│
└── standalone-preview/       # Interactive Browser Preview Platform
    ├── index.html            # Standalone storefront with live cart, USD/EUR toggle & tracking
    └── assets/images/products/ # 54 unique vector SVGs (Vial, HPLC CoA, Cold-Chain Pack)
```

---

## 🚀 Quick Start & Deployment Instructions

### 1. WordPress Theme Installation
1. Zip the `phoenics-theme/` directory into `phoenics-theme.zip`.
2. In WordPress Admin: **Appearance > Themes > Add New > Upload Theme**.
3. Activate **Phoenics Peptide Luxury Biotech Theme**.

### 2. Shipping Plugin Installation
1. Zip the `phoenics-shipping/` directory into `phoenics-shipping.zip`.
2. In WordPress Admin: **Plugins > Add New > Upload Plugin**.
3. Activate **Phoenics Global Shipping & Cold-Chain Tracking**.
4. Create a WordPress Page titled `Track Order` with slug `track-order`, assign the template **Order Tracking Portal** or insert shortcode `[phoenics_order_tracking]`.

### 3. Product Catalog Import
1. In WordPress Admin: **WooCommerce > Products > Import**.
2. Upload `setup/products.csv`.
3. Map fields (WooCommerce automatically auto-maps standard headers).
4. Click **Run the Importer** to instantly populate all 20 research compounds with size variants, package tiers, CAS numbers, and purity ratings!

### 4. Configure Payment Gateways
- Follow `setup/stripe-setup.md` for credit cards.
- Follow `setup/btcpay-server-setup.md` for personal Bitcoin, Lightning & USDT payments.
