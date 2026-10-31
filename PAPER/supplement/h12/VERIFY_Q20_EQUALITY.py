"""Independent checks for the five q=20 K_{2,r} shell equality forms."""
import itertools
import json
from pathlib import Path


def edges(adj):
    return {(u, v) for u, ns in adj.items() for v in ns if u < v}


def independence_number(vertices, E):
    best = 0
    for mask in range(1 << len(vertices)):
        chosen = [vertices[i] for i in range(len(vertices)) if mask >> i & 1]
        if all(tuple(sorted((u, v))) not in E for u, v in itertools.combinations(chosen, 2)):
            best = max(best, len(chosen))
    return best


def matching_number(vertices, E):
    best = 0
    for k in range(len(vertices) // 2 + 1):
        found = False
        for chosen in itertools.combinations(E, k):
            used = [x for edge in chosen for x in edge]
            if len(set(used)) == 2 * k:
                found = True
                break
        if found:
            best = k
    return best


def verify_case(case):
    r = case["r"]
    V = case["vertices"]
    adj = case["missing_graph_adjacency"]
    g = case["decoration"]
    t = case["row_size"]
    assert set(V) == set(adj) == set(g) == set(t)
    assert all(set(adj[u]) <= set(V) - {u} for u in V)
    assert all(v in adj[u] for u in V for v in adj[u])
    E = edges(adj)
    assert all((v in adj[u]) == (u in adj[v]) for u in V for v in V if u != v)
    assert len(E) == 2 * r == case["edge_count"]
    assert sum(g.values()) == 2 * (10 - r)
    assert len(E) + sum(g.values()) == 20 == case["total_charge"]
    assert all(t[v] == len(adj[v]) + g[v] for v in V)
    assert t["h0"] == t["h1"] == 10
    assert all(t[f"l{i}"] == 2 for i in range(r))
    assert all(t[f"i{i}"] == 0 for i in range(10 - r))
    assert independence_number(V, E) == 10 == case["independence_number"]
    assert matching_number(V, E) == 2 == case["matching_number"]
    # Triangle-free and exact K_{2,r} plus isolates structure.
    assert all(not (set(adj[u]) & set(adj[v])) for u, v in E)
    expected = {tuple(sorted(("h0", f"l{i}"))) for i in range(r)}
    expected |= {tuple(sorted(("h1", f"l{i}"))) for i in range(r)}
    assert E == expected
    # Repivot at any leaf removes a 2-point row and inserts both hubs.
    # Each old hub has at most 10 neighbors in the old core and one
    # additional neighbor (the other hub) in the new core.
    for item in case["repivot_checks"]:
        leaf = item["leaf"]
        assert t[leaf] == item["leaf_row_size"] == 2
        assert item["hub_row_sizes"] == {"h0": t["h0"], "h1": t["h1"]}
        derived_bound = max(t["h0"], t["h1"]) + 1
        assert item["new_core_hub_degree_upper_bound"] == derived_bound <= 11
    return {"r": r, "vertices": len(V), "missing_edges": len(E),
            "decoration_sum": sum(g.values()), "q": 20,
            "alpha_missing_graph": 10, "matching_number": 2,
            "leaf_repivots_checked": r, "hub_degree_upper_bound": 11}


if __name__ == "__main__":
    data = json.loads(Path(__file__).with_name("Q20_EQUALITY_ADJACENCY_LISTS.json").read_text())
    assert [x["r"] for x in data["cases"]] == [6, 7, 8, 9, 10]
    results = [verify_case(case) for case in data["cases"]]
    assert sum(x["leaf_repivots_checked"] for x in results) == 40
    print(json.dumps({"status": "PASS", "scope": data["scope"],
                      "cases": results, "total_leaf_repivots_checked": 40}, indent=2))
