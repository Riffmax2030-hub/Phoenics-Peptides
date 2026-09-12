# Phoenics Peptide — Kinsta Managed WordPress Setup Guide

This guide details the exact production deployment architecture for **phoenicspeptide.com** on Kinsta.

---

## 1. Plan & Data Center Selection
- **Recommended Plan:** Kinsta Business 1 or Single 35k (scales dynamically with traffic surges).
- **Primary Data Center Location:** 
  - **Option A (Americas/Global):** Google Cloud Platform (GCP) **Council Bluffs, Iowa (us-central1)** or **Ashburn, Virginia (us-east4)**.
  - **Option B (Europe/Africa hybrid):** GCP **Frankfurt, Germany (europe-west3)**.
- **PHP Version:** PHP 8.2 or 8.3 (WooCommerce optimized).
- **Database:** MariaDB 10.11 / MySQL 8.0 with InnoDB buffer tuned.

---

## 2. Cloudflare Enterprise & Edge CDN Configuration
Kinsta includes free Cloudflare Enterprise integration.
1. Add custom domain `phoenicspeptide.com` and `www.phoenicspeptide.com`.
2. Update Nameservers or Point A Records to Kinsta Site IP.
3. Enable **Edge Caching** in MyKinsta dashboard (caches HTML output in 275+ global points of presence across USA, Canada, Europe, Africa, and Asia).
4. Set **Automatic SSL** (Wildcard TLS 1.3).
5. Enable **Early Hints** and **Image Optimization (WebP on the fly)**.

---

## 3. Uploading Theme & Custom Shipping Plugin

### Via SFTP or SSH:
```bash
# Upload Phoenics Theme
wp-content/themes/phoenics-theme/

# Upload Custom Shipping Plugin
wp-content/plugins/phoenics-shipping/
```

### Via WordPress Admin:
1. Go to **Appearance > Themes > Add New > Upload Theme** -> Select `phoenics-theme.zip`.
2. Go to **Plugins > Add New > Upload Plugin** -> Select `phoenics-shipping.zip`.
3. Activate both.

---

## 4. Performance & Caching Rules
Add the following WooCommerce cache exclusions in Kinsta NGINX config (handled automatically by Kinsta for standard WooCommerce paths):
- `/cart/*`
- `/checkout/*`
- `/my-account/*`
- `/track-order/*` (ensures live telemetry lookup is always non-cached dynamic AJAX)
