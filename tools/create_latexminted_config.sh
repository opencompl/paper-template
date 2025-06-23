#!/usr/bin/env bash

FILE="${HOME}/.latexminted_config"

if [[ -f "$FILE" ]]; then
    echo "Error: ${FILE} already exists"
fi

echo '{
  "security": {
      "enable_cwd_config": true
  }
}' > "$FILE"
