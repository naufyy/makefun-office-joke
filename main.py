"""One-line entry for make.fun (office joke).

Writes the winning entry to /output/entry.txt.
Deterministic: same bytes on every run.
"""

from pathlib import Path

ENTRY = "The office plant died, so HR sent a condolence email and a replacement plant on a shorter probation."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
