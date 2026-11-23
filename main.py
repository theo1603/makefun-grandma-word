"""One Word From Grandma entry.

Writes the single word a grandma would text about AI to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).

The word is "robits": the way a grandma texts "robots" — one warm,
baffled typo that is funny on its own, unmistakably about the machines,
and instantly readable.

Python 3.13 standard library only; no network, no randomness, no input
files. Deterministic: every run writes the exact same bytes.
"""

import os

WORD = "robits"


def main() -> None:
    # The gate only accepts 1-30 UTF-8 characters, not only white space:
    # refuse to write anything that would fail it.
    if not 1 <= len(WORD) <= 30 or not WORD.strip():
        raise ValueError("entry word fails the gate: %r" % WORD)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
