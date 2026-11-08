# richardcollins.org

Personal website and research hub for **Richard Collins**.

Live at: [https://richardcollins.org](https://richardcollins.org)

## Structure

```text
├── index.html       # Main landing page
├── style.css        # Responsive styling (light/dark mode aware)
├── CNAME            # Custom domain configuration for GitHub Pages
└── README.md        # Project documentation
```

## Local Development

You can open `index.html` directly in your browser or run a quick local web server:

```bash
# Python 3
python3 -m http.server 8000

# Open in browser
open http://localhost:8000
```

## GitHub Pages & Custom Domain Setup

1. **GitHub Pages Source**:
   - Go to your repository settings on GitHub: **Settings** &rarr; **Pages**.
   - Under **Build and deployment** &rarr; **Source**, select **Deploy from a branch**.
   - Choose branch `main` and folder `/ (root)`. Click **Save**.

2. **Custom Domain**:
   - The repository includes a `CNAME` file set to `richardcollins.org`.
   - On GitHub Pages settings, verify that **Custom domain** displays `richardcollins.org`.
   - Check **Enforce HTTPS** once the certificate finishes provisioning.

3. **DNS Configuration (at your domain registrar / DNS provider)**:
   Add the following DNS records for `richardcollins.org`:

   - **A Records** (for apex `@` domain):
     - `185.199.108.153`
     - `185.199.109.153`
     - `185.199.110.153`
     - `185.199.111.153`
   - **CNAME Record** (for `www` subdomain):
     - Host: `www`
     - Value: `richardkcollins.github.io`
