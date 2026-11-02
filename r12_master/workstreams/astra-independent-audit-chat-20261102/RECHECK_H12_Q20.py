#!/usr/bin/env python3
"""Independent exact recheck of the q=20 12-shell equality normal form.

This checker starts AFTER the analytic reductions:
  * a maximum 2-matching gives a C4 on four shell vertices;
  * equality forces the other eight shell vertices independent and undecorated;
  * triangle-freeness and absence of a 3-matching force all exterior attachments
    to meet one fixed side of the C4.

It exhausts every possible attachment pattern from the eight exterior vertices
to the two hubs, and every decoration allocation on the four C4 vertices.
It checks all edge-weight inequalities and the alpha(M)<=10 condition.
"""
from itertools import product
from collections import Counter
import json


def compositions(total, length, prefix=()):
    if length == 1:
        yield prefix + (total,)
    else:
        for first in range(total + 1):
            yield from compositions(total - first, length - 1,
                                    prefix + (first,))


def alpha_c4_one_side(pattern):
    # The C4 has hubs x0,x1 and opposite-side vertices y0,y1.
    # Each exterior vertex is adjacent to a subset of {x0,x1}.
    n_not_x0 = sum(1 for code in pattern if not (code & 1))
    n_not_x1 = sum(1 for code in pattern if not (code & 2))
    n_neither = sum(1 for code in pattern if code == 0)
    return max(10, 1 + n_not_x0, 1 + n_not_x1, 2 + n_neither)


def main():
    patterns_tested = 0
    patterns_after_edge_floor = 0
    decoration_allocations_tested = 0
    feasible = []

    for pattern in product(range(4), repeat=8):
        patterns_tested += 1
        hub_external_degrees = [
            sum(1 for code in pattern if code & 1),
            sum(1 for code in pattern if code & 2),
        ]
        external_edges = sum(code.bit_count() for code in pattern)

        # e(M)=4+external_edges >= 11, while q=e(M)+sum(g)=20.
        if not 7 <= external_edges <= 16:
            continue
        patterns_after_edge_floor += 1
        decoration_total = 16 - external_edges

        # C4 vertex order is (x0,y0,x1,y1).
        for g in compositions(decoration_total, 4):
            decoration_allocations_tested += 1
            t = [
                2 + hub_external_degrees[0] + g[0],
                2 + g[1],
                2 + hub_external_degrees[1] + g[2],
                2 + g[3],
            ]
            assert sum(t) == 24

            # Every C4 edge has t(u)+t(v)>=12.
            if any(t[u] + t[v] < 12
                   for u, v in ((0, 1), (1, 2), (2, 3), (3, 0))):
                continue

            # Every exterior edge has the same pair-row lower bound.
            valid = True
            for code in pattern:
                exterior_degree = code.bit_count()
                for bit, hub_index in ((1, 0), (2, 2)):
                    if code & bit and t[hub_index] + exterior_degree < 12:
                        valid = False
                        break
                if not valid:
                    break
            if not valid:
                continue

            alpha = alpha_c4_one_side(pattern)
            if alpha > 10:
                continue
            feasible.append((pattern, g, t, alpha, external_edges))

    # Exact classification of all feasible labeled configurations.
    assert patterns_tested == 4 ** 8
    assert all(all(code in (0, 3) for code in pattern)
               for pattern, *_ in feasible)
    assert all(t == [10, 2, 10, 2]
               for _, _, t, _, _ in feasible)
    assert all(g == (8 - r_ext, 0, 8 - r_ext, 0)
               for pattern, g, _, _, _ in feasible
               for r_ext in [sum(code == 3 for code in pattern)])
    r_values = [sum(code == 3 for code in pattern) + 2
                for pattern, *_ in feasible]
    assert all(6 <= r <= 10 for r in r_values)

    by_r = Counter(r_values)
    assert dict(sorted(by_r.items())) == {6: 70, 7: 56, 8: 28, 9: 8, 10: 1}
    result = {
        "status": "PASS",
        "all_attachment_patterns": patterns_tested,
        "patterns_meeting_eM_floor": patterns_after_edge_floor,
        "decoration_allocations_checked": decoration_allocations_tested,
        "feasible_labeled_configurations": len(feasible),
        "feasible_configurations_by_r": dict(sorted(by_r.items())),
        "normal_form": "K_{2,r} disjoint_union (10-r)K_1",
        "r_range": [6, 10],
        "forced_hub_weights": [10, 10],
        "forced_low_weights": [2] * 10,
        "hub_decorations": "g_hub=10-r on each hub",
        "all_eight_exterior_decorations": 0,
        "scope": "finite check after the analytic C4/one-side-attachment reduction; does not replace proof of those reductions or the surrounding graph theorems"
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
