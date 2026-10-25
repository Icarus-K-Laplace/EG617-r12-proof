#!/usr/bin/env python3
"""Arithmetic replay for the delta13 epsilonU=1 3K4+K6, K4-K6 edge case.

Checks only the exact U-edge ledger, saturation degree gaps, and cover ceiling;
it does not prove the graph-theoretic transversal or label lemmas.
"""
def check_u_ledger():
    assert 112 - 13 == 99
    assert 3 * (7 * 6 // 2) + (8 * 7 // 2) == 91
    assert 99 - 91 == 8

def check_saturation_gaps():
    # A nonsaturated U vertex would need W-degree >=8, while the maximum
    # degree from U into W is 7 for small parts and 6 for D.
    assert 7 < 8
    assert 6 < 8
    # A nonsaturated W vertex has U-degree >=12. K6 vertices are <=10;
    # the K4 endpoint is <=11.
    assert 10 < 12
    assert 11 < 12

def check_cover_capacity():
    # Three K4 components each have common-neighbour capacity at most 9;
    # the K6 capacity is at most floor(E6/2) <= 1 because E_W=3.
    assert 3 * 9 + (3 // 2) == 28
    assert 28 < 29

if __name__ == "__main__":
    check_u_ledger()
    check_saturation_gaps()
    check_cover_capacity()
    print("DELTA13_EPS1_3K4_K6_K4K6_EDGE_ARITHMETIC_OK")
