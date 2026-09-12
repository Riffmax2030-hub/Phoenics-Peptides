# Phoenics Peptide — Render Static Deployment Guide

## Quick Setup (Zero Cost, 2 Minutes)

### 1. Push to GitHub
Commit and push this repository to your GitHub account:
```bash
git add .
git commit -m "Deploy Phoenics Peptide production storefront"
git push origin main
```

### 2. Connect to Render
1. Log in to [render.com](https://render.com) (Free account).
2. Click **New +** → **Static Site**.
3. Select your repository.
4. Set the following build options:
   - **Name:** `phoenics-peptide`
   - **Branch:** `main`
   - **Build Command:** *(Leave empty)*
   - **Publish Directory:** `phoenicspeptide/standalone-preview`
5. Click **Create Static Site**.

### 3. Done!
Your storefront will immediately be live on a fast global CDN with automated SSL at:
`https://phoenics-peptide.onrender.com`

---

## Setting Up Your Custom Domain (Optional)
1. In your Render Dashboard, select **Custom Domains**.
2. Enter your domain (e.g. `phoenicspeptide.com`).
3. Add the CNAME / A record in your domain registrar (Namecheap, GoDaddy, Cloudflare) as instructed by Render.
4. SSL certificate is automatically generated for free.
