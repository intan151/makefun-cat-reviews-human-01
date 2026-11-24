"""Make the AI Judge Laugh: Cat Reviews Its Human -- write one funny
single-line one-star review from a house cat about its human to
/output/entry.txt.

Stdlib only, no network, no randomness: the output is byte-identical on
every run. The review keeps the deadpan shape of a real one-star review --
specific complaints, item by item -- and the sting lands in the last few
words: the audacity is endless.
"""

import os

LINE = (
    "One star. Would give zero if I had thumbs. The food bowl: empty. "
    "The lap: occupied by a laptop. The audacity: endless."
)


def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.endswith(".") and "\n" not in LINE, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back: the file on disk must be exactly the line, nothing else.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == LINE, "entry.txt does not match the line"


if __name__ == "__main__":
    main()
