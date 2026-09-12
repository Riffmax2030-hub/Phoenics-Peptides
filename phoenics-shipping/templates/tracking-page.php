<?php
/**
 * Frontend Public Tracking Portal Template
 */

if (!defined('ABSPATH')) {
    exit;
}
?>
<div class="phoenics-tracking-wrapper">
    <div class="tracking-search-card">
        <div class="tracking-search-header">
            <span class="satellite-pulse"></span>
            <h2>Global Cold-Chain Satellite Tracking</h2>
            <p>Real-time telemetry and logistics status for international analytical research shipments.</p>
        </div>

        <form id="phoenics-tracking-form" class="tracking-search-form">
            <div class="input-group">
                <input type="text" id="phoenics-tracking-input" placeholder="Enter Phoenics Order # (e.g. 1042) or Carrier Tracking AWB" required />
                <button type="submit" id="phoenics-tracking-btn">
                    <span>Inspect Shipment</span> &rarr;
                </button>
            </div>
            <div class="tracking-hints">
                <span>⚡ Supports DHL Express, FedEx International, USPS, Canada Post & Aramex</span>
            </div>
        </form>

        <div id="phoenics-tracking-loader" class="tracking-loader" style="display:none;">
            <div class="spinner"></div>
            <p>Querying international cold-chain logistics telemetry...</p>
        </div>

        <div id="phoenics-tracking-error" class="tracking-error" style="display:none;"></div>
    </div>

    <!-- LIVE TELEMETRY RESULT DISPLAY -->
    <div id="phoenics-tracking-result" class="tracking-result-card" style="display:none;">
        <div class="result-top-bar">
            <div>
                <span class="label">SHIPMENT STATUS</span>
                <h3 id="res-status" class="status-badge">In Transit (Air Cargo)</h3>
            </div>
            <div class="cold-chain-telemetry">
                <span class="temp-icon">❄️</span>
                <div>
                    <span class="temp-label">COLD-CHAIN INTEGRITY</span>
                    <strong id="res-cold-chain">-20°C (Lyophilized Nitrogen Pack)</strong>
                </div>
            </div>
        </div>

        <div class="timeline-container">
            <ul class="timeline-steps">
                <li class="step step-done" id="step-ordered">
                    <div class="step-icon">✓</div>
                    <div class="step-label">Order Validated</div>
                    <div class="step-time" id="res-date-created">Sept 12, 2026</div>
                </li>
                <li class="step step-done" id="step-qc">
                    <div class="step-icon">🔬</div>
                    <div class="step-label">HPLC/MS Purity &gt;99% QC</div>
                    <div class="step-time">Passed Batch Certificate</div>
                </li>
                <li class="step step-done" id="step-packed">
                    <div class="step-icon">❄️</div>
                    <div class="step-label">Cold-Chain Packaged</div>
                    <div class="step-time" id="res-origin">Boston Central Hub</div>
                </li>
                <li class="step step-active" id="step-transit">
                    <div class="step-icon">✈️</div>
                    <div class="step-label">International Transit</div>
                    <div class="step-time" id="res-carrier-info">DHL Express Priority</div>
                </li>
                <li class="step" id="step-delivered">
                    <div class="step-icon">📦</div>
                    <div class="step-label">Laboratory Delivery</div>
                    <div class="step-time" id="res-est-deliv">Est: 2-3 Days</div>
                </li>
            </ul>
        </div>

        <div class="shipment-meta-grid">
            <div class="meta-item">
                <span class="meta-title">Order Identifier</span>
                <span class="meta-val" id="res-order-id">#1042</span>
            </div>
            <div class="meta-item">
                <span class="meta-title">Assigned Logistics Partner</span>
                <span class="meta-val" id="res-carrier-name">DHL Express Worldwide</span>
            </div>
            <div class="meta-item">
                <span class="meta-title">Master Air Waybill (AWB)</span>
                <span class="meta-val highlight" id="res-awb">794820194821</span>
            </div>
            <div class="meta-item">
                <span class="meta-title">Target Delivery Window</span>
                <span class="meta-val" id="res-delivery-window">Within 48-72 Hours</span>
            </div>
        </div>

        <div class="carrier-action-footer">
            <a id="res-carrier-link" href="#" target="_blank" class="carrier-btn">
                <span>View Official Carrier Satellite Telemetry</span> &rarr;
            </a>
        </div>
    </div>
</div>
