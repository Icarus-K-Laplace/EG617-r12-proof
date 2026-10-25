#!/usr/bin/env python3
"""Arithmetic replay for the delta13 epsilonU=1 3K4+K6 K4-K4 edge case.

Checks only the U-edge ledger, reverse-saturation degree bounds, and capacity
inequalities. It does not prove the graph-theoretic independent-set arguments.
"""
def check_u_ledger():
    assert 112 - 13 == 99
    assert 3 * (7 * 6 // 2) + (8 * 7 // 2) == 91
    assert 99 - 91 == 8

def check_degree_gaps():
    # A nonsaturated U vertex has W-degree at least six. If its W-degree is
    # seven, it is the unique possible epsilon_U=1 exception.
    assert 6 + 1 == 7
    # A nonsaturated W vertex has U-degree at least twelve; D vertices and
    # K6 vertices are below that threshold.
    assert 6 < 8
    assert 10 < 12
    assert 11 < 12

def check_capacity_bounds():
    # Three K4 capacities are at most 9; K6 is at most floor(E6/2) <= 1.
    assert 3 * 9 + (3 // 2) == 28
    assert 28 < 29
    # With one U exception, at least 28 vertices must be covered. If all
    # three K4 capacities equal 9, two labels repeat among the two allowed
    # small parts, creating overlap of at least seven vertices.
    assert 28 - 7 == 21
    assert 21 < 28

if __name__ == "__main__":
    check_u_ledger()
    check_degree_gaps()
    check_capacity_bounds()
    print("DELTA13_EPS1_3K4_K6_K4K4_EDGE_ARITHMETIC_OK")
