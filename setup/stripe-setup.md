# Phoenics Peptide — Stripe Worldwide Payment Gateway Setup

Stripe provides compliant worldwide credit card processing covering North America, Europe, Canada, and parts of Asia and Africa.

---

## 1. Stripe Account Activation
1. Sign up or log into [dashboard.stripe.com](https://dashboard.stripe.com).
2. Complete institutional business verification under **Biotechnology / Analytical Reagents / In-Vitro Research Supplies**.
3. Enable **3D Secure 2.0 (SCA Compliance)** for EU, UK, and global card security.

---

## 2. API Keys Configuration
1. Navigate to **Developers > API Keys**.
2. Copy your:
   - **Publishable Key:** `pk_live_...`
   - **Secret Key:** `sk_live_...`

---

## 3. WooCommerce Stripe Integration
1. Install **WooCommerce Stripe Payment Gateway** plugin.
2. Go to **WooCommerce > Settings > Payments > Stripe Credit Card**.
3. Check **Enable Stripe**.
4. Enter your Publishable Key and Secret Key.
5. Enable **Inline Credit Card Form** (cleaner UX).
6. Enable **Apple Pay / Google Pay / Microsoft Pay**.
7. Set Webhook Endpoint in Stripe Dashboard:
   - URL: `https://phoenicspeptide.com/?wc-api=wc_stripe`
   - Events to listen to: `payment_intent.succeeded`, `payment_intent.payment_failed`, `charge.dispute.created`.

---

## 4. Multi-Currency Support
Stripe automatically accepts charges in 135+ currencies and settles into your primary business account currency (USD, EUR, GBP, or CAD). Combined with our theme's multi-currency switcher, foreign customers see their local currency throughout their shopping and checkout experience!
