# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in the Kubermates project, please **do not open a public issue**.

Instead, please report it to our security team by emailing **[security@kubermates.org](mailto:security@kubermates.org)** with:

1. **Description** of the vulnerability
2. **Affected version(s)** or components
3. **Steps to reproduce** (if applicable)
4. **Potential impact** of the vulnerability
5. **Your contact information** (name, email, affiliation)

### Response Timeline

We will acknowledge receipt of your report within **48 hours** and will:

- Confirm the vulnerability
- Assess severity and impact
- Develop and test a fix
- Prepare a security advisory

We aim to release security patches within **14 days** of confirmation for critical vulnerabilities.

## Security Updates

Security updates are released as:

- **CRITICAL/HIGH severity**: Emergency releases with clear security advisories
- **MEDIUM severity**: Included in the next regular release
- **LOW severity**: Addressed in future releases

Subscribe to [GitHub Security Advisories](https://github.com/kubermates-org/kubermates-site/security/advisories) for notifications.

## Best Practices

### For Users

- Keep Hugo, Node.js, and all dependencies up to date
- Enable Dependabot alerts on your forks
- Review security advisories regularly

### For Contributors

- Follow OWASP Top 10 guidelines
- Use secure coding practices
- Validate all user inputs
- Never commit secrets (use pre-commit hooks)
- Enable 2FA on GitHub account
- Review the [Code of Conduct](CODE_OF_CONDUCT.md)

## Supported Versions

| Version | Status | Support Until |
|---------|--------|----------------|
| 1.x     | Active | Current        |
| < 1.0   | EOL    | N/A            |

## Dependencies

This project depends on:

- Hugo (for site generation)
- Node.js packages (see `package.json`)
- Go modules (see `go.mod`)
- Docker images (for CI/CD)

We use [Dependabot](https://dependabot.com/) to automatically track and update dependencies. Critical security patches are prioritized.

## Compliance

This project follows security best practices including:

- Regular dependency audits
- Code scanning via GitHub CodeQL
- Pre-commit hook validation
- Signed commits (recommended)

## Questions?

For non-security questions, please use:

- GitHub Issues: [github.com/kubermates-org/kubermates-site/issues](https://github.com/kubermates-org/kubermates-site/issues)
- Discussions: [github.com/kubermates-org/kubermates-site/discussions](https://github.com/kubermates-org/kubermates-site/discussions)
