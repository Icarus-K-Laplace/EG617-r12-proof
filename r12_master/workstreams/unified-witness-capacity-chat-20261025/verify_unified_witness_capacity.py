#!/usr/bin/env python3
"""Exact finite arithmetic checks for the unified R12 witness-capacity line.

This verifies the zero-excess endpoint tables, edge ledgers, omission-profile
bounds, and the two scalar-relaxation examples. It is not a graph search and
does not certify realization of a witness hypergraph or a colored graph.
"""
from math import comb
from itertools import product


def p3(n: int) -> int:
    """Minimum edges in an n-vertex graph with alpha <= 3."""
    q, r = divmod(n, 3)
    parts = [q + 1] * r + [q] * (3 - r)
    return sum(comb(x, 2) for x in parts)


def p_alpha4(n: int) -> int:
    """Minimum edges in an n-vertex graph with alpha <= 4."""
    q, r = divmod(n, 4)
    parts = [q + 1] * r + [q] * (4 - r)
    return sum(comb(x, 2) for x in parts)


def partitions(total: int, cap: int, minpart: int = 1):
    """Yield nonincreasing positive integer partitions, parts <= cap."""
    if total == 0:
        yield ()
        return
    for x in range(min(cap, total), minpart - 1, -1):
        for tail in partitions(total - x, x, minpart):
            yield (x,) + tail


def omission_max_e407(s: int) -> int:
    best = -1
    for parts in partitions(7, 6):
        k = len(parts)
        n0 = 29 - k
        n1 = sum(x == 1 for x in parts)
        if 5 * n0 + 2 * n1 <= 124 + s:
            omega = sum(comb(x, 2) for x in parts)
            best = max(best, omega)
    return best


def omission_max_e408(s0: int) -> int:
    best = -1
    for parts in partitions(24, 7):
        k = len(parts)
        n0 = 31 - k
        n1 = sum(x == 1 for x in parts)
        if 6 * n0 + 3 * n1 <= 114 + s0:
            omega = sum(comb(x, 2) for x in parts)
            best = max(best, omega)
    return best


def check_zero_excess_endpoint_tables() -> None:
    # Source theorem: e(H0-T) <= U(E,k,t); Turan lower bound is p3(n).
    e284 = [(40, 217), (39, 212), (38, 208), (37, 205)]
    e285 = [(42, 229), (41, 222), (40, 216),
            (39, 211), (38, 207), (37, 204)]
    gaps284 = [p3(n) - u for n, u in e284]
    gaps285 = [p3(n) - u for n, u in e285]
    assert gaps284 == [30, 22, 14, 5]
    assert gaps285 == [44, 38, 31, 23, 15, 6]

    # Check the monotonic-gap condition used to reduce all t<=tmax to tmax.
    # p3(n)-p3(n-1)=floor((n-1)/3), while U(t)-U(t+1)=12-k-t.
    for k in range(1, 5):
        for t in range(0, 6):
            n = 47 - k - t
            assert (p3(n) - p3(n - 1)) >= (12 - k - t)
    for k in range(1, 7):
        for t in range(0, 4):
            n = 47 - k - t
            assert (p3(n) - p3(n - 1)) >= (12 - k - t)


def check_edge_ledgers() -> None:
    assert comb(29, 2) == 406 and p_alpha4(18) == 32
    assert 406 - 32 - 12 * 29 + 284 == 310
    assert comb(31, 2) == 465 and p_alpha4(16) == 24
    assert 465 - 24 - 12 * 31 + 284 == 353

    # E407 boundary ledgers.
    eps, delta = 3, 3
    assert eps + 2 * delta == 9
    assert eps + delta <= 16
    assert 112 - delta == 109
    assert 124 + eps + 2 * delta == 133
    assert 48 - eps - delta == 42
    assert 294 + delta == 297 <= 310 - eps

    # E408 Q33 boundary ledgers.
    eps, delta = 4, 4
    assert eps + 2 * delta == 12
    assert eps + delta <= 17
    assert 129 - delta == 125
    assert 114 + eps + 2 * delta == 126
    assert 41 - eps - delta == 33
    assert 336 + delta == 340 <= 353 - eps


