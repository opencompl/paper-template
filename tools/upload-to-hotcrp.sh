#!/usr/bin/env bash
set -euo pipefail

default_config_file=".github/hotcrp.env"
config_file="${1:-$default_config_file}"

usage() {
  cat <<'EOF'
Usage:
  tools/upload-to-hotcrp.sh [CONFIG_FILE]
  tools/upload-to-hotcrp.sh --help

Uploads a paper PDF to the configured HotCRP submission.

CONFIG_FILE is sourced as a shell env file. If omitted, .github/hotcrp.env is
sourced when it exists; otherwise existing environment variables are used.

Required values:
  HOTCRP_SITE_URL          HotCRP site base URL, for example https://asplos26.hotcrp.com
  HOTCRP_PID               Numeric HotCRP paper ID
  HOTCRP_TOKEN             HotCRP API token

GitHub Actions control:
  HOTCRP_ACTION_UPLOAD_ENABLED
                           In GitHub Actions, must be exactly true to upload.
                           Defaults to false.

Optional overrides:
  HOTCRP_PDF               PDF to upload. Defaults to submission.pdf.

Local example:
  HOTCRP_TOKEN=... tools/upload-to-hotcrp.sh .github/hotcrp.env
  HOTCRP_SITE_URL=... HOTCRP_PID=123 HOTCRP_TOKEN=... tools/upload-to-hotcrp.sh
EOF
}

die() {
  printf 'error: %s\n' "$*" >&2
  exit 1
}

require_var() {
  local name="$1"
  local value="${!name:-}"

  if [ -z "$value" ] || [ "$value" = "TODO" ] || [ "$value" = "TODO_REPLACE_ME" ]; then
    die "$name is not set. Update $config_file or provide it in the environment."
  fi
}

require_command() {
  local name="$1"

  command -v "$name" >/dev/null 2>&1 || die "required command is not available: $name"
}

case "${1:-}" in
  -h|--help)
    usage
    exit 0
    ;;
esac

if [ "$#" -gt 0 ] || [ -f "$config_file" ]; then
  [ -f "$config_file" ] || die "missing HotCRP config file: $config_file"

  set -a
  # shellcheck source=/dev/null
  . "$config_file"
  set +a
fi

HOTCRP_ACTION_UPLOAD_ENABLED="${HOTCRP_ACTION_UPLOAD_ENABLED:-false}"
HOTCRP_PDF="${HOTCRP_PDF:-submission.pdf}"

if [ "${GITHUB_ACTIONS:-false}" = "true" ] && [ "$HOTCRP_ACTION_UPLOAD_ENABLED" != "true" ]; then
  printf 'HotCRP upload is disabled by %s; set HOTCRP_ACTION_UPLOAD_ENABLED=true to enable it.\n' "$config_file"
  exit 0
fi

require_var HOTCRP_SITE_URL
require_var HOTCRP_PID
require_var HOTCRP_TOKEN

require_command curl
require_command python3
require_command zip

HOTCRP_SITE_URL="${HOTCRP_SITE_URL%/}"

case "$HOTCRP_PID" in
  ''|*[!0-9]*)
    die "HOTCRP_PID must be a numeric paper ID."
    ;;
esac

[ -f "$HOTCRP_PDF" ] || die "missing PDF to upload: $HOTCRP_PDF"

workdir="$(mktemp -d)"
trap 'rm -rf "$workdir"' EXIT

cp "$HOTCRP_PDF" "$workdir/submission.pdf"

cat > "$workdir/data.json" <<EOF
{
  "object": "paper",
  "pid": $HOTCRP_PID,
  "submission": { "content_file": "submission.pdf" }
}
EOF

(
  cd "$workdir"
  zip -q upload.zip data.json submission.pdf
)

curl -fsS \
  -H "Authorization: bearer $HOTCRP_TOKEN" \
  -H "Content-Type: application/zip" \
  --data-binary @"$workdir/upload.zip" \
  "$HOTCRP_SITE_URL/api/paper" \
  > hotcrp-response.json

python3 - <<'PY'
import json
import sys

with open("hotcrp-response.json") as f:
    response = json.load(f)

print(json.dumps(response, indent=2))

if not response.get("ok") or not response.get("valid", False):
    sys.exit("HotCRP upload failed")
PY
