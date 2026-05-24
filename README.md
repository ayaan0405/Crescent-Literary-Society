# 🌙 Crescent Literary Society (CLS)

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Glossary/HTML5)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Netlify](https://img.shields.io/badge/Netlify-00C896?style=for-the-badge&logo=netlify&logoColor=white)](https://www.netlify.com/)
[![Decap CMS](https://img.shields.io/badge/Decap%20CMS-FF6B6B?style=for-the-badge&logo=decap-cms&logoColor=white)](https://decapcms.org/)

The official premium web application for the **Crescent Literary Society (CLS)**, established in 2006. Engineered with blazing fast performance, surgical code architecture, custom HSL styling, and dark theme support.

---

## 📖 Overview

The Crescent Literary Society website is a high-fidelity, responsive, multi-page application that serves as the digital hub for our members, publications, and four core wings. The site integrates **Decap CMS** with a secure GitHub backend for direct content publishing and is hosted on **Netlify** with dynamic forms, optimized asset caching, and robust security headers.

---

## ✨ Features

- **⚡ Blazing Fast Architecture:** Vanilla HTML5, CSS3, and modern async ES6+ Javascript with zero bloated frameworks.
- **🎨 HSL Design Token System:** Implements a state-of-the-art dark and light theme toggle fueled purely by uniform HSL color tokens in CSS.
- **🔗 Slug-Based Routing:** Modern, SEO-optimized URL routing replacing brittle indices (`post.html?slug=my-first-post`).
- **🛡️ Secure Client-Side Engine:** Parallel fetches via `Promise.allSettled()`, robust runtime validation, and robust DOM-based XSS mitigation.
- **📝 Seamless Content Management:** Decap CMS workspace at `/admin/` for content creators to draft, preview, and publish blogs, newsletter volumes, and carousel images.
- **✉️ Netlify Form Integrations:** Pure JS submission with honeypot spam protection, real-time client-side validation, and elegant success overlays.
- **🚀 Advanced SEO & Accessibility:** Proper HTML5 semantic tags, absolute Open Graph parameters, automatic micro-animations, standard sitemap configurations, and explicit image dimensions to prevent layout shifts (CLS).

---

## 🛠️ Tech Stack

- **Core Structure:** Semantic HTML5 Markup
- **Styling:** Custom CSS3 with dynamic transitions and variables
- **Logic:** Vanilla JS (ES6+)
- **Content Management:** Decap CMS with Git Gateway
- **Hosting & Services:** Netlify, Netlify Identity, Netlify Forms

---

## 💻 Local Development

Modern web browsers restrict static XMLHttpRequests (CORS) over local file protocols. To launch the site locally with fully working CMS loaders, you need to run a simple server:

### Option 1: Python Server (Recommended)
Launch a fast Python HTTP server:
```powershell
python -m http.server 8080
```
Navigate to: **[http://localhost:8080](http://localhost:8080)**

### Option 2: Node static server
```bash
npx serve . -p 8080
```
Navigate to: **[http://localhost:8080](http://localhost:8080)**

---

## ✍️ CMS Usage

Non-technical administrators can manage all publications and dynamic sliders easily:

1. Launch your local server and navigate to `/admin/` (or go to `https://crescentlitsociety.com/admin/`).
2. Log in using your authorized GitHub developer credentials.
3. Manage **Blogs**, **Meraki Magazine**, **Crescent Line Newsletter**, **Carousels**, and **Members** list.
4. Press **Publish**; Netlify will compile, compress, and deploy the new data immediately to the CDN.

---

## 🌐 Deployment

The codebase is structured to deploy smoothly to Netlify with the custom parameters defined in `netlify.toml`:
- Excludes development and maintenance scripts (stored securely in `/scripts/`).
- Enforces strict security configurations like `X-Frame-Options: DENY`, `X-Content-Type-Options: nosniff`, and custom `Permissions-Policy` headers.
- Implements immutable long-term caching for static assets, scripts, and CSS (`max-age=31536000`), with immediate revalidation for HTML structures.

---

## 🤝 Contributing

We take pride in keeping our repository surgically clean, robustly commented, and well-structured.
- Ensure all Javascript includes JSDoc block comments.
- Do not introduce inline scripts or styles; keep layouts semantic.
- Run maintenance scripts within `/scripts/` to keep page sections synchronized.
