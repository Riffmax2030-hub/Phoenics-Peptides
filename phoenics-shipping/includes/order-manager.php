<?php
/**
 * Order Shipping & Tracking Manager
 */

if (!defined('ABSPATH')) {
    exit;
}

class Phoenics_Order_Manager {

    public function __construct() {
        // Add metabox to WooCommerce order edit screen
        add_action('add_meta_boxes', array($this, 'add_shipping_metabox'));
        add_action('woocommerce_process_shop_order_meta', array($this, 'save_shipping_meta'));
        
        // Show tracking in WooCommerce customer view order page
        add_action('woocommerce_order_details_after_order_table', array($this, 'display_tracking_in_customer_order'), 10, 1);

        // AJAX tracking lookup for public search
        add_action('wp_ajax_phoenics_lookup_tracking', array($this, 'ajax_lookup_tracking'));
        add_action('wp_ajax_nopriv_phoenics_lookup_tracking', array($this, 'ajax_lookup_tracking'));
    }

    public function add_shipping_metabox() {
        $screen = class_exists('\Automattic\WooCommerce\Internal\DataStores\Orders\CustomOrdersTableController') && 
                  wc_get_container()->get(\Automattic\WooCommerce\Internal\DataStores\Orders\CustomOrdersTableController::class)->custom_orders_table_usage_is_enabled()
                  ? wc_get_page_screen_id('shop-order') : 'shop_order';

        add_meta_box(
            'phoenics_shipping_details',
            __('❄️ Phoenics Cold-Chain & Global Shipment Tracking', 'phoenics-shipping'),
            array($this, 'render_shipping_metabox'),
            $screen,
            'side',
            'high'
        );
    }

    public function render_shipping_metabox($post_or_order_object) {
        $order = ($post_or_order_object instanceof WP_Post) ? wc_get_order($post_or_order_object->ID) : $post_or_order_object;
        if (!$order) return;

        $carrier = $order->get_meta('_phoenics_carrier', true);
        $tracking_number = $order->get_meta('_phoenics_tracking_number', true);
        $ship_date = $order->get_meta('_phoenics_ship_date', true);
        $est_delivery = $order->get_meta('_phoenics_est_delivery', true);
        $cold_chain = $order->get_meta('_phoenics_cold_chain', true);
        $origin_hub = $order->get_meta('_phoenics_origin_hub', true);

        wp_nonce_field('phoenics_save_shipping_meta', 'phoenics_shipping_nonce');
        ?>
        <div class="phoenics-meta-panel" style="padding:10px 0;">
            <p>
                <label for="phoenics_carrier"><strong><?php _e('Logistics Carrier:', 'phoenics-shipping'); ?></strong></label><br>
                <select name="phoenics_carrier" id="phoenics_carrier" style="width:100%;margin-top:4px;">
                    <option value="dhl" <?php selected($carrier, 'dhl'); ?>>DHL Express Worldwide</option>
                    <option value="fedex" <?php selected($carrier, 'fedex'); ?>>FedEx International / Priority</option>
                    <option value="usps" <?php selected($carrier, 'usps'); ?>>USPS Priority Mail Insured</option>
                    <option value="canadapost" <?php selected($carrier, 'canadapost'); ?>>Canada Post International</option>
                    <option value="aramex" <?php selected($carrier, 'aramex'); ?>>Aramex Bio-Cargo (Africa/ME)</option>
                    <option value="custom" <?php selected($carrier, 'custom'); ?>>Direct Diplomatic Courier</option>
                </select>
            </p>

            <p>
                <label for="phoenics_tracking_number"><strong><?php _e('Master Tracking Number:', 'phoenics-shipping'); ?></strong></label><br>
                <input type="text" name="phoenics_tracking_number" id="phoenics_tracking_number" value="<?php echo esc_attr($tracking_number); ?>" style="width:100%;" placeholder="e.g. 794918239014" />
            </p>

            <p>
                <label for="phoenics_origin_hub"><strong><?php _e('Fulfillment Hub Origin:', 'phoenics-shipping'); ?></strong></label><br>
                <select name="phoenics_origin_hub" id="phoenics_origin_hub" style="width:100%;">
                    <option value="USA Central (Boston Biotech Park)" <?php selected($origin_hub, 'USA Central (Boston Biotech Park)'); ?>>USA Central (Boston Biotech Park)</option>
                    <option value="European Hub (Frankfurt Bio-Depot)" <?php selected($origin_hub, 'European Hub (Frankfurt Bio-Depot)'); ?>>European Hub (Frankfurt Bio-Depot)</option>
                    <option value="Canada Annex (Toronto Facility)" <?php selected($origin_hub, 'Canada Annex (Toronto Facility)'); ?>>Canada Annex (Toronto Facility)</option>
                    <option value="Asia-Pacific Transit (Singapore Hub)" <?php selected($origin_hub, 'Asia-Pacific Transit (Singapore Hub)'); ?>>Asia-Pacific Transit (Singapore Hub)</option>
                </select>
            </p>

            <p>
                <label for="phoenics_cold_chain"><strong><?php _e('Cold-Chain Temperature Monitor:', 'phoenics-shipping'); ?></strong></label><br>
                <select name="phoenics_cold_chain" id="phoenics_cold_chain" style="width:100%;">
                    <option value="Optimal: Lyophilized Nitrogen Pack (-20°C)" <?php selected($cold_chain, 'Optimal: Lyophilized Nitrogen Pack (-20°C)'); ?>>Lyophilized Nitrogen Pack (-20°C)</option>
                    <option value="Standard: Insulated Foam + Polar Gel (2°C - 8°C)" <?php selected($cold_chain, 'Standard: Insulated Foam + Polar Gel (2°C - 8°C)'); ?>>Insulated Foam + Polar Gel (2°C - 8°C)</option>
                    <option value="Ambient: Desiccant Controlled Pouch (15°C - 25°C)" <?php selected($cold_chain, 'Ambient: Desiccant Controlled Pouch (15°C - 25°C)'); ?>>Ambient Desiccant Pouch (15°C - 25°C)</option>
                </select>
            </p>

            <p>
                <label for="phoenics_est_delivery"><strong><?php _e('Estimated Delivery Window:', 'phoenics-shipping'); ?></strong></label><br>
                <input type="text" name="phoenics_est_delivery" id="phoenics_est_delivery" value="<?php echo esc_attr($est_delivery); ?>" style="width:100%;" placeholder="e.g. 2-3 Business Days" />
            </p>

            <?php if (!empty($tracking_number)): 
                $carrier_url = self::get_carrier_url($carrier, $tracking_number);
            ?>
                <div style="background:#e0f2fe;padding:8px 10px;border-radius:4px;border-left:3px solid #0284c7;margin-top:10px;">
                    <a href="<?php echo esc_url($carrier_url); ?>" target="_blank" style="text-decoration:none;font-weight:600;color:#0369a1;">
                        🔗 <?php _e('Test Live Carrier Tracking Link', 'phoenics-shipping'); ?> &rarr;
                    </a>
                </div>
            <?php endif; ?>
        </div>
        <?php
    }

