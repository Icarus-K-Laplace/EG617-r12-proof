#!/usr/bin/env python3
"""Exact arithmetic verifier for the R12 witness-packing note.

Checks Turan edge counts, the two union-size boundary arguments, exact-129
color counts, zero-excess witness counts, and the local second-Turan audit
example. It does NOT certify graph realization or the T61 input contracts.
Uses only the Python standard library.
"""
from math import comb


def turan_edges(n: int, r: int) -> int:
    """Number of edges in the balanced complete r-partite Turan graph."""
    q, rem = divmod(n, r)
    parts = [q + 1] * rem + [q] * (r - rem)
    return comb(n, 2) - sum(comb(s, 2) for s in parts)


def part_sizes(n: int, r: int) -> tuple[int, ...]:
    q, rem = divmod(n, r)
    return tuple([q + 1] * rem + [q] * (r - rem))


def main() -> None:
    expected_t4 = {
        19: 135,
        27: 273,
        28: 294,
        29: 315,
        30: 337,
        31: 360,
    }
    for n, expected in expected_t4.items():
        got = turan_edges(n, 4)
        print(f"t_4({n})={got}")
        assert got == expected

    # Exact residual color-count excess.
    total_pairs = comb(61, 2)
    e407_non_target = total_pairs - 407
    e408_non_target = total_pairs - 408
    assert total_pairs == 1830
    assert e407_non_target == 1423 == 11 * 129 + 4
    assert e408_non_target == 1422 == 11 * 129 + 3
    print("E407 exact-129 colors >= 7; E408 exact-129 colors >= 8")

    # E407 boundary v=28: the residual 19-set has at least 36 edges,
    # but the core edge identity gives at most 32.
    e_h_w_lower = comb(19, 2) - turan_edges(19, 4)
    assert e_h_w_lower == 36
    assert 284 - 84 - 168 == 32
    print("E407 v=28 contradiction: e(H[W]) >= 36 but <= 32")

    # v=30 is impossible when there are at least 56 edge-disjoint K4s:
    # Brouwer threshold forces four-partiteness; no partition of 30 into
    # four positive parts has every pair-product >= 56.
    assert 6 * 56 == 336
    assert 337 - (30 // 4) + 1 == 331
    assert 336 > 331
    admissible = []
    for a in range(1, 31):
        for b in range(a, 31):
            for c in range(b, 31):
                d = 30 - a - b - c
                if d < c:
                    continue
                sizes = (a, b, c, d)
                if sum(sizes) == 30 and all(x * y >= 56
                                            for i, x in enumerate(sizes)
                                            for y in sizes[i + 1:]):
                    admissible.append(sizes)
    assert admissible == []
    print("v=30 impossible for 56 linear K4 witnesses")

    # Stronger zero-excess count: six disjoint B-labelled Q-sets per color,
    # at most four can meet the positive-excess vertex set.
    assert 6 - 4 == 2
    assert 7 * 2 == 14
    assert 8 * 2 == 16
    print("Zero-excess B-labelled witnesses: E407 >=14; E408 Q33 >=16")

    # Shell-incidence union lemma for E407 Q32 templates A/C.
    # e(A,H)=32+e(M), so the excess shell-incidence budget is e(M)-15.
    # For full rows (k_b=3), |union D_b| >= 15-beta-c_rest.
    assert 32 + 22 - 47 == 7  # example A profile: e(M)=22
    assert 15 - 0 - 4 == 11  # Template A, n1<=4
    assert 15 - 1 - 4 == 10  # Template C, beta=1, n1<=4
    assert 11 > 3 and 10 > 3
    print("Full-row support union: Template A >=11; Template C >=10")

    # Audit the m=10 star lemma's second-Turan inference. If e(H[U]) <=143,
    # then its complement has >=292 edges, above the non-tripartite bound
    # 300 - floor(30/3) + 1 = 291. This forces tripartiteness, not completeness.
    assert turan_edges(30, 3) == 300
    assert 300 - (30 // 3) + 1 == 291
    assert 435 - 143 == 292 > 291
    # A local model: three K10 parts plus one cross-part edge has 136 edges;
    # the ten triples (a_i,b_i,c_i) remain independent if the added edge is
    # a_0 b_1. Each part is a clique, so alpha is at most three.
    local_e_h_u = 3 * comb(10, 2) + 1
    local_alpha_upper = 3
    assert local_e_h_u == 136
    assert local_alpha_upper == 3
    assert 435 - local_e_h_u == 299
    print("Star-lemma audit: tripartite does not imply complete; g=1 gives e=136")

    # Independent audit of the linear-witness transversal theorem.
    for t in range(0, 5):
        assert t * ((29 - t) // 3) + comb(t, 2) < 49
    for t in range(0, 6):
        assert t * ((31 - t) // 3) + comb(t, 2) < 56
    assert 2 * 49 - 5 * ((29 - 5) // 3) == 58 > 5 * ((29 - 1) // 3)
    assert 2 * 49 - 6 * ((29 - 6) // 3) == 56 > 6 * ((29 - 1) // 3)
    assert 2 * 56 - 6 * ((31 - 6) // 3) == 64 > 6 * ((31 - 1) // 3)
    print("Transversal floor: tau(Q)>=7 for both boundary kernels")

    # Correct boundary windows; do not infer non-four-partiteness from a
    # failure to be complete four-partite.
    assert comb(29, 2) - 294 == 112
    assert comb(29, 2) - (294 + 16) == 96
    assert 284 - 96 - (124 + 2 * 16) == 32
    assert comb(31, 2) - 336 == 129
    assert comb(31, 2) - (336 + 17) == 112
    assert 284 - 112 - (114 + 2 * 17) == 24
    assert turan_edges(29, 4) - (294 + 16) == 5
    assert turan_edges(31, 4) - (336 + 17) == 7
    assert turan_edges(29, 4) - 294 == 21
    assert turan_edges(31, 4) - 336 == 24
    print("Boundary windows: E407 delta+eps_U<=16; E408 delta+eps_U<=17")

    print("ALL WITNESS-PACKING ARITHMETIC CHECKS PASSED")
    print("Scope: arithmetic only; no graph-completion or root-theorem certificate.")


if __name__ == "__main__":
    main()
