#!/usr/bin/env python3
"""Deterministic finite-tail instance generator for EG617 general-r.

This generator deliberately certifies only a reduced scalar CSP obtained after
explicit analytic assumptions.  It is NOT a colouring-existence certificate.
All arithmetic is integer arithmetic and the JSON payload is canonically hashed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

SCHEMA = "eg617-finite-tail-csp-v1"
PROFILES = ("residual-core", "near-anchor")


def canonical_bytes(obj: object) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("ascii")


def generate_instance(r: int, profile: str = "residual-core") -> dict:
    if not isinstance(r, int) or isinstance(r, bool) or r < 4:
        raise ValueError("r must be an integer >= 4")
    if profile not in PROFILES:
        raise ValueError(f"profile must be one of {PROFILES}")

    q_cap = 3 * r + 2 if profile == "residual-core" else 3 * r - 1
    assumption_ids = ["RC"]
    if profile == "near-anchor":
        assumption_ids.append("ANCHOR_K8")

    candidates = []
    for d in range(r + 1):
        base = d * (r + 1 - d)
        if base <= q_cap:
            partner = r + 1 - d
            orbit = sorted({x for x in (d, partner) if 0 <= x <= r})
            candidates.append(
                {
                    "d": d,
                    "repivot_base": base,
                    "orbit": orbit,
                    "orbit_rep": min(orbit),
                }
            )

    payload = {
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
        "candidate_missing_degrees": [row["d"] for row in candidates],
        "symmetry": {
            "implemented": [
                "endpoint reflection d <-> r+1-d when both values lie in [0,r]"
            ],
            "orbit_representatives": sorted({row["orbit_rep"] for row in candidates}),
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
    return {
        "payload": payload,
        "payload_sha256": hashlib.sha256(canonical_bytes(payload)).hexdigest(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("r", type=int)
    parser.add_argument("--profile", choices=PROFILES, default="residual-core")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    instance = generate_instance(args.r, args.profile)
    text = json.dumps(instance, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
