# Security Policy

## Data Collection Scope

This skill collects **publicly available information only**. Specifically:

- Public news articles and media reports
- Public social media posts and discussions
- Public search engine results
- Publicly displayed aggregate statistics (e.g., topic view counts, video play counts)

## What This Skill Does NOT Do

- Does **not** access private accounts, direct messages, or private profiles
- Does **not** collect, store, or transmit personal identifiable information (PII)
- Does **not** use any APIs that require authentication or credentials
- Does **not** install or execute any external software, scripts, or binaries
- Does **not** make any network requests except through the host platform's built-in web tools
- Does **not** access system files, SSH keys, keychains, or browser profiles
- Does **not** require or store any API keys, tokens, or secrets
- Does **not** modify any system settings or configurations
- Does **not** communicate with any external servers or endpoints

## Data Handling

- All collected data is processed in-memory during the current session
- Generated reports are written to the user's local workspace directory only
- No data is transmitted to any third-party service
- No data persists beyond the user's local file system
- Users are responsible for managing and securing their generated reports

## Dependencies

- **Zero external dependencies** — This skill requires no third-party packages, libraries, or external resources
- **No npm/pip packages** — All functionality relies on the host AI assistant platform's built-in tools
- **No external CSS/JS/fonts** — The HTML report template uses only inline CSS and system fonts

## Runtime Behavior

This skill operates as a **read-only, on-demand tool**:

- Runs only when explicitly triggered by the user
- Does not run automatically or persistently
- Does not modify other skills or system files
- Does not request elevated privileges or permissions

## Vulnerability Reporting

If you discover a security vulnerability in this skill, please:

1. Do not open a public issue
2. Contact the maintainer through GitHub's private vulnerability reporting feature
3. Include a description of the vulnerability and steps to reproduce

## Compliance

Users of this skill are responsible for:

- Complying with applicable laws and regulations in their jurisdiction
- Ensuring their use case does not violate platform terms of service
- Not using generated reports for harassment, defamation, or illegal purposes
