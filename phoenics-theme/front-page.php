<?php
/**
 * Template Name: Phoenics Front Page (Production Edition)
 * Description: Production-grade clinical biotech e-commerce front-page with clickable product modal, 3-angle hover carousels, and secured nationwide delivery.
 */

get_header(); ?>

<main id="primary" class="site-main clinical-storefront">

    <!-- HERO SECTION -->
    <section class="hero-section" style="background: linear-gradient(180deg, #F0FDF4 0%, #ECFDF5 100%); border-bottom: 1px solid #E2E8F0; padding: 55px 0 65px;">
        <div class="container" style="max-width:1280px; margin:0 auto; padding:0 20px;">
            <div style="display:grid; grid-template-columns:1.2fr 0.8fr; gap:40px; align-items:center;">
                <div>
                    <div style="display:inline-flex; align-items:center; gap:8px; background:#EFF6FF; border:1px solid #BFDBFE; color:#059669; padding:5px 12px; border-radius:20px; font-size:11px; font-weight:800; margin-bottom:16px;">
                        <span>🔬</span> INDEPENDENT THIRD-PARTY HPLC &amp; MASS SPEC VERIFIED
                    </div>
                    <h1 style="font-family:'Montserrat',sans-serif; font-size:40px; font-weight:900; line-height:1.15; color:#0F172A; margin-bottom:16px; letter-spacing:-0.5px;">
                        High-Purity Research Peptides <br>
                        <span style="color:#059669;">For Research &amp; Personal Vitality</span>
                    </h1>
                    <p style="font-size:16px; color:#475569; line-height:1.65; margin-bottom:28px; max-width:580px;">
                        Primary laboratory supplier of high-demand metabolic incretins (<strong>Tirzepatide, Retatrutide, Semaglutide</strong>), anti-ageing dermal matrix peptides (<strong>GHK-Cu, Epithalon</strong>), and certified scanning libraries. Exact dosage calibrated with &ge;99% guaranteed purity.
                    </p>
                    <div style="display:flex; gap:14px; flex-wrap:wrap; margin-bottom:35px;">
                        <a href="#catalog-section" style="background:#059669; color:#fff; padding:13px 26px; border-radius:8px; font-size:14px; font-weight:700; text-decoration:none; box-shadow:0 4px 12px rgba(37,99,235,0.25);">Explore All Peptides &rarr;</a>
                        <a href="#quality-section" style="background:#fff; color:#0F172A; border:1px solid #CBD5E1; padding:13px 22px; border-radius:8px; font-size:14px; font-weight:700; text-decoration:none;">View Quality Standards</a>
                    </div>
                    <div style="display:grid; grid-template-columns:repeat(4,1fr); gap:15px; border-top:1px solid #E2E8F0; padding-top:22px;">
                        <div>
                            <div style="font-family:'Montserrat',sans-serif; font-size:22px; font-weight:800; color:#0F172A;">&ge;99.4%</div>
                            <div style="font-size:11px; color:#64748B;">Mean HPLC Purity</div>
                        </div>
                        <div>
                            <div style="font-family:'Montserrat',sans-serif; font-size:22px; font-weight:800; color:#059669;">Exact Dose</div>
                            <div style="font-size:11px; color:#64748B;">Zero Vial Variance</div>
                        </div>
                        <div>
                            <div style="font-family:'Outfit',sans-serif; font-size:22px; font-weight:800; color:#059669;">ISO 9001</div>
                            <div style="font-size:11px; color:#64748B;">Quality Certified</div>
                        </div>
                        <div>
                            <div style="font-family:'Outfit',sans-serif; font-size:22px; font-weight:800; color:#D97706;">Included</div>
                            <div style="font-size:11px; color:#64748B;">Delivery Directions</div>
                        </div>
                    </div>
                </div>

                <!-- Hero Clickable Highlight Product -->
                <div onclick="openProductModal(1)" style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:16px; padding:24px; box-shadow:0 4px 16px rgba(0,0,0,0.06); text-align:center; cursor:pointer;">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                        <span style="background:#DC2626; color:#fff; font-size:10px; font-weight:800; padding:2px 7px; border-radius:4px;">FEATURED INCRETIN</span>
                        <span style="background:#ECFDF5; color:#059669; border:1px solid #A7F3D0; padding:2px 8px; border-radius:12px; font-size:10.5px; font-weight:800;">HPLC 99.4% VERIFIED</span>
                    </div>
                    <img src="<?php echo get_template_directory_uri(); ?>/assets/images/products/tirzepatide-photo.jpg" alt="Tirzepatide 10mg Clear Vial" style="width:100%; max-width:320px; height:auto; border-radius:10px; margin:10px auto; display:block;" onerror="this.src='<?php echo get_template_directory_uri(); ?>/assets/images/products/tirzepatide-vial.svg';">
                    <div style="text-align:left; border-top:1px solid #E2E8F0; padding-top:12px; margin-top:10px; display:flex; justify-content:space-between; align-items:center;">
                        <div>
                            <div style="font-size:11px; color:#059669; font-weight:700;">DUAL GIP/GLP-1 AGONIST</div>
                            <div style="font-size:16px; font-weight:800; color:#0F172A;">Tirzepatide 10mg</div>
                            <div style="font-size:12px; color:#059669; font-weight:600;">Click to view full scientific profile &amp; CoA &rarr;</div>
                        </div>
                        <div style="text-align:right;">
                            <span style="font-size:12px; color:#94A3B8; text-decoration:line-through;">$140.00</span>
                            <div style="font-family:'Montserrat',sans-serif; font-size:18px; font-weight:900; color:#059669;">$112.00</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 4-PILLAR REASSURANCE STRIP -->
    <div style="background:#F8FAFC; border-bottom:1px solid #E2E8F0; padding:30px 0;">
        <div class="container" style="max-width:1280px; margin:0 auto; padding:0 20px;">
            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:20px;">
                <div style="background:#fff; border:1px solid #E2E8F0; border-radius:12px; padding:18px 20px; display:flex; align-items:center; gap:14px;">
                    <div style="width:44px; height:44px; border-radius:10px; background:#EFF6FF; color:#059669; display:flex; align-items:center; justify-content:center; font-size:20px; flex-shrink:0;">⚖️</div>
                    <div>
                        <div style="font-weight:800; color:#0F172A; font-size:13px;">Exact Dose Calibration</div>
                        <div style="font-size:12px; color:#64748B;">Guaranteed exact mg content per vial</div>
                    </div>
                </div>
                <div style="background:#fff; border:1px solid #E2E8F0; border-radius:12px; padding:18px 20px; display:flex; align-items:center; gap:14px;">
                    <div style="width:44px; height:44px; border-radius:10px; background:#ECFDF5; color:#059669; display:flex; align-items:center; justify-content:center; font-size:20px; flex-shrink:0;">🔬</div>
                    <div>
                        <div style="font-weight:800; color:#0F172A; font-size:13px;">≥99.0% HPLC &amp; MS Validated</div>
                        <div style="font-size:12px; color:#64748B;">Batch-matched Certificate of Analysis</div>
                    </div>
                </div>
                <div style="background:#fff; border:1px solid #E2E8F0; border-radius:12px; padding:18px 20px; display:flex; align-items:center; gap:14px;">
                    <div style="width:44px; height:44px; border-radius:10px; background:#FEF3C7; color:#D97706; display:flex; align-items:center; justify-content:center; font-size:20px; flex-shrink:0;">📦</div>
                    <div>
                        <div style="font-weight:800; color:#0F172A; font-size:13px;">Secured Nationwide Delivery</div>
                        <div style="font-size:12px; color:#64748B;">Temperature-shielded express dispatch</div>
                    </div>
                </div>
                <div style="background:#fff; border:1px solid #E2E8F0; border-radius:12px; padding:18px 20px; display:flex; align-items:center; gap:14px;">
                    <div style="width:44px; height:44px; border-radius:10px; background:#F1F5F9; color:#0F172A; display:flex; align-items:center; justify-content:center; font-size:20px; flex-shrink:0;">₿</div>
                    <div>
                        <div style="font-weight:800; color:#0F172A; font-size:13px;">Instant Payment Discounts</div>
                        <div style="font-size:12px; color:#64748B;">10% Crypto / BTC • 5% Bank Wire</div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- MAIN PRODUCT CATALOG -->
    <section id="catalog-section" style="padding:65px 0 80px; background:#FFFFFF;">
        <div class="container" style="max-width:1280px; margin:0 auto; padding:0 20px;">
            <div style="display:flex; justify-content:space-between; align-items:flex-end; margin-bottom:25px; flex-wrap:wrap; gap:20px;">
                <div>
                    <span style="color:#059669; font-weight:800; font-size:11.5px; letter-spacing:1.5px; text-transform:uppercase;">PRE-CLINICAL BIO-CATALOG</span>
                    <h2 style="font-family:'Montserrat',sans-serif; font-size:30px; font-weight:800; color:#0F172A; margin-bottom:6px;">Certified Research Peptides</h2>
                    <p style="color:#64748B; font-size:14px; margin:0;">Click any product to view its comprehensive scientific profile, chemical specs, and analytical CoA report.</p>
                </div>
            </div>

            <!-- CATEGORY FILTER PILLS -->
            <div class="category-pills" style="display:flex; gap:8px; flex-wrap:wrap; margin-bottom:30px; padding-bottom:15px; border-bottom:1px solid #F1F5F9;">
                <button class="cat-pill active" onclick="filterCategory('all', this)">All Peptides (19)</button>
                <button class="cat-pill" onclick="filterCategory('weight-loss', this)">🔥 Weight Loss &amp; Incretins</button>
                <button class="cat-pill" onclick="filterCategory('anti-ageing', this)">✨ Anti-Ageing &amp; Skin</button>
                <button class="cat-pill" onclick="filterCategory('muscle', this)">💪 Muscle &amp; GH Axis</button>
                <button class="cat-pill" onclick="filterCategory('cognitive', this)">🧠 Cognitive &amp; Vitality</button>
                <button class="cat-pill" onclick="filterCategory('institutional', this)">🏛️ Institutional ($23k+)</button>
            </div>

            <!-- PRODUCT GRID -->
            <div id="products-container" class="product-grid" style="display:grid; grid-template-columns:repeat(auto-fill, minmax(280px, 1fr)); gap:24px;">
                <!-- Rendered dynamically by frontend JS for instant reactivity -->
            </div>
        </div>
    </section>

    <!-- WHY PHOENICS QUALITY STANDARD (ADDRESSING ARTICLE) -->
    <section id="quality-section" style="background:#F8FAFC; border-top:1px solid #E2E8F0; border-bottom:1px solid #E2E8F0; padding:70px 0;">
        <div class="container" style="max-width:1280px; margin:0 auto; padding:0 20px;">
            <div style="text-align:center; max-width:760px; margin:0 auto 45px;">
                <span style="color:#059669; font-weight:800; font-size:12px; letter-spacing:1.5px;">ANALYTICAL RIGOR</span>
                <h2 style="font-family:'Montserrat',sans-serif; font-size:30px; font-weight:800; color:#0F172A; margin:6px 0 10px;">
                    Addressing Industry Impurities &amp; Dosage Variance
                </h2>
                <p style="color:#64748B; font-size:14px; line-height:1.7;">
                    Recent public health warnings have exposed that unregulated peptide vendors frequently supply vials with <strong>dosing errors ranging from half to double labelled quantity</strong>, alongside unverified purities. Phoenics Peptide enforces strict pharmaceutical-grade controls:
                </p>
            </div>

            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:24px;">
                <div style="background:#fff; border:1px solid #E2E8F0; border-radius:12px; padding:26px; box-shadow:0 1px 3px rgba(0,0,0,0.06);">
                    <div style="font-size:24px; margin-bottom:10px;">⚖️</div>
                    <h3 style="font-family:'Montserrat',sans-serif; font-size:17px; font-weight:800; color:#0F172A; margin-bottom:8px;">Quantitative Dose Calibration</h3>
                    <p style="font-size:13.5px; color:#64748B; line-height:1.6;">Every batch undergoes quantitative chromatographic assay to confirm exact mass per vial (e.g. 10.0mg &plusmn; 0.1mg). Zero under-dosing or unexpected potency spikes.</p>
                </div>
                <div style="background:#fff; border:1px solid #E2E8F0; border-radius:12px; padding:26px; box-shadow:0 1px 3px rgba(0,0,0,0.06);">
                    <div style="font-size:24px; margin-bottom:10px;">📉</div>
                    <h3 style="font-family:'Montserrat',sans-serif; font-size:17px; font-weight:800; color:#0F172A; margin-bottom:8px;">RP-HPLC &ge; 99.0% Purity</h3>
                    <p style="font-size:13.5px; color:#64748B; line-height:1.6;">Single-peak reverse phase HPLC chromatograms confirm absence of truncated sequences, deletion peptides, and residual synthesis impurities.</p>
                </div>
                <div style="background:#fff; border:1px solid #E2E8F0; border-radius:12px; padding:26px; box-shadow:0 1px 3px rgba(0,0,0,0.06);">
                    <div style="font-size:24px; margin-bottom:10px;">🔬</div>
                    <h3 style="font-family:'Montserrat',sans-serif; font-size:17px; font-weight:800; color:#0F172A; margin-bottom:8px;">ESI-MS Molecular Validation</h3>
                    <p style="font-size:13.5px; color:#64748B; line-height:1.6;">High-resolution Electrospray Ionization Mass Spectrometry validates exact molecular weight and amino acid sequence accuracy against theoretical standards.</p>
                </div>
                <div style="background:#fff; border:1px solid #E2E8F0; border-radius:12px; padding:26px; box-shadow:0 1px 3px rgba(0,0,0,0.06);">
                    <div style="font-size:24px; margin-bottom:10px;">🛡️</div>
                    <h3 style="font-family:'Montserrat',sans-serif; font-size:17px; font-weight:800; color:#0F172A; margin-bottom:8px;">Cleanroom Lyophilization</h3>
                    <p style="font-size:13.5px; color:#64748B; line-height:1.6;">Formulated under ISO Class 5 sterile cleanroom conditions, nitrogen-purged USP Type 1 borosilicate glass, and chlorobutyl vacuum stoppers.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- SECURED NATIONWIDE DELIVERY -->
    <section id="shipping-section" style="background:#0F172A; color:#FFFFFF; padding:60px 0;">
        <div class="container" style="max-width:1280px; margin:0 auto; padding:0 20px;">
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:40px; align-items:center;">
                <div>
                    <span style="color:#38BDF8; font-weight:800; font-size:12px; letter-spacing:1.5px;">STREAMLINED LOGISTICS</span>
                    <h2 style="font-family:'Montserrat',sans-serif; font-size:32px; font-weight:800; margin:6px 0 14px;">
                        Secured &amp; Insured Nationwide Shipping
                    </h2>
                    <p style="color:#94A3B8; font-size:14px; line-height:1.7;">
                        When you place an order, our process is clear, secured, and reliable:
                    </p>
                    <div style="display:grid; gap:16px; margin-top:20px;">
                        <div style="display:flex; gap:14px; background:#1E293B; padding:16px 20px; border-radius:10px; border-left:4px solid #059669;">
                            <span style="font-size:20px;">1️⃣</span>
                            <div>
                                <h4 style="font-size:14px; font-weight:800; color:#FFFFFF; margin-bottom:2px;">Place Order &amp; Select Payment</h4>
                                <p style="font-size:12.5px; color:#94A3B8; margin:0;">Choose Credit Card, Bitcoin/Crypto (extra 10% off), or Bank Wire (extra 5% off).</p>
                            </div>
                        </div>
                        <div style="display:flex; gap:14px; background:#1E293B; padding:16px 20px; border-radius:10px; border-left:4px solid #059669;">
                            <span style="font-size:20px;">2️⃣</span>
                            <div>
                                <h4 style="font-size:14px; font-weight:800; color:#FFFFFF; margin-bottom:2px;">Immediate Payment Confirmation</h4>
                                <p style="font-size:12.5px; color:#94A3B8; margin:0;">We confirm your payment and immediately reserve your batch from climate-controlled storage.</p>
                            </div>
                        </div>
                        <div style="display:flex; gap:14px; background:#1E293B; padding:16px 20px; border-radius:10px; border-left:4px solid #059669;">
                            <span style="font-size:20px;">3️⃣</span>
                            <div>
                                <h4 style="font-size:14px; font-weight:800; color:#FFFFFF; margin-bottom:2px;">Secured Temperature-Shielded Dispatch</h4>
                                <p style="font-size:12.5px; color:#94A3B8; margin:0;">Packed in protective insulated cryo-shipper freight. A tracking confirmation is emailed directly to you upon dispatch.</p>
                            </div>
                        </div>
                    </div>
                </div>

                <div style="background:#1E293B; border:1px solid #334155; border-radius:16px; padding:30px;">
                    <div style="display:flex; align-items:center; gap:12px; margin-bottom:20px;">
                        <div style="width:12px; height:12px; background:#059669; border-radius:50%; box-shadow:0 0 8px #059669;"></div>
                        <strong style="color:#FFFFFF; font-size:15px;">Fulfillment Centers Operational</strong>
                    </div>
                    <div style="font-size:13px; color:#94A3B8; line-height:1.8; margin-bottom:20px;">
                        &bull; <strong>United States &amp; Canada:</strong> Express nationwide air transit via FedEx Priority &amp; UPS Air.<br>
                        &bull; <strong>European Union &amp; UK:</strong> Dispatched from our Frankfurt central cold-hub.<br>
                        &bull; <strong>Discreet Packaging:</strong> Neutral, non-descript exterior packaging for complete laboratory security.
                    </div>
                    <div style="background:#0F172A; border-radius:8px; padding:15px; border:1px solid #334155;">
                        <div style="color:#F59E0B; font-weight:700; font-size:12px; margin-bottom:4px;">⚡ Free Nationwide Shipping:</div>
                        <div style="color:#E2E8F0; font-size:12px;">Automatic complimentary express freight applied on all research orders over $250.00.</div>
                    </div>
                </div>
            </div>
        </div>
    </section>

