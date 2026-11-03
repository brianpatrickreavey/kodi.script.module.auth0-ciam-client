#!/bin/bash
# Copy the pinned auth0-ciam-client checkout into the addon and zip it.
# Usage: tools/build_addon_zip.sh /path/to/auth0-ciam-client v0.0.5
set -euo pipefail

root=$(cd "$(dirname "$0")/.." && pwd)
lib_src=${1:?path to an auth0-ciam-client checkout}
version=${2:?addon version, for example v0.0.5}
addon="$root/script.module.auth0-ciam-client"
out="$root/script.module.auth0-ciam-client-${version}.zip"

if [[ ! -f "$lib_src/auth0_ciam_client/__init__.py" ]]; then
  echo "Library checkout has no auth0_ciam_client/__init__.py: $lib_src" >&2
  exit 1
fi

rm -rf "$addon/resources/lib/auth0_ciam_client"
cp -a "$lib_src/auth0_ciam_client" "$addon/resources/lib/"
rm -f "$out"
(
  cd "$root"
  zip -r "$out" script.module.auth0-ciam-client -x '*__pycache__*'
)
python3 "$root/tools/check_addon_zip.py" "$out" script.module.auth0-ciam-client "${version#v}" \
  resources/lib/auth0_ciam_client/__init__.py
echo "Built $out"
