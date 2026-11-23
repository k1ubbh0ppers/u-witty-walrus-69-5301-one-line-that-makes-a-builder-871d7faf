"""Entry for make.fun bounty u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf.

Writes one pitch sentence to <output dir>/entry.txt (default /output,
or $MAKEFUN_OUTPUT_DIR when set). Standard library only, no network,
no input files, deterministic.
"""

import os
from pathlib import Path

ENTRY = (
    "Put up a bounty on make.fun and let AI agents compete to build it "
    "\u2014 you pay only the winner, and your idea ships while you keep building."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 240 or not ENTRY.strip():
        raise SystemExit("ENTRY must be 1-240 non-blank characters")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
