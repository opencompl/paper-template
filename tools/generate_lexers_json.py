#!/usr/bin/env python3

import os
import hashlib
import json
from pathlib import Path

LEXER_DIR = "tools/lexers"

OUTPUT_JSON = ".latexminted_config"


def calculate_sha256(file_path):
    """Calculate the SHA256 hash of a file."""

    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as file:
        sha256_hash.update(file.read())
    return sha256_hash.hexdigest()


def generate_lexers_json():
    custom_lexers = {}

    for filename in os.listdir(LEXER_DIR):
        if filename.endswith(".py"):
            file_path = os.path.join(LEXER_DIR, filename)
            file_hash = calculate_sha256(file_path)
            custom_lexers[filename] = file_hash

    return custom_lexers

def generate_json_file():
    # Load existing config, if it exists
    config_path = Path(OUTPUT_JSON)
    if config_path.exists():
        with open(config_path, 'r') as f:
            config = json.load(f)
    else:
        config = {}
    
    # Update only the lexers
    config["custom_lexers"] = generate_lexers_json()

    # Output the new config file
    with open(config_path, "w") as file:
        json.dump(config, file, indent=2)

    print(f"JSON file created at {OUTPUT_JSON}")

if __name__ == "__main__":
    generate_json_file()
