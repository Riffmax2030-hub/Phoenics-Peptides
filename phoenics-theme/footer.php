<?php
/**
 * Phoenics Peptide Theme Footer
 */

if (!defined('ABSPATH')) {
    exit;
}
?>

<footer id="site-footer" class="main-footer">
    <!-- MANDATORY SCIENTIFIC & REGULATORY RESEARCH NOTICE -->
    <div class="regulatory-disclaimer-band">
        <div class="container">
            <div class="disclaimer-inner">
                <span class="alert-icon">⚠️</span>
                <p>
                    <strong>IMPORTANT SCIENTIFIC & REGULATORY NOTICE:</strong> All chemical products, lyophilized peptides, and analytical reagents distributed by <strong>Phoenics Peptide</strong> (phoenicspeptide.com) are strictly synthesized, formulated, and sold exclusively for <em>in-vitro</em> laboratory research, analytical diagnostics, and biomedical academic experimentation. Under no circumstances are these products intended or authorized for human consumption, clinical application, therapeutic treatment, food additives, or veterinary use. All buyers confirm adherence to their respective regional laboratory safety standards and regulatory import protocols.
                </p>
            </div>
        </div>
    </div>

    <div class="container footer-main-content">
        <div class="footer-grid">
            <!-- COL 1: BRAND OVERVIEW -->
            <div class="footer-col brand-col">
                <div class="footer-logo">
                    <img src="<?php echo get_template_directory_uri(); ?>/assets/images/logo-white.svg" alt="Phoenics Peptide" width="220" height="52" onerror="this.onerror=null; this.src='<?php echo get_template_directory_uri(); ?>/assets/images/logo.jpg';">
                </div>
                <p class="brand-bio">
                    Global synthesis gateway providing analytical-grade, third-party HPLC & MS verified research peptides for leading universities, laboratories, and biotechnology innovators worldwide.
                </p>
                <div class="lab-quality-stamp">
                    <span class="stamp-icon">🛡️</span>
                    <div>
                        <strong>&ge; 99.0% PURITY GUARANTEED</strong>
                        <span>Batch COA Certificate with every vial</span>
                    </div>
                </div>
            </div>

            <!-- COL 2: RESEARCH & CATALOG -->
            <div class="footer-col">
                <h4 class="col-title">Analytical Catalog</h4>
                <ul class="footer-links">
                    <li><a href="<?php echo esc_url(home_url('/shop/?category=healing-recovery')); ?>">BPC-157 & TB-500</a></li>
                    <li><a href="<?php echo esc_url(home_url('/shop/?category=growth-hormone')); ?>">CJC-1295 & Ipamorelin</a></li>
                    <li><a href="<?php echo esc_url(home_url('/shop/?category=growth-hormone')); ?>">MK-677 (Ibutamoren)</a></li>
                    <li><a href="<?php echo esc_url(home_url('/shop/?category=cognitive-nootropic')); ?>">Selank, Semax & Dihexa</a></li>
                    <li><a href="<?php echo esc_url(home_url('/shop/?category=longevity-antiaging')); ?>">Epithalon & LL-37</a></li>
                    <li><a href="<?php echo esc_url(home_url('/shop/?category=sexual-vitality')); ?>">PT-141 & Kisspeptin-10</a></li>
                    <li><a href="<?php echo esc_url(home_url('/shop/')); ?>">Full Synthesis Directory</a></li>
                </ul>
            </div>

            <!-- COL 3: LOGISTICS & HUBS -->
            <div class="footer-col">
                <h4 class="col-title">Global Bio-Logistics</h4>
                <ul class="footer-links">
                    <li><a href="<?php echo esc_url(home_url('/track-order/')); ?>"><strong>📦 Live Cold-Chain Tracking</strong></a></li>
                    <li><a href="<?php echo esc_url(home_url('/research/')); ?>">HPLC & Mass Spec Protocols</a></li>
                    <li><a href="<?php echo esc_url(home_url('/about/')); ?>">Fulfillment Facility Standards</a></li>
                    <li><a href="<?php echo esc_url(home_url('/contact/')); ?>">Institutional Bulk Inquiries</a></li>
                </ul>
                <div class="hubs-list">
                    <strong>DISPATCH HUBS:</strong>
                    <div class="hub-tags">
                        <span>🇺🇸 Boston, USA</span>
                        <span>🇩🇪 Frankfurt, EU</span>
                        <span>🇨🇦 Toronto, CA</span>
                        <span>🇸🇬 Singapore Hub</span>
                    </div>
                </div>
            </div>

            <!-- COL 4: PAYMENTS & CRYPTO -->
            <div class="footer-col payment-col">
                <h4 class="col-title">Worldwide Payment Gateways</h4>
                <p class="pay-note">Encrypted, 3D-Secure 2.0 and decentralized settlement accepted in 195+ countries.</p>
                
                <div class="payment-badges-grid">
                    <div class="pay-badge visa" title="Visa">VISA</div>
                    <div class="pay-badge mc" title="Mastercard">MASTERCARD</div>
                    <div class="pay-badge amex" title="American Express">AMEX</div>
                    <div class="pay-badge paypal" title="PayPal">PAYPAL</div>
                    <div class="pay-badge btc" title="Bitcoin / Lightning Network">₿ BITCOIN</div>
                    <div class="pay-badge eth" title="Ethereum">Ξ ETHEREUM</div>
                    <div class="pay-badge usdt" title="USDT Stablecoin">₮ USDT</div>
                    <div class="pay-badge usdc" title="USDC">USDC</div>
                </div>

                <div class="carrier-badges-row">
                    <span class="carrier-tag dhl">DHL Express</span>
                    <span class="carrier-tag fedex">FedEx Priority</span>
                    <span class="carrier-tag usps">USPS Tracked</span>
                    <span class="carrier-tag aramex">Aramex</span>
                </div>
            </div>
        </div>

        <div class="footer-bottom-bar">
            <p>&copy; <?php echo date('Y'); ?> Phoenics Peptide (phoenicspeptide.com). All Rights Reserved.</p>
            <div class="legal-nav">
                <a href="<?php echo esc_url(home_url('/terms-and-conditions/')); ?>">Terms of Service</a>
                <span class="sep">&bull;</span>
                <a href="<?php echo esc_url(home_url('/privacy-policy/')); ?>">Privacy Policy</a>
                <span class="sep">&bull;</span>
                <a href="<?php echo esc_url(home_url('/refund-policy/')); ?>">Refund & Cold-Chain Policy</a>
                <span class="sep">&bull;</span>
                <a href="<?php echo esc_url(home_url('/research-disclaimer/')); ?>">Research Compliance</a>
            </div>
        </div>
    </div>
</footer>

<?php wp_footer(); ?>
</body>
</html>
