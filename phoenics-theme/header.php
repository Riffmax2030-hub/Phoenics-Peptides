<!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
    <meta charset="<?php bloginfo('charset'); ?>">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="profile" href="https://gmpg.org/xfn/11">
    <?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>

<!-- TOP GLOBAL NOTICE & CRYPTO TICKER BAR (USD & EUR ONLY) -->
<div class="top-announcement-bar">
    <div class="container bar-content">
        <div class="announcement-left">
            <span class="pulse-dot"></span>
            <span>🔥 <strong>PROMOTIONAL RESEARCH SALE:</strong> 20% Discount Active Across All Compounds • Free Insured Cold-Chain Freight &gt;$250</span>
        </div>
        <div class="announcement-right">
            <span class="crypto-perk">₿ <strong>Pay with BTC / Crypto:</strong> Extra 10% Off | <strong>Wire:</strong> 5% Off</span>
            <div class="currency-selector-wrapper">
                <select id="phoenics-currency-selector" class="currency-dropdown" aria-label="Select Currency">
                    <option value="USD" selected>USD ($)</option>
                    <option value="EUR">EUR (€)</option>
                </select>
            </div>
        </div>
    </div>
</div>

<!-- MAIN HEADER -->
<header id="site-header" class="main-header">
    <div class="container header-container">
        <!-- BRAND LOGO -->
        <div class="header-logo">
            <a href="<?php echo esc_url(home_url('/')); ?>" class="brand-link">
                <img src="<?php echo get_template_directory_uri(); ?>/assets/images/logo.svg" alt="Phoenics Peptide Logo" class="brand-svg-logo" width="230" height="55" onerror="this.onerror=null; this.src='<?php echo get_template_directory_uri(); ?>/assets/images/logo.jpg';">
            </a>
        </div>

        <!-- DESKTOP NAVIGATION -->
        <nav class="desktop-nav" aria-label="Main Navigation">
            <ul class="nav-menu">
                <li class="menu-item"><a href="<?php echo esc_url(home_url('/')); ?>">Home</a></li>
                <li class="menu-item has-dropdown">
                    <a href="<?php echo esc_url(home_url('/shop/')); ?>">
                        Research Catalog <span class="arrow">&dtrif;</span>
                    </a>
                    <div class="mega-dropdown">
                        <div class="mega-dropdown-grid">
                            <div class="mega-col">
                                <h4>Incretin & Metabolic (US #1)</h4>
                                <ul>
                                    <li><a href="<?php echo esc_url(home_url('/shop/?category=metabolic-incretin')); ?>">Tirzepatide Dual Agonist</a></li>
                                    <li><a href="<?php echo esc_url(home_url('/shop/?category=metabolic-incretin')); ?>">Retatrutide Triple GGG</a></li>
                                    <li><a href="<?php echo esc_url(home_url('/shop/?category=metabolic-incretin')); ?>">Semaglutide GLP-1</a></li>
                                    <li><a href="<?php echo esc_url(home_url('/shop/?category=metabolic-incretin')); ?>">Cagrilintide Amylin Analog</a></li>
                                </ul>
                            </div>
                            <div class="mega-col">
                                <h4>Cellular Repair & GH Axis</h4>
                                <ul>
                                    <li><a href="<?php echo esc_url(home_url('/shop/?category=healing-recovery')); ?>">BPC-157 Pentadecapeptide</a></li>
                                    <li><a href="<?php echo esc_url(home_url('/shop/?category=healing-recovery')); ?>">TB-500 Thymosin Beta-4</a></li>
                                    <li><a href="<?php echo esc_url(home_url('/shop/?category=healing-recovery')); ?>">GHK-Cu Copper Tripeptide</a></li>
                                    <li><a href="<?php echo esc_url(home_url('/shop/?category=growth-hormone')); ?>">CJC-1295 + Ipamorelin Blend</a></li>
                                    <li><a href="<?php echo esc_url(home_url('/shop/?category=growth-hormone')); ?>">Tesamorelin & MK-677</a></li>
                                </ul>
                            </div>
                            <div class="mega-col">
                                <h4>Mitochondrial & Nootropic</h4>
                                <ul>
                                    <li><a href="<?php echo esc_url(home_url('/shop/?category=longevity-mitochondrial')); ?>">MOTS-c Mitochondrial Sequence</a></li>
                                    <li><a href="<?php echo esc_url(home_url('/shop/?category=longevity-mitochondrial')); ?>">Epithalon Telomere Ligand</a></li>
                                    <li><a href="<?php echo esc_url(home_url('/shop/?category=cognitive-nootropic')); ?>">Semax & Selank Heptapeptides</a></li>
                                    <li><a href="<?php echo esc_url(home_url('/shop/?category=receptor-vitality')); ?>">PT-141 Bremelanotide</a></li>
                                </ul>
                            </div>
                            <div class="mega-col highlight-col">
                                <h4>Institutional & Bulk ($23k+)</h4>
                                <p>Custom 384-peptide scanning libraries, epitope mapping suites, and 10-gram cGMP bulk synthesis for university & pharma labs.</p>
                                <a href="<?php echo esc_url(home_url('/shop/?category=institutional')); ?>" class="mega-cta-btn">View Institutional Arrays &rarr;</a>
                            </div>
                        </div>
                    </div>
                </li>
                <li class="menu-item"><a href="<?php echo esc_url(home_url('/research/')); ?>">Science & Protocols</a></li>
                <li class="menu-item"><a href="<?php echo esc_url(home_url('/track-order/')); ?>" class="nav-tracking-link">📦 Track Shipment</a></li>
                <li class="menu-item"><a href="<?php echo esc_url(home_url('/about/')); ?>">About Phoenics</a></li>
                <li class="menu-item"><a href="<?php echo esc_url(home_url('/contact/')); ?>">Contact Lab</a></li>
            </ul>
        </nav>

        <!-- HEADER ACTIONS -->
        <div class="header-actions">
            <!-- PAYMENT DISCOUNTS PILL -->
            <div class="crypto-header-pill" title="10% Discount with Bitcoin / Crypto • 5% with Bank Wire">
                <span class="crypto-sym btc">₿</span>
                <span class="crypto-sym eth">Ξ</span>
                <span class="crypto-txt">10% OFF CRYPTO</span>
            </div>

            <!-- MY ACCOUNT -->
            <a href="<?php echo esc_url(get_permalink(get_option('woocommerce_myaccount_page_id'))); ?>" class="action-btn account-btn" title="Researcher Portal">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
            </a>

            <!-- SHOPPING CART -->
            <?php if (class_exists('WooCommerce')) : ?>
            <a href="<?php echo esc_url(wc_get_cart_url()); ?>" class="action-btn cart-btn" id="header-cart-trigger">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="9" cy="21" r="1"></circle><circle cx="20" cy="21" r="1"></circle><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path></svg>
                <span class="cart-badge-count"><?php echo WC()->cart->get_cart_contents_count(); ?></span>
            </a>
            <?php endif; ?>

            <!-- MOBILE HAMBURGER -->
            <button class="mobile-menu-toggle" id="mobile-nav-btn" aria-label="Toggle Navigation Menu">
                <span></span><span></span><span></span>
            </button>
        </div>
    </div>
</header>

<!-- MOBILE MENU DRAWER -->
<div id="mobile-nav-drawer" class="mobile-drawer">
    <div class="drawer-header">
        <img src="<?php echo get_template_directory_uri(); ?>/assets/images/logo.svg" alt="Phoenics Peptide" width="180">
        <button id="drawer-close-btn">&times;</button>
    </div>
    <ul class="mobile-menu-list">
        <li><a href="<?php echo esc_url(home_url('/')); ?>">Home</a></li>
        <li><a href="<?php echo esc_url(home_url('/shop/')); ?>">All Research Peptides</a></li>
        <li><a href="<?php echo esc_url(home_url('/shop/?category=metabolic-incretin')); ?>">Tirzepatide & Retatrutide</a></li>
        <li><a href="<?php echo esc_url(home_url('/shop/?category=institutional')); ?>">Institutional Libraries ($23k+)</a></li>
        <li><a href="<?php echo esc_url(home_url('/track-order/')); ?>">📦 Track Order & Cold-Chain</a></li>
        <li><a href="<?php echo esc_url(home_url('/research/')); ?>">Science & Reconstitution</a></li>
        <li><a href="<?php echo esc_url(home_url('/contact/')); ?>">Contact Support</a></li>
    </ul>
</div>
<div id="mobile-nav-overlay" class="mobile-nav-overlay"></div>
