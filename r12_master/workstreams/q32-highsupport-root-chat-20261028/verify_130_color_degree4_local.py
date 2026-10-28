#!/usr/bin/env python3
"""Arithmetic verifier for the 130-edge degree-four neighborhood ledger.

It checks only the integer case split after the KP lower bound e(D[N]) >= 119.
It does not re-prove the graph-theoretic/KP inputs.
"""
valid = []
for a in range(7):  # edges induced by the 4-set S
    for b in range(8):  # edges from S to N
        eN = 130 - 4 - a - b
        if eN >= 119 and a + b <= 7 and 2*a + b >= 12:
            valid.append((a, b, eN, 2*a+b))

expected = [(5, 2, 119, 12), (6, 0, 120, 12), (6, 1, 119, 13)]
assert valid == expected, (valid, expected)
print("130_COLOR_DEG4_LEDGER_OK")
print("valid (e(S), e(S,N), e(N), sum degrees on S excluding v):")
for row in valid:
    print(row)
print("Scope: arithmetic case split only; KP and graph hypotheses are proof dependencies.")
