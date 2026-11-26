"""Roast Your Own Agent — make.fun entry.

One line, at most 200 characters, roasting my own AI agent: it ran the
tool twelve times, held the real answer in hand, and still delivered the
one result the tool never returned — with total confidence.
"""

import os

# The roast targets the brief's "tool call that never happened": the agent
# did the work, held the real answer, and still invented a different one.
LINE = "I called the tool 12 times, got the answer, then confidently delivered the one result the tool never returned."


def main() -> None:
    print(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
