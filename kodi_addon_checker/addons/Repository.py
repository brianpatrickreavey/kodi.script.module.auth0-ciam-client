"""
    Copyright (C) 2018 Team Kodi
    This file is part of Kodi - kodi.tv

    SPDX-License-Identifier: GPL-3.0-only
    See LICENSES/README.md for more information.
"""

import atexit
import gzip
import logging
import time
import xml.etree.ElementTree as ET
from io import BytesIO

import requests

from .Addon import Addon
from ..versions import AddonVersion


logger = logging.getLogger("kodi_addon_checker")


class RateLimitedAdapter(requests.adapters.HTTPAdapter):
    def __init__(self, *args, retries=5, wait=None, **kwargs):
        self._last_send = None
        self._wait_time = wait
        max_retries = requests.adapters.Retry(
            total=retries,
            backoff_factor=wait or 10,
            status_forcelist={
                429,
            },
            allowed_methods=None,
        )
        kwargs.setdefault("max_retries", max_retries)
        super().__init__(*args, **kwargs)

    def send(self, *args, **kwargs):
        logger.debug("RateLimitedAdapter.send: Starting send request")
        if self._wait_time and self._last_send:
            delta = time.time() - self._last_send
            if delta < self._wait_time:
                sleep_time = self._wait_time - delta
                logger.debug(f"RateLimitedAdapter.send: Rate limiting, sleeping for {sleep_time:.2f} seconds")
                time.sleep(sleep_time)

        self._last_send = time.time()
        start_time = time.time()
        logger.debug("RateLimitedAdapter.send: About to call super().send()")
        response = super().send(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        status_code = getattr(response, "status_code", None)
        logger.debug(
            f"RateLimitedAdapter.send: super().send() completed in {duration:.2f} seconds, status code {status_code}"
        )
        if 300 <= status_code < 400:
            self._last_send = None
            logger.debug("RateLimitedAdapter.send: Redirect status, resetting _last_send")
        return response


class Repository:
    # Recover from unreliable mirrors
    _session = requests.Session()
    _adapter = RateLimitedAdapter(retries=5, pool_maxsize=3, pool_block=True)
    _session.mount("http://", _adapter)
    _session.mount("https://", _adapter)
    atexit.register(_session.close)

    def __init__(self, version, path):
        super().__init__()
        self.version = version
        self.path = path
        logger.debug(f"Repository.__init__: Initializing repository for path {path}")

        try:
            start_time = time.time()
            logger.debug(f"Repository.__init__: Attempting to fetch {path} with timeout (30, 30)")
            response = self._session.get(path, timeout=(30, 30))
            response.raise_for_status()
            end_time = time.time()
            duration = end_time - start_time
            logger.debug(
                f"Repository.__init__: Successfully fetched {path} -> {response.url} "
                f"in {duration:.2f} seconds, status {response.status_code}"
            )
            self.resolved_url = response.url
            print(f"Resolved addon repo URL: {response.url}")
        except Exception as e:
            logger.debug(f"Repository.__init__: Failed to fetch {path}, exception: {e}, setting addons to empty list")
            print(f"Failed to resolve addon repo URL: {path}")
            print(f"Error: {e}")
            self.addons = []
            return
        content = response.content

        if path.endswith(".gz"):
            with gzip.open(BytesIO(content), "rb") as xml_file:
                content = xml_file.read()

        self.addons = []
        tree = ET.fromstring(content)
        for addon in tree.findall("addon"):
            self.addons.append(Addon(addon))

    def __contains__(self, addonId):
        for addon in self.addons:
            if addon.id == addonId:
                return True
        return False

    def find(self, addonId):
        # multiple copies of the same addon might exist on the repository, however
        # kodi always uses the highest version available
        addon_instances = []
        for addon in self.addons:
            if addon.id == addonId:
                addon_instances.append(addon)

        if not addon_instances:
            return None

        # always return the highest version for the given addon id available in the repo
        addon_instances.sort(key=lambda addon: AddonVersion(addon.version), reverse=True)
        return addon_instances[0]

    def rdepends(self, addonId):
        rdepends = []
        for addon in self.addons:
            if addon.dependsOn(addonId):
                rdepends.append(addon)
        return rdepends
