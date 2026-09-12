(function($) {
    'use strict';

    $(document).ready(function() {
        var $form = $('#phoenics-tracking-form');
        var $input = $('#phoenics-tracking-input');
        var $btn = $('#phoenics-tracking-btn');
        var $loader = $('#phoenics-tracking-loader');
        var $error = $('#phoenics-tracking-error');
        var $result = $('#phoenics-tracking-result');

        // Check URL query param e.g. ?tracking_id=1042
        var urlParams = new URLSearchParams(window.location.search);
        var trackingParam = urlParams.get('tracking_id');
        if (trackingParam) {
            $input.val(trackingParam);
            performLookup(trackingParam);
        }

        $form.on('submit', function(e) {
            e.preventDefault();
            var query = $.trim($input.val());
            if (!query) return;
            performLookup(query);
        });

        function performLookup(query) {
            $error.hide();
            $result.hide();
            $loader.show();
            $btn.prop('disabled', true);

            // AJAX call to WordPress
            $.ajax({
                url: phoenics_tracking_ajax.ajax_url,
                type: 'POST',
                data: {
                    action: 'phoenics_lookup_tracking',
                    nonce: phoenics_tracking_ajax.nonce,
                    tracking_query: query
                },
                success: function(response) {
                    $loader.hide();
                    $btn.prop('disabled', false);

                    if (response.success && response.data) {
                        var d = response.data;
                        $('#res-status').text(d.order_status);
                        $('#res-cold-chain').text(d.cold_chain);
                        $('#res-order-id').text('#' + d.order_id);
                        $('#res-carrier-name').text(d.carrier + ' Priority Cargo');
                        $('#res-awb').text(d.tracking_number);
                        $('#res-delivery-window').text(d.est_delivery);
                        $('#res-date-created').text(d.date_created);
                        $('#res-origin').text(d.origin_hub);
                        $('#res-carrier-info').text(d.carrier);
                        $('#res-est-deliv').text(d.est_delivery);
                        $('#res-carrier-link').attr('href', d.carrier_url);

                        $result.fadeIn(250);
                    } else {
                        var msg = (response.data && response.data.message) ? response.data.message : 'Unable to find tracking records for this identifier.';
                        $error.text(msg).show();
                    }
                },
                error: function() {
                    $loader.hide();
                    $btn.prop('disabled', false);
                    $error.text('Logistics telemetry network timeout. Please check your connection or try again.').show();
                }
            });
        }
    });
})(jQuery);