    public function save_shipping_meta($order_id) {
        if (!isset($_POST['phoenics_shipping_nonce']) || !wp_verify_nonce($_POST['phoenics_shipping_nonce'], 'phoenics_save_shipping_meta')) {
            return;
        }

        $order = wc_get_order($order_id);
        if (!$order) return;

        $old_tracking = $order->get_meta('_phoenics_tracking_number', true);

        $carrier = sanitize_text_field($_POST['phoenics_carrier']);
        $tracking_number = sanitize_text_field($_POST['phoenics_tracking_number']);
        $origin_hub = sanitize_text_field($_POST['phoenics_origin_hub']);
        $cold_chain = sanitize_text_field($_POST['phoenics_cold_chain']);
        $est_delivery = sanitize_text_field($_POST['phoenics_est_delivery']);

        $order->update_meta_data('_phoenics_carrier', $carrier);
        $order->update_meta_data('_phoenics_tracking_number', $tracking_number);
        $order->update_meta_data('_phoenics_origin_hub', $origin_hub);
        $order->update_meta_data('_phoenics_cold_chain', $cold_chain);
        $order->update_meta_data('_phoenics_est_delivery', $est_delivery);
        $order->update_meta_data('_phoenics_ship_date', current_time('mysql'));
        $order->save();

        // If tracking was newly added, fire tracking dispatch email
        if (!empty($tracking_number) && $tracking_number !== $old_tracking) {
            do_action('phoenics_order_shipped_with_tracking', $order_id, $carrier, $tracking_number);
        }
    }

    public static function get_carrier_url($carrier, $tracking_number) {
        switch ($carrier) {
            case 'dhl':
                return "https://www.dhl.com/en/express/tracking.html?AWB=" . rawurlencode($tracking_number);
            case 'fedex':
                return "https://www.fedex.com/fedextrack/?trknbr=" . rawurlencode($tracking_number);
            case 'usps':
                return "https://tools.usps.com/go/TrackConfirmAction?tLabels=" . rawurlencode($tracking_number);
            case 'canadapost':
                return "https://www.canadapost-postescanada.ca/track-reperage/en#/resultList?searchFor=" . rawurlencode($tracking_number);
            case 'aramex':
                return "https://www.aramex.com/us/en/track/results?mode=0&ShipmentNumber=" . rawurlencode($tracking_number);
            default:
                return "https://phoenicspeptide.com/track-order/?tracking_id=" . rawurlencode($tracking_number);
        }
    }

