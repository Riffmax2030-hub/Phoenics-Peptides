<?php
/**
 * Admin Fulfillment & Global Shipping Console
 */

if (!defined('ABSPATH')) {
    exit;
}

class Phoenics_Admin_Shipping_Dashboard {

    public function __construct() {
        add_action('admin_menu', array($this, 'register_admin_menu'));
        add_action('admin_init', array($this, 'handle_bulk_actions'));
    }

    public function register_admin_menu() {
        add_menu_page(
            __('Phoenics Shipping', 'phoenics-shipping'),
            __('📦 Bio-Logistics', 'phoenics-shipping'),
            'manage_woocommerce',
            'phoenics-shipping-dashboard',
            array($this, 'render_dashboard_page'),
            'dashicons-airplane',
            56
        );
    }

    public function handle_bulk_actions() {
        if (!isset($_POST['phoenics_quick_ship_nonce']) || !wp_verify_nonce($_POST['phoenics_quick_ship_nonce'], 'phoenics_quick_ship_action')) {
            return;
        }

        if (isset($_POST['order_id']) && isset($_POST['tracking_num']) && !empty($_POST['tracking_num'])) {
            $order_id = absint($_POST['order_id']);
            $carrier = sanitize_text_field($_POST['carrier']);
            $tracking = sanitize_text_field($_POST['tracking_num']);
            $cold_chain = sanitize_text_field($_POST['cold_chain']);

            $order = wc_get_order($order_id);
            if ($order) {
                $order->update_meta_data('_phoenics_carrier', $carrier);
                $order->update_meta_data('_phoenics_tracking_number', $tracking);
                $order->update_meta_data('_phoenics_cold_chain', $cold_chain);
                $order->update_status('completed', __('Order packaged and dispatched with carrier tracking.', 'phoenics-shipping'));
                $order->save();

                do_action('phoenics_order_shipped_with_tracking', $order_id, $carrier, $tracking);
                add_settings_error('phoenics_shipping_notices', 'shipped', sprintf(__('Order #%s dispatched and customer notified via email.', 'phoenics-shipping'), $order_id), 'updated');
            }
        }
    }

    public function render_dashboard_page() {
        // Query recent unfulfilled orders
        $orders = wc_get_orders(array(
            'limit'   => 25,
            'status'  => array('wc-processing', 'wc-cold-packing', 'wc-on-hold'),
            'orderby' => 'date',
            'order'   => 'DESC',
        ));
        ?>
        <div class="wrap phoenics-dashboard-wrap" style="max-width:1200px;">
            <div style="display:flex;align-items:center;justify-content:space-between;margin:20px 0 25px;padding:20px;background:#0d1b2a;border-radius:10px;color:#fff;">
                <div>
                    <h1 style="color:#00d2ff;margin:0;font-size:24px;letter-spacing:1px;">❄️ Phoenics Peptide — Global Cold-Chain Fulfillment Hub</h1>
                    <p style="margin:5px 0 0;color:#94a3b8;font-size:13px;">Manage international shipments across USA, Canada, Europe, Africa, and Asia</p>
                </div>
                <div>
                    <span style="background:#10b981;color:#fff;padding:8px 16px;border-radius:20px;font-weight:700;font-size:13px;">
                        ACTIVE DISPATCH QUEUE: <?php echo count($orders); ?> ORDERS
                    </span>
                </div>
            </div>

            <?php settings_errors('phoenics_shipping_notices'); ?>

            <div style="background:#fff;border-radius:8px;box-shadow:0 2px 10px rgba(0,0,0,0.06);overflow:hidden;">
                <table class="wp-list-table widefat fixed striped">
                    <thead>
                        <tr style="background:#f8fafc;">
                            <th style="width:75px;">Order #</th>
                            <th style="width:140px;">Customer & Country</th>
                            <th>Research Items</th>
                            <th style="width:110px;">Destination Hub</th>
                            <th style="width:120px;">Carrier Choice</th>
                            <th style="width:170px;">Assign Tracking #</th>
                            <th style="width:130px;">Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php if (empty($orders)): ?>
                            <tr>
                                <td colspan="7" style="text-align:center;padding:30px;color:#64748b;">
                                    🎉 All international orders are fully packaged and dispatched!
                                </td>
                            </tr>
                        <?php else: ?>
                            <?php foreach ($orders as $order): 
                                $country = $order->get_shipping_country() ?: $order->get_billing_country();
                                $order_items = array();
                                foreach ($order->get_items() as $item) {
                                    $order_items[] = $item->get_quantity() . 'x ' . $item->get_name();
                                }
                            ?>
                                <tr>
                                    <td><strong>#<?php echo $order->get_id(); ?></strong></td>
                                    <td>
                                        <strong><?php echo esc_html($order->get_formatted_billing_full_name()); ?></strong><br>
                                        <span class="badge" style="background:#e2e8f0;padding:2px 6px;border-radius:3px;font-size:11px;font-weight:700;">
                                            🌍 <?php echo esc_html($country); ?>
                                        </span>
                                    </td>
                                    <td><small><?php echo implode('<br>', $order_items); ?></small></td>
                                    <td>
                                        <?php 
                                            if ($country === 'US') echo '🇺🇸 USA Boston';
                                            elseif ($country === 'CA') echo '🇨🇦 Toronto Depot';
                                            elseif (in_array($country, array('GB','DE','FR','IT','ES','NL','CH'))) echo '🇪🇺 Frankfurt Bio';
                                            elseif (in_array($country, array('NG','ZA','KE','EG','GH'))) echo '🌍 Africa Hub';
                                            else echo '🌏 Asia-Pacific';
                                        ?>
                                    </td>
                                    <form method="post">
                                        <?php wp_nonce_field('phoenics_quick_ship_action', 'phoenics_quick_ship_nonce'); ?>
                                        <input type="hidden" name="order_id" value="<?php echo $order->get_id(); ?>">
                                        <td>
                                            <select name="carrier" style="width:100%;font-size:12px;">
                                                <option value="dhl">DHL Express</option>
                                                <option value="fedex" selected>FedEx Priority</option>
                                                <option value="usps">USPS Priority</option>
                                                <option value="aramex">Aramex Cargo</option>
                                                <option value="canadapost">Canada Post</option>
                                            </select>
                                        </td>
                                        <td>
                                            <input type="text" name="tracking_num" placeholder="Scan or enter AWB #" style="width:100%;font-size:12px;" required />
                                            <input type="hidden" name="cold_chain" value="Lyophilized Nitrogen Pack (-20°C)">
                                        </td>
                                        <td>
                                            <button type="submit" class="button button-primary" style="background:#0284c7;border-color:#0284c7;font-weight:600;">
                                                🚀 Dispatch & Email
                                            </button>
                                        </td>
                                    </form>
                                </tr>
                            <?php endforeach; ?>
                        <?php endif; ?>
                    </tbody>
                </table>
            </div>
        </div>
        <?php
    }
}

new Phoenics_Admin_Shipping_Dashboard();
