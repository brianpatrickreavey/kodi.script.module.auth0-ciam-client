# script.module.auth0-ciam-client

This Kodi addon provides the `auth0_ciam_client` library as a script module for use by other Kodi addons.

## Installation

Install via Kodi Add-on Browser > Install from Repository > Kodi Add-on Repository > Program Add-ons > Auth0 CIAM Client.

## Usage

Import the module in your Kodi addon:

```python
from resources.lib.auth0_ciam_client import Core
```

Refer to the [auth0_ciam_client documentation](https://github.com/brianpatrickreavey/auth0-ciam-client) for API details.

## Dependencies

- `script.module.requests`
- `script.module.beautifulsoup4`

## License

GPL-3.0-only
