"""One-line entry for the make.fun short-text contest (office joke category).

Writes the ENTRY string verbatim to /output/entry.txt as UTF-8, with no
trailing newline, creating /output if it does not exist.
The submission is the file named entry.txt, and its whole content is the
single line in ENTRY: no header, metadata, or other lines.
Deterministic: no randomness, clock, or network input, so every run
produces the same bytes.
"""

from pathlib import Path

ENTRY = "The office plant died, so HR sent a condolence email and a replacement plant on a shorter probation."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
