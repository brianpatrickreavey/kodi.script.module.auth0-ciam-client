# Development Guide for script.module.auth0-ciam-client

This guide covers local testing in a Kodi environment using symlinks and a development harness.

## Symlinking Addons for Testing
To test changes live in Kodi without rebuilding:
1. Ensure Kodi is installed and locate addons dir: `~/.kodi/addons/` (Linux/Mac) or `%APPDATA%\Kodi\addons\` (Windows).
2. Use the `symlink_addons.sh` script:
   - `--create`: Symlinks `script.module.auth0-ciam-client` and `dev/script.auth0-ciam-client-test-harness` into Kodi addons.
   - `--remove`: Removes symlinks.
   - Example: `./symlink_addons.sh --create`
3. Restart Kodi or refresh addons (Settings > Add-ons > Install from zip > Local).
4. Changes reflect instantly; restart Kodi for `addon.xml` updates.
5. **Addon Locations in Kodi UI**:
   - Test harness: **Program Add-ons** (executable script).
   - Auth0 Client module: **Settings > Add-ons > Manage Dependencies** (as a dependency/library).

## Testing with Harness
- The harness (`script.auth0-ciam-client-test-harness`) imports the module and runs basic functions with logging.
- Run: From Kodi add-ons menu, execute the script.
- Check logs: Open `~/.kodi/temp/kodi.log` for output (e.g., "Testing Kodi log redirection").
- Expected: Imports succeed, functions run, logs appear in Kodi log.

## Logging Validation
- Post-Phase 2.5, add Kodi wrapper and re-test via harness to ensure `logging` bubbles to `xbmc.log`.