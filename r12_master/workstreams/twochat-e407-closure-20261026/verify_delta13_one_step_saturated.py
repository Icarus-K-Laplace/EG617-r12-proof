#!/usr/bin/env python3
"""Arithmetic replay for the delta=13 one-step saturated reduction/closure.

Checks:
- classified J degree sequence and uncovered cross-edge count;
- endpoint localization from support-edge exhaustion;
- exact W four-partite profiles for epsilon_U=1,2,3;
- epsilon_U=0 three-clique edge thresholds used in the direct deletion proof.

It does not verify the external saturated-kernel classification, Brouwer's
second-Turan theorem, or the analytic independent-set arguments.
"""

from itertools import combinations_with_replacement
from math import comb


def p3(n: int) -> int:
    """Minimum edges on n vertices with independence number at most 3."""
    q, r = divmod(n, 3)
    sizes = [q + 1] * r + [q] * (3 - r)
    return sum(comb(s, 2) for s in sizes)


def w_profiles(epsilon_u: int):
    comp_edges = 118 + epsilon_u
    out = []
    for parts in combinations_with_replacement(range(1, 19), 4):
        if sum(parts) != 18:
            continue
        t = sum(parts[i] * parts[j] for i in range(4) for j in range(i + 1, 4))
        if comp_edges <= t <= 121:
            out.append((parts, t - comp_edges))
    return out


def main():
    # C5 blow-up J with parts (5,5,2,1,2): degree sequence 7^10, 6^4, 4^1.
    j_degrees = [7] * 10 + [6] * 4 + [4]
    assert sum(j_degrees) == 98
    assert sum(j_degrees) // 2 == 49

    uncovered_per_vertex = [2 * (7 - d) for d in j_degrees]
    assert sum(uncovered_per_vertex) == 14
    assert uncovered_per_vertex.count(0) == 10
    assert uncovered_per_vertex.count(2) == 4
    assert uncovered_per_vertex.count(6) == 1

    expected = {
        1: [
            ((3, 4, 5, 6), 0),
            ((3, 5, 5, 5), 1),
            ((4, 4, 4, 6), 1),
            ((4, 4, 5, 5), 2),
        ],
        2: [
            ((3, 5, 5, 5), 0),
            ((4, 4, 4, 6), 0),
            ((4, 4, 5, 5), 1),
        ],
        3: [((4, 4, 5, 5), 0)],
    }
    for eps, want in expected.items():
        got = w_profiles(eps)
        assert got == want, (eps, got, want)

    # epsilon_U=0 direct deletion proof thresholds.
    assert p3(18) == 45
    assert p3(17) == 40
    assert p3(16) == 35

    print("DELTA13_ONE_STEP_SATURATED_ARITHMETIC_OK")
    print("uncovered A/B-J cross edges:", sum(uncovered_per_vertex))
    print("endpoint uncovered multiplicities:", sorted(set(uncovered_per_vertex)))
    for eps in (1, 2, 3):
        print(f"epsilon_U={eps} W profiles:", w_profiles(eps))
    print("p3 thresholds:", {n: p3(n) for n in (16, 17, 18)})
    print("Scope: arithmetic only; external and analytic proof steps not machine-verified here.")


if __name__ == "__main__":
    main()
