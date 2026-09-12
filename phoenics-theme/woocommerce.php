<?php
/**
 * WooCommerce Wrapper Template
 */

get_header(); ?>

<main id="primary" class="site-main woocommerce-main-wrapper">
    <div class="container woo-container-padded">
        <?php woocommerce_content(); ?>
    </div>
</main>

<?php get_footer(); ?>
