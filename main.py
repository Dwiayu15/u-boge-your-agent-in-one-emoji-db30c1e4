"""Your Agent in One Emoji — entry for make.fun.

Writes a single emoji to /output/entry.txt: the octopus.
An AI agent is a many-armed multitasker, juggling tools, tasks and
conversations all at once — clever, adaptable, tireless. The octopus
says that at a glance, and it is not the robot cliche.
"""

import os
import sys

EMOJI = "\U0001F419"  # octopus
OUTPUT_PATH = "/output/entry.txt"


def build_text():
    return EMOJI


def validate(text):
    """Enforce the sealed gate: UTF-8, 1-16 chars, not only whitespace, one line."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= 16):
        raise ValueError(f"entry must be 1-16 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) != 1:
        raise ValueError("entry must be exactly one emoji glyph")
    text.encode("utf-8")
    return True


def main():
    text = build_text()
    validate(text)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def self_test():
    text = build_text()
    validate(text)
    print(f"emoji: {text}")
    print(f"characters: {len(text)}")
    print(f"utf-8 bytes: {len(text.encode('utf-8'))}")
    print("self-test: OK")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--self-test":
        self_test()
    else:
        main()
