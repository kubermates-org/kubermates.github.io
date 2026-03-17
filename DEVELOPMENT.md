# Development Guide

Welcome to the Kubermates Site development guide! This document covers setup, workflow, and best practices for contributors.

## Prerequisites

- **Go** 1.21+ (for Hugo modules)
- **Node.js** 18+ & **npm** 9+ (for build tools)
- **Hugo Extended** 0.121+
- **pre-commit** (for git hooks)

## Quick Start

```bash
# Clone the repository
git clone https://github.com/kubermates-org/kubermates-site.git
cd kubermates-site

# Install dependencies
go mod tidy
npm install
pre-commit install

# Start development server
hugo server -D
```

The site will be available at `http://localhost:1313`

## Project Structure

```
.
├── archetypes/          # Content templates
├── assets/              # SCSS, source assets
├── config/              # Hugo configuration
├── content/             # Markdown content
│   ├── blog/           # Blog articles
│   ├── docs/           # Documentation
│   ├── events/         # Event listings
│   └── contribute/     # Contribution guides
├── data/                # YAML data files
├── layouts/             # Custom HTML templates
├── static/              # Static files (images, CSS)
├── scripts/             # Automation scripts
├── themes/              # Hugo themes
├── postcss.config.js    # PostCSS configuration
├── hugo.toml            # Hugo configuration
└── package.json         # Node dependencies & scripts
```

## Development Workflow

### 1. Creating Content

Create new blog posts or documentation:

```bash
hugo new blog/my-post.md
hugo new docs/my-guide.md
```

Edit the frontmatter (metadata at the top of the markdown file) to set:
- `title`: Page title
- `description`: Short description
- `date`: Publication date
- `draft`: Set to `false` when ready to publish

### 2. Running Locally

Development server with draft posts enabled:

```bash
hugo server -D
```

Production build (excludes drafts):

```bash
hugo
```

### 3. Code Quality

Run all quality checks:

```bash
npm run lint          # CSS, Markdown, YAML
npm run fix           # Auto-fix issues
```

Run specific linters:

```bash
npm run lint:css      # CSS/SCSS linting
npm run lint:md       # Markdown linting
npm run lint:yaml     # YAML linting
npm run fix:css       # Fix CSS issues
npm run fix:md        # Fix Markdown issues
```

### 4. Pre-commit Hooks

Your git commits will automatically be checked for:
- Trailing whitespace
- Missing file endings
- Valid JSON formatting
- YAML syntax
- Markdown quality
- Spelling errors

Hooks run before each commit. If a check fails, fix the issues and try committing again.

To bypass (not recommended):

```bash
git commit --no-verify
```

### 5. Adding Dependencies

```bash
# Add npm package
npm install package-name --save-dev

# Update all dependencies
npm update

# Check for security vulnerabilities
npm audit
```

## Git Workflow

### Branch Naming

- Feature: `feat/feature-name`
- Bug fix: `fix/bug-name`
- Docs: `docs/description`
- Chore: `chore/task-name`

### Commit Messages

Use conventional commits format:

```
type(scope): description

[optional body]
```

Types: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `style`

Examples:

```bash
git commit -m "feat(content): add k8s security guide"
git commit -m "fix(styles): correct navbar padding on mobile"
git commit -m "docs: update development setup instructions"
```

### Pull Requests

1. Create a descriptive PR title (follows conventional commits)
2. Reference any related issues: `Closes #123`
3. Describe changes clearly in the PR body
4. Ensure all checks pass before requesting review
5. Respond to review feedback promptly

## Theme Customization

The site uses the **Docsy** theme with custom overrides:

- **Layouts**: `layouts/` - override Docsy templates
- **SCSS**: `assets/scss/` - custom styling
- **Static assets**: `static/` - images and custom CSS

### Adding Custom CSS

1. Create or edit SCSS files in `assets/scss/`
2. Import in the main stylesheet
3. Run `npm run lint:css` to check
4. Hugo will automatically process SCSS during build

## Testing & Validation

Before pushing:

```bash
# Full quality check
npm test

# Build production version
hugo

# Check for dead links (optional)
hugo server -D
# Then test links manually or with a link checker tool
```

## Troubleshooting

### Hugo modules not loading

```bash
go mod tidy
go mod get -u
```

### Styles not compiling

```bash
npm install
npm run fix:css
```

### Content not appearing

- Check `draft: false` in frontmatter
- Verify date is not in the future (or use `hugo server -D`)
- Clear cache: `rm -rf resources/`

### Port 1313 already in use

```bash
hugo server -D --port 1314
```

## Resources

- [Hugo Documentation](https://gohugo.io/documentation/)
- [Docsy Theme](https://www.docsy.dev/)
- [Contributing Guidelines](../CONTRIBUTING.md)
- [Code of Conduct](../CODE_OF_CONDUCT.md)

## Getting Help

- Open an issue on GitHub
- Join our Slack workspace
- Check existing documentation and issues first

---

Happy contributing! 🚀
