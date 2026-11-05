#!/usr/bin/env python3
"""Small independent arithmetic/orbit checker for the E286--COVER interface.

Standard library only. This is NOT a graph search or proof checker. It verifies:
- the 10 support orbits from the four-seed incidence quotient;
- the displayed scalar blocker minima on their full finite integer domain;
- shared-center overlap inequalities on the bounded clique-size domain;
- the exact 61 -> 47 pivot edge ledger and E407/E408 boundary arithmetic;
- the d=2 K4 repivot lower-bound identity used in COVER Section 10.

Run:
    python -B RECHECK_E286_COVER_INTERFACE_20261103.py
"""
from itertools import combinations_with_replacement, permutations, product
import json


def pos(x):
    return max(0, x)


def support_orbits():
    perms = list(permutations(range(4)))
    types = [m for m in range(16) if m.bit_count() >= 2]
    out = {}
    for h in (3, 4, 5):
        reps = set()
        raw = 0
        for rows in combinations_with_replacement(types, h):
            if sum(m.bit_count() - 1 for m in rows) != 5:
                continue
            degrees = [
                sum(bool(m & (1 << i)) for m in rows)
                for i in range(4)
            ]
            if min(degrees) < 2:
                continue
            raw += 1
            images = []
            for p in perms:
                mapped = []
                for m in rows:
                    mapped.append(sum(
                        1 << p[i] for i in range(4) if m & (1 << i)
                    ))
                images.append(tuple(sorted(mapped)))
            reps.add(min(images))
        out[h] = {
            "raw_multisets": raw,
            "orbits": len(reps),
            "representatives": [list(x) for x in sorted(reps)],
        }
    assert [out[h]["orbits"] for h in (3, 4, 5)] == [2, 3, 5]
    assert sum(out[h]["orbits"] for h in (3, 4, 5)) == 10
    return out


def scalar_checks():
    functions = {
        "f11": lambda a, b: pos(10-a-b) + a*pos(b-2) + b*pos(a-2),
        "f10_11": lambda a, b: pos(9-a-b) + a*pos(b-3) + b*pos(a-2),
        "f9_11": lambda a, b: pos(8-a-b) + a*pos(b-4) + b*pos(a-2),
        "f10_10": lambda a, b: pos(8-a-b) + a*pos(b-3) + b*pos(a-3),
        "star10": lambda a, b: pos(9-a-b) + a*(b-1) + b*pos(a-2),
        "two_mixed_K9": lambda a, b: pos(8-a-b) + a*(b-1) + b*pos(a-2),
        "mixed": lambda a, b: pos(9-a-b) + a*pos(b-2) + b*pos(a-2),
    }
    out = {}
    for name, f in functions.items():
        values = [(f(a, b), a, b) for a in range(1, 12) for b in range(1, 12)]
        minimum = min(x[0] for x in values)
        out[name] = {
            "minimum": minimum,
            "argmin": [[a, b] for value, a, b in values if value == minimum],
        }
    expected = {
        "f11": 6, "f10_11": 4, "f9_11": 2, "f10_10": 2,
        "star10": 6, "two_mixed_K9": 5, "mixed": 5,
    }
    assert {k: v["minimum"] for k, v in out.items()} == expected
    return out


def overlap_checks():
    k11_bad = [
        (a, b) for a, b in product(range(12), repeat=2)
        if pos(a+b-2) < pos(a-2) + pos(b-2)
    ]
    k10_bad = [
        (a, b, c) for a, b, c in product(range(12), repeat=3)
        if sum(x == 0 for x in (a, b, c)) <= 1
        and pos(a+b+c-3) < pos(a-2) + pos(b-2) + pos(c-2)
    ]
    assert not k11_bad and not k10_bad
    return {
        "K11_two_incidence_counterexamples": len(k11_bad),
        "K10_three_incidence_counterexamples_at_most_one_zero": len(k10_bad),
        "scope": "finite check of the exact pointwise inequalities; the inequalities also follow algebraically",
    }


def pivot_ledger():
    rows = []
    for E in (407, 408):
        q_upper = E - 91 - 287
        rows.append({
            "parent_edges": E,
            "core_floor": 287,
            "max_charge": q_upper,
            "q30_core_edges": E - 91 - 30,
            "q31_core_edges": E - 91 - 31,
        })
    assert rows == [
        {"parent_edges": 407, "core_floor": 287, "max_charge": 29,
         "q30_core_edges": 286, "q31_core_edges": 285},
        {"parent_edges": 408, "core_floor": 287, "max_charge": 30,
         "q30_core_edges": 287, "q31_core_edges": 286},
    ]
    return rows


def k4_repivot_identity():
    # q_p=30, S is a two-vertex edge in M[K4], so d=2 and e_M(S)=1.
    # q_p = t(S)-1+rho, hence rho=31-t(S).
    # q_y = 2*(13-2)+rho+h_12+kappa+b.
    # The complementary pair R is also an M-edge and t(R)>=12 by EDGE12.
    # Since t(K4)=36, t(S)<=24, whence q_y>=29.
    # EDGE13 sharpens t(R)>=13, t(S)<=23, whence q_y>=30.
    for tS in range(25):
        assert 53 - tS >= 29
    for tS in range(24):
        assert 53 - tS >= 30
    return {
        "q_parent": 30,
        "d": 2,
        "missing_edges_inside_S": 1,
        "rho_identity": "rho = 31 - t(S)",
        "q_y_identity": "q_y = 53 - t(S) + h12 + kappa + b",
        "K4_row_union_total": 36,
        "EDGE12_lower_bound_on_complementary_pair": 12,
        "resulting_tS_upper_bound": 24,
        "resulting_qy_lower_bound": 29,
        "EDGE13_sharpened_complementary_pair": 13,
        "sharpened_tS_upper_bound": 23,
        "sharpened_qy_lower_bound": 30,
    }


def main():
    result = {
        "support_orbits": support_orbits(),
        "scalar_blocker_minima": scalar_checks(),
        "shared_center_overlap": overlap_checks(),
        "pivot_edge_ledger": pivot_ledger(),
        "K4_d2_repivot": k4_repivot_identity(),
        "status": "PASS_ARITHMETIC_AND_FINITE_QUOTIENT_CHECKS_ONLY",
        "not_certified": [
            "full E286 analytic proof",
            "full COVER analytic proof",
            "all 61-vertex graphs",
            "Lean or other proof-assistant kernel certification",
            "clean root verifier execution",
        ],
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
