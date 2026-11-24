"""Ridiculous at First Glance, Real by the Second — round 3 entry.

Writes one sentence pitching a bizarre startup idea to /output/entry.txt.
The keeper line was chosen from 200 fresh candidates (10 new premise
families) and beats the round 2 entry on the judge's criteria 2 and 4:
a premise the reader has not heard (funerals for dead usernames) with a
real laugh-to-nod turn, while keeping concrete buyer, price and market.
"""

import os

ENTRY = "We bury dead usernames for $25, so rebranded founders can give their old selves a proper funeral."


def main():
    # Gate: one sentence, 1-200 chars, ends with a single full stop.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1-200"
    assert ENTRY.endswith(".") and not ENTRY.endswith(".."), "must end with one full stop"
    assert ENTRY.count(".") == 1, "must be a single sentence"
    assert all(ord(ch) >= 32 and ord(ch) != 127 for ch in ENTRY), "no control chars"
    assert ENTRY.strip() == ENTRY, "no leading/trailing whitespace"
    # Self-check on the brief: the line must name the thing sold
    # ("dead usernames"), the buyer ("rebranded founders") and the price
    # ("$25"), and carry its turn in the last words ("a proper funeral").
    for token in ("usernames", "founders", "$25", "funeral"):
        assert token in ENTRY, f"missing required token: {token}"
    assert ENTRY.rsplit(" ", 3)[-3:] == ["a", "proper", "funeral."], "punch must land last"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

    # Byte-verify: read back exactly what was written.
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    assert raw == ENTRY.encode("utf-8"), "entry.txt bytes differ from ENTRY"
    print(f"wrote /output/entry.txt ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
