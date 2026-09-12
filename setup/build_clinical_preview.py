import os

content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Phoenics Peptide — Clinical Research & Analytical Gateway</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Montserrat:wght@600;700;800;900&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../phoenics-theme/style.css">
    <link rel="stylesheet" href="../phoenics-theme/assets/css/main.css">
    <link rel="stylesheet" href="../phoenics-theme/assets/css/woocommerce.css">
    <link rel="stylesheet" href="../phoenics-shipping/assets/css/tracking.css">
    <style>
        /* ==========================================================================
           CLINICAL MEDICAL & WORDPRESS E-COMMERCE THEME (WHITE / NAVY / SAPPHIRE)
           ========================================================================== */
        :root {
            --bg-page: #FFFFFF;
            --bg-subtle: #F8FAFC;
            --bg-card: #FFFFFF;
            --border-subtle: #E2E8F0;
            --border-focus: #2563EB;
            --text-heading: #0F172A;
            --text-body: #334155;
            --text-muted: #64748B;
            --color-primary: #2563EB;
            --color-primary-dark: #1D4ED8;
            --color-primary-light: #EFF6FF;
            --color-emerald: #059669;
            --color-emerald-light: #ECFDF5;
            --color-amber: #D97706;
            --color-amber-light: #FEF3C7;
            --color-crimson: #DC2626;
            --color-crimson-light: #FEE2E2;
            --shadow-sm: 0 1px 3px rgba(0,0,0,0.06);
            --shadow-md: 0 4px 20px rgba(0,0,0,0.06);
            --shadow-lg: 0 12px 35px rgba(0,0,0,0.08);
            --font-main: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            --font-heading: 'Montserrat', sans-serif;
            --font-mono: 'Space Mono', monospace;
        }

        body {
            background-color: var(--bg-page);
            color: var(--text-body);
            font-family: var(--font-main);
            margin: 0;
            padding: 0;
            line-height: 1.6;
        }

        /* TOP ANNOUNCEMENT BAR */
        .top-announcement-bar {
            background-color: #0F172A;
            color: #FFFFFF;
            font-size: 12px;
            padding: 9px 0;
            border-bottom: 1px solid #1E293B;
        }
        .top-bar-inner {
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1280px;
            margin: 0 auto;
            padding: 0 20px;
            flex-wrap: wrap;
            gap: 10px;
        }
        .announcement-badge {
            background: #DC2626;
            color: #fff;
            padding: 2px 8px;
            border-radius: 4px;
            font-weight: 800;
            font-size: 10px;
            margin-right: 8px;
            letter-spacing: 0.5px;
        }
        .currency-dropdown-clean {
            background: #1E293B;
            color: #FFFFFF;
            border: 1px solid #334155;
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 11px;
            font-weight: 700;
            cursor: pointer;
            outline: none;
        }

        /* MAIN HEADER */
        .site-header {
            background: #FFFFFF;
            border-bottom: 1px solid var(--border-subtle);
            position: sticky;
            top: 0;
            z-index: 900;
            box-shadow: var(--shadow-sm);
        }
        .header-inner {
            max-width: 1280px;
            margin: 0 auto;
            padding: 16px 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 20px;
        }
        .header-logo img {
            height: 48px;
            width: auto;
            display: block;
        }
        .nav-links {
            display: flex;
            list-style: none;
            margin: 0;
            padding: 0;
            gap: 28px;
        }
        .nav-links a {
            color: #1E293B;
            text-decoration: none;
            font-weight: 600;
            font-size: 14px;
            transition: color 0.2s ease;
        }
        .nav-links a:hover {
            color: var(--color-primary);
        }
        .header-actions-clean {
            display: flex;
            align-items: center;
            gap: 15px;
        }
        .crypto-pill-tag {
            background: var(--color-amber-light);
            color: var(--color-amber);
            border: 1px solid #FCD34D;
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 11px;
            font-weight: 800;
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .cart-trigger-btn {
            background: var(--color-primary-light);
            color: var(--color-primary);
            border: 1px solid #BFDBFE;
            padding: 8px 16px;
            border-radius: 8px;
            font-weight: 700;
            font-size: 13px;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 8px;
            transition: all 0.2s ease;
        }
        .cart-trigger-btn:hover {
            background: var(--color-primary);
            color: #FFFFFF;
        }
        .cart-count-badge {
            background: var(--color-emerald);
            color: #fff;
            padding: 2px 7px;
            border-radius: 12px;
            font-size: 11px;
            font-weight: 800;
        }

        /* CLINICAL SPLIT HERO */
        .clinical-hero {
            background: linear-gradient(135deg, #F0F9FF 0%, #FFFFFF 50%, #F8FAFC 100%);
            border-bottom: 1px solid var(--border-subtle);
            padding: 70px 0 80px;
        }
        .hero-container {
            max-width: 1280px;
            margin: 0 auto;
            padding: 0 20px;
            display: grid;
            grid-template-columns: 1.15fr 0.85fr;
            gap: 50px;
            align-items: center;
        }
        .hero-badge-clean {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: #DBEAFE;
            color: #1E40AF;
            padding: 5px 14px;
            border-radius: 20px;
            font-size: 11px;
            font-weight: 800;
            letter-spacing: 0.5px;
            margin-bottom: 18px;
        }
        .hero-title-clean {
            font-family: var(--font-heading);
            font-size: 42px;
            font-weight: 900;
            color: var(--text-heading);
            line-height: 1.15;
            margin: 0 0 18px 0;
            letter-spacing: -0.5px;
        }
        .hero-title-clean span {
            color: var(--color-primary);
        }
        .hero-desc-clean {
            font-size: 16px;
            color: var(--text-muted);
            margin: 0 0 28px 0;
            line-height: 1.7;
        }
        .hero-actions-group {
            display: flex;
            gap: 14px;
            margin-bottom: 35px;
            flex-wrap: wrap;
        }
        .btn-primary-blue {
            background: var(--color-primary);
            color: #FFFFFF;
            padding: 13px 26px;
            border-radius: 8px;
            font-weight: 700;
            font-size: 14px;
            text-decoration: none;
            box-shadow: 0 4px 14px rgba(37, 99, 235, 0.35);
            transition: all 0.2s ease;
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }
        .btn-primary-blue:hover {
            background: var(--color-primary-dark);
            transform: translateY(-1px);
        }
        .btn-outline-slate {
            background: #FFFFFF;
            color: #334155;
            border: 1px solid var(--border-subtle);
            padding: 13px 22px;
            border-radius: 8px;
            font-weight: 700;
            font-size: 14px;
            text-decoration: none;
            transition: all 0.2s ease;
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }
        .btn-outline-slate:hover {
            background: #F1F5F9;
            border-color: #CBD5E1;
        }
        .hero-trust-metrics {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
            border-top: 1px solid var(--border-subtle);
            padding-top: 22px;
        }
        .trust-metric-box {
            background: #FFFFFF;
            padding: 10px 12px;
            border-radius: 8px;
            border: 1px solid var(--border-subtle);
            text-align: center;
        }
        .metric-bold {
            font-size: 16px;
            font-weight: 800;
            color: var(--text-heading);
            display: block;
        }
        .metric-sub {
            font-size: 10px;
            color: var(--text-muted);
            font-weight: 600;
        }

        /* HERO RIGHT SHOWCASE CARD */
        .hero-visual-card {
            background: #FFFFFF;
            border: 1px solid var(--border-subtle);
            border-radius: 16px;
            padding: 24px;
            box-shadow: var(--shadow-lg);
            position: relative;
        }
        .hero-visual-img {
            width: 100%;
            height: 380px;
            object-fit: cover;
            border-radius: 12px;
            display: block;
        }
        .floating-hero-tag {
            position: absolute;
            bottom: 35px;
            left: 35px;
            right: 35px;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(8px);
            border: 1px solid var(--border-subtle);
            border-radius: 10px;
            padding: 12px 18px;
            box-shadow: var(--shadow-md);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        /* 4-COLUMN BENEFIT / CERTIFICATION STRIP */
        .benefit-strip {
            background: var(--bg-subtle);
            border-bottom: 1px solid var(--border-subtle);
            padding: 35px 0;
        }
        .benefit-grid {
            max-width: 1280px;
            margin: 0 auto;
            padding: 0 20px;
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 24px;
        }
        .benefit-item {
            display: flex;
            align-items: flex-start;
            gap: 14px;
        }
        .benefit-icon {
            background: #FFFFFF;
            border: 1px solid var(--border-subtle);
            width: 44px;
            height: 44px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 22px;
            flex-shrink: 0;
            box-shadow: var(--shadow-sm);
        }
        .benefit-item h4 {
            margin: 0 0 3px 0;
            font-size: 14px;
            color: var(--text-heading);
            font-weight: 700;
        }
        .benefit-item p {
            margin: 0;
            font-size: 12px;
            color: var(--text-muted);
            line-height: 1.4;
        }

        /* CATEGORY FILTER PILLS BAR */
        .category-filter-section {
            padding: 40px 0 20px;
            max-width: 1280px;
            margin: 0 auto;
            padding-left: 20px;
            padding-right: 20px;
        }
        .filter-header-flex {
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            margin-bottom: 20px;
            flex-wrap: wrap;
            gap: 15px;
        }
        .filter-pills-bar {
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
        }
        .filter-pill {
            background: #FFFFFF;
            border: 1px solid var(--border-subtle);
            color: #475569;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .filter-pill:hover, .filter-pill.active {
            background: var(--color-primary);
            color: #FFFFFF;
            border-color: var(--color-primary);
            box-shadow: 0 2px 8px rgba(37, 99, 235, 0.25);
        }

        /* PRODUCT CARDS GRID (CLEAN WORDPRESS / WOOCOMMERCE STYLE) */
        .products-grid-section {
            max-width: 1280px;
            margin: 0 auto 70px;
            padding: 0 20px;
        }
        .clean-products-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 24px;
        }
        .clean-product-card {
            background: var(--bg-card);
            border: 1px solid var(--border-subtle);
            border-radius: 12px;
            padding: 18px;
            box-shadow: var(--shadow-sm);
            transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
            position: relative;
            display: flex;
            flex-direction: column;
        }
        .clean-product-card:hover {
            transform: translateY(-4px);
            box-shadow: var(--shadow-md);
            border-color: #93C5FD;
        }

        /* 3-PICTURE REACTIVE HOVER CAROUSEL */
        .card-carousel-box {
            position: relative;
            width: 100%;
            height: 240px;
            border-radius: 8px;
            overflow: hidden;
            background: #F8FAFC;
            margin-bottom: 14px;
            border: 1px solid #F1F5F9;
        }
        .carousel-track-flex {
            display: flex;
            width: 300%;
            height: 100%;
            transition: transform 0.35s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .carousel-slide-item {
            width: 33.333%;
            height: 100%;
            position: relative;
        }
        .carousel-slide-item img {
            width: 100%;
            height: 100%;
            object-fit: contain;
            background: #F8FAFC;
            display: block;
        }

        /* HOVER DIRECTION ARROWS */
        .clean-arrow {
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            width: 32px;
            height: 32px;
            border-radius: 50%;
            background: #FFFFFF;
            border: 1px solid var(--border-subtle);
            color: #1E293B;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 15px;
            font-weight: 800;
            cursor: pointer;
            z-index: 5;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
            transition: all 0.2s ease;
            opacity: 0.85;
        }
        .card-carousel-box:hover .clean-arrow {
            opacity: 1;
        }
        .clean-arrow:hover {
            background: var(--color-primary);
            color: #FFFFFF;
            border-color: var(--color-primary);
            box-shadow: 0 0 10px rgba(37, 99, 235, 0.5);
            transform: translateY(-50%) scale(1.1);
        }
        .clean-arrow.prev { left: 8px; }
        .clean-arrow.next { right: 8px; }

        .view-caption-pill {
            position: absolute;
            bottom: 8px;
            left: 8px;
            background: rgba(255, 255, 255, 0.95);
            border: 1px solid var(--border-subtle);
            color: #334155;
            font-size: 10px;
            font-weight: 700;
            padding: 3px 8px;
            border-radius: 4px;
            z-index: 4;
            backdrop-filter: blur(4px);
            pointer-events: none;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }
        .card-pips-row {
            position: absolute;
            bottom: 8px;
            right: 8px;
            display: flex;
            gap: 4px;
            z-index: 4;
        }
        .clean-pip {
            width: 14px;
            height: 4px;
            border-radius: 2px;
            background: #CBD5E1;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .clean-pip.active {
            background: var(--color-primary);
            width: 20px;
        }

        /* CARD CONTENT DETAILS */
        .card-meta-top {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 8px;
        }
        .sale-badge-pill {
            background: var(--color-crimson);
            color: #FFFFFF;
            font-size: 10px;
            font-weight: 800;
            padding: 2px 8px;
            border-radius: 12px;
        }
        .purity-badge-pill {
            background: var(--color-emerald-light);
            color: var(--color-emerald);
            border: 1px solid #A7F3D0;
            font-size: 10px;
            font-weight: 800;
            padding: 2px 8px;
            border-radius: 10px;
        }
        .card-title-text {
            color: var(--text-heading);
            font-size: 16px;
            font-weight: 800;
            margin: 0 0 4px 0;
            font-family: var(--font-heading);
        }
        .card-cat-text {
            color: var(--text-muted);
            font-size: 12px;
            margin: 0 0 8px 0;
        }
        .card-specs-bar {
            background: #F1F5F9;
            color: #475569;
            font-size: 11px;
            padding: 5px 8px;
            border-radius: 4px;
            margin-bottom: 10px;
            font-family: var(--font-mono);
        }
        .crypto-rebate-tag {
            background: var(--color-amber-light);
            color: var(--color-amber);
            border: 1px solid #FCD34D;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 11px;
            font-weight: 700;
            margin-bottom: 12px;
        }
        .variant-pills-wrap {
            display: flex;
            gap: 6px;
            margin: 6px 0 10px;
        }
        .variant-pill-item {
            background: #F8FAFC;
            border: 1px solid var(--border-subtle);
            color: #475569;
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 11px;
            font-weight: 700;
            cursor: pointer;
        }
        .variant-pill-item.active {
            background: var(--color-primary);
            color: #FFFFFF;
            border-color: var(--color-primary);
        }
        .pack-select-clean {
            width: 100%;
            background: #FFFFFF;
            border: 1px solid var(--border-subtle);
            color: #334155;
            padding: 6px;
            border-radius: 6px;
            font-size: 12px;
            margin-bottom: 14px;
        }
        .card-pricing-row {
            margin-top: auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-top: 1px solid var(--border-subtle);
            padding-top: 12px;
        }
        .price-strike-gray {
            color: #94A3B8;
            text-decoration: line-through;
            font-size: 13px;
            margin-right: 6px;
        }
        .price-sale-bold {
            color: var(--color-emerald);
            font-size: 20px;
            font-weight: 900;
        }
        .add-cart-btn-clean {
            background: var(--color-primary);
            color: #FFFFFF;
            border: none;
            padding: 9px 16px;
            border-radius: 6px;
            font-weight: 800;
            font-size: 13px;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .add-cart-btn-clean:hover {
            background: var(--color-primary-dark);
            transform: scale(1.02);
        }

        /* INSTITUTIONAL LUXURY NAVY SECTION */
        .institutional-section {
            background: #0A192F;
            color: #FFFFFF;
            padding: 85px 0;
            border-top: 1px solid #1E293B;
            border-bottom: 1px solid #1E293B;
        }
        .inst-header-center {
            text-align: center;
            max-width: 800px;
            margin: 0 auto 50px;
        }
        .inst-badge-gold {
            background: var(--color-amber);
            color: #000;
            font-size: 11px;
            font-weight: 900;
            padding: 4px 12px;
            border-radius: 20px;
            letter-spacing: 0.5px;
            display: inline-block;
            margin-bottom: 10px;
        }
        .inst-card {
            background: #112240;
            border: 1px solid #233554;
            border-radius: 12px;
            padding: 22px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.4);
            color: #FFFFFF;
            display: flex;
            flex-direction: column;
        }
        .inst-card:hover {
            border-color: #64FFDA;
            transform: translateY(-4px);
        }

        /* QUALITY & CERTIFICATIONS */
        .section-qa-rules {
            background: #FFFFFF;
            padding: 80px 0;
            border-bottom: 1px solid var(--border-subtle);
        }
        .qa-container {
            max-width: 1280px;
            margin: 0 auto;
            padding: 0 20px;
        }
        .cert-cards-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            margin-bottom: 40px;
        }
        .cert-card-clean {
            background: #FFFFFF;
            border: 1px solid var(--border-subtle);
            border-radius: 10px;
            padding: 24px 20px;
            text-align: center;
            box-shadow: var(--shadow-sm);
        }
        .cert-card-clean h3 {
            margin: 12px 0 6px 0;
            font-size: 15px;
            color: var(--text-heading);
            font-family: var(--font-heading);
        }
        .cert-card-clean p {
            margin: 0;
            font-size: 12px;
            color: var(--text-muted);
            line-height: 1.5;
        }

        /* SATELLITE TRACKING CONSOLE (CLEAN) */
        .tracking-section-clean {
            background: var(--bg-subtle);
            padding: 70px 0;
            border-bottom: 1px solid var(--border-subtle);
        }
        .tracking-box-clean {
            max-width: 860px;
            margin: 0 auto;
            background: #FFFFFF;
            border: 1px solid var(--border-subtle);
            border-radius: 14px;
            padding: 35px;
            box-shadow: var(--shadow-md);
        }

        /* CART DRAWER & MODAL */
        .cart-drawer-overlay {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(15, 23, 42, 0.6); backdrop-filter: blur(4px);
            z-index: 9998; opacity: 0; visibility: hidden; transition: all 0.3s ease;
        }
        .cart-drawer-overlay.active { opacity: 1; visibility: visible; }
        .cart-drawer {
            position: fixed; top: 0; right: -440px; width: 420px; max-width: 90vw; height: 100%;
            background: #FFFFFF; color: #0F172A; z-index: 9999; box-shadow: -10px 0 35px rgba(0,0,0,0.15);
            display: flex; flex-direction: column; transition: right 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            border-left: 1px solid var(--border-subtle);
        }
        .cart-drawer.open { right: 0; }
        .drawer-header { padding: 22px; border-bottom: 1px solid var(--border-subtle); display: flex; justify-content: space-between; align-items: center; }
        .drawer-header h3 { margin: 0; font-family: var(--font-heading); color: var(--color-primary); font-size: 18px; }
        .drawer-close { background: none; border: none; color: #64748B; font-size: 26px; cursor: pointer; }
        .cart-items-body { flex: 1; overflow-y: auto; padding: 20px; }
        .cart-item-clean { display: flex; justify-content: space-between; align-items: center; padding: 12px 0; border-bottom: 1px solid var(--border-subtle); }
        .cart-item-clean h4 { margin: 0 0 3px 0; font-size: 14px; color: var(--text-heading); }
        .cart-item-clean span { font-size: 12px; color: var(--text-muted); }
        .drawer-foot { padding: 20px; border-top: 1px solid var(--border-subtle); background: var(--bg-subtle); }
        .subtotal-row { display: flex; justify-content: space-between; font-size: 16px; font-weight: 800; margin-bottom: 15px; color: var(--text-heading); }

        /* CHECKOUT MODAL */
        .checkout-modal {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(15, 23, 42, 0.7); backdrop-filter: blur(6px);
            z-index: 10000; display: none; align-items: center; justify-content: center; padding: 20px;
        }
        .checkout-modal.active { display: flex; }
        .modal-card-clean {
            background: #FFFFFF; border: 1px solid var(--border-subtle); border-radius: 14px;
            width: 620px; max-width: 100%; max-height: 90vh; overflow-y: auto; padding: 32px; color: #0F172A;
            box-shadow: 0 25px 60px rgba(0,0,0,0.25); position: relative;
        }
        .modal-close-clean { position: absolute; top: 16px; right: 20px; font-size: 24px; color: #64748B; background: none; border: none; cursor: pointer; }
        .modal-tabs-row { display: flex; gap: 8px; margin: 20px 0 15px; flex-wrap: wrap; }
        .modal-tab-btn { flex: 1; min-width: 110px; padding: 10px 8px; font-size: 12px; font-weight: 700; border-radius: 6px; background: #F8FAFC; color: #475569; border: 1px solid var(--border-subtle); cursor: pointer; text-align: center; }
        .modal-tab-btn.active { background: var(--color-primary); color: #FFFFFF; border-color: var(--color-primary); }
        .modal-tab-btn .badge-disc { display: block; font-size: 10px; color: var(--color-emerald); font-weight: 800; }
        .modal-tab-btn.active .badge-disc { color: #DBEAFE; }
        .modal-tab-pane { display: none; background: #F8FAFC; padding: 20px; border-radius: 8px; border: 1px solid var(--border-subtle); margin-bottom: 20px; }
        .modal-tab-pane.active { display: block; }

        /* FOOTER */
        .site-footer-clean {
            background: #0F172A;
            color: #94A3B8;
            padding: 60px 0 25px;
            font-size: 13px;
        }
        .footer-inner {
            max-width: 1280px;
            margin: 0 auto;
            padding: 0 20px;
        }
        .disclaimer-banner-clean {
            background: #1E293B;
            border-left: 4px solid var(--color-amber);
            padding: 14px 20px;
            border-radius: 6px;
            color: #CBD5E1;
            margin-bottom: 45px;
            font-size: 12px;
            line-height: 1.6;
        }
        .footer-cols-grid {
            display: grid;
            grid-template-columns: 1.5fr 1fr 1fr 1.2fr;
            gap: 40px;
            margin-bottom: 40px;
        }
        .footer-col h4 {
            color: #FFFFFF;
            font-size: 15px;
            margin: 0 0 16px 0;
            font-family: var(--font-heading);
        }
        .footer-col ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        .footer-col ul li {
            margin-bottom: 10px;
        }
        .footer-col ul li a {
            color: #94A3B8;
            text-decoration: none;
        }
        .footer-col ul li a:hover {
            color: #FFFFFF;
        }
        .footer-bottom-copy {
            border-top: 1px solid #1E293B;
            padding-top: 25px;
            text-align: center;
            color: #64748B;
            font-size: 12px;
        }
    </style>
</head>
<body>

    <!-- TOP ANNOUNCEMENT & DUAL CURRENCY BAR (USD & EUR ONLY) -->
    <div class="top-announcement-bar">
        <div class="top-bar-inner">
            <div>
                <span class="announcement-badge">20% RESEARCH SALE</span>
                <span>All Catalog Peptides Discounted &bull; Insured -20°C Cold-Chain Direct Delivery</span>
            </div>
            <div style="display:flex;align-items:center;gap:15px;">
                <span style="color:#FCD34D;">⚡ <strong>Pay with BTC/USDT:</strong> 10% Off | <strong>Wire:</strong> 5% Off</span>
                <div>
                    <!-- DUAL CURRENCY SWITCHER (USD / EUR) -->
                    <select id="preview-currency" class="currency-dropdown-clean" aria-label="Select Currency">
                        <option value="USD" selected>USD ($)</option>
                        <option value="EUR">EUR (€)</option>
                    </select>
                </div>
            </div>
        </div>
    </div>

    <!-- MAIN WORDPRESS NAVIGATION HEADER -->
    <header class="site-header">
        <div class="header-inner">
            <div class="header-logo">
                <a href="#hero">
                    <img src="assets/images/logo.svg" alt="Phoenics Peptide" onerror="this.onerror=null; this.src='assets/images/logo.jpg';">
                </a>
            </div>

            <nav>
                <ul class="nav-links">
                    <li><a href="#hero">Home</a></li>
                    <li><a href="#catalog">Research Catalog (20% Off)</a></li>
                    <li><a href="#institutional" style="color:#D97706;font-weight:800;">Institutional ($23k+)</a></li>
                    <li><a href="#certifications">Certifications & Rules</a></li>
                    <li><a href="#tracking">📦 Satellite Tracking</a></li>
                </ul>
            </nav>

            <div class="header-actions-clean">
                <div class="crypto-pill-tag">
                    <span>₿</span> 10% OFF CRYPTO
                </div>
                <button class="cart-trigger-btn" id="open-cart-btn">
                    <span>🛒 Cart</span>
                    <span class="cart-count-badge" id="cart-counter">0</span>
                </button>
            </div>
        </div>
    </header>

    <!-- CLINICAL SPLIT HERO SECTION -->
    <section id="hero" class="clinical-hero">
        <div class="hero-container">
            <div>
                <div class="hero-badge-clean">
                    <span>🔬</span> ANALYTICAL PURITY &ge; 99.0% &bull; HPLC & MS DUAL-VERIFIED
                </div>
                <h1 class="hero-title-clean">
                    Precision Peptide Synthesis <br>
                    <span>For Groundbreaking Research</span>
                </h1>
                <p class="hero-desc-clean">
                    Leading primary supplier of high-demand metabolic incretins (Tirzepatide, Retatrutide, Semaglutide), tissue regenerative sequences (BPC-157, TB-500, GHK-Cu), and institutional 384-peptide scanning libraries ($23,450) across North America and Europe.
                </p>
                <div class="hero-actions-group">
                    <a href="#catalog" class="btn-primary-blue">Explore 3-Angle Product Catalog &rarr;</a>
                    <a href="#tracking" class="btn-outline-slate">📦 Track Cold-Chain Shipment</a>
                </div>

                <div class="hero-trust-metrics">
                    <div class="trust-metric-box">
                        <span class="metric-bold">&gt;99.3%</span>
                        <span class="metric-sub">Mean HPLC Purity</span>
                    </div>
                    <div class="trust-metric-box">
                        <span class="metric-bold">USD & EUR</span>
                        <span class="metric-sub">Dual Settlement</span>
                    </div>
                    <div class="trust-metric-box">
                        <span class="metric-bold">-20°C</span>
                        <span class="metric-sub">Cold-Chain Preserved</span>
                    </div>
                    <div class="trust-metric-box">
                        <span class="metric-bold">10% OFF</span>
                        <span class="metric-sub">BTC / Crypto Rebate</span>
                    </div>
                </div>
            </div>

            <div class="hero-visual-card">
                <!-- High-res photorealistic AI render from Gemini -->
                <img src="assets/images/products/tirzepatide-photo.jpg" alt="Tirzepatide Cleanroom Pedestal" class="hero-visual-img" onerror="this.onerror=null; this.src='assets/images/product-vial.jpg';">
                <div class="floating-hero-tag">
                    <div>
                        <strong style="color:#0F172A;font-size:13px;display:block;">TIRZEPATIDE 10MG (DUAL AGONIST)</strong>
                        <span style="color:#64748B;font-size:11px;">Analytical Purity &ge;99.4% &bull; Lot #TPT1024</span>
                    </div>
                    <span style="background:#ECFDF5;color:#059669;font-size:11px;font-weight:800;padding:4px 10px;border-radius:12px;border:1px solid #A7F3D0;">IN STOCK &bull; SALE</span>
                </div>
            </div>
        </div>
    </section>

    <!-- 4-COLUMN QUALITY ASSURANCE & BENEFITS STRIP -->
    <section class="benefit-strip">
        <div class="benefit-grid">
            <div class="benefit-item">
                <div class="benefit-icon">🏛️</div>
                <div>
                    <h4>ISO 9001:2015 Certified</h4>
                    <p>Standardized chemical synthesis process controls and complete batch validation.</p>
                </div>
            </div>
            <div class="benefit-item">
                <div class="benefit-icon">🔬</div>
                <div>
                    <h4>HPLC & MS Dual QC</h4>
                    <p>Individual Reverse-Phase HPLC and Electrospray MS Certificate of Analysis included.</p>
                </div>
            </div>
            <div class="benefit-item">
                <div class="benefit-icon">❄️</div>
                <div>
                    <h4>-20°C Cold-Chain Transit</h4>
                    <p>Phase-change refrigerant packaging with electronic temperature monitor tags.</p>
                </div>
            </div>
            <div class="benefit-item">
                <div class="benefit-icon">✈️</div>
                <div>
                    <h4>Direct Global Air Freight</h4>
                    <p>Express courier dispatch via DHL, FedEx, and USPS from Boston, Frankfurt & Toronto.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- CATEGORY FILTER PILLS & HEADING -->
    <section id="catalog" class="category-filter-section">
        <div class="filter-header-flex">
            <div>
                <span style="color:#2563EB;font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase;">PRECISION RESEARCH CATALOG</span>
                <h2 style="font-family:var(--font-heading);font-size:28px;color:#0F172A;margin:4px 0 0 0;">High-Demand Research Peptides</h2>
                <p style="color:#64748B;font-size:14px;margin:4px 0 0 0;">Hover over the direction arrows <strong>(&lsaquo; &rsaquo;)</strong> on any product to preview all 3 perspectives: <strong>Container &bull; HPLC CoA &bull; Cold-Chain Box</strong>.</p>
            </div>
            <div class="filter-pills-bar">
                <button class="filter-pill active" onclick="filterCategory('all', this)">All Compounds (18)</button>
                <button class="filter-pill" onclick="filterCategory('Metabolic', this)">Metabolic & GLP-1 (4)</button>
                <button class="filter-pill" onclick="filterCategory('Healing', this)">Healing & Recovery (3)</button>
                <button class="filter-pill" onclick="filterCategory('Secretagogue', this)">GH Secretagogues (3)</button>
                <button class="filter-pill" onclick="filterCategory('Longevity', this)">Longevity & Nootropic (5)</button>
                <button class="filter-pill" onclick="filterCategory('Institutional', this)">Institutional ($23k+) (3)</button>
            </div>
        </div>
    </section>

    <!-- 4-COLUMN PRODUCTS GRID -->
    <section class="products-grid-section">
        <div class="clean-products-grid" id="product-grid">
            <!-- Dynamically populated via JS with hover carousels -->
        </div>
    </section>

    <!-- INSTITUTIONAL & PHARMA SCALE SECTION ($5,000 to $23,450+) -->
    <section id="institutional" class="institutional-section">
        <div class="inst-header-center">
            <span class="inst-badge-gold">PHARMACEUTICAL & INSTITUTIONAL SCALE</span>
            <h2 style="font-family:var(--font-heading);font-size:32px;margin:8px 0;">High-Throughput Peptide Libraries & Bulk Synthesis</h2>
            <p style="color:#94A3B8;font-size:14px;margin:0;">Direct fulfillment for university laboratories, pharmaceutical drug discovery teams, and clinical research institutions.</p>
        </div>

        <div style="max-width:1280px;margin:0 auto;padding:0 20px;">
            <div class="clean-products-grid" id="institutional-grid">
                <!-- Dynamically populated via JS -->
            </div>
        </div>
    </section>

    <!-- CERTIFICATIONS, APPROVALS & HANDLING ACCORDION -->
    <section id="certifications" class="section-qa-rules">
        <div class="qa-container">
            <div style="text-align:center;margin-bottom:40px;">
                <span style="color:#2563EB;font-weight:800;font-size:12px;letter-spacing:1px;text-transform:uppercase;">QUALITY ASSURANCE PROTOCOLS</span>
                <h2 style="font-family:var(--font-heading);font-size:28px;color:#0F172A;margin:6px 0 0 0;">Certifications & Laboratory Handling Rules</h2>
            </div>

            <div class="cert-cards-grid">
                <div class="cert-card-clean">
                    <span style="font-size:36px;">🏛️</span>
                    <h3>ISO 9001:2015</h3>
                    <p>Standardized chemical synthesis process controls, documented lot traceability, and raw amino acid batch validation.</p>
                    <span style="display:inline-block;margin-top:12px;background:#ECFDF5;color:#059669;font-size:10px;font-weight:800;padding:3px 8px;border-radius:10px;">ACCREDITED</span>
                </div>
                <div class="cert-card-clean">
                    <span style="font-size:36px;">🔬</span>
                    <h3>HPLC & MS Verification</h3>
                    <p>Every batch verified by analytical Reverse-Phase HPLC and Electrospray MS confirming exact sequence mass and &ge;99% purity.</p>
                    <span style="display:inline-block;margin-top:12px;background:#ECFDF5;color:#059669;font-size:10px;font-weight:800;padding:3px 8px;border-radius:10px;">COA INCLUDED</span>
                </div>
                <div class="cert-card-clean">
                    <span style="font-size:36px;">🛡️</span>
                    <h3>cGMP Cleanroom 10,000</h3>
                    <p>Formulated under positive-pressure HEPA filtered laminar hoods with nitrogen-purged borosilicate vial crimp sealing.</p>
                    <span style="display:inline-block;margin-top:12px;background:#ECFDF5;color:#059669;font-size:10px;font-weight:800;padding:3px 8px;border-radius:10px;">CLASS 7</span>
                </div>
                <div class="cert-card-clean">
                    <span style="font-size:36px;">❄️</span>
                    <h3>Cold-Chain -20°C</h3>
                    <p>Insulated phase-change refrigerant packaging with electronic temperature loggers preserving tertiary peptide structure.</p>
                    <span style="display:inline-block;margin-top:12px;background:#ECFDF5;color:#059669;font-size:10px;font-weight:800;padding:3px 8px;border-radius:10px;">ACTIVE LOG</span>
                </div>
            </div>

            <!-- COMPLIANCE GUIDELINE BOX -->
            <div style="background:#F8FAFC;border:1px solid var(--border-subtle);border-radius:12px;padding:30px;">
                <h3 style="color:#0F172A;font-family:var(--font-heading);margin-top:0;font-size:18px;">Laboratory Handling Rules & In-Vitro Compliance Guide</h3>
                <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));gap:24px;margin-top:16px;font-size:13px;color:#475569;line-height:1.6;">
                    <div>
                        <strong style="color:#1E293B;font-size:14px;">1. Aseptic Reconstitution</strong><br>
                        Allow the lyophilized vial to equilibrate to room temperature inside a laminar flow hood before drawing Bacteriostatic Water down the glass wall.
                    </div>
                    <div>
                        <strong style="color:#1E293B;font-size:14px;">2. Vortexing Prohibition</strong><br>
                        Do not agitate or vortex reconstituted peptide chains. Gently swirl in circular motion to prevent shear-induced denaturation.
                    </div>
                    <div>
                        <strong style="color:#1E293B;font-size:14px;">3. In-Vitro Research Restriction</strong><br>
                        All compounds are distributed strictly for academic, biological, and physiological assays. Not for in-vivo human or animal application.
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- SATELLITE COLD-CHAIN TRACKING CONSOLE -->
    <section id="tracking" class="tracking-section-clean">
        <div class="tracking-box-clean">
            <div style="text-align:center;margin-bottom:25px;">
                <h2 style="font-family:var(--font-heading);color:#0F172A;margin:0 0 6px 0;font-size:24px;">Global Cold-Chain Satellite Tracking Console</h2>
                <p style="color:#64748B;font-size:14px;margin:0;">Real-time telemetry and temperature validation for international analytical research shipments.</p>
            </div>

            <form id="standalone-tracking-form" style="display:flex;gap:10px;margin-bottom:20px;">
                <input type="text" id="track-input" placeholder="Enter Phoenics Order # (Try #1042) or Carrier AWB" required value="1042" style="flex:1;padding:12px 16px;border:1px solid var(--border-subtle);border-radius:8px;font-size:14px;color:#0F172A;">
                <button type="submit" class="btn-primary-blue" style="border:none;cursor:pointer;">Inspect Shipment &rarr;</button>
            </form>

            <div id="telemetry-card" style="background:#F8FAFC;border:1px solid var(--border-subtle);border-radius:10px;padding:22px;">
                <div style="display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid var(--border-subtle);padding-bottom:14px;margin-bottom:16px;">
                    <div>
                        <span style="font-size:11px;color:#64748B;font-weight:700;">DISPATCH TELEMETRY</span>
                        <h3 id="dyn-status" style="margin:2px 0 0 0;color:#0284C7;font-size:18px;">✈️ In Transit (International Priority Air Freight)</h3>
                    </div>
                    <div style="text-align:right;">
                        <span style="font-size:11px;color:#64748B;font-weight:700;">COLD-CHAIN INTEGRITY</span>
                        <div style="color:#059669;font-weight:800;font-size:14px;">❄️ -20.0°C STABLE (Nitrogen Pack Active)</div>
                    </div>
                </div>

                <div style="display:grid;grid-template-columns:repeat(4, 1fr);gap:12px;font-size:12px;">
                    <div><span style="color:#64748B;">Order Identifier:</span> <strong id="dyn-order-id" style="color:#0F172A;">#1042</strong></div>
                    <div><span style="color:#64748B;">Carrier Partner:</span> <strong id="dyn-carrier" style="color:#0F172A;">DHL Express Worldwide</strong></div>
                    <div><span style="color:#64748B;">Master AWB:</span> <strong id="dyn-awb" style="color:#2563EB;">794820194821</strong></div>
                    <div><span style="color:#64748B;">Destination:</span> <strong id="dyn-dest" style="color:#0F172A;">USA / Europe / Canada</strong></div>
                </div>
            </div>
        </div>
    </section>

    <!-- SLIDE-OUT CART DRAWER -->
    <div class="cart-drawer-overlay" id="cart-overlay"></div>
    <div class="cart-drawer" id="cart-drawer">
        <div class="drawer-header">
            <h3>🔬 Research Cart (<span id="cart-drawer-count">0</span>)</h3>
            <button class="drawer-close" id="close-cart-btn">&times;</button>
        </div>
        <div class="cart-items-body" id="cart-items-container">
            <p style="color:#64748B;text-align:center;margin-top:40px;">Your research cart is empty.</p>
        </div>
        <div class="drawer-foot">
            <div class="subtotal-row">
                <span>Subtotal (Sale Price):</span>
                <span id="cart-subtotal-val">$0.00</span>
            </div>
            <button class="btn-primary-blue" id="checkout-btn" style="width:100%;justify-content:center;padding:14px;">Proceed to Checkout (Up to 10% Extra Off) &rarr;</button>
        </div>
    </div>

    <!-- MULTI-GATEWAY CHECKOUT MODAL WITH LIVE PAYMENT DISCOUNTS -->
    <div class="checkout-modal" id="checkout-modal">
        <div class="modal-card-clean">
            <button class="modal-close-clean" id="modal-close-btn">&times;</button>
            <h3 style="color:#0F172A;margin-top:0;font-family:var(--font-heading);">Checkout Gateway — Order #<span id="chk-order-num">1043</span></h3>
            
            <div style="background:#F0FDF4;border:1px solid #BBF7D0;padding:12px 16px;border-radius:8px;margin-bottom:18px;display:flex;justify-content:space-between;align-items:center;">
                <div>
                    <span style="font-size:12px;color:#166534;">Payable Total:</span>
                    <div id="chk-total" style="color:#15803D;font-size:22px;font-weight:800;">$0.00</div>
                </div>
                <div id="payment-discount-applied" style="background:#15803D;color:#FFFFFF;font-size:11px;font-weight:800;padding:4px 10px;border-radius:20px;">
                    10% CRYPTO DISCOUNT ACTIVE
                </div>
            </div>

            <div class="modal-tabs-row">
                <button class="modal-tab-btn active" data-tab="gw-btc" data-discount="0.10">
                    ₿ Bitcoin / Lightning
                    <span class="badge-disc">Save Extra 10%</span>
                </button>
                <button class="modal-tab-btn" data-tab="gw-usdt" data-discount="0.10">
                    ₮ USDT / Crypto
                    <span class="badge-disc">Save Extra 10%</span>
                </button>
                <button class="modal-tab-btn" data-tab="gw-wire" data-discount="0.05">
                    🏦 Bank Wire / SWIFT
                    <span class="badge-disc">Save Extra 5%</span>
                </button>
                <button class="modal-tab-btn" data-tab="gw-card" data-discount="0">
                    💳 Credit/Debit (Stripe)
                    <span class="badge-disc" style="color:#64748B;">Standard</span>
                </button>
                <button class="modal-tab-btn" data-tab="gw-pp" data-discount="0">
                    🅿️ PayPal
                    <span class="badge-disc" style="color:#64748B;">Standard</span>
                </button>
            </div>

            <!-- BITCOIN TAB -->
            <div class="modal-tab-pane active" id="gw-btc">
                <div style="text-align:center;">
                    <span style="background:#FEF3C7;color:#B45309;font-size:11px;font-weight:800;padding:3px 10px;border-radius:12px;">10% CRYPTO REBATE DEDUCTED</span>
                    <p style="margin:12px 0 6px;font-size:13px;color:#1E293B;">Send exact BTC to Personal Hardware Wallet via BTCPay Server:</p>
                    <div style="font-family:var(--font-mono);font-size:12px;background:#FFFFFF;border:1px solid var(--border-subtle);padding:10px;border-radius:6px;color:#0F172A;word-break:break-all;margin:10px 0;">bc1qphoenicspeptideresearch7829104829104x</div>
                    <p style="font-size:11px;color:#64748B;margin:0;">Direct settlement to personal hardware wallet &bull; 0% processing fees &bull; Instant Lightning broadcast</p>
                </div>
            </div>

            <!-- USDT TAB -->
            <div class="modal-tab-pane" id="gw-usdt">
                <div style="text-align:center;">
                    <span style="background:#ECFDF5;color:#059669;font-size:11px;font-weight:800;padding:3px 10px;border-radius:12px;">10% USDT REBATE DEDUCTED</span>
                    <p style="margin:12px 0 6px;font-size:13px;color:#1E293B;">Send USDT (TRC-20 / ERC-20) via NOWPayments:</p>
                    <div style="font-family:var(--font-mono);font-size:12px;background:#FFFFFF;border:1px solid var(--border-subtle);padding:10px;border-radius:6px;color:#059669;word-break:break-all;margin:10px 0;">TJv941PhoenicsPeptideUSDTNetwork84920</div>
                    <p style="font-size:11px;color:#64748B;margin:0;">Immediate automated blockchain confirmation in 30 seconds</p>
                </div>
            </div>

            <!-- WIRE TAB -->
            <div class="modal-tab-pane" id="gw-wire">
                <span style="background:#E0F2FE;color:#0369A1;font-size:11px;font-weight:800;padding:3px 10px;border-radius:12px;">5% INSTITUTIONAL WIRE DISCOUNT</span>
                <p style="font-size:13px;color:#334155;margin-top:12px;">Bank Transfer / SWIFT Proforma details will be generated upon order confirmation. Net-30 available for verified university procurement offices.</p>
                <div style="font-size:12px;color:#1E293B;background:#FFFFFF;border:1px solid var(--border-subtle);padding:12px;border-radius:6px;margin-top:8px;">
                    Beneficiary: Phoenics Peptide Analytical Reagents LLC<br>
                    Routing/SWIFT: PHNXUS33XXX
                </div>
            </div>

            <!-- STRIPE TAB -->
            <div class="modal-tab-pane" id="gw-card">
                <p style="font-size:12px;color:#64748B;margin-bottom:12px;">Processed securely via Stripe 3D-Secure 2.0 (Visa, Mastercard, AMEX, Apple Pay)</p>
                <input type="text" placeholder="Cardholder Name" style="width:100%;padding:10px;margin-bottom:8px;background:#FFFFFF;border:1px solid var(--border-subtle);border-radius:6px;color:#0F172A;">
                <input type="text" placeholder="Card Number (•••• •••• •••• ••••)" style="width:100%;padding:10px;margin-bottom:8px;background:#FFFFFF;border:1px solid var(--border-subtle);border-radius:6px;color:#0F172A;">
                <div style="display:flex;gap:10px;">
                    <input type="text" placeholder="MM/YY" style="flex:1;padding:10px;background:#FFFFFF;border:1px solid var(--border-subtle);border-radius:6px;color:#0F172A;">
                    <input type="text" placeholder="CVC" style="flex:1;padding:10px;background:#FFFFFF;border:1px solid var(--border-subtle);border-radius:6px;color:#0F172A;">
                </div>
            </div>

            <!-- PAYPAL TAB -->
            <div class="modal-tab-pane" id="gw-pp">
                <p style="font-size:13px;color:#64748B;text-align:center;padding:15px 0;">
                    Click below to authorize through PayPal Worldwide Express or Pay in 4 installment plan.
                </p>
            </div>

            <button class="btn-primary-blue" id="submit-order-btn" style="width:100%;justify-content:center;padding:14px;background:#059669;border:none;cursor:pointer;font-size:15px;">
                🚀 Confirm Research Order & Generate Shipment
            </button>
        </div>
    </div>

    <!-- CLEAN MEDICAL FOOTER WITH REGULATORY DISCLAIMER -->
    <footer class="site-footer-clean">
        <div class="footer-inner">
            <div class="disclaimer-banner-clean">
                <strong>⚠️ 21 CFR § 312.160 REGULATORY COMPLIANCE NOTICE:</strong> All chemical substances and peptides cataloged on phoenicspeptide.com are distributed exclusively for in-vitro laboratory analytical experimentation and scientific research. Not for human or veterinary administration, diagnostic procedure, or household use. Handle only by qualified investigators.
            </div>

            <div class="footer-cols-grid">
                <div class="footer-col">
                    <img src="assets/images/logo-white.svg" alt="Phoenics Peptide" style="height:44px;margin-bottom:14px;" onerror="this.onerror=null; this.src='assets/images/logo.jpg';">
                    <p style="margin:0;line-height:1.7;">High-purity peptide synthesis gateway engineered for laboratory precision, documented analytical purity, and cold-chain integrity across North America, Europe, and Asia.</p>
                </div>
                <div class="footer-col">
                    <h4>Global Fulfillment Hubs</h4>
                    <ul>
                        <li>🇺🇸 Boston Central Facility (USA)</li>
                        <li>🇩🇪 Frankfurt European Hub (EU)</li>
                        <li>🇨🇦 Toronto Logistics Depot (Canada)</li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Carriers & Cold-Chain</h4>
                    <ul>
                        <li>DHL Express Worldwide Priority</li>
                        <li>FedEx International Priority Air</li>
                        <li>USPS Insured Priority Mail</li>
                        <li>-20°C Monitored Cryo-Freight</li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Accepted Settlement Gateways</h4>
                    <div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:10px;">
                        <span style="background:#1E293B;padding:4px 8px;border-radius:4px;color:#FCD34D;font-weight:800;font-size:11px;">₿ BITCOIN (-10%)</span>
                        <span style="background:#1E293B;padding:4px 8px;border-radius:4px;color:#34D399;font-weight:800;font-size:11px;">₮ USDT (-10%)</span>
                        <span style="background:#1E293B;padding:4px 8px;border-radius:4px;color:#38BDF8;font-weight:800;font-size:11px;">WIRE (-5%)</span>
                        <span style="background:#1E293B;padding:4px 8px;border-radius:4px;color:#CBD5E1;font-size:11px;">VISA / MC</span>
                        <span style="background:#1E293B;padding:4px 8px;border-radius:4px;color:#CBD5E1;font-size:11px;">PAYPAL</span>
                    </div>
                </div>
            </div>

            <div class="footer-bottom-copy">
                &copy; 2026 Phoenics Peptide (phoenicspeptide.com). All Rights Reserved. ISO 9001:2015 Accredited Synthesis Provider.
            </div>
        </div>
    </footer>

    <!-- INTERACTIVE STORE SCRIPT -->
    <script>
        // High-Demand Products with 3 distinct real image perspectives (All 15 Retail Research Peptides)
        const products = [
            { 
                id: 1, code: "tirzepatide", name: "Tirzepatide (Dual GIP/GLP-1)", cat: "Metabolic & Incretin Signaling (US #1)", group: "Metabolic", regPrice: 140.00, salePrice: 112.00, 
                sizes: ["5mg", "10mg", "15mg", "30mg"], cas: "2023788-19-2", purity: "99.4%",
                images: [
                    { url: "assets/images/products/tirzepatide-photo.jpg", caption: "View 1/3: Tirzepatide 10mg Lyophilized Vial" },
                    { url: "assets/images/products/tirzepatide-coa.svg", caption: "View 2/3: HPLC Chromatography CoA (99.4%)" },
                    { url: "assets/images/products/tirzepatide-pack.svg", caption: "View 3/3: Cold-Chain Insulated Box (-20°C)" }
                ]
            },
            { 
                id: 2, code: "retatrutide", name: "Retatrutide (Triple GGG Agonist)", cat: "Triple GLP-1/GIP/GCGR Signaling", group: "Metabolic", regPrice: 175.00, salePrice: 139.00, 
                sizes: ["5mg", "10mg", "15mg"], cas: "2381089-83-2", purity: "99.3%",
                images: [
                    { url: "assets/images/products/retatrutide-photo.jpg", caption: "View 1/3: Retatrutide 10mg Lyophilized Vial" },
                    { url: "assets/images/products/retatrutide-coa.svg", caption: "View 2/3: HPLC Chromatography CoA (99.3%)" },
                    { url: "assets/images/products/retatrutide-pack.svg", caption: "View 3/3: Cold-Chain Insulated Box (-20°C)" }
                ]
            },
            { 
                id: 3, code: "semaglutide", name: "Semaglutide (Selective GLP-1)", cat: "Metabolic Incretin Benchmark", group: "Metabolic", regPrice: 115.00, salePrice: 89.00, 
                sizes: ["2mg", "5mg", "10mg"], cas: "910463-68-2", purity: "99.5%",
                images: [
                    { url: "assets/images/products/semaglutide-vial.svg", caption: "View 1/3: Semaglutide 5mg Lyophilized Vial" },
                    { url: "assets/images/products/semaglutide-coa.svg", caption: "View 2/3: HPLC Chromatography CoA (99.5%)" },
                    { url: "assets/images/products/semaglutide-pack.svg", caption: "View 3/3: Cold-Chain Insulated Box (-20°C)" }
                ]
            },
            { 
                id: 4, code: "cagrilintide", name: "Cagrilintide (Amylin Analog)", cat: "Dual Amylin/Calcitonin Receptor Ligand", group: "Metabolic", regPrice: 130.00, salePrice: 99.00, 
                sizes: ["5mg", "10mg"], cas: "1415456-99-3", purity: "99.2%",
                images: [
                    { url: "assets/images/products/cagrilintide-vial.svg", caption: "View 1/3: Cagrilintide 5mg Lyophilized Vial" },
                    { url: "assets/images/products/cagrilintide-coa.svg", caption: "View 2/3: HPLC Chromatography CoA (99.2%)" },
                    { url: "assets/images/products/cagrilintide-pack.svg", caption: "View 3/3: Cold-Chain Insulated Box (-20°C)" }
                ]
            },
            { 
                id: 5, code: "bpc157", name: "BPC-157 Pentadecapeptide", cat: "Cellular & Tissue Repair Benchmark", group: "Healing", regPrice: 52.00, salePrice: 39.00, 
                sizes: ["5mg", "10mg"], cas: "137525-51-0", purity: "99.4%",
                images: [
                    { url: "assets/images/products/bpc157-vial.svg", caption: "View 1/3: BPC-157 5mg Lyophilized Vial" },
                    { url: "assets/images/products/bpc157-coa.svg", caption: "View 2/3: HPLC Chromatography CoA (99.4%)" },
                    { url: "assets/images/products/bpc157-pack.svg", caption: "View 3/3: Cold-Chain Insulated Box (-20°C)" }
                ]
            },
            { 
                id: 6, code: "tb500", name: "TB-500 (Thymosin Beta-4)", cat: "Actin Filament Polymerization", group: "Healing", regPrice: 58.00, salePrice: 44.00, 
                sizes: ["5mg", "10mg"], cas: "77591-33-4", purity: "99.5%",
                images: [
                    { url: "assets/images/products/tb500-vial.svg", caption: "View 1/3: TB-500 5mg Lyophilized Vial" },
                    { url: "assets/images/products/tb500-coa.svg", caption: "View 2/3: HPLC Chromatography CoA (99.5%)" },
                    { url: "assets/images/products/tb500-pack.svg", caption: "View 3/3: Cold-Chain Insulated Box (-20°C)" }
                ]
            },
            { 
                id: 7, code: "ghkcu", name: "GHK-Cu Copper Tripeptide", cat: "Copper Chelated Matrix Remodeling", group: "Healing", regPrice: 42.00, salePrice: 32.00, 
                sizes: ["50mg", "100mg"], cas: "49557-75-7", purity: "99.6%",
                images: [
                    { url: "assets/images/products/ghkcu-photo.jpg", caption: "View 1/3: GHK-Cu 50mg Royal Blue Powder Vial" },
                    { url: "assets/images/products/ghkcu-coa.svg", caption: "View 2/3: HPLC Chromatography CoA (99.6%)" },
                    { url: "assets/images/products/ghkcu-pack.svg", caption: "View 3/3: Cold-Chain Insulated Box (-20°C)" }
                ]
            },
            { 
                id: 8, code: "cjcipam", name: "CJC-1295 + Ipamorelin Blend", cat: "Dual Synergistic GH Secretagogue", group: "Secretagogue", regPrice: 85.00, salePrice: 64.00, 
                sizes: ["10mg Dual"], cas: "Mod GRF/Ipam", purity: "99.3%",
                images: [
                    { url: "assets/images/products/cjcipam-vial.svg", caption: "View 1/3: CJC+Ipam 10mg Co-Lyophilized Vial" },
                    { url: "assets/images/products/cjcipam-coa.svg", caption: "View 2/3: HPLC Dual Peak CoA (99.3%)" },
                    { url: "assets/images/products/cjcipam-pack.svg", caption: "View 3/3: Cold-Chain Insulated Box (-20°C)" }
                ]
            },
            { 
                id: 9, code: "tesamorelin", name: "Tesamorelin (Trans-3-Hexenoyl)", cat: "Lipodystrophy & GHRH Axis", group: "Secretagogue", regPrice: 78.00, salePrice: 59.00, 
                sizes: ["2mg", "5mg", "10mg"], cas: "218949-48-5", purity: "99.2%",
                images: [
                    { url: "assets/images/products/tesamorelin-vial.svg", caption: "View 1/3: Tesamorelin 5mg Lyophilized Vial" },
                    { url: "assets/images/products/tesamorelin-coa.svg", caption: "View 2/3: HPLC Chromatography CoA (99.2%)" },
                    { url: "assets/images/products/tesamorelin-pack.svg", caption: "View 3/3: Cold-Chain Insulated Box (-20°C)" }
                ]
            },
            { 
                id: 10, code: "mk677", name: "MK-677 Ibutamoren Mesylate", cat: "Oral Bioavailable Ghrelin Mimetic", group: "Secretagogue", regPrice: 65.00, salePrice: 49.00, 
                sizes: ["30mL Solution (25mg/mL)"], cas: "159752-10-0", purity: "99.5%",
                images: [
                    { url: "assets/images/products/mk677-photo.jpg", caption: "View 1/3: MK-677 30mL Amber Dropper Bottle" },
                    { url: "assets/images/products/mk677-coa.svg", caption: "View 2/3: HPLC Analytical Assay CoA (99.5%)" },
                    { url: "assets/images/products/mk677-pack.svg", caption: "View 3/3: Padded Laboratory Courier Pack" }
                ]
            },
            { 
                id: 11, code: "motsc", name: "MOTS-c Mitochondrial Peptide", cat: "Longevity & Cellular Energy", group: "Longevity", regPrice: 75.00, salePrice: 56.00, 
                sizes: ["5mg", "10mg"], cas: "12S rRNA", purity: "99.3%",
                images: [
                    { url: "assets/images/products/motsc-vial.svg", caption: "View 1/3: MOTS-c 10mg Amber Protective Vial" },
                    { url: "assets/images/products/motsc-coa.svg", caption: "View 2/3: HPLC Chromatography CoA (99.3%)" },
                    { url: "assets/images/products/motsc-pack.svg", caption: "View 3/3: Cold-Chain Insulated Box (-20°C)" }
                ]
            },
            { 
                id: 12, code: "epithalon", name: "Epithalon (Pineal Tetrapeptide)", cat: "Telomerase Induction & Circadian", group: "Longevity", regPrice: 60.00, salePrice: 45.00, 
                sizes: ["10mg", "20mg", "50mg"], cas: "307297-39-8", purity: "99.4%",
                images: [
                    { url: "assets/images/products/epithalon-vial.svg", caption: "View 1/3: Epithalon 10mg Lyophilized Vial" },
                    { url: "assets/images/products/epithalon-coa.svg", caption: "View 2/3: HPLC Chromatography CoA (99.4%)" },
                    { url: "assets/images/products/epithalon-pack.svg", caption: "View 3/3: Cold-Chain Insulated Box (-20°C)" }
                ]
            },
            { 
                id: 13, code: "semax", name: "Semax ACTH(4-10) Fragment", cat: "Nootropic BDNF Hippocampal Ligand", group: "Longevity", regPrice: 55.00, salePrice: 42.00, 
                sizes: ["30mg Metered Spray"], cas: "80714-61-0", purity: "99.5%",
                images: [
                    { url: "assets/images/products/semax-photo.jpg", caption: "View 1/3: Semax 10mL Amber Nasal Spray" },
                    { url: "assets/images/products/semax-coa.svg", caption: "View 2/3: HPLC Chromatography CoA (99.5%)" },
                    { url: "assets/images/products/semax-pack.svg", caption: "View 3/3: Cold-Chain Insulated Box (-20°C)" }
                ]
            },
            { 
                id: 14, code: "selank", name: "Selank Tuftsin Heptapeptide", cat: "Anxiolytic GABAergic Modulator", group: "Longevity", regPrice: 45.00, salePrice: 34.00, 
                sizes: ["10mg Metered Spray"], cas: "129954-34-3", purity: "99.6%",
                images: [
                    { url: "assets/images/products/selank-vial.svg", caption: "View 1/3: Selank 10mL Amber Nasal Spray" },
                    { url: "assets/images/products/selank-coa.svg", caption: "View 2/3: HPLC Chromatography CoA (99.6%)" },
                    { url: "assets/images/products/selank-pack.svg", caption: "View 3/3: Cold-Chain Insulated Box (-20°C)" }
                ]
            },
            { 
                id: 15, code: "pt141", name: "PT-141 Bremelanotide", cat: "Central Melanocortin MC3R/MC4R", group: "Longevity", regPrice: 62.00, salePrice: 47.00, 
                sizes: ["10mg"], cas: "189745-56-8", purity: "99.4%",
                images: [
                    { url: "assets/images/products/pt141-vial.svg", caption: "View 1/3: PT-141 10mg Lyophilized Vial" },
                    { url: "assets/images/products/pt141-coa.svg", caption: "View 2/3: HPLC Chromatography CoA (99.4%)" },
                    { url: "assets/images/products/pt141-pack.svg", caption: "View 3/3: Cold-Chain Insulated Box (-20°C)" }
                ]
            }
        ];

        // Institutional & Pharma Products ($5,000 to $23,450)
        const institutionalProducts = [
            { 
                id: 16, code: "library384", name: "Custom 384-Peptide Scanning Library", cat: "Institutional Screening Array", group: "Institutional", regPrice: 27500.00, salePrice: 23450.00, 
                format: "4x 96-Well Format (384 Sequences)", note: "100% Electrospray MS Mass Validation • Dry-Ice Air Cargo Included",
                images: [
                    { url: "assets/images/products/library384-photo.jpg", caption: "View 1/3: 384-Well Robotic Microplate Array" },
                    { url: "assets/images/products/library384-coa.svg", caption: "View 2/3: 100% Electrospray MS Plate Report" },
                    { url: "assets/images/products/library384-pack.svg", caption: "View 3/3: Cryogenic Nitrogen Air Freight Crate" }
                ]
            },
            { 
                id: 17, code: "bulk10g", name: "Bulk cGMP-Grade Synthesis Lot (10 Grams)", cat: "Preclinical Master Lot", group: "Institutional", regPrice: 18500.00, salePrice: 14900.00, 
                format: "10.0 Grams (10,000mg) Single Lot", note: "Purity ≥98.5% • Endotoxin <5 EU/mg • TFA <1.0% Certified",
                images: [
                    { url: "assets/images/products/bulk10g-photo.jpg", caption: "View 1/3: 100mL Heavy Amber Bulk Reagent Jar" },
                    { url: "assets/images/products/bulk10g-coa.svg", caption: "View 2/3: cGMP Endotoxin & Purity Analysis" },
                    { url: "assets/images/products/bulk10g-pack.svg", caption: "View 3/3: Vacuum Cleanroom Freight Container" }
                ]
            },
            { 
                id: 18, code: "kinase96", name: "Kinase Target Master Profiling Suite (96)", cat: "Enzymatic Screening", group: "Institutional", regPrice: 11800.00, salePrice: 9450.00, 
                format: "96 Phosphorylated Motifs", note: "Systematic Kinase Selectivity & Catalytic Affinity Assay",
                images: [
                    { url: "assets/images/products/kinase96-vial.svg", caption: "View 1/3: 96-Well Microplate Kinase Suite" },
                    { url: "assets/images/products/kinase96-coa.svg", caption: "View 2/3: HPLC Chromatography Purity Dossier" },
                    { url: "assets/images/products/kinase96-pack.svg", caption: "View 3/3: Temperature-Monitored Flight Pack" }
                ]
            }
        ];

        // Currency Rates (USD and EUR ONLY)
        const rates = {
            'USD': { symbol: '$', rate: 1.0 },
            'EUR': { symbol: '€', rate: 0.92 }
        };

        let currentCurrency = 'USD';
        let currentFilter = 'all';
        let cart = [];
        let activePaymentDiscount = 0.10;
        const carouselStates = {};

        function getProductData(id) {
            return products.find(x => x.id === id) || institutionalProducts.find(x => x.id === id);
        }

        window.goToSlide = function(id, slideIndex) {
            const track = document.getElementById('track-' + id);
            const cap = document.getElementById('cap-' + id);
            const pips = document.getElementById('pips-' + id);
            const prod = getProductData(id);
            if (!track || !prod) return;

            carouselStates[id] = slideIndex;
            track.style.transform = `translateX(-${slideIndex * 33.333}%)`;
            if (cap && prod.images[slideIndex]) {
                cap.textContent = prod.images[slideIndex].caption;
            }
            if (pips) {
                pips.querySelectorAll('.clean-pip').forEach((p, idx) => {
                    p.classList.toggle('active', idx === slideIndex);
                });
            }
        };

        window.slideNext = function(id) {
            let current = carouselStates[id] || 0;
            current = (current + 1) % 3;
            goToSlide(id, current);
        };

        window.slidePrev = function(id) {
            let current = carouselStates[id] || 0;
            current = (current - 1 + 3) % 3;
            goToSlide(id, current);
        };

        window.togglePill = function(el) {
            el.parentElement.querySelectorAll('.variant-pill-item').forEach(p => p.classList.remove('active'));
            el.classList.add('active');
        };

        window.filterCategory = function(group, btn) {
            document.querySelectorAll('.filter-pill').forEach(b => b.classList.remove('active'));
            if (btn) btn.classList.add('active');
            currentFilter = group;
            renderProducts();
        };

        function renderProducts() {
            const grid = document.getElementById('product-grid');
            grid.innerHTML = '';
            const curr = rates[currentCurrency];

            const filtered = currentFilter === 'all' 
                ? products 
                : products.filter(p => p.group === currentFilter);

            filtered.forEach((p) => {
                const regConverted = (p.regPrice * curr.rate).toFixed(2);
                const saleConverted = (p.salePrice * curr.rate).toFixed(2);
                const btcPrice = (p.salePrice * 0.90 * curr.rate).toFixed(2);
                const discPercent = Math.round((1 - p.salePrice / p.regPrice) * 100);

                const card = document.createElement('div');
                card.className = 'clean-product-card';
                card.innerHTML = `
                    <div class="card-meta-top">
                        <span class="sale-badge-pill">SALE -${discPercent}%</span>
                        <div class="purity-badge-pill">HPLC &ge; ${p.purity}</div>
                    </div>

                    <!-- 3-IMAGE REACTIVE HOVER CAROUSEL -->
                    <div class="card-carousel-box" id="carousel-${p.id}">
                        <div class="carousel-track-flex" id="track-${p.id}">
                            ${p.images.map(img => `
                                <div class="carousel-slide-item">
                                    <img src="${img.url}" alt="${p.name}" loading="lazy">
                                </div>
                            `).join('')}
                        </div>
                        <div class="clean-arrow prev" onmouseenter="slidePrev(${p.id})" onclick="slidePrev(${p.id})">&lsaquo;</div>
                        <div class="clean-arrow next" onmouseenter="slideNext(${p.id})" onclick="slideNext(${p.id})">&rsaquo;</div>
                        
                        <div class="view-caption-pill" id="cap-${p.id}">${p.images[0].caption}</div>
                        
                        <div class="card-pips-row" id="pips-${p.id}">
                            <span class="clean-pip active" onmouseenter="goToSlide(${p.id}, 0)" onclick="goToSlide(${p.id}, 0)"></span>
                            <span class="clean-pip" onmouseenter="goToSlide(${p.id}, 1)" onclick="goToSlide(${p.id}, 1)"></span>
                            <span class="clean-pip" onmouseenter="goToSlide(${p.id}, 2)" onclick="goToSlide(${p.id}, 2)"></span>
                        </div>
                    </div>

                    <h3 class="card-title-text">${p.name}</h3>
                    <p class="card-cat-text">${p.cat}</p>
                    <div class="card-specs-bar">
                        <span>CAS: ${p.cas}</span> &bull; <span>Purity &ge;99%</span>
                    </div>
                    <div class="crypto-rebate-tag">⚡ Pay with BTC: ${curr.symbol}${btcPrice} (-10%)</div>
                    
                    <div style="margin-bottom:8px;font-size:12px;color:#64748B;">
                        <strong>Select Scale:</strong>
                        <div class="variant-pills-wrap">
                            ${p.sizes.map((s, idx) => `<span class="variant-pill-item ${idx === 0 ? 'active' : ''}" onclick="togglePill(this)">${s}</span>`).join('')}
                        </div>
                    </div>
                    <div>
                        <select class="pack-select-clean">
                            <option value="1">1 Vial (Standard)</option>
                            <option value="3">3 Vials (10% Off)</option>
                            <option value="5">5 Vials (15% Off)</option>
                            <option value="10">10 Vials Kit (25% Off Bulk)</option>
                        </select>
                    </div>
                    <div class="card-pricing-row">
                        <div>
                            <span class="price-strike-gray">${curr.symbol}${regConverted}</span>
                            <span class="price-sale-bold">${curr.symbol}${saleConverted}</span>
                        </div>
                        <button class="add-cart-btn-clean" onclick="addToCart(${p.id})">+ Add to Cart</button>
                    </div>
                `;
                grid.appendChild(card);
            });

            // RENDER INSTITUTIONAL SECTION
            const instGrid = document.getElementById('institutional-grid');
            instGrid.innerHTML = '';
            institutionalProducts.forEach((ip) => {
                const regConverted = (ip.regPrice * curr.rate).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
                const saleConverted = (ip.salePrice * curr.rate).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
                const wirePrice = (ip.salePrice * 0.90 * curr.rate).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });

                const card = document.createElement('div');
                card.className = 'inst-card';
                card.innerHTML = `
                    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
                        <span style="background:#D97706;color:#000;font-size:10px;font-weight:900;padding:3px 8px;border-radius:12px;">INSTITUTIONAL LOT</span>
                        <div style="background:#1E293B;color:#64FFDA;padding:2px 8px;border-radius:10px;font-size:11px;font-weight:700;">${ip.format}</div>
                    </div>

                    <div class="card-carousel-box" id="carousel-${ip.id}" style="background:#0A192F;">
                        <div class="carousel-track-flex" id="track-${ip.id}">
                            ${ip.images.map(img => `
                                <div class="carousel-slide-item">
                                    <img src="${img.url}" alt="${ip.name}" loading="lazy" style="background:#0A192F;">
                                </div>
                            `).join('')}
                        </div>
                        <div class="clean-arrow prev" onmouseenter="slidePrev(${ip.id})" onclick="slidePrev(${ip.id})">&lsaquo;</div>
                        <div class="clean-arrow next" onmouseenter="slideNext(${ip.id})" onclick="slideNext(${ip.id})">&rsaquo;</div>
                        <div class="view-caption-pill" id="cap-${ip.id}" style="background:#112240;color:#fff;border-color:#233554;">${ip.images[0].caption}</div>
                        <div class="card-pips-row" id="pips-${ip.id}">
                            <span class="clean-pip active" onmouseenter="goToSlide(${ip.id}, 0)" onclick="goToSlide(${ip.id}, 0)"></span>
                            <span class="clean-pip" onmouseenter="goToSlide(${ip.id}, 1)" onclick="goToSlide(${ip.id}, 1)"></span>
                            <span class="clean-pip" onmouseenter="goToSlide(${ip.id}, 2)" onclick="goToSlide(${ip.id}, 2)"></span>
                        </div>
                    </div>

                    <h3 style="color:#fff;font-size:18px;margin:10px 0 6px 0;font-family:var(--font-heading);">${ip.name}</h3>
                    <p style="color:#8892B0;font-size:12px;margin:0 0 10px 0;">${ip.cat}</p>
                    <div style="background:#0A192F;color:#CCD6F6;font-size:11px;padding:8px 10px;border-radius:4px;margin-bottom:12px;">
                        <span>${ip.note}</span>
                    </div>
                    <div style="background:#172A45;color:#FCD34D;padding:6px 10px;border-radius:4px;font-size:11px;font-weight:700;margin-bottom:15px;">
                        ⚡ Wire / SWIFT / BTC 10% Off: ${curr.symbol}${wirePrice}
                    </div>
                    <div style="margin-top:auto;display:flex;justify-content:space-between;align-items:center;border-top:1px solid #233554;padding-top:14px;">
                        <div>
                            <span style="color:#64748B;text-decoration:line-through;font-size:13px;margin-right:6px;">${curr.symbol}${regConverted}</span>
                            <span style="color:#64FFDA;font-size:22px;font-weight:900;">${curr.symbol}${saleConverted}</span>
                        </div>
                        <button style="background:#64FFDA;color:#0A192F;font-weight:900;padding:10px 16px;border-radius:6px;border:none;cursor:pointer;" onclick="addToCart(${ip.id})">+ Requisition Order</button>
                    </div>
                `;
                instGrid.appendChild(card);
            });
        }

        window.addToCart = function(productId) {
            const prod = getProductData(productId);
            if (!prod) return;
            cart.push(prod);
            updateCartUI();
            openCart();
        };

        function updateCartUI() {
            document.getElementById('cart-counter').textContent = cart.length;
            document.getElementById('cart-drawer-count').textContent = cart.length;
            const container = document.getElementById('cart-items-container');
            const curr = rates[currentCurrency];

            if (cart.length === 0) {
                container.innerHTML = '<p style="color:#64748B;text-align:center;margin-top:40px;">Your research cart is empty.</p>';
                document.getElementById('cart-subtotal-val').textContent = curr.symbol + "0.00";
                return;
            }

            let subtotal = 0;
            container.innerHTML = '';
            cart.forEach((item, idx) => {
                const itemPrice = item.salePrice * curr.rate;
                subtotal += itemPrice;
                const row = document.createElement('div');
                row.className = 'cart-item-clean';
                row.innerHTML = `
                    <div>
                        <h4>${item.name}</h4>
                        <span>Lyophilized Analytical Reagent &bull; Purity &ge;99%</span>
                    </div>
                    <div style="display:flex;align-items:center;gap:12px;">
                        <span style="font-weight:800;color:#059669;font-size:15px;">${curr.symbol}${itemPrice.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</span>
                        <button onclick="removeFromCart(${idx})" style="background:none;border:none;color:#EF4444;cursor:pointer;font-size:18px;font-weight:bold;">&times;</button>
                    </div>
                `;
                container.appendChild(row);
            });

            document.getElementById('cart-subtotal-val').textContent = curr.symbol + subtotal.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
            recalculateCheckoutTotal(subtotal);
        }

        function recalculateCheckoutTotal(rawSubtotal) {
            if (rawSubtotal === undefined) {
                const curr = rates[currentCurrency];
                rawSubtotal = cart.reduce((acc, item) => acc + item.salePrice * curr.rate, 0);
            }
            const curr = rates[currentCurrency];
            const discountedTotal = rawSubtotal * (1 - activePaymentDiscount);
            document.getElementById('chk-total').textContent = curr.symbol + discountedTotal.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
            
            const discountBadge = document.getElementById('payment-discount-applied');
            if (activePaymentDiscount === 0.10) {
                discountBadge.style.display = 'block';
                discountBadge.textContent = '⚡ 10% CRYPTO DISCOUNT ACTIVE';
                discountBadge.style.background = '#15803D';
            } else if (activePaymentDiscount === 0.05) {
                discountBadge.style.display = 'block';
                discountBadge.textContent = '⚡ 5% WIRE DISCOUNT ACTIVE';
                discountBadge.style.background = '#0369A1';
            } else {
                discountBadge.style.display = 'none';
            }
        }

        window.removeFromCart = function(index) {
            cart.splice(index, 1);
            updateCartUI();
        };

        function openCart() {
            document.getElementById('cart-drawer').classList.add('open');
            document.getElementById('cart-overlay').classList.add('active');
        }

        function closeCart() {
            document.getElementById('cart-drawer').classList.remove('open');
            document.getElementById('cart-overlay').classList.remove('active');
        }

        document.getElementById('open-cart-btn').addEventListener('click', openCart);
        document.getElementById('close-cart-btn').addEventListener('click', closeCart);
        document.getElementById('cart-overlay').addEventListener('click', closeCart);

        // Checkout Modal
        document.getElementById('checkout-btn').addEventListener('click', () => {
            if (cart.length === 0) {
                alert("Please add research compounds to your cart before proceeding.");
                return;
            }
            closeCart();
            recalculateCheckoutTotal();
            document.getElementById('checkout-modal').classList.add('active');
        });

        document.getElementById('modal-close-btn').addEventListener('click', () => {
            document.getElementById('checkout-modal').classList.remove('active');
        });

        // Gateway Tabs with Payment Discounts
        document.querySelectorAll('.modal-tab-btn').forEach(tab => {
            tab.addEventListener('click', () => {
                document.querySelectorAll('.modal-tab-btn').forEach(t => t.classList.remove('active'));
                document.querySelectorAll('.modal-tab-pane').forEach(c => c.classList.remove('active'));
                tab.classList.add('active');
                document.getElementById(tab.getAttribute('data-tab')).classList.add('active');
                
                activePaymentDiscount = parseFloat(tab.getAttribute('data-discount')) || 0;
                recalculateCheckoutTotal();
            });
        });

        // Submit Order
        document.getElementById('submit-order-btn').addEventListener('click', () => {
            document.getElementById('checkout-modal').classList.remove('active');
            alert("✅ Research Requisition Received!\\n\\nOrder #1043 has been authorized with payment discount applied. Confirmation email with HPLC COA certificate and international tracking dispatched.");
            cart = [];
            updateCartUI();
        });

        // Currency Change (USD & EUR ONLY)
        document.getElementById('preview-currency').addEventListener('change', (e) => {
            currentCurrency = e.target.value;
            renderProducts();
            updateCartUI();
        });

        // Tracking Form Simulation
        document.getElementById('standalone-tracking-form').addEventListener('submit', (e) => {
            e.preventDefault();
            const val = document.getElementById('track-input').value;
            document.getElementById('dyn-order-id').textContent = '#' + val;
            document.getElementById('telemetry-card').scrollIntoView({ behavior: 'smooth' });
        });

        // Init
        renderProducts();
    </script>
</body>
</html>
"""

dest = r"c:\Users\DATA ENG. OLA\Desktop\Riffmax Technology\riffmax-org-agent\phoenicspeptide\standalone-preview\index.html"
with open(dest, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Successfully generated clean clinical medical preview at {dest}")