    public function display_tracking_in_customer_order($order) {
        $tracking_number = $order->get_meta('_phoenics_tracking_number', true);
        if (empty($tracking_number)) return;

        $carrier = $order->get_meta('_phoenics_carrier', true);
        $carrier_url = self::get_carrier_url($carrier, $tracking_number);
        $origin_hub = $order->get_meta('_phoenics_origin_hub', true);
        $cold_chain = $order->get_meta('_phoenics_cold_chain', true);
        $est_delivery = $order->get_meta('_phoenics_est_delivery', true);
        ?>
        <div class="phoenics-customer-tracking-box" style="margin:25px 0;padding:20px;background:#0d1b2a;color:#fff;border-radius:8px;box-shadow:0 10px 25px rgba(0,0,0,0.15);">
            <div style="display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid rgba(255,255,255,0.15);padding-bottom:12px;margin-bottom:15px;">
                <h3 style="margin:0;color:#00d2ff;font-family:'Montserrat',sans-serif;font-size:18px;">
                    ❄️ <?php _e('Cold-Chain Shipment Dispatch & Tracking', 'phoenics-shipping'); ?>
                </h3>
                <span style="background:#10b981;color:#fff;padding:3px 10px;border-radius:12px;font-size:12px;font-weight:600;">ACTIVE IN TRANSIT</span>
            </div>

            <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(200px, 1fr));gap:15px;margin-bottom:15px;font-size:14px;">
                <div>
                    <span style="color:#94a3b8;"><?php _e('Carrier:', 'phoenics-shipping'); ?></span><br>
                    <strong><?php echo strtoupper(esc_html($carrier)); ?> Priority Air</strong>
                </div>
                <div>
                    <span style="color:#94a3b8;"><?php _e('Tracking Number:', 'phoenics-shipping'); ?></span><br>
                    <code style="background:#1b263b;color:#38bdf8;padding:2px 6px;border-radius:4px;"><?php echo esc_html($tracking_number); ?></code>
                </div>
                <div>
                    <span style="color:#94a3b8;"><?php _e('Origin Bio-Hub:', 'phoenics-shipping'); ?></span><br>
                    <strong><?php echo esc_html($origin_hub); ?></strong>
                </div>
                <div>
                    <span style="color:#94a3b8;"><?php _e('Temperature Control:', 'phoenics-shipping'); ?></span><br>
                    <span style="color:#fcd34d;"><?php echo esc_html($cold_chain); ?></span>
                </div>
            </div>

            <div style="margin-top:15px;text-align:right;">
                <a href="<?php echo esc_url($carrier_url); ?>" target="_blank" class="button" style="background:#00d2ff;color:#0d1b2a;padding:10px 18px;font-weight:700;border-radius:6px;text-decoration:none;display:inline-block;">
                    <?php _e('View Live Carrier Tracking &rarr;', 'phoenics-shipping'); ?>
                </a>
            </div>
        </div>
        <?php
    }

    public function ajax_lookup_tracking() {
        check_ajax_referer('phoenics_track_nonce', 'nonce');

        $query = isset($_POST['tracking_query']) ? sanitize_text_field($_POST['tracking_query']) : '';
        if (empty($query)) {
            wp_send_json_error(array('message' => 'Please enter an Order ID or Tracking Number.'));
        }

        // Search by Order ID
        $order = wc_get_order($query);
        if (!$order) {
            // Search by meta tracking number
            $orders = wc_get_orders(array(
                'limit'        => 1,
                'meta_key'     => '_phoenics_tracking_number',
                'meta_value'   => $query,
                'meta_compare' => '='
            ));
            if (!empty($orders)) {
                $order = $orders[0];
            }
        }

        if (!$order) {
            wp_send_json_error(array('message' => 'No active shipment found matching this identifier. Please verify your order number or tracking number.'));
        }

        $tracking_number = $order->get_meta('_phoenics_tracking_number', true);
        $carrier = $order->get_meta('_phoenics_carrier', true) ?: 'DHL Express';
        $origin_hub = $order->get_meta('_phoenics_origin_hub', true) ?: 'USA Central Bio-Hub';
        $cold_chain = $order->get_meta('_phoenics_cold_chain', true) ?: 'Lyophilized Dry Gel Pack (-20°C)';
        $est_delivery = $order->get_meta('_phoenics_est_delivery', true) ?: '2-3 Business Days';
        $status = $order->get_status();

        wp_send_json_success(array(
            'order_id'       => $order->get_id(),
            'order_status'   => wc_get_order_status_name($status),
            'carrier'        => strtoupper($carrier),
            'tracking_number'=> $tracking_number ?: 'Pending Dispatch Scan',
            'carrier_url'    => !empty($tracking_number) ? self::get_carrier_url($carrier, $tracking_number) : '#',
            'origin_hub'     => $origin_hub,
            'cold_chain'     => $cold_chain,
            'est_delivery'   => $est_delivery,
            'date_created'   => wc_format_datetime($order->get_date_created())
        ));
    }
}

new Phoenics_Order_Manager();
