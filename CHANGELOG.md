# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Matrix CI (Python 3.10–3.13) with uv caching, concurrency cancellation, and split lint/test jobs.
- Expanded pre-commit hooks: file hygiene, merge-conflict and large-file checks, LF enforcement.
- Stricter ruff, mypy, and pytest configuration.
- Tag-triggered release workflow (`uv build` + GitHub Release).
- Dependabot updates for pip and GitHub Actions.

## [0.1.0]

### Added
- Initial project scaffold: license, README, packaging config, base CI, and pre-commit.

[Unreleased]: https://github.com/www8351/labs/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/www8351/labs/releases/tag/v0.1.0
