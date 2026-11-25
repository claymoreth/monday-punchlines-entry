"""Monday Morning Punchlines entry.

Writes exactly one punchline to entry.txt in the output directory.
"""

import os

TEXT = "My weekend was a free trial. Monday is the subscription renewal email."


def output_path():
    """Resolve entry.txt path from MAKEFUN_OUTPUT_DIR, default /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    path = output_path()
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
