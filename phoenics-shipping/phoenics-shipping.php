<?php
/**
 * Plugin Name: Phoenics Global Shipping & Cold-Chain Tracking
 * Plugin URI: https://phoenicspeptide.com
 * Description: Enterprise international shipping management, cold-chain temperature monitoring status, multi-carrier live tracking (FedEx, DHL, USPS, Canada Post, Aramex), and automated customer dispatch emails for Phoenics Peptide.
 * Version: 2.4.0
 * Author: Phoenics Peptide Engineering Team
 * Author URI: https://phoenicspeptide.com
 * Text Domain: phoenics-shipping
 * Domain Path: /languages
 * Requires at least: 5.8
 * Requires PHP: 7.4
 * WC requires at least: 5.0
 * WC tested up to: 8.5
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

define('PHOENICS_SHIPPING_VERSION', '2.4.0');
define('PHOENICS_SHIPPING_PATH', plugin_dir_path(__FILE__));
define('PHOENICS_SHIPPING_URL', plugin_dir_url(__FILE__));

class Phoenics_Shipping_Core {
    private static $instance = null;

    public static function get_instance() {
        if (self::$instance === null) {
            self::$instance = new self();
        }
        return self::$instance;
    }

    private function __construct() {
        // Check if WooCommerce is active
        add_action('plugins_loaded', array($this, 'init_plugin'));
    }

    public function init_plugin() {
        if (!class_exists('WooCommerce')) {
            add_action('admin_notices', array($this, 'woocommerce_missing_notice'));
            return;
        }

        require_once PHOENICS_SHIPPING_PATH . 'includes/order-manager.php';
        require_once PHOENICS_SHIPPING_PATH . 'includes/tracking-emails.php';
        
        if (is_admin()) {
            require_once PHOENICS_SHIPPING_PATH . 'admin/shipping-dashboard.php';
        }

        // Register tracking shortcode
        add_shortcode('phoenics_order_tracking', array($this, 'render_tracking_shortcode'));

        // Enqueue scripts & styles
        add_action('wp_enqueue_scripts', array($this, 'enqueue_public_assets'));
        add_action('admin_enqueue_scripts', array($this, 'enqueue_admin_assets'));

        // Add custom order statuses
        add_filter('wc_order_statuses', array($this, 'register_custom_order_statuses'));
        add_action('init', array($this, 'register_post_statuses'));
    }

    public function register_post_statuses() {
        register_post_status('wc-cold-packing', array(
            'label'                     => _x('Cold-Chain Packaged', 'Order status', 'phoenics-shipping'),
            'public'                    => true,
            'exclude_from_search'       => false,
            'show_in_admin_all_list'    => true,
            'show_in_admin_status_list' => true,
            'label_count'               => _n_noop('Cold-Pack Packaged (%s)', 'Cold-Pack Packaged (%s)', 'phoenics-shipping')
        ));

        register_post_status('wc-in-transit-air', array(
            'label'                     => _x('In Transit (Air Cargo)', 'Order status', 'phoenics-shipping'),
            'public'                    => true,
            'exclude_from_search'       => false,
            'show_in_admin_all_list'    => true,
            'show_in_admin_status_list' => true,
            'label_count'               => _n_noop('In Transit Air (%s)', 'In Transit Air (%s)', 'phoenics-shipping')
        ));

        register_post_status('wc-customs-cleared', array(
            'label'                     => _x('Customs Cleared', 'Order status', 'phoenics-shipping'),
            'public'                    => true,
            'exclude_from_search'       => false,
            'show_in_admin_all_list'    => true,
            'show_in_admin_status_list' => true,
            'label_count'               => _n_noop('Customs Cleared (%s)', 'Customs Cleared (%s)', 'phoenics-shipping')
        ));
    }

    public function register_custom_order_statuses($order_statuses) {
        $new_statuses = array();
        foreach ($order_statuses as $key => $status) {
            $new_statuses[$key] = $status;
            if ('wc-processing' === $key) {
                $new_statuses['wc-cold-packing'] = _x('Cold-Chain Packaged', 'Order status', 'phoenics-shipping');
                $new_statuses['wc-in-transit-air'] = _x('In Transit (Air Cargo)', 'Order status', 'phoenics-shipping');
                $new_statuses['wc-customs-cleared'] = _x('Customs Cleared', 'Order status', 'phoenics-shipping');
            }
        }
        return $new_statuses;
    }

    public function enqueue_public_assets() {
        wp_enqueue_style('phoenics-tracking-css', PHOENICS_SHIPPING_URL . 'assets/css/tracking.css', array(), PHOENICS_SHIPPING_VERSION);
        wp_enqueue_script('phoenics-tracking-js', PHOENICS_SHIPPING_URL . 'assets/js/tracking.js', array('jquery'), PHOENICS_SHIPPING_VERSION, true);
        wp_localize_script('phoenics-tracking-js', 'phoenics_tracking_ajax', array(
            'ajax_url' => admin_url('admin-ajax.php'),
            'nonce'    => wp_create_nonce('phoenics_track_nonce')
        ));
    }

    public function enqueue_admin_assets($hook) {
        if (strpos($hook, 'phoenics-shipping') !== false || strpos($hook, 'shop_order') !== false) {
            wp_enqueue_style('phoenics-shipping-admin-css', PHOENICS_SHIPPING_URL . 'assets/css/admin.css', array(), PHOENICS_SHIPPING_VERSION);
        }
    }

    public function render_tracking_shortcode($atts) {
        ob_start();
        include PHOENICS_SHIPPING_PATH . 'templates/tracking-page.php';
        return ob_get_clean();
    }

    public function woocommerce_missing_notice() {
        echo '<div class="error"><p>' . esc_html__('Phoenics Global Shipping requires WooCommerce to be installed and active.', 'phoenics-shipping') . '</p></div>';
    }
}

Phoenics_Shipping_Core::get_instance();
