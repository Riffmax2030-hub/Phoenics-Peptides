# Phoenics Peptide — Bitcoin & Crypto Gateway Architecture

## 1. Personal Bitcoin & Lightning Gateway: BTCPay Server (0% Fees, Direct to Your Wallet)

**BTCPay Server** is a self-hosted, open-source cryptocurrency payment processor. It ensures:
- **0% Processing Fees** (no middleman taking 1-3%).
- **Direct-to-Wallet Settlement:** Funds land directly in your cold storage hardware wallet (Trezor, Ledger, Coldcard) or software wallet (Electrum, BlueWallet).
- **Censorship Resistant:** No third party can freeze your peptide sales funds or deny transactions.
- **Lightning Network Support:** Instant, sub-cent fee transactions for global buyers.

---

### Step 1: Deploying BTCPay Server
You have two simple options:
1. **Free/Managed Community Host:** Use a trusted hosted instance like **LunaNode BTCPay** (~$9/mo) or **Voltage Cloud**.
2. **Dedicated Cloud VPS (DigitalOcean / Hetzner):**
   ```bash
   # One-line Docker deployment on Ubuntu 22.04 LTS
   git clone https://github.com/btcpayserver/btcpayserver-docker
   cd btcpayserver-docker
   export BTCPAY_HOST="btcpay.phoenicspeptide.com"
   export NBITCOIN_NETWORK="mainnet"
   export BTCPAYGEN_CRYPTO1="btc"
   export BTCPAYGEN_LIGHTNING="clightning"
   . ./btcpay-setup.sh -i
   ```

---

### Step 2: Connecting Your Personal Bitcoin Wallet
1. In your BTCPay Server dashboard, navigate to **Store Settings > Payment Methods > BTC**.
2. Click **Set up wallet**.
3. Import your **Extended Public Key (xPub / yPub / zPub)** from your hardware wallet (Ledger, Trezor, or Electrum).
   - *Note: The xPub ONLY allows viewing addresses and receiving funds; private keys NEVER touch the server.*
4. Save settings. BTCPay will now generate a fresh, unused Bitcoin address for every customer checkout.

---

### Step 3: WooCommerce Integration
1. In WordPress Admin, install the official plugin: **BTCPay Server for WooCommerce**.
2. Go to **WooCommerce > Settings > Payments > BTCPay Server**.
3. Click **Connect to BTCPay Server** (Authorize API key).
4. Select your store.
5. In **Order Status on Payment**, set to `Processing` or `Cold-Chain Packaged`.

---

## 2. Multi-Crypto Gateway: NOWPayments (USDT, USDC, ETH, SOL)

To cater to international clients in Europe, Asia, and Africa who prefer stablecoins (USDT TRC20/ERC20, USDC) or Ethereum:

1. Sign up at [nowpayments.io](https://nowpayments.io).
2. Enter your payout wallet addresses (e.g. USDT TRC20 for near-zero gas fees).
3. Generate your API Key and IPN Secret Key.
4. In WordPress Admin, install **NOWPayments for WooCommerce**.
5. Enable coins: `USDT`, `USDC`, `ETH`, `SOL`, `LTC`.
6. Enable **Auto-Coin Conversion to USDT** if you want all receipts immediately consolidated into stable USD-pegged tokens.

---

## 3. Customer Experience at Checkout
- The customer selects **"₿ Pay with Bitcoin / Lightning"** or **"🪙 Pay with USDT / Crypto"**.
- An dynamic QR code and exact cryptographic invoice are generated with live exchange rate locked for 20 minutes.
- Once the blockchain transaction broadcasts (0-conf or 1 confirmation), WooCommerce automatically updates order status to **Paid / Processing** and dispatches the confirmation email!
