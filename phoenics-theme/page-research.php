<?php
/**
 * Template Name: Research & Science Laboratory
 */

get_header(); ?>

<main id="primary" class="site-main research-page-layout">
    <!-- PAGE HEADER -->
    <section class="page-hero-banner">
        <div class="container">
            <span class="hero-subtag">BIOCHEMICAL VERIFICATION & PROTOCOLS</span>
            <h1 class="page-title">Analytical Science & HPLC/MS Laboratory Protocols</h1>
            <p class="page-subtitle">Standard Operating Procedures, High-Performance Liquid Chromatography benchmarks, and laboratory reconstitution guidelines for Phoenics Peptide analytical compounds.</p>
        </div>
    </section>

    <div class="container main-content-container">
        <!-- METHODOLOGY & PURITY BENCHMARK -->
        <section class="research-grid-section">
            <div class="science-card">
                <div class="icon-circle">🔬</div>
                <h3>Solid-Phase Peptide Synthesis (SPPS)</h3>
                <p>All peptide sequences distributed by Phoenics Peptide are manufactured via state-of-the-art Fmoc solid-phase peptide synthesis on automated robotic synthesizers, ensuring minimal side reactions and maximum chain assembly efficiency.</p>
            </div>

            <div class="science-card">
                <div class="icon-circle">📊</div>
                <h3>Reverse-Phase HPLC Purity Testing</h3>
                <p>Every batch undergoes analytical RP-HPLC utilizing C18 columns with gradient acetonitrile/water mobile phases containing 0.1% TFA. Compounds are only cleared for inventory upon achieving a verified optical purity &ge; 99.0%.</p>
            </div>

            <div class="science-card">
                <div class="icon-circle">⚖️</div>
                <h3>Electrospray Ionization MS (ESI-MS)</h3>
                <p>Exact molecular weight confirmation is executed using high-resolution electrospray ionization mass spectrometry to verify that the synthesized peptide matches theoretical sequence molecular mass within ±1 Dalton.</p>
            </div>
        </section>

        <!-- LAB RECONSTITUTION GUIDE -->
        <section class="reconstitution-protocol-card">
            <h2>Standard Laboratory Reconstitution Guidelines (In-Vitro Use Only)</h2>
            <div class="protocol-steps">
                <div class="proto-step">
                    <span class="step-num">01</span>
                    <h4>Aseptic Acclimation</h4>
                    <p>Remove the lyophilized peptide vial from -20°C freezer and allow it to reach ambient room temperature (20-25°C) inside a laminar flow cabinet for 15-20 minutes before unscrewing the cap to prevent moisture condensation.</p>
                </div>
                <div class="proto-step">
                    <span class="step-num">02</span>
                    <h4>Reconstitution Diluent</h4>
                    <p>Swab the rubber septum with a 70% isopropyl alcohol wipe. Using a sterile laboratory syringe, slowly introduce sterile 0.9% Bacteriostatic Water or scientific sterile saline down the inner glass wall of the vial.</p>
                </div>
                <div class="proto-step">
                    <span class="step-num">03</span>
                    <h4>Gentle Solubilization</h4>
                    <p>Do NOT vortex vigorously. Gently swirl the vial in circular motion until the lyophilized cake is fully dissolved into a crystal-clear, colorless solution.</p>
                </div>
                <div class="proto-step">
                    <span class="step-num">04</span>
                    <h4>Aliquot & Preservation</h4>
                    <p>For extended research experiments, divide the reconstituted solution into single-use sterile microcentrifuge tubes to prevent repetitive freeze-thaw cycles. Store at 2-8°C for short term (up to 21 days) or -20°C for long term.</p>
                </div>
            </div>
        </section>
    </div>
</main>

<?php get_footer(); ?>
