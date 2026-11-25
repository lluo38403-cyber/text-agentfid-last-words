"""Famous Last Words at 1 Percent — make.fun entry.

Writes one line to /output/entry.txt: the funniest last words a
phone would say when its battery hits 1 percent. The phone dies
doing what it loved — ignoring the low-battery warning for six
hours straight — and says so with its final breath.
"""

import os

ENTRY = (
    "If anyone asks, I died doing what I loved: ignoring my own "
    "low-battery warning for six hours straight."
)

MAX_CHARS = 199


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
