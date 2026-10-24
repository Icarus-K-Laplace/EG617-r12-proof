#!/usr/bin/env python3
"""Independent checker for explicit colored-incidence symmetry witnesses.

The implementation exhaustively canonicalizes only small objects (at most
8 vertices and a bounded role-preserving group). It does not claim to be a
scalable canonical-labeling engine for EG617 graph instances.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
OBJECT_SCHEMA = "eg617-colored-incidence-object-v1"
WITNESS_SCHEMA = "eg617-graph-symmetry-witness-v1"
TEST_SCHEMA = "eg617-graph-symmetry-test-vectors-v1"
MAX_VERTICES = 8
MAX_ACTIONS = 200_000


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def normalize_pair(u: str, v: str) -> tuple[str, str]:
    if u == v:
        raise AssertionError("loops are not allowed")
    return (u, v) if u < v else (v, u)


def validate_object(obj: dict[str, Any]) -> None:
    if obj.get("schema") != OBJECT_SCHEMA:
        raise AssertionError("unknown colored-incidence object schema")
    vertices = obj.get("vertices")
    colors = obj.get("colors")
    if not isinstance(vertices, list) or len(vertices) != len(set(vertices)) or not all(isinstance(v, str) for v in vertices):
        raise AssertionError("vertices must be a unique string list")
    if not isinstance(colors, list) or not colors or len(colors) != len(set(colors)) or not all(isinstance(c, str) for c in colors):
        raise AssertionError("colors must be a nonempty unique string list")
    if len(vertices) > MAX_VERTICES:
        raise AssertionError(f"exhaustive witness checker is limited to {MAX_VERTICES} vertices")
    role_partition = obj.get("role_partition")
    color_partition = obj.get("color_partition")
    if not isinstance(role_partition, dict) or set(role_partition) != set(vertices):
        raise AssertionError("role_partition must assign every vertex exactly one role")
    if not all(isinstance(x, str) and x for x in role_partition.values()):
        raise AssertionError("role names must be nonempty strings")
    if not isinstance(color_partition, dict) or set(color_partition) != set(colors):
        raise AssertionError("color_partition must assign every color exactly one class")
    if not all(isinstance(x, str) and x for x in color_partition.values()):
        raise AssertionError("color-class names must be nonempty strings")
    edges = obj.get("edges")
    if not isinstance(edges, list):
        raise AssertionError("edges must be a list")
    seen = set()
    for edge in edges:
        if not isinstance(edge, dict) or set(edge) != {"u", "v", "color"}:
            raise AssertionError("each edge must contain exactly u, v, color")
        u, v, color = edge["u"], edge["v"], edge["color"]
        if u not in vertices or v not in vertices or color not in colors:
            raise AssertionError("edge endpoint or color is outside the declared universe")
        pair = normalize_pair(u, v)
        if pair in seen:
            raise AssertionError("parallel/duplicate colored edges are not allowed")
        seen.add(pair)
    constraints = obj.get("constraints")
    if not isinstance(constraints, dict) or set(constraints) != {"global", "vertex_indexed", "color_indexed"}:
        raise AssertionError("constraints must have global, vertex_indexed, color_indexed fields")
    if not isinstance(constraints["global"], list) or not all(isinstance(x, str) for x in constraints["global"]):
        raise AssertionError("global constraints must be strings")
    if not isinstance(constraints["vertex_indexed"], list) or not isinstance(constraints["color_indexed"], list):
        raise AssertionError("indexed constraints must be lists")
    for item in constraints["vertex_indexed"]:
        if not isinstance(item, dict) or item.get("vertex") not in vertices:
            raise AssertionError("vertex-indexed constraint has invalid vertex")
    for item in constraints["color_indexed"]:
        if not isinstance(item, dict) or item.get("color") not in colors:
            raise AssertionError("color-indexed constraint has invalid color")


def _permutation_products(groups: list[list[str]]):
    permutations = [list(itertools.permutations(group)) for group in groups]
    for product in itertools.product(*permutations):
        yield [x for group_order in product for x in group_order]


def canonical_encoding(obj: dict[str, Any]) -> str:
    validate_object(obj)
    vertices = obj["vertices"]
    colors = obj["colors"]
    roles = obj["role_partition"]
    color_classes = obj["color_partition"]
    role_names = sorted(set(roles.values()))
    vertex_groups = [sorted(v for v in vertices if roles[v] == role) for role in role_names]
    color_class_names = sorted(set(color_classes.values()))
    color_groups = [sorted(c for c in colors if color_classes[c] == cls) for cls in color_class_names]
    vertex_actions = math.prod(math.factorial(len(g)) for g in vertex_groups)
    color_actions = math.prod(math.factorial(len(g)) for g in color_groups)
    if vertex_actions * color_actions > MAX_ACTIONS:
        raise AssertionError("role-preserving group is too large for this exhaustive checker")
    best: str | None = None
    for ordered_vertices in _permutation_products(vertex_groups):
        vmap = {v: f"v{i}" for i, v in enumerate(ordered_vertices)}
        for ordered_colors in _permutation_products(color_groups):
            cmap = {c: f"c{i}" for i, c in enumerate(ordered_colors)}
            encoded_edges = []
            for edge in obj["edges"]:
                u, v = sorted((vmap[edge["u"]], vmap[edge["v"]]))
                encoded_edges.append({"u": u, "v": v, "color": cmap[edge["color"]]})
            encoded_edges.sort(key=canonical_json)
            encoded_vertices = [
                {"id": vmap[v], "role": roles[v]} for v in vertices
            ]
            encoded_vertices.sort(key=lambda x: x["id"])
            encoded_colors = [
                {"id": cmap[c], "class": color_classes[c]} for c in colors
            ]
            encoded_colors.sort(key=lambda x: x["id"])
            constraints = obj["constraints"]
            encoded_constraints = {
                "global": sorted(constraints["global"]),
                "vertex_indexed": [],
                "color_indexed": [],
            }
            for item in constraints["vertex_indexed"]:
                transformed = dict(item)
                transformed["vertex"] = vmap[item["vertex"]]
                encoded_constraints["vertex_indexed"].append(transformed)
            for item in constraints["color_indexed"]:
                transformed = dict(item)
                transformed["color"] = cmap[item["color"]]
                encoded_constraints["color_indexed"].append(transformed)
            encoded_constraints["vertex_indexed"].sort(key=canonical_json)
            encoded_constraints["color_indexed"].sort(key=canonical_json)
            encoding = canonical_json({
                "schema": OBJECT_SCHEMA,
                "vertices": encoded_vertices,
                "colors": encoded_colors,
                "edges": encoded_edges,
                "constraints": encoded_constraints,
            })
            if best is None or encoding < best:
                best = encoding
    if best is None:
        raise AssertionError("no canonical labeling generated")
    return best


def verify_witness(original: dict[str, Any], representative: dict[str, Any], witness: dict[str, Any]) -> dict[str, Any]:
    validate_object(original)
    validate_object(representative)
    if witness.get("schema") != WITNESS_SCHEMA:
        raise AssertionError("unknown witness schema")
    vmap = witness.get("vertex_permutation")
    cmap = witness.get("color_permutation")
    if not isinstance(vmap, dict) or set(vmap) != set(original["vertices"]) or set(vmap.values()) != set(representative["vertices"]) or len(vmap) != len(set(vmap.values())):
        raise AssertionError("vertex map is not a bijection")
    if not isinstance(cmap, dict) or set(cmap) != set(original["colors"]) or set(cmap.values()) != set(representative["colors"]) or len(cmap) != len(set(cmap.values())):
        raise AssertionError("color map is not a bijection")
    for vertex, image in vmap.items():
        if original["role_partition"][vertex] != representative["role_partition"][image]:
            raise AssertionError("vertex permutation does not preserve distinguished roles")
    for color, image in cmap.items():
        if original["color_partition"][color] != representative["color_partition"][image]:
            raise AssertionError("color permutation does not preserve color classes")

    mapped_edges = []
    for edge in original["edges"]:
        u, v = normalize_pair(vmap[edge["u"]], vmap[edge["v"]])
        mapped_edges.append({"u": u, "v": v, "color": cmap[edge["color"]]})
    mapped_edges.sort(key=canonical_json)
    target_edges = [dict(e) for e in representative["edges"]]
    target_edges.sort(key=canonical_json)
    if mapped_edges != target_edges:
        raise AssertionError("mapped colored incidences do not equal representative edges")

    def map_constraints(obj: dict[str, Any]) -> dict[str, Any]:
        source = obj["constraints"]
        return {
            "global": sorted(source["global"]),
            "vertex_indexed": sorted(
                [dict(item, vertex=vmap[item["vertex"]]) for item in source["vertex_indexed"]],
                key=canonical_json,
            ),
            "color_indexed": sorted(
                [dict(item, color=cmap[item["color"]]) for item in source["color_indexed"]],
                key=canonical_json,
            ),
        }

    if map_constraints(original) != {
        "global": sorted(representative["constraints"]["global"]),
        "vertex_indexed": sorted(representative["constraints"]["vertex_indexed"], key=canonical_json),
        "color_indexed": sorted(representative["constraints"]["color_indexed"], key=canonical_json),
    }:
        raise AssertionError("constraints are not preserved by the supplied action")

    original_code = canonical_encoding(original)
    representative_code = canonical_encoding(representative)
    if original_code != representative_code:
        raise AssertionError("objects are not in the same role-preserving colored-incidence orbit")
    if witness.get("original_canonical_encoding") != original_code:
        raise AssertionError("original canonical encoding field mismatch")
    if witness.get("representative_canonical_encoding") != representative_code:
        raise AssertionError("representative canonical encoding field mismatch")
    return {
        "status": "PASS",
        "original_canonical_encoding": original_code,
        "representative_canonical_encoding": representative_code,
        "vertex_bijection_checked": len(vmap),
        "color_bijection_checked": len(cmap),
        "roles_preserved": True,
        "constraints_preserved": True,
    }


def build_state(spec: dict[str, Any], assignment: tuple[str, ...]) -> dict[str, Any]:
    edges = []
    for pair, color in zip(spec["edge_pairs"], assignment):
        u, v = normalize_pair(pair[0], pair[1])
        edges.append({"u": u, "v": v, "color": color})
    edges.sort(key=canonical_json)
    return {
        "schema": OBJECT_SCHEMA,
        "vertices": list(spec["vertices"]),
        "colors": list(spec["colors"]),
        "role_partition": dict(spec["role_partition"]),
        "color_partition": dict(spec["color_partition"]),
        "edges": edges,
        "constraints": json.loads(json.dumps(spec["constraints"])),
    }


def verify_test_vectors(path: Path) -> dict[str, Any]:
    vectors = json.loads(path.read_text(encoding="utf-8"))
    if vectors.get("schema") != TEST_SCHEMA:
        raise AssertionError("unknown test-vector schema")
    spec = vectors["state_space_spec"]
    vertices = spec["vertices"]
    colors = spec["colors"]
    edge_pairs = spec["edge_pairs"]
    if len(vertices) > MAX_VERTICES or len(colors) ** len(edge_pairs) > 10_000:
        raise AssertionError("test vector exceeds bounded exhaustive enumeration limits")
    assignments = list(itertools.product(colors, repeat=len(edge_pairs)))
    expected_states = []
    for assignment in assignments:
        state_id = "".join(str(colors.index(c)) for c in assignment)
        expected_states.append({"state_id": state_id, "object": build_state(spec, assignment)})
    states = vectors.get("states")
    if states != expected_states:
        raise AssertionError("pre-quotient state catalog is not the complete exact enumeration")
    codes = {state["state_id"]: canonical_encoding(state["object"]) for state in states}
    expected_rep_ids = {}
    for state_id, code in codes.items():
        expected_rep_ids.setdefault(code, state_id)
        if state_id < expected_rep_ids[code]:
            expected_rep_ids[code] = state_id
    representatives = vectors.get("representatives")
    expected_ids = sorted(expected_rep_ids.values())
    if [item.get("representative_id") for item in representatives] != expected_ids:
        raise AssertionError("representatives are not exactly one lexicographically least state per orbit")
    rep_objects = {item["representative_id"]: item["object"] for item in representatives}
    for item in representatives:
        if item["object"] != states[int(item["representative_id"], len(colors))]["object"]:
            raise AssertionError("representative object does not match its state ID")
    rep_codes = [canonical_encoding(rep_objects[rep_id]) for rep_id in expected_ids]
    if len(rep_codes) != len(set(rep_codes)):
        raise AssertionError("two retained representatives belong to the same orbit")

    witnesses = vectors.get("witnesses")
    if not isinstance(witnesses, list) or len(witnesses) != len(states):
        raise AssertionError("one witness is required for every pre-quotient state")
    if [w.get("state_id") for w in witnesses] != [s["state_id"] for s in states]:
        raise AssertionError("witness list must cover each state exactly once in canonical order")
    for witness in witnesses:
        state_id = witness["state_id"]
        rep_id = witness["representative_id"]
        if rep_id not in rep_objects or codes[state_id] != canonical_encoding(rep_objects[rep_id]):
            raise AssertionError("witness assigns a state to the wrong orbit representative")
        verify_witness(states[int(state_id, len(colors))]["object"], rep_objects[rep_id], {
            "schema": WITNESS_SCHEMA,
            "vertex_permutation": witness["vertex_permutation"],
            "color_permutation": witness["color_permutation"],
            "original_canonical_encoding": witness["original_canonical_encoding"],
            "representative_canonical_encoding": witness["representative_canonical_encoding"],
        })

    pre_digest_payload = [{"state_id": s["state_id"], "canonical_encoding": codes[s["state_id"]]} for s in states]
    post_digest_payload = sorted(set(codes.values()))
    pre_digest = sha256_text(canonical_json(pre_digest_payload))
    post_digest = sha256_text(canonical_json(post_digest_payload))
    if vectors.get("prequotient_state_set_sha256") != pre_digest:
        raise AssertionError("pre-quotient state-set digest mismatch")
    if vectors.get("postquotient_orbit_set_sha256") != post_digest:
        raise AssertionError("post-quotient orbit-set digest mismatch")
    return {
        "status": "PASS",
        "test_id": vectors.get("test_id"),
        "prequotient_states": len(states),
        "orbit_representatives": len(representatives),
        "witnesses_checked": len(witnesses),
        "representatives_pairwise_inequivalent": True,
        "prequotient_state_set_sha256": pre_digest,
        "postquotient_orbit_set_sha256": post_digest,
        "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": "exhaustive toy colored-incidence system only; no EG617 graph-level symmetry reduction is certified"
    }


def verify_standalone_witness(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    result = verify_witness(data["original"], data["representative"], data)
    result["verifier_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", type=Path, default=ROOT / "GRAPH_SYMMETRY_TEST_VECTORS.json")
    parser.add_argument("--mode", choices=["test-vectors", "witness"], default="test-vectors")
    args = parser.parse_args()
    result = verify_test_vectors(args.input) if args.mode == "test-vectors" else verify_standalone_witness(args.input)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