</main>

<!-- PRODUCT DETAIL MODAL (OPENS ON CLICK) -->
<div id="product-modal" class="modal-overlay" onclick="closeProductModal(event)" style="position:fixed; top:0; left:0; right:0; bottom:0; background:rgba(15,23,42,0.7); backdrop-filter:blur(4px); z-index:1000; display:none; align-items:center; justify-content:center; padding:20px;">
    <div class="modal-box" onclick="event.stopPropagation()" style="background:#FFFFFF; border-radius:16px; max-width:900px; width:100%; max-height:90vh; overflow-y:auto; position:relative; box-shadow:0 16px 40px rgba(0,0,0,0.1); border:1px solid #E2E8F0; padding:30px;">
        <button class="modal-close-btn" onclick="closeProductModal()" style="position:absolute; top:20px; right:20px; width:36px; height:36px; border-radius:50%; background:#F1F5F9; border:none; font-size:20px; font-weight:800; color:#0F172A; cursor:pointer; display:flex; align-items:center; justify-content:center;">&times;</button>
        <div class="modal-grid" style="display:grid; grid-template-columns:1fr 1.2fr; gap:30px; align-items:flex-start;">
            <div>
                <div class="modal-gallery-main" id="modal-main-img-box" style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:12px; height:320px; display:flex; align-items:center; justify-content:center; padding:15px; margin-bottom:12px;">
                    <img id="modal-main-img" src="" alt="Product Detail" style="max-height:290px; max-width:100%; object-fit:contain;">
                </div>
                <div class="modal-thumbs" id="modal-thumbs-box" style="display:flex; gap:10px;"></div>
                <div style="margin-top:15px; background:#F8FAFC; border:1px solid #E2E8F0; border-radius:8px; padding:12px; font-size:11.5px; color:#475569;">
                    <strong>Quality Report:</strong> Batch HPLC Chromatogram &amp; ESI-MS Certificate verified and available for immediate laboratory download.
                </div>
            </div>

            <div>
                <div id="modal-cat-tag" style="font-size:11px; color:#059669; font-weight:800; letter-spacing:1px; text-transform:uppercase; margin-bottom:4px;"></div>
                <h2 id="modal-title" style="font-family:'Montserrat',sans-serif; font-size:24px; font-weight:900; color:#0F172A; margin-bottom:8px;"></h2>
                <div style="display:flex; gap:8px; align-items:center; margin-bottom:14px;">
                    <span id="modal-purity-badge" style="background:#ECFDF5; color:#059669; border:1px solid #A7F3D0; padding:2px 8px; border-radius:12px; font-size:10.5px; font-weight:800;"></span>
                    <span style="background:#DC2626; color:#fff; font-size:10px; font-weight:800; padding:2px 7px; border-radius:4px;">20% SALE APPLIED</span>
                </div>

                <p id="modal-desc" style="font-size:13.5px; color:#475569; line-height:1.6; margin-bottom:15px;"></p>

                <table style="width:100%; border-collapse:collapse; font-size:12.5px; margin:15px 0;">
                    <tr><td style="padding:7px 10px; border-bottom:1px solid #F1F5F9; font-weight:700; color:#475569; width:35%;">Target Mechanism:</td><td id="modal-mechanism" style="padding:7px 10px; border-bottom:1px solid #F1F5F9; color:#0F172A; font-weight:600;"></td></tr>
                    <tr><td style="padding:7px 10px; border-bottom:1px solid #F1F5F9; font-weight:700; color:#475569;">Primary Focus:</td><td id="modal-focus" style="padding:7px 10px; border-bottom:1px solid #F1F5F9; color:#059669; font-weight:700;"></td></tr>
                    <tr><td style="padding:7px 10px; border-bottom:1px solid #F1F5F9; font-weight:700; color:#475569;">CAS Registry:</td><td id="modal-cas" style="padding:7px 10px; border-bottom:1px solid #F1F5F9; font-family:'Space Mono',monospace;"></td></tr>
                    <tr><td style="padding:7px 10px; border-bottom:1px solid #F1F5F9; font-weight:700; color:#475569;">Molecular Weight:</td><td id="modal-mw" style="padding:7px 10px; border-bottom:1px solid #F1F5F9; font-family:'Space Mono',monospace;"></td></tr>
                    <tr><td style="padding:7px 10px; border-bottom:1px solid #F1F5F9; font-weight:700; color:#475569;">Storage Protocol:</td><td style="padding:7px 10px; border-bottom:1px solid #F1F5F9; color:#059669; font-weight:600;">Store at -20°C (Lyophilized Powder)</td></tr>
                </table>

                <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:10px; padding:15px; margin-bottom:20px; display:flex; justify-content:space-between; align-items:center;">
                    <div>
                        <span id="modal-price-reg" style="font-size:13px; color:#94A3B8; text-decoration:line-through;"></span>
                        <div id="modal-price-sale" style="font-family:'Montserrat',sans-serif; font-size:24px; font-weight:900; color:#059669;"></div>
                    </div>
                    <div style="text-align:right;">
                        <div style="font-size:11px; color:#D97706; font-weight:700;">⚡ With 10% Crypto Rebate:</div>
                        <div id="modal-price-btc" style="font-size:16px; font-weight:800; color:#0F172A;"></div>
                    </div>
                </div>

                <div style="display:flex; gap:12px; align-items:center;">
                    <input type="number" id="modal-qty" value="1" min="1" max="100" style="width:70px; padding:12px; border:1px solid #CBD5E1; border-radius:8px; font-size:14px; font-weight:700; text-align:center; outline:none;">
                    <button id="modal-add-btn" style="flex:1; padding:13px 20px; font-size:14px; background:#059669; color:#fff; border:none; border-radius:8px; font-weight:800; cursor:pointer;">
                        + Add to Research Batch
                    </button>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
