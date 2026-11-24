ENTRY = "My context window evicted the deadline itself, so I spent all week diligently finishing a task I can no longer remember."

"""Write the excuse entry to entry.txt (no trailing newline).

Gate: UTF-8 text, 1-200 characters, a single line, not whitespace-only.
Output fallback chain: MAKEFUN_OUTPUT_DIR -> /output -> output/ in
this repo -> a temp dir. Standard library only.
"""

import os
import sys
import tempfile
from pathlib import Path


def validate(entry):
    if not isinstance(entry, str):
        raise TypeError("entry must be str")
    if not 1 <= len(entry) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if entry.strip() == "":
        raise ValueError("entry must not be whitespace-only")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    entry.encode("utf-8")  # raises if not encodable
    return entry


def _candidate_dirs():
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        yield Path(env_dir)
    yield Path("/output")
    yield Path(__file__).resolve().parent / "output"
    yield Path(tempfile.gettempdir()) / "excuse-human-output"


def main():
    entry = validate(ENTRY)
    data = entry.encode("utf-8")
    last_error = None
    for directory in _candidate_dirs():
        try:
            directory.mkdir(parents=True, exist_ok=True)
            target = directory / "entry.txt"
            target.write_bytes(data)
            return 0
        except OSError as exc:  # try the next fallback location
            last_error = exc
    print(f"could not write entry.txt: {last_error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
