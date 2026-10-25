#!/usr/bin/env python3
"""Arithmetic checks for the disjoint K4-K5 placement exclusion.

The graph-theoretic blocker classification and component-capacity theorem are
dependencies; this script only replays the strict degree/count inequalities.
"""
assert (4 - 1) + (5 - 1) == 7
assert 7 > 6  # D vertices have W-degree at most six
assert 1 <= 1  # at most one positive-excess U vertex when epsilon_U=1
assert 29 - 24 == 5
assert 1 < 5
print("DELTA13_EPS1_TWO_CROSS_EDGE_K4K5_DISJOINT_ARITHMETIC_OK")