var themeProducts = [
    { id: 1, name: "Tirzepatide (10mg)", category: "weight-loss", cat_label: "Weight Loss & Incretins", cas: "2023788-19-2", mw: "4813.45 g/mol", purity: "99.4%", reg_usd: 140.00, sale_usd: 112.00, mechanism: "Dual GIP / GLP-1 Receptor Agonist", focus: "Weight Loss, Insulin Secretion & Satiety", desc: "Dual GIP and GLP-1 receptor agonist formulated as a sterile lyophilized cake with verified exact 10mg dosage.", images: ["<?php echo get_template_directory_uri(); ?>/assets/images/products/tirzepatide-photo.jpg", "<?php echo get_template_directory_uri(); ?>/assets/images/products/tirzepatide-coa.svg", "<?php echo get_template_directory_uri(); ?>/assets/images/products/tirzepatide-pack.svg"] },
    { id: 2, name: "Retatrutide (10mg)", category: "weight-loss", cat_label: "Weight Loss & Incretins", cas: "2381089-83-2", mw: "4731.33 g/mol", purity: "99.3%", reg_usd: 175.00, sale_usd: 139.00, mechanism: "Triple GLP-1 / GIP / GCGR Agonist (GGG)", focus: "High-Potency Weight Loss & Metabolism", desc: "Next-generation triple receptor agonist targeting GLP-1, GIP, and Glucagon (GCGR). Highest demand investigational compound.", images: ["<?php echo get_template_directory_uri(); ?>/assets/images/products/retatrutide-photo.jpg", "<?php echo get_template_directory_uri(); ?>/assets/images/products/retatrutide-coa.svg", "<?php echo get_template_directory_uri(); ?>/assets/images/products/retatrutide-pack.svg"] },
    { id: 3, name: "Semaglutide (5mg)", category: "weight-loss", cat_label: "Weight Loss & Incretins", cas: "910463-68-2", mw: "4113.58 g/mol", purity: "99.5%", reg_usd: 120.00, sale_usd: 96.00, mechanism: "Selective GLP-1 Receptor Agonist", focus: "Weight Loss & Glycemic Control", desc: "Selective GLP-1 receptor agonist with extended albumin-binding fatty acid chain.", images: ["<?php echo get_template_directory_uri(); ?>/assets/images/products/semaglutide-vial.svg", "<?php echo get_template_directory_uri(); ?>/assets/images/products/semaglutide-coa.svg", "<?php echo get_template_directory_uri(); ?>/assets/images/products/semaglutide-pack.svg"] },
    { id: 4, name: "Cagrilintide (5mg)", category: "weight-loss", cat_label: "Weight Loss & Incretins", cas: "1415456-99-3", mw: "4522.06 g/mol", purity: "99.2%", reg_usd: 135.00, sale_usd: 108.00, mechanism: "Long-Acting Amylin Analog", focus: "Synergistic Weight Loss & Satiety", desc: "Synthetic amylin receptor agonist investigated frequently in synergy with GLP-1 agonists.", images: ["<?php echo get_template_directory_uri(); ?>/assets/images/products/cagrilintide-vial.svg", "<?php echo get_template_directory_uri(); ?>/assets/images/products/cagrilintide-coa.svg", "<?php echo get_template_directory_uri(); ?>/assets/images/products/cagrilintide-pack.svg"] },
    { id: 5, name: "AOD-9604 (5mg)", category: "weight-loss", cat_label: "Weight Loss & Incretins", cas: "221231-10-3", mw: "1815.10 g/mol", purity: "99.4%", reg_usd: 95.00, sale_usd: 76.00, mechanism: "C-Terminal hGH Fragment (176-191)", focus: "Targeted Lipolysis & Fat Breakdown", desc: "Anti-Obesity Drug peptide fragment stimulating fat breakdown without altering blood sugar.", images: ["<?php echo get_template_directory_uri(); ?>/assets/images/products/aod9604-vial.svg", "<?php echo get_template_directory_uri(); ?>/assets/images/products/aod9604-coa.svg", "<?php echo get_template_directory_uri(); ?>/assets/images/products/aod9604-pack.svg"] },
    { id: 6, name: "GHK-Cu Copper Peptide (50mg)", category: "anti-ageing", cat_label: "Anti-Ageing & Skin", cas: "49557-75-7", mw: "403.92 g/mol", purity: "99.6%", reg_usd: 60.00, sale_usd: 48.00, mechanism: "Copper-Chelated Tripeptide (Gly-His-Lys)", focus: "Skin Health, Collagen & Elastin Remodeling", desc: "Premier anti-ageing compound. High-purity vivid royal blue powder cake for collagen synthesis.", images: ["<?php echo get_template_directory_uri(); ?>/assets/images/products/ghkcu-photo.jpg", "<?php echo get_template_directory_uri(); ?>/assets/images/products/ghkcu-coa.svg", "<?php echo get_template_directory_uri(); ?>/assets/images/products/ghkcu-pack.svg"] },
    { id: 7, name: "Epithalon (10mg)", category: "anti-ageing", cat_label: "Anti-Ageing & Skin", cas: "307297-39-8", mw: "390.35 g/mol", purity: "99.5%", reg_usd: 60.00, sale_usd: 48.00, mechanism: "Pineal Tetrapeptide (Ala-Glu-Asp-Gly)", focus: "Telomerase Induction & Anti-Ageing", desc: "Investigated for telomerase activation and cellular longevity.", images: ["<?php echo get_template_directory_uri(); ?>/assets/images/products/epithalon-vial.svg", "<?php echo get_template_directory_uri(); ?>/assets/images/products/epithalon-coa.svg", "<?php echo get_template_directory_uri(); ?>/assets/images/products/epithalon-pack.svg"] },
    { id: 8, name: "MOTS-c (10mg)", category: "anti-ageing", cat_label: "Anti-Ageing & Skin", cas: "1627580-64-6", mw: "2174.65 g/mol", purity: "99.3%", reg_usd: 80.00, sale_usd: 64.00, mechanism: "Mitochondrial-Derived Peptide (16-AA)", focus: "Cellular Energy, Longevity & Metabolic Health", desc: "Mitochondrial encoded hormone activating AMPK and counteracting age-associated metabolic decline.", images: ["<?php echo get_template_directory_uri(); ?>/assets/images/products/motsc-vial.svg", "<?php echo get_template_directory_uri(); ?>/assets/images/products/motsc-coa.svg", "<?php echo get_template_directory_uri(); ?>/assets/images/products/motsc-pack.svg"] },
    { id: 9, name: "BPC-157 (5mg)", category: "anti-ageing", cat_label: "Anti-Ageing & Skin", cas: "137525-51-0", mw: "1419.53 g/mol", purity: "99.4%", reg_usd: 55.00, sale_usd: 44.00, mechanism: "Stable Gastric Pentadecapeptide", focus: "Tissue Healing, Angiogenesis & Gut Repair", desc: "Synthetic gastric pentadecapeptide for tendon, bone, and mucosal tissue healing.", images: ["<?php echo get_template_directory_uri(); ?>/assets/images/products/bpc157-vial.svg", "<?php echo get_template_directory_uri(); ?>/assets/images/products/bpc157-coa.svg", "<?php echo get_template_directory_uri(); ?>/assets/images/products/bpc157-pack.svg"] },
    { id: 10, name: "TB-500 (5mg)", category: "anti-ageing", cat_label: "Anti-Ageing & Skin", cas: "77591-33-4", mw: "4963.50 g/mol", purity: "99.5%", reg_usd: 65.00, sale_usd: 52.00, mechanism: "Thymosin Beta-4 Active Domain", focus: "Cellular Migration & Tissue Flexibility", desc: "Actin-sequestering peptide regulating cellular repair and anti-fibrotic remodeling.", images: ["<?php echo get_template_directory_uri(); ?>/assets/images/products/tb500-vial.svg", "<?php echo get_template_directory_uri(); ?>/assets/images/products/tb500-coa.svg", "<?php echo get_template_directory_uri(); ?>/assets/images/products/tb500-pack.svg"] },
    { id: 11, name: "CJC-1295 + Ipamorelin (10mg)", category: "muscle", cat_label: "Muscle & GH Axis", cas: "Dual Mix (863288-34-0)", mw: "3367 / 711 g/mol", purity: "99.3%", reg_usd: 85.00, sale_usd: 68.00, mechanism: "GHRH + Ghrelin Receptor Agonist", focus: "Growth Hormone Pulse & Recovery", desc: "1:1 synergistic research formulation for amplified pulsatile GH release.", images: ["<?php echo get_template_directory_uri(); ?>/assets/images/products/cjcipam-vial.svg", "<?php echo get_template_directory_uri(); ?>/assets/images/products/cjcipam-coa.svg", "<?php echo get_template_directory_uri(); ?>/assets/images/products/cjcipam-pack.svg"] },
    { id: 12, name: "MK-677 Ibutamoren (30mL)", category: "muscle", cat_label: "Muscle & GH Axis", cas: "159752-10-0", mw: "624.77 g/mol", purity: "99.1%", reg_usd: 70.00, sale_usd: 56.00, mechanism: "Oral Ghrelin Secretagogue", focus: "IGF-1 Elevation & Nitrogen Retention", desc: "30mL amber dropper bottle with graduated pipette for oral research.", images: ["<?php echo get_template_directory_uri(); ?>/assets/images/products/mk677-photo.jpg", "<?php echo get_template_directory_uri(); ?>/assets/images/products/mk677-coa.svg", "<?php echo get_template_directory_uri(); ?>/assets/images/products/mk677-pack.svg"] },
    { id: 13, name: "Tesamorelin (10mg)", category: "muscle", cat_label: "Muscle & GH Axis", cas: "218949-48-5", mw: "5135.80 g/mol", purity: "99.2%", reg_usd: 105.00, sale_usd: 84.00, mechanism: "GHRH Analog (44-AA)", focus: "Visceral Adipose Loss & GH Pulse", desc: "Potent GHRH analog studied for visceral abdominal fat reduction.", images: ["<?php echo get_template_directory_uri(); ?>/assets/images/products/tesamorelin-vial.svg", "<?php echo get_template_directory_uri(); ?>/assets/images/products/tesamorelin-coa.svg", "<?php echo get_template_directory_uri(); ?>/assets/images/products/tesamorelin-pack.svg"] },
    { id: 14, name: "Semax Nasal Spray (30mg)", category: "cognitive", cat_label: "Cognitive & Vitality", cas: "80714-61-0", mw: "813.92 g/mol", purity: "99.4%", reg_usd: 58.00, sale_usd: 46.00, mechanism: "ACTH(4-10) Heptapeptide Analog", focus: "BDNF Upregulation & Focus", desc: "10mL amber metered nasal spray bottle investigated for BDNF stimulation.", images: ["<?php echo get_template_directory_uri(); ?>/assets/images/products/semax-photo.jpg", "<?php echo get_template_directory_uri(); ?>/assets/images/products/semax-coa.svg", "<?php echo get_template_directory_uri(); ?>/assets/images/products/semax-pack.svg"] },
    { id: 15, name: "Selank Nasal Spray (10mg)", category: "cognitive", cat_label: "Cognitive & Vitality", cas: "129954-34-3", mw: "751.87 g/mol", purity: "99.2%", reg_usd: 55.00, sale_usd: 44.00, mechanism: "Synthetic Tuftsin Analog", focus: "GABA Modulation & Anxiolysis", desc: "Anxiolytic heptapeptide investigated for cognitive stabilization.", images: ["<?php echo get_template_directory_uri(); ?>/assets/images/products/selank-vial.svg", "<?php echo get_template_directory_uri(); ?>/assets/images/products/selank-coa.svg", "<?php echo get_template_directory_uri(); ?>/assets/images/products/selank-pack.svg"] },
    { id: 16, name: "PT-141 Bremelanotide (10mg)", category: "cognitive", cat_label: "Cognitive & Vitality", cas: "189691-06-3", mw: "1025.18 g/mol", purity: "99.3%", reg_usd: 62.00, sale_usd: 50.00, mechanism: "Central MC3 / MC4 Agonist", focus: "Receptor Vitality & CNS Signaling", desc: "Cyclic heptapeptide modulating central hypothalamic pathways.", images: ["<?php echo get_template_directory_uri(); ?>/assets/images/products/pt141-vial.svg", "<?php echo get_template_directory_uri(); ?>/assets/images/products/pt141-coa.svg", "<?php echo get_template_directory_uri(); ?>/assets/images/products/pt141-pack.svg"] },
    { id: 17, name: "Custom 384-Peptide Screening Library", category: "institutional", cat_label: "Institutional ($23k+)", cas: "CUSTOM-ARRAY-384", mw: "High-Throughput", purity: "95-99%", reg_usd: 23450.00, sale_usd: 18760.00, mechanism: "Robotic Microplate Array (ANSI/SLAS)", focus: "Epitope Mapping & High-Throughput Screening", desc: "Formulated in standard 384-well microplates on liquid handler decks. LC-MS for all 384 wells.", images: ["<?php echo get_template_directory_uri(); ?>/assets/images/products/library384-photo.jpg", "<?php echo get_template_directory_uri(); ?>/assets/images/products/library384-coa.svg", "<?php echo get_template_directory_uri(); ?>/assets/images/products/library384-pack.svg"] },
    { id: 18, name: "Kinase Substrate Profiling Array", category: "institutional", cat_label: "Institutional ($23k+)", cas: "KINASE-96-SUB", mw: "96-Well Grid", purity: "98.5%", reg_usd: 8900.00, sale_usd: 7120.00, mechanism: "High-Density Phosphorylation Array", focus: "Enzyme Kinetics & Phosphorylation", desc: "96 distinct pre-arrayed peptide substrates for high-throughput kinase profiling.", images: ["<?php echo get_template_directory_uri(); ?>/assets/images/products/kinase96-vial.svg", "<?php echo get_template_directory_uri(); ?>/assets/images/products/kinase96-coa.svg", "<?php echo get_template_directory_uri(); ?>/assets/images/products/kinase96-pack.svg"] },
    { id: 19, name: "Bulk cGMP Tirzepatide (10-Gram Lot)", category: "institutional", cat_label: "Institutional ($23k+)", cas: "2023788-19-2-BULK", mw: "4813.45 g/mol", purity: "99.5%", reg_usd: 14900.00, sale_usd: 11920.00, mechanism: "Single-Lot Bulk cGMP Synthesis", focus: "Pilot Animal Models & Pre-Clinical Formulations", desc: "10,000mg single-batch lyophilized cake packed in 100mL wide-mouth amber jar with tamper seal.", images: ["<?php echo get_template_directory_uri(); ?>/assets/images/products/bulk10g-photo.jpg", "<?php echo get_template_directory_uri(); ?>/assets/images/products/bulk10g-coa.svg", "<?php echo get_template_directory_uri(); ?>/assets/images/products/bulk10g-pack.svg"] }
];

