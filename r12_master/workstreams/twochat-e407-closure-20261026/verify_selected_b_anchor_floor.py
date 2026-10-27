#!/usr/bin/env python3
"""Arithmetic replay for SELECTED_B_ANCHOR_FLOOR.md.

This verifies only finite counting consequences of the analytic factor theorem.
It is not a graph-realization certificate and does not verify the external
exact-129 factorization itself.
"""

placements = []
for b in range(8):          # seven selected K5 components
    for u in range(4):      # three unselected K5 components
        for g in range(3):  # alpha(G11)=2 and B independent in this color
            if b + u + g == 10:
                placements.append((b, u, g))

expected = [
    (5, 3, 2),
    (6, 2, 2),
    (6, 3, 1),
    (7, 1, 2),
    (7, 2, 1),
    (7, 3, 0),
]
assert placements == expected, placements
assert min(b for b, _, _ in placements) == 5
assert max(b for b, _, _ in placements) == 7

# Audited high-k row floors from the five V12 templates.
h_floor = {"A": 6, "B": 8, "C": 6, "D": 7, "E": 5}
selected_high_floor = {name: max(0, h + 5 - 10) for name, h in h_floor.items()}
assert selected_high_floor == {"A": 1, "B": 3, "C": 1, "D": 2, "E": 0}

# Seven exact-129 colors.
global_floor = {name: 7 * v for name, v in selected_high_floor.items()}
assert global_floor == {"A": 7, "B": 21, "C": 7, "D": 14, "E": 0}

# b=5 has the unique B-placement profile (u,g)=(3,2).
assert [(u, g) for b, u, g in placements if b == 5] == [(3, 2)]

print("SELECTED_B_ANCHOR_FLOOR_ARITHMETIC_OK")
print("placements=", placements)
print("selected_high_floor=", selected_high_floor)
print("global_floor=", global_floor)
