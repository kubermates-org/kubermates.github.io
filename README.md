# Kubermates Site

Welcome to the **Kubermates Site** repository! This site is built with [Hugo](https://gohugo.io/) and serves as the official documentation, blog, and resource hub for the Kubermates community.

## 🚀 Features

- **Blog:** Latest articles and tutorials on Kubernetes, cloud-native technologies, and DevOps best practices.
- **Documentation:** Guides, how-tos, and reference docs for Kubermates tools and projects.
- **Events:** Information about upcoming and past community events.
- **Contributions:** Guidelines and resources for contributing to the site and Kubermates projects.

## 🛠️ Tech Stack

- [Hugo](https://gohugo.io/) static site generator
- [Docsy](https://www.docsy.dev/) theme (customized)
- SCSS for styling
- [Go](https://golang.org/) modules for theme and dependency management
- [PostCSS](https://postcss.org/) for CSS processing

## 📦 Project Structure

- `content/` — Markdown content for blog, docs, events, etc.
- `layouts/` — Custom templates and partials
- `static/` — Static assets (images, JS, etc.)
- `assets/` — SCSS and other asset sources
- `archetypes/` — Content archetypes
- `config/` — Hugo configuration files
- `public/` — Generated site output (do not edit directly)
- `scripts/` — Automation scripts (Python)
- `themes/` — Hugo themes (Docsy and customizations)

## 🏗️ Local Development

### Prerequisites

- [Go](https://golang.org/) (for Hugo modules)
- [Node.js](https://nodejs.org/) & [npm](https://www.npmjs.com/) (for SCSS/PostCSS)
- [Hugo Extended](https://gohugo.io/getting-started/installing/)

### Quick Start

```bash
# Install dependencies
go mod tidy
npm install

# Run the site locally
hugo server
```

The site will be available at [http://localhost:1313](http://localhost:1313).

## 📝 Contributing

We welcome contributions! Please see the `content/contribute/` section and our [CONTRIBUTING guidelines](content/contribute/) for details on how to get involved.

## 📄 License

This repository is licensed under the [Apache 2.0 License](LICENSE) unless otherwise noted.

---

For questions or support, open an issue or join the Kubermates community!