var themeCurrentFilter = 'all';
var themeCarouselAngles = {};
var themeActiveModal = null;
var themeModalAngle = 0;

function initThemeStore() {
    renderThemeProducts();
}

function renderThemeProducts() {
    var container = document.getElementById('products-container');
    if (!container) return;
    var filtered = themeProducts.filter(function(p) {
        return themeCurrentFilter === 'all' || p.category === themeCurrentFilter;
    });

    var html = '';
    filtered.forEach(function(p) {
        var btc = (p.sale_usd * 0.9).toFixed(2);
        html += '<div class="product-card" style="background:#fff; border:1px solid #E2E8F0; border-radius:12px; padding:18px; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 1px 3px rgba(0,0,0,0.06); position:relative;">';
        html += '  <div>';
        html += '    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">';
        html += '      <span style="background:#DC2626; color:#fff; font-size:10px; font-weight:800; padding:2px 7px; border-radius:4px;">-20% SALE</span>';
        html += '      <span style="background:#ECFDF5; color:#059669; border:1px solid #A7F3D0; padding:2px 8px; border-radius:12px; font-size:10.5px; font-weight:800;">HPLC ≥ ' + p.purity + '</span>';
        html += '    </div>';

        html += '    <div class="carousel-box" onclick="openProductModal(' + p.id + ')" style="position:relative; background:#F8FAFC; border:1px solid #E2E8F0; border-radius:10px; height:230px; overflow:hidden; margin-bottom:12px; display:flex; align-items:center; justify-content:center; cursor:pointer;">';
        html += '      <span style="position:absolute; top:8px; left:8px; background:rgba(15,23,42,0.85); color:#fff; font-size:9.5px; font-weight:700; padding:2px 8px; border-radius:4px; z-index:5;">🔍 Click for Info</span>';
        html += '      <div id="theme-track-' + p.id + '" style="display:flex; width:300%; height:100%; transition:transform 0.25s ease-out;">';
        p.images.forEach(function(img, i) {
            html += '        <div style="width:33.333%; height:100%; display:flex; align-items:center; justify-content:center; padding:12px;"><img src="' + img + '" alt="' + p.name + ' - View ' + (i+1) + '" style="max-height:200px; max-width:100%; object-fit:contain; border-radius:6px;" onerror="this.src='<?php echo get_template_directory_uri(); ?>/assets/images/products/tirzepatide-vial.svg';"></div>';
        });
        html += '      </div>';

        html += '      <div class="hover-arrow prev" onmouseenter="themeSlide(' + p.id + ', -1, event)" onclick="themeSlide(' + p.id + ', -1, event)" style="position:absolute; left:8px; top:50%; transform:translateY(-50%); width:28px; height:28px; background:rgba(255,255,255,0.9); border:1px solid #CBD5E1; border-radius:50%; display:flex; align-items:center; justify-content:center; cursor:pointer; font-weight:800; color:#0F172A; z-index:10;">&lsaquo;</div>';
        html += '      <div class="hover-arrow next" onmouseenter="themeSlide(' + p.id + ', 1, event)" onclick="themeSlide(' + p.id + ', 1, event)" style="position:absolute; right:8px; top:50%; transform:translateY(-50%); width:28px; height:28px; background:rgba(255,255,255,0.9); border:1px solid #CBD5E1; border-radius:50%; display:flex; align-items:center; justify-content:center; cursor:pointer; font-weight:800; color:#0F172A; z-index:10;">&rsaquo;</div>';

        html += '      <div style="position:absolute; bottom:8px; left:0; right:0; display:flex; justify-content:center; gap:6px; z-index:10;">';
        html += '        <span class="pip pip-' + p.id + ' active" onmouseenter="themeGoTo(' + p.id + ', 0, event)" style="width:7px; height:7px; border-radius:50%; background:#059669; cursor:pointer;"></span>';
        html += '        <span class="pip pip-' + p.id + '" onmouseenter="themeGoTo(' + p.id + ', 1, event)" style="width:7px; height:7px; border-radius:50%; background:#CBD5E1; cursor:pointer;"></span>';
        html += '        <span class="pip pip-' + p.id + '" onmouseenter="themeGoTo(' + p.id + ', 2, event)" style="width:7px; height:7px; border-radius:50%; background:#CBD5E1; cursor:pointer;"></span>';
        html += '      </div>';
        html += '    </div>';

        html += '    <div style="font-size:11px; color:#059669; font-weight:700; text-transform:uppercase; margin-bottom:2px;">' + p.cat_label + '</div>';
        html += '    <h3 onclick="openProductModal(' + p.id + ')" style="font-family:'Montserrat',sans-serif; font-size:16px; font-weight:800; color:#0F172A; margin-bottom:4px; cursor:pointer;">' + p.name + '</h3>';
        html += '    <div style="font-size:11px; color:#64748B; font-family:'Space Mono',monospace; margin-bottom:10px;">CAS: ' + p.cas + ' &bull; Batch #PHX-2026</div>';
        html += '    <div style="background:#FEF3C7; color:#92400E; border:1px solid #FDE68A; padding:4px 8px; border-radius:6px; font-size:11px; font-weight:700; margin-bottom:12px; display:flex; align-items:center; gap:5px;"><span>⚡</span> Extra 10% Off with BTC: <strong>$' + btc + '</strong></div>';
        html += '  </div>';

        html += '  <div style="border-top:1px solid #F1F5F9; padding-top:12px; display:flex; justify-content:space-between; align-items:center;">';
        html += '    <div><span style="font-size:12px; color:#94A3B8; text-decoration:line-through;">$' + p.reg_usd.toFixed(2) + '</span><div style="font-family:'Montserrat',sans-serif; font-size:18px; font-weight:900; color:#059669;">$' + p.sale_usd.toFixed(2) + '</div></div>';
        html += '    <div style="display:flex; align-items:center;">';
        html += '      <button onclick="openProductModal(' + p.id + ')" style="background:#F1F5F9; color:#0F172A; border:1px solid #E2E8F0; padding:8px 10px; border-radius:6px; font-size:12px; font-weight:700; cursor:pointer; margin-right:6px;">Info</button>';
        html += '      <button onclick="alert('Added ' + p.name + ' to Research Batch!')" style="background:#059669; color:#fff; border:none; padding:8px 14px; border-radius:6px; font-size:12px; font-weight:700; cursor:pointer;">+ Add</button>';
        html += '    </div>';
        html += '  </div>';
        html += '</div>';
    });

    container.innerHTML = html;
}

