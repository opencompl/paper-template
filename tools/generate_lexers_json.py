import os
import hashlib
import json

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

    result = {"custom_lexers": custom_lexers}

    with open(OUTPUT_JSON, "w") as file:
        json.dump(result, file, indent=2)

    print(f"JSON file created at {OUTPUT_JSON}")


if __name__ == "__main__":
    generate_lexers_json()
