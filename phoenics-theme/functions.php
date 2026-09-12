<?php
/**
 * Phoenics Peptide Theme Functions
 */

if (!defined('ABSPATH')) {
    exit;
}

function phoenics_theme_setup() {
    // Add default WordPress features
    add_theme_support('title-tag');
    add_theme_support('post-thumbnails');
    add_theme_support('custom-logo', array(
        'height'      => 80,
        'width'       => 280,
        'flex-height' => true,
        'flex-width'  => true,
    ));
    add_theme_support('html5', array('search-form', 'comment-form', 'comment-list', 'gallery', 'caption', 'style', 'script'));

    // WooCommerce Theme Support
    add_theme_support('woocommerce', array(
        'thumbnail_image_width' => 450,
        'single_image_width'    => 650,
        'product_grid'          => array(
            'default_rows'    => 4,
            'min_rows'        => 2,
            'max_rows'        => 8,
            'default_columns' => 4,
            'min_columns'     => 2,
            'max_columns'     => 5,
        ),
    ));
    add_theme_support('wc-product-gallery-zoom');
    add_theme_support('wc-product-gallery-lightbox');
    add_theme_support('wc-product-gallery-slider');

    // Register Nav Menus
    register_nav_menus(array(
        'primary'  => __('Primary Header Menu', 'phoenics-theme'),
        'catalog'  => __('Catalog Categories Mega Menu', 'phoenics-theme'),
        'footer'   => __('Footer Navigation', 'phoenics-theme'),
    ));
}
add_action('after_setup_theme', 'phoenics_theme_setup');

/**
 * Enqueue Styles and Scripts
 */
function phoenics_enqueue_assets() {
    // Google Fonts
    wp_enqueue_style('phoenics-fonts', 'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Montserrat:wght@600;700;800;900&family=Space+Mono:wght@400;700&display=swap', array(), null);

    // Theme Styles
    wp_enqueue_style('phoenics-main-style', get_template_directory_uri() . '/style.css', array(), '1.0.0');
    wp_enqueue_style('phoenics-custom-css', get_template_directory_uri() . '/assets/css/main.css', array('phoenics-main-style'), '1.0.0');

    if (class_exists('WooCommerce')) {
        wp_enqueue_style('phoenics-woo-css', get_template_directory_uri() . '/assets/css/woocommerce.css', array('phoenics-custom-css'), '1.0.0');
    }

    // Main JS
    wp_enqueue_script('phoenics-main-js', get_template_directory_uri() . '/assets/js/main.js', array('jquery'), '1.0.0', true);

    wp_localize_script('phoenics-main-js', 'phoenics_vars', array(
        'ajax_url'    => admin_url('admin-ajax.php'),
        'cart_url'    => class_exists('WooCommerce') ? wc_get_cart_url() : '#',
        'currency'    => class_exists('WooCommerce') ? get_woocommerce_currency() : 'USD',
        'symbol'      => class_exists('WooCommerce') ? get_woocommerce_currency_symbol() : '$',
    ));
}
add_action('wp_enqueue_scripts', 'phoenics_enqueue_assets');

/**
 * Cart Item Count Dynamic AJAX Fragment
 */
function phoenics_cart_count_fragments($fragments) {
    if (!class_exists('WooCommerce')) return $fragments;
    
    ob_start();
    ?>
    <span class="cart-badge-count">
        <?php echo WC()->cart->get_cart_contents_count(); ?>
    </span>
    <?php
    $fragments['span.cart-badge-count'] = ob_get_clean();
    return $fragments;
}
add_filter('woocommerce_add_to_cart_fragments', 'phoenics_cart_count_fragments');

/**
 * Automatic Compliance & Lab Testing Notice on Single Product
 */
function phoenics_display_product_compliance_badge() {
    ?>
    <div class="product-lab-compliance-card">
        <div class="badge-row">
            <span class="cert-pill">🔬 HPLC/MS Purity &gt;99%</span>
            <span class="cert-pill cold">❄️ Cold-Chain Bio-Packed</span>
            <span class="cert-pill seal">🛡️ Third-Party Batch Verified</span>
        </div>
        <div class="disclaimer-alert">
            <strong>LABORATORY RESEARCH NOTICE:</strong> This chemical peptide compound is synthesized and supplied strictly for in-vitro analytical, physiological, and scientific research. Not for human, veterinary, therapeutic, or diagnostic administration.
        </div>
    </div>
    <?php
}
add_action('woocommerce_single_product_summary', 'phoenics_display_product_compliance_badge', 25);
