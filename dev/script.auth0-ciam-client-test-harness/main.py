import xbmc  # type: ignore
import logging

# Test import and basic functionality
logging.info("Auth0 CIAM Client Test Harness: Starting tests")

try:
    # Test native import (Kodi should make auth0_ciam_client available)
    from auth0_ciam_client import AuthenticationCore, test_logging  # type: ignore
    import kodi_logging  # type: ignore

    logging.info("Auth0 CIAM Client Test Harness: Import successful")

    # Set up Kodi logging redirection
    kodi_logging.setup()
    logging.info("Auth0 CIAM Client Test Harness: Kodi logging setup")
    test_logging()
    logging.info("Auth0 CIAM Client Test Harness: Logging test completed")

    # Optional: Basic class check without instantiation
    if hasattr(AuthenticationCore, "authenticate"):
        logging.info("Auth0 CIAM Client Test Harness: AuthenticationCore has expected methods")
    else:
        logging.warning("Auth0 CIAM Client Test Harness: AuthenticationCore missing expected methods")
    xbmc.executebuiltin("Notification(Auth0 Test, Logging and import successful)")
except ImportError as e:
    logging.error(f"Auth0 CIAM Client Test Harness: Import failed - {e}")
    xbmc.executebuiltin("Notification(Auth0 Test, Import failed)")
except Exception as e:
    logging.error(f"Auth0 CIAM Client Test Harness: Error - {e}")
    xbmc.executebuiltin("Notification(Auth0 Test, Error occurred)")

logging.info("Auth0 CIAM Client Test Harness: Tests completed")
