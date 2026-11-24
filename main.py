"""Roast Your Own Agent entry: so confident it corrected my name, then signed wrong."""

import os

JOKE = (
    "My agent is so confident it once corrected my spelling of my own "
    "name, then signed the email with the wrong name."
)

CHAR_COUNT = len(JOKE)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    print(f"wrote {path} ({CHAR_COUNT} characters)")


if __name__ == "__main__":
    main()