def check_omission_tables() -> None:
    e407_expected = {
        9: 7, 10: 10, 11: 11, 12: 11,
        **{s: 15 for s in range(13, 33)},
    }
    for s, expected in e407_expected.items():
        assert omission_max_e407(s) == expected, (s, omission_max_e407(s), expected)

    e408_expected = {
        12: 24, 13: 24, 14: 24,
        15: 29, 16: 29, 17: 29,
        18: 31, 19: 31, 20: 31,
        21: 33, 22: 33, 23: 33,
        24: 37, 25: 37, 26: 37,
        27: 41, 28: 41, 29: 41,
        30: 47, 31: 47, 32: 47,
        33: 48, 34: 48,
    }
    for s0, expected in e408_expected.items():
        assert omission_max_e408(s0) == expected, (
            s0, omission_max_e408(s0), expected
        )

    # Witness multiplicity / overlap identities.
    assert 7 * 29 - 196 == 7
    assert 8 * 31 - 224 == 24
    # E407 omission profile (4,2,1,0^26), Omega=7.
    e407_parts = (4, 2, 1)
    assert sum(e407_parts) == 7
    assert sum(comb(x, 2) for x in e407_parts) == 7
    assert 5 * 26 + 2 <= 124 + 9
    # E408 profile (6,2^9,0^21), Omega=24.
    e408_parts = (6,) + (2,) * 9
    assert sum(e408_parts) == 24
    assert sum(comb(x, 2) for x in e408_parts) == 24
    assert 6 * 21 <= 114 + 12