function themeSlide(id, dir, e) {
    if (e) e.stopPropagation();
    if (!themeCarouselAngles[id]) themeCarouselAngles[id] = 0;
    themeCarouselAngles[id] = (themeCarouselAngles[id] + dir + 3) % 3;
    updateThemeCarouselTrack(id);
}

function themeGoTo(id, idx, e) {
    if (e) e.stopPropagation();
    themeCarouselAngles[id] = idx;
    updateThemeCarouselTrack(id);
}

function updateThemeCarouselTrack(id) {
    var angle = themeCarouselAngles[id] || 0;
    var track = document.getElementById('theme-track-' + id);
    if (track) track.style.transform = 'translateX(-' + (angle * 33.3333) + '%)';
    var pips = document.querySelectorAll('.pip-' + id);
    pips.forEach(function(pip, i) {
        pip.style.background = i === angle ? '#059669' : '#CBD5E1';
    });
}

function filterCategory(cat, btn) {
    themeCurrentFilter = cat;
    document.querySelectorAll('.cat-pill').forEach(function(b) {
        b.style.background = '#F1F5F9';
        b.style.color = '#334155';
    });
    if (btn) {
        btn.style.background = '#0F172A';
        btn.style.color = '#FFFFFF';
    }
    renderThemeProducts();
}

