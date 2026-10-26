#!/usr/bin/env python3
"""Arithmetic audit for the 49-block support omission-degree identity.

This script checks integer consequences only. It is not a graph-realization
or E407 terminal-exclusion certificate.
"""

def feasible_profiles():
    for delta in range(3, 17):
        for eps_u in range(5):
            if delta + eps_u <= 16 and eps_u + 2 * delta >= 9:
                yield delta, eps_u


def partitions_of_seven():
    """Yield nonincreasing positive integer partitions of 7."""
    def rec(remaining, ceiling, prefix):
        if remaining == 0:
            yield tuple(prefix)
            return
        for part in range(min(remaining, ceiling), 0, -1):
            yield from rec(remaining - part, part, prefix + [part])
    yield from rec(7, 7, [])


def main():
    partitions = list(partitions_of_seven())
    assert len(partitions) == 15
    assert all(sum(parts) == 7 and len(parts) <= 7 for parts in partitions)

    profiles = list(feasible_profiles())
    assert len(profiles) == 56

    # For each possible omission multiplicity profile, at most seven U-points
    # are omitted in any color class, and at least 22 of the 29 points have r=0.
    for parts in partitions:
        k = len(parts)
        assert k <= 7
        assert 29 - k >= 22
        # If every W vertex is assigned to one of four disjoint clique parts
        # and each part has size >=4, the summed omitted-point budget is >=14.
        assert 21 - k >= 14

    # Check the aggregate identity:
    # sum_u d_W(u) = 5*29 + epsilon_U - 3*sum(r_u) + sum(x_u)
    #              = 124 + epsilon_U + 2*delta.
    for delta, eps_u in profiles:
        lhs = 5 * 29 + eps_u - 3 * 7 + 2 * delta
        rhs = 124 + eps_u + 2 * delta
        assert lhs == rhs

    # The min-size-four W-component corollary excludes these budget profiles
    # from that specific structural regime (not from E407 in general).
    excluded_for_cmin4 = [
        (delta, eps_u) for delta, eps_u in profiles
        if 2 * delta + eps_u < 14
    ]
    assert len(excluded_for_cmin4) == 12

    print("E407_SUPPORT_OMISSION_IDENTITY_ARITHMETIC_OK")
    print(f"omission multiplicity partitions: {len(partitions)}")
    print(f"feasible (delta, epsilon_U) profiles: {len(profiles)}")
    print("every omission profile leaves at least 22 points with r_u=0")
    print(f"profiles failing the c_min=4 budget: {excluded_for_cmin4}")
    print("Scope: arithmetic only; no graph realization or template closure.")


if __name__ == "__main__":
    main()
