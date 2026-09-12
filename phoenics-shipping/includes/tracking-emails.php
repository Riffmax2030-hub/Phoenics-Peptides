<?php
/**
 * Automated Customer Tracking & Dispatch Emails
 */

if (!defined('ABSPATH')) {
    exit;
}

class Phoenics_Tracking_Emails {

    public function __construct() {
        add_action('phoenics_order_shipped_with_tracking', array($this, 'send_tracking_dispatch_email'), 10, 3);
    }

    public function send_tracking_dispatch_email($order_id, $carrier, $tracking_number) {
        $order = wc_get_order($order_id);
        if (!$order) return;

        $recipient_email = $order->get_billing_email();
        $customer_name = $order->get_billing_first_name() . ' ' . $order->get_billing_last_name();
        $carrier_url = Phoenics_Order_Manager::get_carrier_url($carrier, $tracking_number);
        $cold_chain = $order->get_meta('_phoenics_cold_chain', true) ?: 'Lyophilized Dry Gel Pack (-20°C)';
        $est_delivery = $order->get_meta('_phoenics_est_delivery', true) ?: '2-3 Business Days';
        $origin_hub = $order->get_meta('_phoenics_origin_hub', true) ?: 'Phoenics Boston Central Bio-Hub';

        $subject = sprintf('[Phoenics Peptide] 🚀 Cold-Chain Shipment Dispatched: Order #%s (Tracking: %s)', $order_id, $tracking_number);

        // Build items list
        $items_html = '';
        foreach ($order->get_items() as $item_id => $item) {
            $items_html .= sprintf(
                '<tr>
                    <td style="padding:10px 12px;border-bottom:1px solid #e2e8f0;font-size:14px;color:#1e293b;"><strong>%s</strong></td>
                    <td style="padding:10px 12px;border-bottom:1px solid #e2e8f0;font-size:14px;color:#64748b;text-align:center;">%s</td>
                    <td style="padding:10px 12px;border-bottom:1px solid #e2e8f0;font-size:14px;color:#0f172a;text-align:right;">%s</td>
                </tr>',
                esc_html($item->get_name()),
                esc_html($item->get_quantity()),
                wc_price($order->get_item_total($item, false, true))
            );
        }

        ob_start();
        ?>
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <style>
                body { font-family: 'Segoe UI', Helvetica, Arial, sans-serif; background-color: #f1f5f9; margin: 0; padding: 0; }
                .container { max-width: 620px; margin: 30px auto; background: #ffffff; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.08); }
                .header { background: #0d1b2a; padding: 35px 30px; text-align: center; color: #ffffff; }
                .content { padding: 30px; color: #334155; line-height: 1.6; }
                .tracking-card { background: #0f172a; color: #ffffff; border-radius: 8px; padding: 22px; margin: 25px 0; }
                .btn { display: inline-block; background: #00d2ff; color: #0d1b2a; text-decoration: none; padding: 13px 26px; border-radius: 6px; font-weight: 700; font-size: 15px; margin-top: 15px; }
                .footer { background: #f8fafc; padding: 20px 30px; text-align: center; font-size: 12px; color: #94a3b8; border-top: 1px solid #e2e8f0; }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1 style="margin:0;font-size:24px;letter-spacing:2px;color:#00d2ff;">PHOENICS PEPTIDE</h1>
                    <p style="margin:6px 0 0;font-size:12px;letter-spacing:1px;color:#94a3b8;">GLOBAL RESEARCH LOGISTICS • DISPATCH CONFIRMATION</p>
                </div>
                <div class="content">
                    <p>Dear <strong><?php echo esc_html($customer_name); ?></strong>,</p>
                    <p>Your research order <strong>#<?php echo esc_html($order_id); ?></strong> has successfully passed laboratory quality inspection (HPLC/MS &gt;99% purity) and has been packaged in cold-chain bio-thermal insulation.</p>
                    
                    <div class="tracking-card">
                        <div style="font-size:12px;text-transform:uppercase;letter-spacing:1px;color:#38bdf8;margin-bottom:8px;">Live Shipment Information</div>
                        <div style="font-size:18px;font-weight:700;margin-bottom:15px;color:#fff;">Carrier: <?php echo strtoupper(esc_html($carrier)); ?> Priority Air</div>
                        <div style="font-size:14px;margin-bottom:6px;"><strong>Tracking Number:</strong> <code style="color:#fcd34d;"><?php echo esc_html($tracking_number); ?></code></div>
                        <div style="font-size:14px;margin-bottom:6px;"><strong>Origin Depot:</strong> <?php echo esc_html($origin_hub); ?></div>
                        <div style="font-size:14px;margin-bottom:6px;"><strong>Thermal Status:</strong> <?php echo esc_html($cold_chain); ?></div>
                        <div style="font-size:14px;margin-bottom:15px;"><strong>Estimated Arrival:</strong> <?php echo esc_html($est_delivery); ?></div>
                        <div style="text-align:center;">
                            <a href="<?php echo esc_url($carrier_url); ?>" class="btn" target="_blank">Track Real-Time Package &rarr;</a>
                        </div>
                    </div>

                    <h3 style="color:#0d1b2a;border-bottom:2px solid #00d2ff;padding-bottom:6px;font-size:16px;">Shipment Contents</h3>
                    <table style="width:100%;border-collapse:collapse;margin-top:10px;">
                        <thead>
                            <tr style="background:#f8fafc;">
                                <th style="text-align:left;padding:8px 12px;font-size:12px;color:#64748b;">Item Description</th>
                                <th style="text-align:center;padding:8px 12px;font-size:12px;color:#64748b;">Qty</th>
                                <th style="text-align:right;padding:8px 12px;font-size:12px;color:#64748b;">Subtotal</th>
                            </tr>
                        </thead>
                        <tbody>
                            <?php echo $items_html; ?>
                        </tbody>
                    </table>

                    <div style="margin-top:25px;background:#fef3c7;border-left:4px solid #f59e0b;padding:12px 15px;font-size:13px;color:#92400e;">
                        <strong>Storage Note upon Arrival:</strong> Please transfer lyophilized peptide vials immediately to -20°C storage for maximum molecular stability and longevity.
                    </div>
                </div>
                <div class="footer">
                    <p>Phoenics Peptide • Global Analytical Research Supplies</p>
                    <p style="font-size:11px;">All compounds sold strictly for in-vitro laboratory research and analytical assays. Not for human or animal consumption.</p>
                </div>
            </div>
        </body>
        </html>
        <?php
        $message = ob_get_clean();

        $headers = array('Content-Type: text/html; charset=UTF-8', 'From: Phoenics Peptide Logistics <shipping@phoenicspeptide.com>');
        wp_mail($recipient_email, $subject, $message, $headers);
    }
}

new Phoenics_Tracking_Emails();
