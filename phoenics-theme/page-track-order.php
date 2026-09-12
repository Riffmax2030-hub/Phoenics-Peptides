<?php
/**
 * Template Name: Order Tracking Portal
 */

get_header(); ?>

<main id="primary" class="site-main page-tracking-layout">
    <section class="page-hero-banner tracking-banner">
        <div class="container">
            <span class="hero-subtag">GLOBAL SATELLITE DISPATCH TELEMETRY</span>
            <h1 class="page-title">Real-Time Cold-Chain Order Tracking</h1>
            <p class="page-subtitle">Track your research shipment across international air cargo carriers with active temperature validation.</p>
        </div>
    </section>

    <div class="container tracking-page-container">
        <?php echo do_shortcode('[phoenics_order_tracking]'); ?>
    </div>
</main>

<?php get_footer(); ?>
