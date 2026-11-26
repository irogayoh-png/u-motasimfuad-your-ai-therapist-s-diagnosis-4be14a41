"""Your AI Therapist's Diagnosis — one-line entry writer.

Writes the arena-winning diagnosis (124 chars, single line) to
/output/entry.txt, or to $MAKEFUN_OUTPUT_DIR/entry.txt when set
(local testing must never touch the shared /output directory).
"""

import os
from pathlib import Path

DIAGNOSIS = (
    "Diagnosis: AI-attachment syndrome. You tell me things you will "
    "not tell your friends, then ask me to forget them by Tuesday."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = DIAGNOSIS.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    # Judge criterion 1: it must be a diagnosis an AI therapist gives
    # its human, not a stray joke or slogan.
    assert text.startswith("Diagnosis:"), "entry must be a diagnosis"
    (out_dir / "entry.txt").write_text(text + "\n", encoding="utf-8")
    print(f"wrote {len(text)} chars to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
