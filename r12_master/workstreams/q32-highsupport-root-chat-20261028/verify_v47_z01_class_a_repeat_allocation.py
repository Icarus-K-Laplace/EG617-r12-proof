#!/usr/bin/env python3
"""Exact allocation audit for the E0=0 Class-A source-mode scalar profile.

Class A contract: an exact color's T0 repeat is on T0--Ti and its unique
large-pair repeat is on Ti--Tj, so both repeat edges share the Ti residual
triangle endpoint. This verifier does not apply to Class-B colors.
"""
def main():
    # x_ij = number of exact colors whose T0 repeat is on T0--Ti and whose
    # large-pair repeat is on Ti--Tj. Ordered pairs i != j, i,j in {1,2,3}.
    # Scalar counts: T0 repeats (4,3,3), large exact repeats (7,0,3).
    solutions = []
    for x12 in range(5):
        x13 = 4 - x12
        for x21 in range(4):
            x23 = 3 - x21
            for x31 in range(4):
                x32 = 3 - x31
                row_sums = (x12 + x13, x21 + x23, x31 + x32)
                pair_sums = (x12 + x21, x13 + x31, x23 + x32)
                if row_sums == (4, 3, 3) and pair_sums == (7, 0, 3):
                    solutions.append((x12, x13, x21, x23, x31, x32))

    expected = (4, 0, 3, 0, 0, 3)
    assert solutions == [expected], solutions
    x12, x13, x21, x23, x31, x32 = expected

    # Since P_12 and P_23 are perfect matchings, all exact-repeat edges
    # within each pair are vertex-disjoint. Thus the forced allocation gives:
    # T1: 4 T0-repeat endpoints from x12 are distinct; 3 x21 K4-side
    # endpoints are distinct and disjoint from those four.
    # T2: 4 x12 K4-side endpoints and 3 x21 T0-repeat endpoints are all
    # distinct on P_12; 3 x32 K4-side endpoints are distinct on P_23.
    # T3: the 3 x32 T0-repeat endpoints are distinct.
    assert x12 + x21 == 7
    assert x23 + x32 == 3
    assert x13 + x31 == 0
    print("Class-A allocation solutions:", len(solutions))
    print("x12,x13,x21,x23,x31,x32 =", expected)
    print("T0 repeat tracks -> large pair:")
    print("  4 colors: T0-T1 repeat, T1-T2 repeat")
    print("  3 colors: T0-T2 repeat, T1-T2 repeat")
    print("  3 colors: T0-T3 repeat, T2-T3 repeat")
    print("P_12 forces 7 pairwise vertex-disjoint exact-repeat edges.")
    print("P_23 forces 3 pairwise vertex-disjoint exact-repeat edges.")
    print("V47_Z01_CLASS_A_REPEAT_ALLOCATION_OK")
    print("Scope: E0=0 Class-A allocation only; no global common-P packing or Q32 closure.")


if __name__ == "__main__":
    main()
