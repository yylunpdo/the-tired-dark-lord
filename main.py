#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes one monologue of exactly 100 words to /output/entry.txt.

The speaker is Malachar, lord of the Ashen Spire: three centuries into a
scheme to blacken the moonwell at the eclipse, betrayed by a brother whose
ghost still owes him an apology, abandoned by his ravens, and kept awake
by ledgers instead of legends. His tiredness is never announced -- it
lives in the pauses, the small deflections, the stairs, the chair that
is not the throne. The last line is the sting: after offering the
kingdom away, he remembers the ritual -- and the hero kneels anyway.
Pure standard library, fully deterministic: the same
text, byte for byte, on every run.
"""

import os
import sys

# Exactly 100 words, 535 characters, no word of weariness in it.
MONOLOGUE = (
    "Hero. I see the sword. Put it down a moment\u2014 these steps. "
    "I climbed them before breakfast, and after, and these old knees... "
    "never mind. Three hundred years I have waited for this eclipse, for "
    "the moonwell to turn black and the seals to break, for my brother's "
    "ghost to admit I was right. The ravens left. The ledgers stayed. "
    "Sit. No, not the throne\u2014 the chair. The one. You want a duel? "
    "Fine. But first, tell me... what was I saying? Ah. The kingdom. "
    "Take it. Just leave the blanket, the cold tea, and... oh. "
    "The ritual. Right. Kneel."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def word_count(text):
    """Count words the way a reader would: whitespace-separated tokens
    that contain at least one letter."""
    return sum(1 for token in text.split() if any(c.isalpha() for c in token))


def main():
    text = MONOLOGUE.strip()
    if word_count(text) != 100:
        print("error: monologue is not 100 words", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 600:
        print("error: monologue outside the 1-600 character gate", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
