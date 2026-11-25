#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry.

Writes one deadpan sick-day excuse to /output/entry.txt.
The excuse: the fridge died, so the sender "fixed" the problem by eating
everything in it before it spoiled — and gave themself food poisoning
on purpose. One clause of setup, payoff at the very end.
"""
import os

EXCUSE = "Can't come in — my fridge died, so I ate everything in it before it spoiled and gave myself food poisoning on purpose."

OUTPUT_PATHS = ("/output/entry.txt", "output/entry.txt")


def main():
    text = EXCUSE.strip()
    if not (1 <= len(text) <= 200):
        raise SystemExit("excuse must be 1-200 characters, got %d" % len(text))
    for path in OUTPUT_PATHS:
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
            return
        except OSError:
            continue
    raise SystemExit("no writable output path")

if __name__ == "__main__":
    main()
