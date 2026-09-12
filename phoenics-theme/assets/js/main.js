(function($) {
    'use strict';

    $(document).ready(function() {
        // Mobile Drawer
        var $drawer = $('#mobile-nav-drawer');
        var $overlay = $('#mobile-nav-overlay');
        var $openBtn = $('#mobile-nav-btn');
        var $closeBtn = $('#drawer-close-btn');

        $openBtn.on('click', function() {
            $drawer.addClass('open');
            $overlay.addClass('active');
        });

        $closeBtn.add($overlay).on('click', function() {
            $drawer.removeClass('open');
            $overlay.removeClass('active');
        });

        // Sticky Header scroll
        var $header = $('#site-header');
        $(window).on('scroll', function() {
            if ($(window).scrollTop() > 40) {
                $header.addClass('scrolled');
            } else {
                $header.removeClass('scrolled');
            }
        });

        // Multi-Currency Converter (USD and EUR ONLY)
        var rates = {
            'USD': { symbol: '$', rate: 1.0 },
            'EUR': { symbol: '€', rate: 0.92 }
        };

        var $currSelector = $('#phoenics-currency-selector');
        var savedCurrency = localStorage.getItem('phoenics_curr') || 'USD';
        if (savedCurrency !== 'USD' && savedCurrency !== 'EUR') {
            savedCurrency = 'USD';
        }
        $currSelector.val(savedCurrency);

        $currSelector.on('change', function() {
            var selected = $(this).val();
            localStorage.setItem('phoenics_curr', selected);
            applyCurrency(selected);
        });

        function applyCurrency(code) {
            var curr = rates[code] || rates['USD'];
            // Update currency symbols across price elements with data-usd-price
            $('[data-usd-price]').each(function() {
                var basePrice = parseFloat($(this).attr('data-usd-price'));
                if (!isNaN(basePrice)) {
                    var converted = (basePrice * curr.rate).toFixed(2);
                    $(this).html(curr.symbol + converted);
                }
            });
            $('[data-usd-sale]').each(function() {
                var salePrice = parseFloat($(this).attr('data-usd-sale'));
                if (!isNaN(salePrice)) {
                    var converted = (salePrice * curr.rate).toFixed(2);
                    $(this).html(curr.symbol + converted);
                }
            });
        }

        applyCurrency(savedCurrency);
    });
})(jQuery);
