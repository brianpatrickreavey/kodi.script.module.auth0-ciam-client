# Kodi Script Module for Auth0 CIAM Client - Specification

## Overview
This specification outlines the plan to convert the `auth0_ciam_client` Python library into a standalone Kodi script module (`script.module.auth0-ciam-client`). The goal is to enable official Kodi repository distribution, allowing other Kodi addons (e.g., Angel Studios) to depend on it instead of bundling the code. The library remains unmodified and Kodi-agnostic, distributed separately via PyPI.

Key principles:
- No modifications to the original `auth0_ciam_client` codebase.
- Separation into two repos: `auth0-ciam-client` (PyPI library) and `script.module.auth0-ciam-client` (Kodi addon).
- Achieve 90%+ unit test coverage, targeting 100% by v1.0.0.
- Follow Kodi addon conventions, semver, and makeachangelog format.

## Requirements
- **Dependencies**: All must be available as Kodi script addons (e.g., `script.module.requests`, `script.module.beautifulsoup4`).
- **Auth Flow**: Supports click-through simulation for JWT token retrieval. No direct Kodi UI integration; used by other addons.
- **Compatibility**: Python 3.9+ (matching Kodi Nexus+). Kodi-independent tests.
- **Security**: Token handling security remains the responsibility of the library and consuming addons. No sensitive data in logs/exceptions.
- **Size**: Bundle entire library (small footprint); exclude extraneous items like `__pycache__`.

## Repository Structure
- **auth0-ciam-client**: Original library repo (PyPI).
- **script.module.auth0-ciam-client**: New addon repo with:
  - `script.module.auth0-ciam-client/`: Addon directory containing:
    - `addon.xml`: Metadata and dependencies.
    - `resources/lib/auth0_ciam_client/`: Bundled `auth0_ciam_client` package.
  - `README.md`: Kodi-focused documentation.
  - `CHANGELOG.md`: Following makeachangelog spec.
  - `.gitignore`: Exclude `__pycache__`, `.git`, etc.
  - `LICENSE.txt`: Copied from library.
  - `pyproject.toml`: Dev dependencies and tools.

## Implementation Steps

### Phase 1: Setup and Bundling
1. Create `script.module.auth0-ciam-client` repo.
2. Add basic files: `addon.xml`, `README.md`, `CHANGELOG.md`, `.gitignore`, `LICENSE.txt`.
3. Bundle `auth0_ciam_client`:
   - Local dev: Symlink from library repo to `resources/lib/`.
   - Production: GitHub CI checks out/pip-installs library for clean bundling.
4. Update `addon.xml` with metadata:
   - ID: `script.module.auth0-ciam-client`
   - Version: Start at 0.1.0 (sync with library).
   - Dependencies: `script.module.requests`, `script.module.beautifulsoup4`.
   - Author, description, etc.
   - Optional: Platform restrictions, changelog link.

### Phase 2: Testing and Validation
1. Run existing unit tests (no modifications, so should pass).
2. Revert library logging to standard Python logging; defer Kodi wrapper (`kodi_logging.py`) addition until Phase 2.5 completion, as testing requires live Kodi environment.
3. Add Kodi-specific tests: Logging wrapper, import loading in Kodi environment.
4. Use `kodi-addon-checker` for validation.
5. Ensure 90% coverage; add tests for any addon additions.
6. Test bundling: Clean zip excludes `__pycache__` (via `.gitignore` and `make clean`).

### Phase 2.5: Kodi Testing Harness (Development-Only)
1. Create a minimal test harness addon (`script.auth0-ciam-client-test-harness`) in `dev/script.auth0-ciam-client-test-harness/` with `addon.xml` and `main.py` to import and exercise the module (e.g., basic auth flow, logging calls).
2. Symlink both `script.module.auth0-ciam-client` and `script.auth0-ciam-client-test-harness` into local Kodi addons directory for live testing.
3. Use harness to validate imports, functions, and logging in Kodi environment; check `kodi.log` for output.
4. Document in DEVELOPMENT.md: Symlinking steps, script usage, log verification.
5. Provide `symlink_addons.sh` script for automated symlinking (--create, --remove).
6. Do not include harness in releases (exclude from builds/zips).

### Phase 3: CI/CD and Releases
1. Set up GitHub Actions: Kodi checks, zip creation, releases on tags (e.g., `v0.1.0`).
2. Sync versions with library initially; allow addon-specific patches later.
3. Changelog: Initial entry for bundling; sync manually or via CI from library.

### Phase 4: Documentation and Submission
1. README: Kodi installation (via repo), developer usage examples (e.g., imports), dependencies.
2. Follow script.module.requests patterns: Minimal, focused on Kodi.
3. Submit to Kodi repo: Include changelog, license.
4. No i18n initially (English-only, like requests); add placeholders if needed later.

### Phase 5: Migration and Future
1. Angel Studios: Switch dependency post-1.0.0; no concerns pre-1.0.0.
2. Future extensions: Optional `extensions/` for custom auth flows (no changes to library).
3. Monitoring: GitHub issues; no built-in Kodi analytics.
4. Security: Sanitize logs; advise on secure config.

## Tradeoffs and Concerns
- **Bundling vs. Selective**: Full bundle (small size); trade off simplicity for minimalism.
- **Logging**: Revert library for standards; addon wraps for Kodi.
- **Versioning**: Sync with library; addon may diverge for Kodi fixes.
- **No UI/UX**: Pure module; consumers handle interfaces.
- **Dependencies**: Must be Kodi addons; ensures portability.
- **Testing**: Library tests suffice; add Kodi integration only.
- **Size/Security**: Clean zips; no new risks from bundling.

## Timeline and Milestones
- **Phase 1: Completed** (setup, bundling) - Repo created, files added, symlinked library.
- **Refactor: Completed** (uv/pyproject.toml migration) - Both repos migrated to uv, pyproject.toml added, dependencies synced.
- **Phase 2: Completed** (testing) - Unit tests pass (82% coverage, close to 90%), kodi-addon-checker validates structure (dev artifacts noted), logging already Kodi-compatible.
- **Phase 2.5: Completed** (Kodi testing harness) - Harness created, symlinked, tested imports/logging in Kodi, documented in DEVELOPMENT.md, symlink script provided.
- Phase 3: 1 week (CI/CD).
- Phase 4: 1 week (docs, submission).
- Phase 5: Ongoing (migration, updates).

## Open Items
- Research Kodi submission process for exact requirements.
- Confirm addon.xml details with Kodi team if needed.
- Test in actual Kodi environment for import/loading.

## References
- [Kodi Add-on Structure](https://kodi.wiki/view/Add-on_structure)
- [Kodi Script Sources](https://kodi.wiki/view/Script_sources)
- [Submitting Add-ons to Kodi](https://kodi.wiki/view/Submitting_Add-ons)
- [Kodi Add-on Development](https://kodi.wiki/view/Add-on_development)

This spec is derived from TODO.md and the interview. Iterate as needed.</content>
<parameter name="filePath">/home/bpreavey/Code/kodi.script.module.auth0-ciam-client/SPEC.md