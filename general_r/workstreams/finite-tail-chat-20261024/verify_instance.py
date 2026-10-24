#!/usr/bin/env python3
"""Independent verifier for eg617-finite-tail-csp-v1 instances.

Intentionally does not import generate_instance.py.  It re-derives every field
from (r, profile), checks canonical symmetry representatives, and checks SHA256.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

SCHEMA = "eg617-finite-tail-csp-v1"


def canonical_bytes(obj: object) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("ascii")


def expected_payload(r: int, profile: str) -> dict:
    if r < 4:
        raise AssertionError("r < 4")
    if profile not in ("residual-core", "near-anchor"):
        raise AssertionError("unknown profile")

    q_cap = 3 * r + 2 if profile == "residual-core" else 3 * r - 1
    assumption_ids = ["RC"] + (["ANCHOR_K8"] if profile == "near-anchor" else [])
    degrees = []
    reps = set()
    for d in range(r + 1):
        if d * (r + 1 - d) <= q_cap:
            degrees.append(d)
            partner = r + 1 - d
            orbit = [x for x in (d, partner) if 0 <= x <= r]
            reps.add(min(orbit))

    return {
        "schema": SCHEMA,
        "problem": "Erdos-617 finite-tail reduced backend",
        "r": r,
        "profile": profile,
        "theorem_scope": "conditional reduced scalar CSP; not a colouring-existence certificate",
        "parameters": {
            "global_order": r * r + 1,
            "residual_order": 4 * r + 1,
            "design_terminal_order": 5 * r + 1,
            "pivot_degree": r + 1,
            "core_order": 3 * r - 1,
            "core_min_degree": r,
            "core_alpha_max": 3,
            "core_omega_max": r - 1,
            "residual_edge_cap": 2 * r * r + 4 * r + 4,
            "core_edge_floor": (r * (3 * r - 1) + 2) // 2,
            "q_cap": q_cap,
        },
        "assumption_ids": assumption_ids,
        "constraints": [
            "0 <= d <= r",
            "q >= d*(r+1-d)",
            f"q <= {q_cap}",
        ],
        "candidate_missing_degrees": degrees,
        "symmetry": {
            "implemented": [
                "endpoint reflection d <-> r+1-d when both values lie in [0,r]"
            ],
            "orbit_representatives": sorted(reps),
            "reserved": [
                "color permutation",
                "vertex permutation",
                "canonical labeling",
                "stabilizer refinement",
            ],
        },
        "status": {
            "generator_supported": True,
            "general_reduction_source_supported": r >= 12,
            "eg617_r_certified_by_this_instance": False,
        },
    }


def verify(path: Path) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    payload = obj["payload"]
    if payload.get("schema") != SCHEMA:
        raise AssertionError("schema mismatch")
    r = payload["r"]
    profile = payload["profile"]
    expected = expected_payload(r, profile)
    if payload != expected:
        raise AssertionError("payload differs from independent re-derivation")
    digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
    if digest != obj.get("payload_sha256"):
        raise AssertionError("SHA256 mismatch")
    return {
        "status": "PASS",
        "r": r,
        "profile": profile,
        "payload_sha256": digest,
        "candidate_degrees": len(payload["candidate_missing_degrees"]),
        "orbit_representatives": len(payload["symmetry"]["orbit_representatives"]),
        "warning": "PASS certifies this reduced CSP encoding only, not EG617(r)",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("instance", type=Path)
    args = parser.parse_args()
    print(json.dumps(verify(args.instance), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
