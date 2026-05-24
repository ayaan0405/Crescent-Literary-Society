# 🌙 Crescent Literary Society (CLS) Website

Welcome to the official repository of the **Crescent Literary Society (CLS)** website. This codebase powers a highly polished, responsive, and dynamic web application featuring the society's active wings, creative publications, blogs, and an administrative dashboard powered by **Decap CMS** (formerly Netlify CMS).

---

## 🚀 Quick Start: Running the Site Locally

Due to security restrictions in modern web browsers (CORS), opening the `.html` files directly via double-clicking (the `file://` protocol) will prevent dynamic content (such as blog posts, newsletters, and member lists stored in JSON format) from loading.

To view the website with all its dynamic content active, you **must run a local web server**.

### Option 1: Using Python (Recommended & Easiest)
If you have Python installed, you can launch a local server instantly:

1. Open your terminal (Command Prompt, PowerShell, or Git Bash) in this project folder.
2. Run the following command:
   ```bash
   python -m http.server 8080
   ```
3. Open your browser and navigate to: **[http://localhost:8080](http://localhost:8080)**

### Option 2: Using Node.js (npm / npx)
If you prefer Node/npm, you can use any static server library like `serve`:

1. Run the server using `npx`:
   ```bash
   npx serve . -p 8080
   ```
2. Open your browser and navigate to: **[http://localhost:8080](http://localhost:8080)**

---

## 🎨 Tech Stack & Architecture

This website is engineered to be blazing fast, visually stunning, and extremely lightweight:

* **Frontend Structure:** Standard modern HTML5, structured semantically.
* **Styling & Aesthetics:** Custom CSS3 with advanced animations, custom HSL color-tailored systems, and dark theme variables for a premium, immersive reader experience. No bloated CSS frameworks are used, ensuring maximum performance.
* **Dynamic Loading:** A bespoke client-side JavaScript engine (`js/cms-loader.js`) that dynamically fetches and renders content directly from localized `.json` files.
* **CMS & Content Management:** Integrated with **Decap CMS**, allowing non-technical editors to publish blog posts, issues, and modify carousels without touching a single line of code.
* **Hosting & Backend Integration:** Configured for seamless deployment on **Netlify**, utilizing **Netlify Forms** for interactive forms (such as contact forms).

---

## 📁 Repository Structure

```tree
e:\CLS
├── admin/                    # Decap CMS Admin Dashboard
│   ├── config.yml            # Schema and configurations for the CMS collections
│   └── index.html            # Dashboard entry point
├── assets/                   # Static media assets (logos, illustrations, default icons)
├── css/                      # Core stylesheets
│   ├── global.css            # Custom utility variables, color tokens, and layout styles
│   ├── animations.css        # Interactive hover states, page transition styles, and animations
│   └── [page-specific].css  # Styles tailored to individual views (about, blog, etc.)
├── data/                     # Content Database (JSON files)
│   ├── blog/                 # Blog post JSONs
│   ├── crescent-line/        # Newsletter issue JSONs
│   ├── meraki/               # Magazine issue JSONs
│   ├── carousel/             # Dynamic Homepage/Wing slideshow details
│   └── members.json          # Society Editorial Board listing
├── js/                       # Client-side JavaScript logic
│   ├── main.js               # Navigation menu, core interactions, and theme controls
│   ├── cms-loader.js         # AJAX-based parser for JSON content and markdown rendering
│   ├── carousel.js           # Infinite touch-friendly slideshow controllers
│   └── contact.js            # Netlify AJAX contact form processor
├── [page].html               # Core pages (index, about, wings, publications, connect)
└── README.md                 # This manual
```

---

## ✍️ Managing Content (CMS)

To add new blogs, newsletters, magazine issues, or update the home page slideshow, you can access the admin dashboard.

1. Start your local web server.
2. In your browser, navigate to: **`http://localhost:8080/admin/`** (or your live production domain `/admin/`).
3. Log in using your registered society GitHub account.
4. From the left-hand menu, you can select and manage:
   * **Blogs:** Create and edit literary entries.
   * **Meraki Magazine:** Upload and manage issue details.
   * **Crescent Line:** Release news and writeups.
   * **Carousels:** Swap out and rearrange landing page slider images.
   * **Members:** Update the list of editorial board members.

> [!TIP]
> For a comprehensive walkthrough of CMS operations, image optimization guidelines, and troubleshooting, please refer to the **Website Operations Manual** located in this workspace.

---

## 🛠️ Internal Maintenance Scripts

The repository contains several utility Python scripts in the root directory that help keep the design consistent across all HTML pages. You do not need to run these during normal updates, but they are useful when performing site-wide structural changes:

* **`sync_footers.py` / `update_footer.py`:** Updates the footer structure across every page in the project to make sure social links, copyrights, and disclaimers are uniformly identical.
* **`fix_ui.py`:** Resolves navigation bar menu mismatches and ensures uniform styling variables are applied cleanly.
* **`add_yt.py` / `update_yt.py`:** Standardizes video components and social icons across standard templates.

---

## 🌐 Deploying to Production (Netlify)

The site is configured to automatically redeploy every time you push code changes to the main branch of your GitHub repository. Netlify detects changes to the `.json` data files (committed via the CMS or manually) and triggers a fast rebuild of the site.

### ⚠️ Netlify Build Limit Note
* The free tier of Netlify includes **300 minutes of build time per month**. 
* Every publication or edit in the CMS triggers a fresh deploy (build). 
* To conserve build minutes, try to combine multiple CMS draft publishes into a single publishing action, and preview your work locally using the Python server before merging massive changes.
