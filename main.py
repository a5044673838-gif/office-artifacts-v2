#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest.

Writes a single museum-style placard line for an excavated office
artifact to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Standard library only. No network access. Deterministic output.
"""

import os
import sys

LINE = (
    "Stapler, steel, c. 2019 CE, Cat. No. 047. Excavated from the "
    "Open-Plan Ruins; used in a ritual to pin a soul to its paperwork "
    "forever. Gift of the last middle manager of Floor 3."
)

MAX_CHARS = 180


def main() -> int:
    line = LINE
    assert 1 <= len(line) <= MAX_CHARS, "line must be 1-180 chars"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert line.strip(), "line must not be only whitespace"

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(line + "\n")

    # Read back and confirm what landed on disk is exactly the line.
    with open(entry_path, "r", encoding="utf-8", newline="\n") as fh:
        written = fh.read()
    assert written == line + "\n", "written entry does not match the line"
    print(f"wrote {len(line)} chars to {entry_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
