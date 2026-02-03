"""
Kodi logging wrapper for auth0_ciam_client.

This module provides a logging handler that redirects Python logging to Kodi's xbmc.log
with appropriate log levels.
"""

import logging
import xbmc  # type: ignore


class KodiLogHandler(logging.Handler):
    """
    Logging handler that redirects messages to Kodi's xbmc.log.
    """

    def emit(self, record):
        msg = self.format(record)
        if record.levelno >= logging.CRITICAL:
            xbmc.log(msg, xbmc.LOGFATAL)
        elif record.levelno >= logging.ERROR:
            xbmc.log(msg, xbmc.LOGERROR)
        elif record.levelno >= logging.WARNING:
            xbmc.log(msg, xbmc.LOGWARNING)
        elif record.levelno >= logging.INFO:
            xbmc.log(msg, xbmc.LOGINFO)
        else:
            xbmc.log(msg, xbmc.LOGDEBUG)


def setup(root_logger_name="auth0_ciam_client"):
    """
    Set up Kodi logging for the specified logger and its children.
    Call this after importing the auth0_ciam_client module.
    """
    logger = logging.getLogger(root_logger_name)
    handler = KodiLogHandler()
    handler.setFormatter(logging.Formatter("%(name)s: %(message)s"))
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)  # Allow all levels to be handled
    logger.propagate = False  # Prevent propagation to avoid double logging