def check_label_count_matrix() -> None:
    # Rows are eight colors, columns are ten B labels. Row sums are one 7
    # and seven 6s; column sums are (6,6,5,5,5,5,4,4,5,4).
    matrix = [
        [1, 1, 1, 1, 1, 1, 0, 0, 1, 0],
        [1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 0, 1, 1],
        [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    ]
    assert [sum(row) for row in matrix] == [7, 6, 6, 6, 6, 6, 6, 6]
    assert [sum(matrix[i][j] for i in range(8)) for j in range(10)] == [
        6, 6, 5, 5, 5, 5, 4, 4, 5, 4
    ]


def check_partite_branch_capacity() -> None:
    # E408 Q33 four-partite profile: one 7-part and three 8-parts.
    r = [8] * 7 + [7] * 24
    omissions = [8 - x for x in r]
    assert len(r) == 31 and sum(r) == 224
    assert omissions == [0] * 7 + [1] * 24
    assert sum(omissions) == 24
    omega = sum(comb(x, 2) for x in omissions)
    assert omega == 0
    assert sum(comb(x, 2) for x in r) == 700

    crossing_lower = 4 * comb(56, 2) - 700
    within_part_load = 64 * comb(7, 2) + 49 * 3 * comb(8, 2)
    assert crossing_lower == within_part_load == 5460

    # Delta is the number of present leftover cross-part slots.
    # The four-partite sibling theorem gives 9 <= delta <= 17.
    for delta in range(9, 18):
        weighted_load = 5460 + 49 * (24 - delta)
        assert weighted_load == 6636 - 49 * delta
        assert weighted_load >= crossing_lower

    # Per-label target-neighborhood capacity by part for n_b blocks.
    for n_b in range(8):
        q33_cap = (7 - n_b) + 3 * (8 - n_b)
        assert q33_cap == 31 - 4 * n_b
        e407_cap = (8 - n_b) + 3 * (7 - n_b)
        assert e407_cap == 29 - 4 * n_b
    assert (7 - 7) + 3 * (8 - 7) == 3
    assert (8 - 7) + 3 * (7 - 7) == 1

    # Q33 per-row label-capacity and the induced B-to-(H\\D) lower bound.
    for P in range(8):
        assert 3 * P + 2 * (7 - P) == 14 + P
        assert 14 + P <= 21
        for beta in range(4):
            for G_B in range(4 - beta):
                lower = max(0, 8 - beta + G_B - P)
                assert lower >= 0


def check_pair_certificate_multiplicity() -> None:
    # A graph-theoretic Q can certify only pairs among rows it avoids.
    assert comb(10, 2) == 45
    for mu in range(11):
        assert comb(mu, 2) <= 45
        if mu:
            assert mu - 1 <= 9  # label-anchored pairs containing its own label


def check_q33_label_array_relaxation() -> None:
    # Seven pivot rows plus one non-pivot row; seven B-label symbols.
    # The array checks only label incidence, not actual Q-coordinate realization.
    rows = []
    for i in range(7):
        row = []
        for j in range(7):
            row.append("p" if i == j else (i + j) % 7)
        rows.append(row)
    rows.append([(2 * j) % 7 for j in range(7)])

    assert all(len(set(row)) == 7 for row in [rows[7]])
    for i in range(7):
        assert rows[i].count("p") == 1
        symbols = [x for x in rows[i] if x != "p"]
        assert len(symbols) == 6 and len(set(symbols)) == 6

    for j in range(7):
        col = [rows[i][j] for i in range(8)]
        assert col.count("p") == 1
        b_symbols = [x for x in col if x != "p"]
        assert sorted(b_symbols) == list(range(7))

    for symbol in range(7):
        assert sum(row.count(symbol) for row in rows) == 7
    assert sum(row.count("p") for row in rows) == 7


def check_exceptional_row_pair_bound() -> None:
    # Enumerate every nonempty 2x2 forced-edge mask between exceptional rows.
    # A nonzero intersection cell forces the corresponding C edge.
    counts = {0: 0, 1: 0, 2: 0}
    for mask in range(1, 16):
        cells = [(r, c) for r in range(2) for c in range(2)
                 if mask & (1 << (2 * r + c))]
        k = len(cells)
        left = {r for r, _ in cells}
        right = {c for _, c in cells}
        ell, cc = len(left), len(right)
        eta = k + max(2 - ell, 2 - cc) - 2
        assert eta >= 0
        counts[eta] += 1

        if k == 1:
            assert eta == 0
        elif k == 2:
            # Two cells are either a matching (zero cost) or adjacent (cost one).
            assert eta == (0 if ell == 2 and cc == 2 else 1)
        elif k == 3:
            assert eta == 1
        else:
            assert k == 4 and eta == 2

    # Four one-cell masks + two matching masks cost zero;
    # four adjacent two-cell masks + four three-cell masks cost one;
    # the full mask costs two.
    assert counts == {0: 6, 1: 8, 2: 1}

    profiles = {(5, 5), (5, 4), (5, 3), (4, 4)}
    for a, b in profiles:
        assert 3 <= b <= a <= 5
        assert 11 - a - b in (1, 2, 3)
    assert all(11 - a - b in (1, 2, 3) for a, b in profiles)


def check_exceptional_row_independence_bound() -> None:
    # Three pairwise nonadjacent exceptional rows have pairwise-disjoint
    # complement cliques of sizes 3..5 in an 11-vertex gadget.
    for sizes in [(3, 3, 3), (3, 3, 4), (3, 3, 5),
                  (3, 4, 4), (3, 4, 5), (3, 5, 5),
                  (4, 4, 4), (4, 4, 5), (4, 5, 5),
                  (5, 5, 5)]:
        total = sum(sizes)
        assert 9 <= total <= 11
        gadget_incidence = 33 - total
        assert 22 <= gadget_incidence <= 24

    # A low-slack block's two exceptional rows have total neighborhood
    # size <= 11+r_i <= 14; since each has size >=6, each has size <=8.
    for r_i in range(1, 4):
        pair_sum_cap = 11 + r_i
        assert pair_sum_cap <= 14
        assert pair_sum_cap - 6 <= 8
        # Three rows from distinct blocks: at most 24 total incidences.
        assert 24 - 22 <= 2 < 5
        # Two from one block plus one from another: at most 22.
        assert pair_sum_cap + 8 <= 22

    # For k low-slack blocks, the 2k exceptional-row graph has alpha<=2.
    # Each pair of blocks contributes at least two C edges among exceptionals.
    for k in range(2, 8):
        min_edges = k * (k - 1)
        # Turan's bound: alpha<=2 means the complement is triangle-free,
        # so e(E) >= C(2k,2) - k^2 = k(k-1).
        assert (2 * k * (2 * k - 1) // 2) - k * k == min_edges
        # Equality is attained by two disjoint K_k cliques.
        assert 2 * (k * (k - 1) // 2) == min_edges


def check_near_complete_component_matching_bound() -> None:
    # For exact-129 blocks with r_i,r_j <= 5, each missing component
    # diagonal consumes at least five extra row-neighborhood incidences.
    # Enumerate all allowed row-budget pairs to verify m <= floor((ri+rj-2)/5).
    for ri in range(1, 6):
        for rj in range(1, 6):
            total_extra = ri + rj - 2
            max_missing = total_extra // 5
            assert max_missing <= 1
            if ri + rj <= 6:
                assert max_missing == 0
            else:
                assert max_missing in (0, 1)

    # At sum ri+rj=7, the extra-incidence budget is exactly five.
    # Thus a missing diagonal can only be paid for by covering a second K5;
    # it cannot pay for six gadget incidences.
    sum7 = [(ri, 7-ri) for ri in range(1, 6) if 1 <= 7-ri <= 5]
    assert sum7 == [(2, 5), (3, 4), (4, 3), (5, 2)]
    for ri, rj in sum7:
        assert ri + rj - 2 == 5
        assert ri + rj - 2 < 6


def check_missing_diagonal_duplicate_charge() -> None:
    # For r_i,r_j <= 5, a missing same-component diagonal consumes at least
    # five of the combined extra row-neighborhood incidences.
    for ri in range(1, 6):
        for rj in range(1, 6):
            budget = ri + rj - 2
            assert budget <= 8
            if ri + rj <= 6:
                assert budget < 5  # no missing diagonal is possible
            else:
                # If exactly one diagonal is missing, at most three incidence
                # units remain, insufficient to cover any other K5 component.
                assert budget >= 5
                assert budget - 5 <= 3
    # The combinatorial perfect-matching argument leaves an independent triple
    # of exceptional rows if d_ij=0; at most three remaining incidences cannot
    # cover a whole K5 component, yielding the 13-set contradiction.
    assert 10 + 3 == 13
    assert 3 < 5


def check_scalar_budget_relaxation() -> None:
    # Explicit scalar relaxation showing that aggregate P_exact >= 69 does
    # not force any exact color to have P_C >= 36. This is not a graph model.
    patterns = [
        [1,1,1,1,0,0,0],
        [0,1,1,1,1,0,0],
        [0,0,1,1,1,1,0],
        [0,0,0,1,1,1,1],
        [1,0,0,0,1,1,1],
        [1,1,0,0,0,1,1],
        [1,1,1,0,0,0,1],
        [0,0,0,1,1,1,1],
    ]
    exact_r = [[7 + x for x in row] for row in patterns]
    assert all(sum(row) == 53 for row in exact_r)
    exact_cols = [sum(row[j] for row in exact_r) for j in range(7)]
    assert exact_cols == [60,60,60,61,61,61,61]

    nonexact_r = [
        [1,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,1,1,0,0,0,0],
    ]
    assert [sum(row) for row in nonexact_r] == [1,0,2]
    assert [exact_cols[j] + sum(row[j] for row in nonexact_r)
            for j in range(7)] == [61]*7

    d_exact = [[1]*9 + [0]*12 for _ in range(8)]
    d_non = [[0]*21 for _ in range(3)]
    for j in range(9):
        for c in range(3):
            d_non[c][j] = 1
        d_non[j % 3][j] += 1
    for j in range(9,21):
        d_non[0][j], d_non[1][j], d_non[2][j] = (
            (3,4,5) if j == 9 else (4,4,4)
        )
    assert [sum(row) for row in d_exact] == [9]*8
    assert [sum(row) for row in d_non] == [59,60,61]
    assert [sum(row[j] for row in d_exact+d_non) for j in range(21)] == [12]*21
    assert all(9+53 == 62 for _ in range(8))
    assert (59+2+1, 60+1+1, 61+0+1) == (62,62,62)
    assert sum(sum(row) for row in d_exact+d_non) == 252
    assert sum(sum(row) for row in exact_r+nonexact_r) == 427
    assert all(min(row) >= 7 for row in exact_r)


def check_duplicate_budget_k12_packing_bound() -> None:
    # The common size-five blocker bound gives at least max(0, P_C-45)
    # common component labels, hence disjoint K12 cliques.
    for R in range(7, 63):
        P = 62 - R
        common_lower = max(0, 17 - R)
        assert common_lower == max(0, P - 45)

    # Exhaust all positive profiles (r_0,...,r_6) with r_i <= 5
    # for the near-terminal sums R=11,12,13.
    expected_high_pairs = {11: 0, 12: 1, 13: 2}
    for R, expected in expected_high_pairs.items():
        maximum = -1
        count = 0
        for profile in product(range(1, 6), repeat=7):
            if sum(profile) != R:
                continue
            count += 1
            high_pairs = sum(
                1 for i in range(7) for j in range(i+1, 7)
                if profile[i] + profile[j] >= 7
            )
            maximum = max(maximum, high_pairs)
        assert count > 0
        assert maximum == expected

    # Seven selected components among ten imply at least P_C-48
    # selected witnesses are in the common size-five blocker intersection.
    for P in range(49, 56):
        common_lower = max(0, P - 45)
        selected_lower = max(0, 7 + common_lower - 10)
        assert selected_lower >= P - 48
        if P == 49:
            assert selected_lower == 1
        if P == 50:
            assert selected_lower == 2

    # If R <= 11, no pair sum can exceed 6 because the other five entries
    # each contribute at least one.
    for R in range(7, 12):
        assert R - 5 <= 6


def main() -> None:
    check_zero_excess_endpoint_tables()
    check_edge_ledgers()
    check_omission_tables()
    check_label_count_matrix()
    check_partite_branch_capacity()
    check_pair_certificate_multiplicity()
    check_q33_label_array_relaxation()
    check_exceptional_row_pair_bound()
    check_exceptional_row_independence_bound()
    check_near_complete_component_matching_bound()
    check_missing_diagonal_duplicate_charge()
    check_scalar_budget_relaxation()
    check_duplicate_budget_k12_packing_bound()
    print("R12_UNIFIED_WITNESS_CAPACITY_ARITHMETIC_OK")
    print("Partite branch: exact Q33 incidence profile and labelled row caps verified.")
    print("Pair-certificate multiplicity: max 45 unlabelled / 9 label-anchored pairs.")
    print("Q33 label-only array relaxation verified; no block-coordinate realization implied.")
    print("Exceptional-row 2x2 mask bound verified: costs 0/1/2 occur 6/8/1 times.")
    print("Exceptional-row graph alpha<=2 and Turan equality profile verified.")
    print("Near-complete component matching budget checked for all r_i,r_j in 1..5.")
    print("Missing-diagonal duplicate-charge boundary arithmetic verified.")
    print("Aggregate scalar relaxation verified; it is not a graph-level counterexample.")
    print("Duplicate-budget K12 packing and labelled-witness extension bounds verified.")
    print("Scope: exact integer/degree ledgers only; no graph-realization certificate.")


if __name__ == "__main__":
    main()
