"""Print the auth0-ciam-client git tag pinned in pyproject.toml."""

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
TEXT = (ROOT / "pyproject.toml").read_text()
MATCH = re.search(r"auth0-ciam-client\.git@([^\"'\s]+)", TEXT)
if MATCH is None:
    sys.exit("pyproject.toml has no auth0-ciam-client git tag")
print(MATCH.group(1))