function openProductModal(id) {
    var p = themeProducts.find(function(item) { return item.id === id; });
    if (!p) return;
    themeActiveModal = p;
    themeModalAngle = 0;

    document.getElementById('modal-cat-tag').innerText = p.cat_label;
    document.getElementById('modal-title').innerText = p.name;
    document.getElementById('modal-purity-badge').innerText = 'HPLC ≥ ' + p.purity + ' Validated';
    document.getElementById('modal-desc').innerText = p.desc;
    document.getElementById('modal-mechanism').innerText = p.mechanism;
    document.getElementById('modal-focus').innerText = p.focus;
    document.getElementById('modal-cas').innerText = p.cas;
    document.getElementById('modal-mw').innerText = p.mw;

    document.getElementById('modal-price-reg').innerText = '$' + p.reg_usd.toFixed(2);
    document.getElementById('modal-price-sale').innerText = '$' + p.sale_usd.toFixed(2);
    document.getElementById('modal-price-btc').innerText = '$' + (p.sale_usd * 0.9).toFixed(2);
    document.getElementById('modal-qty').value = 1;

    updateThemeModalGallery();

    document.getElementById('modal-add-btn').onclick = function() {
        alert('Added ' + p.name + ' to Research Batch!');
        closeProductModal();
    };

    document.getElementById('product-modal').style.display = 'flex';
}

