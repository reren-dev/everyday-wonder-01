"""Everyday Wonder: one sentence about a small everyday moment.

Writes the entry sentence to /output/entry.txt. The gate requires
UTF-8 text of 1 to 200 characters, not only whitespace.
"""

import os

SENTENCE = (
    "The escalator handrail drifts a fraction slower than the steps, "
    "so your hand arrives at the top a little behind you."
)

MAX_CHARS = 200


def check(sentence):
    """Enforce the gate locally before writing anything."""
    if not sentence or not sentence.strip():
        raise ValueError("sentence must not be empty or only whitespace")
    if len(sentence) > MAX_CHARS:
        raise ValueError(
            "sentence is %d characters, over the %d limit"
            % (len(sentence), MAX_CHARS)
        )
    if sentence.count(".") != 1 or not sentence.endswith("."):
        raise ValueError("entry must be exactly one sentence")


def main():
    check(SENTENCE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    os.replace(tmp_path, path)


if __name__ == "__main__":
    main()
