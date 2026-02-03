import sys
from unittest.mock import Mock

sys.path.insert(0, "script.module.auth0-ciam-client")
sys.modules["xbmc"] = Mock()