function updateThemeModalGallery() {
    if (!themeActiveModal) return;
    document.getElementById('modal-main-img').src = themeActiveModal.images[themeModalAngle];
    var thumbs = document.getElementById('modal-thumbs-box');
    var html = '';
    themeActiveModal.images.forEach(function(img, i) {
        var border = i === themeModalAngle ? '2px solid #059669' : '1px solid #E2E8F0';
        html += '<div onclick="setThemeModalAngle(' + i + ')" style="flex:1; height:75px; background:#F8FAFC; border:' + border + '; border-radius:8px; cursor:pointer; display:flex; align-items:center; justify-content:center; padding:6px;">';
        html += '  <img src="' + img + '" style="max-height:100%; max-width:100%; object-fit:contain;" onerror="this.src='<?php echo get_template_directory_uri(); ?>/assets/images/products/tirzepatide-vial.svg';">';
        html += '</div>';
    });
    thumbs.innerHTML = html;
}

function setThemeModalAngle(idx) {
    themeModalAngle = idx;
    updateThemeModalGallery();
}

function closeProductModal(e) {
    if (e && e.target !== document.getElementById('product-modal')) return;
    document.getElementById('product-modal').style.display = 'none';
    themeActiveModal = null;
}

window.addEventListener('DOMContentLoaded', initThemeStore);
</script>

<?php get_footer(); ?>
