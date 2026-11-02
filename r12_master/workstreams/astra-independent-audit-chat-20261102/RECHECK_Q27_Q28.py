#!/usr/bin/env python3
"""Independent q=27/q=28 bipartite-shell enumeration for EG617 R12.

Standard-library only. Reconstructs the 3-hub/10-low shell states from
row multiplicities, Hall's inequalities, EDGE12 and INS11. It does not
import or read the frozen COVER verifier or its output.
"""
import itertools as it
import json


def compositions(total, length):
    if length == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in compositions(total - first, length - 1):
            yield (first,) + tail


def partitions(total, length, minimum=0):
    if length == 0:
        if total == 0:
            yield ()
        return
    for first in range(minimum, total // length + 1):
        for tail in partitions(total - first, length - 1, first):
            yield (first,) + tail


def canonical(hub_weights, rows):
    candidates = []
    for perm in it.permutations(range(3)):
        weights = tuple(hub_weights[i] for i in perm)
        mapped = []
        for mask, decoration in rows:
            new_mask = sum(
                1 << j for j, i in enumerate(perm) if (mask >> i) & 1
            )
            mapped.append((new_mask, decoration))
        candidates.append((weights, tuple(sorted(mapped))))
    return min(candidates)


def expected_states(q):
    result = set()
    if q == 27:
        for k in (8, 9):
            result.add(canonical(
                (9, 9, 9),
                [(7, 0)] * k + [(0, 0)] * (10 - k)
            ))
    elif q == 28:
        for k in (8, 9):
            result.add(canonical(
                (9, 9, 10),
                [(7, 0)] * k + [(0, 0)] * (10 - k)
            ))
        for k in (7, 8):
            result.add(canonical(
                (9, 9, 9),
                [(7, 0)] * k + [(3, 1)] + [(0, 0)] * (9 - k)
            ))
        for k in (8, 9):
            result.add(canonical(
                (9, 9, 9),
                [(7, 0)] * (k - 1) + [(7, 1)] + [(0, 0)] * (10 - k)
            ))
            result.add(canonical(
                (9, 9, 9),
                [(7, 0)] * k + [(0, 1)] + [(0, 0)] * (9 - k)
            ))
    else:
        raise ValueError("only q=27 and q=28 are in scope")
    return result


def enumerate_states(q):
    states = set()
    counts = {
        "row_vectors": 0,
        "row_vectors_after_edge_and_hall": 0,
        "hub_decoration_trials": 0,
        "complete_decoration_allocations": 0,
    }

    # Eight possible low-row neighborhoods, one for each subset of 3 hubs.
    for multiplicities in compositions(10, 8):
        counts["row_vectors"] += 1
        z = sum(c * mask.bit_count()
                for mask, c in enumerate(multiplicities))
        if not 22 <= z <= q:
            continue

        # Hall's seven nonempty-subset inequalities are alpha(M) <= 10.
        if any(
            sum(c for mask, c in enumerate(multiplicities) if mask & subset)
            < subset.bit_count()
            for subset in range(1, 8)
        ):
            continue
        counts["row_vectors_after_edge_and_hall"] += 1

        hub_degrees = [
            sum(c for mask, c in enumerate(multiplicities)
                if (mask >> i) & 1)
            for i in range(3)
        ]
        total_decoration = q - z

        for hub_decoration_total in range(total_decoration + 1):
            for hub_decorations in compositions(hub_decoration_total, 3):
                counts["hub_decoration_trials"] += 1
                hub_weights = tuple(
                    hub_degrees[i] + hub_decorations[i] for i in range(3)
                )
                low_budget = total_decoration - hub_decoration_total
                groups = []
                minimum_budget = 0

                for mask, multiplicity in enumerate(multiplicities):
                    if multiplicity == 0:
                        continue
                    degree = mask.bit_count()
                    # EDGE12 for every hub-low edge.
                    floor = max(
                        [0] + [
                            12 - degree - hub_weights[i]
                            for i in range(3) if (mask >> i) & 1
                        ]
                    )
                    # If the low point is regular, INS11 must also hold.
                    if sum(
                        hub_weights[i] for i in range(3)
                        if (mask >> i) & 1
                    ) < degree * (12 - degree):
                        floor = max(floor, 1)
                    groups.append((mask, multiplicity, floor))
                    minimum_budget += multiplicity * floor

                if minimum_budget > low_budget:
                    continue

                def allocate(group_index, remaining, rows):
                    if group_index == len(groups):
                        if remaining != 0:
                            return
                        counts["complete_decoration_allocations"] += 1

                        # INS11 for each regular hub.
                        for i in range(3):
                            if hub_decorations[i] == 0:
                                neighbor_weight = sum(
                                    mask.bit_count() + decoration
                                    for mask, decoration in rows
                                    if (mask >> i) & 1
                                )
                                if neighbor_weight < (
                                    hub_degrees[i] * (12 - hub_degrees[i])
                                ):
                                    return

                        states.add(canonical(hub_weights, rows))
                        return

                    mask, multiplicity, floor = groups[group_index]
                    reserve = sum(
                        c * f for _, c, f in groups[group_index + 1:]
                    )
                    for budget in range(
                        multiplicity * floor, remaining - reserve + 1
                    ):
                        for allocation in partitions(budget, multiplicity, floor):
                            allocate(
                                group_index + 1,
                                remaining - budget,
                                rows + [(mask, g) for g in allocation],
                            )

                allocate(0, low_budget, [])

    assert counts["row_vectors"] == 19448
    return states, counts


def check_all_subsets(state, q):
    hub_weights, rows = state
    weights = list(hub_weights) + [
        mask.bit_count() + decoration for mask, decoration in rows
    ]
    adjacency = [set() for _ in range(13)]
    for vertex, (mask, _) in enumerate(rows, start=3):
        for hub in range(3):
            if (mask >> hub) & 1:
                adjacency[hub].add(vertex)
                adjacency[vertex].add(hub)

    hub_degrees = [len(adjacency[i]) for i in range(3)]
    decorations = [
        hub_weights[i] - hub_degrees[i] for i in range(3)
    ] + [decoration for _, decoration in rows]

    assert min(decorations) >= 0
    z = sum(map(len, adjacency)) // 2
    assert z >= 22 and z + sum(decorations) == q

    # EDGE12.
    for i in range(13):
        for j in adjacency[i]:
            assert weights[i] + weights[j] >= 12

    # Every one of the 2^13 subset identities, and alpha(M) <= 10.
    for subset in range(1 << 13):
        inside = [i for i in range(13) if (subset >> i) & 1]
        outside = [i for i in range(13) if not ((subset >> i) & 1)]
        e_inside = sum(
            1 for i, j in it.combinations(inside, 2) if j in adjacency[i]
        )
        e_outside = sum(
            1 for i, j in it.combinations(outside, 2) if j in adjacency[i]
        )
        assert (
            sum(weights[i] for i in inside)
            - e_inside
            + e_outside
            + sum(decorations[i] for i in outside)
        ) == q
        if len(inside) >= 11:
            assert e_inside > 0

    # INS11 at every regular vertex.
    for vertex in range(13):
        if decorations[vertex] != 0:
            continue
        neighborhood = sorted(adjacency[vertex])
        degree = len(neighborhood)
        e_neighborhood = sum(
            1 for i, j in it.combinations(neighborhood, 2)
            if j in adjacency[i]
        )
        assert (
            sum(weights[i] for i in neighborhood) - 2 * e_neighborhood
            >= degree * (12 - degree)
        )


def main():
    output = {"status": "PASS", "q": {}}
    total_subset_checks = 0
    for q in (27, 28):
        states, counts = enumerate_states(q)
        expected = expected_states(q)
        assert states == expected
        for state in states:
            check_all_subsets(state, q)
            total_subset_checks += 1 << 13
        output["q"][str(q)] = {
            "canonical_state_count": len(states),
            "counters": counts,
            "states": [
                {"hub_weights": list(weights), "rows": [list(r) for r in rows]}
                for weights, rows in sorted(states)
            ],
        }
    output["direct_subset_checks"] = total_subset_checks
    assert total_subset_checks == 81920
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
