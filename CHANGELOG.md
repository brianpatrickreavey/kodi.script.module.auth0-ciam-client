# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.5] - 2026-11-01

### Changed
- Pin `auth0-ciam-client` at git tag `v0.2.2`.
- Put that library inside the release zip. The zip build fails if `auth0_ciam_client/__init__.py` is missing.

## [0.0.1] - 2026-02-02

### Added
- Initial release bundling `auth0_ciam_client` library for Kodi.
- Support for Auth0 CIAM authentication flows.
- Dependencies on `script.module.requests` and `script.module.beautifulsoup4`.