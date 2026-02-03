import logging
from unittest.mock import Mock, patch
import xbmc  # type: ignore

from resources.lib.kodi_logging import KodiLogHandler, setup


class TestKodiLogHandler:
    @patch("xbmc.log")
    def test_emit_debug(self, mock_xbmc_log):
        handler = KodiLogHandler()
        handler.setFormatter(logging.Formatter("%(name)s: %(message)s"))
        record = Mock()
        record.levelno = logging.DEBUG
        record.getMessage = Mock(return_value="debug message")
        record.exc_text = None
        record.exc_info = None
        record.stack_info = None
        record.name = "test"
        handler.emit(record)
        mock_xbmc_log.assert_called_once_with("test: debug message", xbmc.LOGDEBUG)

    @patch("xbmc.log")
    def test_emit_info(self, mock_xbmc_log):
        handler = KodiLogHandler()
        handler.setFormatter(logging.Formatter("%(name)s: %(message)s"))
        record = Mock()
        record.levelno = logging.INFO
        record.getMessage = Mock(return_value="info message")
        record.exc_text = None
        record.exc_info = None
        record.stack_info = None
        record.name = "test"
        handler.emit(record)
        mock_xbmc_log.assert_called_once_with("test: info message", xbmc.LOGINFO)

    @patch("xbmc.log")
    def test_emit_warning(self, mock_xbmc_log):
        handler = KodiLogHandler()
        handler.setFormatter(logging.Formatter("%(name)s: %(message)s"))
        record = Mock()
        record.levelno = logging.WARNING
        record.getMessage = Mock(return_value="warning message")
        record.exc_text = None
        record.exc_info = None
        record.stack_info = None
        record.name = "test"
        handler.emit(record)
        mock_xbmc_log.assert_called_once_with("test: warning message", xbmc.LOGWARNING)

    @patch("xbmc.log")
    def test_emit_error(self, mock_xbmc_log):
        handler = KodiLogHandler()
        handler.setFormatter(logging.Formatter("%(name)s: %(message)s"))
        record = Mock()
        record.levelno = logging.ERROR
        record.getMessage = Mock(return_value="error message")
        record.exc_text = None
        record.exc_info = None
        record.stack_info = None
        record.name = "test"
        handler.emit(record)
        mock_xbmc_log.assert_called_once_with("test: error message", xbmc.LOGERROR)

    @patch("xbmc.log")
    def test_emit_critical(self, mock_xbmc_log):
        handler = KodiLogHandler()
        record = Mock()
        record.levelno = logging.CRITICAL
        record.getMessage = Mock(return_value="critical message")
        record.exc_text = None
        record.exc_info = None
        record.stack_info = None
        record.name = "test"
        handler.emit(record)
        mock_xbmc_log.assert_called_once_with("test: critical message", 4)  # xbmc.LOGFATAL


class TestSetup:
    @patch("logging.getLogger")
    def test_setup_default_logger(self, mock_get_logger):
        mock_logger = Mock()
        mock_get_logger.return_value = mock_logger
        setup()
        mock_get_logger.assert_called_once_with("auth0_ciam_client")
        mock_logger.addHandler.assert_called_once()
        handler = mock_logger.addHandler.call_args[0][0]
        assert isinstance(handler, KodiLogHandler)
        mock_logger.setLevel.assert_called_with(logging.DEBUG)
        assert not mock_logger.propagate

    @patch("logging.getLogger")
    def test_setup_custom_logger(self, mock_get_logger):
        mock_logger = Mock()
        mock_get_logger.return_value = mock_logger
        setup("custom_logger")
        mock_get_logger.assert_called_once_with("custom_logger")
