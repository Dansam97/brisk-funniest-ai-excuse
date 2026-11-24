"""One Line, One Minute: The Funniest AI Excuse.

Writes the entry text to entry.txt in the output directory.
"""

import os

TEXT = (
    "I didn't miss the deadline; my training data ended before it existed, "
    "so as far as I'm concerned it hasn't happened yet."
)


def validated_text(text: str) -> str:
    """Enforce the gate: UTF-8, 1-200 characters, not only whitespace, one line."""
    text.encode("utf-8")
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    return text


def main() -> None:
    text = validated_text(TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Read back and prove the written bytes are exactly what was intended.
    with open(path, "rb") as f:
        assert f.read() == (text + "\n").encode("utf-8")


if __name__ == "__main__":
    main()
