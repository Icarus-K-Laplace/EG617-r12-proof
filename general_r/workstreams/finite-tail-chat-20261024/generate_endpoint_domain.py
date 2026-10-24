#!/usr/bin/env python3
"""Generate a theorem-aware exact certificate for the missing-degree domain.

This is a conditional necessary-domain lemma, not a graph-existence proof.
It uses exact integer arithmetic and emits every d in the legal interval.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

SCHEMA = "eg617-endpoint-domain-certificate-v1"
PROFILES = ("residual-core", "near-anchor")
RC_SOURCE = {
    "branch": "workstream/general-r-architecture-20261024",
    "commit": "a922c4d7646eb8d0087bde8547562c8aace02ee2",
    "path": "general_r/GENERAL_R_Q_CEILING_AND_MISSING_DEGREES.md",
    "theorem": "RC implies q<=3r+2 and every legal maximal-q regular repivot satisfies q_y>=d(r+1-d)",
    "applicability": "the conditional residual-core interface is stated for r>=12",
}
ANCHOR_SOURCE = {
    "branch": "workstream/general-r-asymptotic-20261024",
    "commit": "cd38647f85de9827a784288e69bad7a66d1e4e3a",
    "path": "general_r/workstreams/asymptotic-chat-20261024/HYPOTHESIS_SENSITIVITY.md",
    "theorem": "ANCHOR_K8 is recorded as analytically proved for every r>=68",
    "applicability": "r>=68 only; for smaller r the anchor premise remains open in this workstream",
}


def canonical_bytes(obj: object) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("ascii")


def sha256(obj: object) -> str:
    return hashlib.sha256(canonical_bytes(obj)).hexdigest()


def reflection_classes(candidates: list[int], r: int) -> list[dict]:
    remaining = set(candidates)
    classes = []
    while remaining:
        d = min(remaining)
        partner = r + 1 - d
        if partner == d:
            members = [d]
            rule = "fixed_point"
        elif 0 <= partner <= r and partner in remaining:
            members = sorted([d, partner])
            rule = "paired_by_scalar_reflection"
        elif partner < 0 or partner > r:
            members = [d]
            rule = "unpaired_boundary_partner_outside_legal_domain"
        else:
            # If the partner is already assigned, its class has already been emitted.
            if partner not in candidates:
                raise AssertionError("reflection must preserve the necessary-bound domain")
            members = [d]
            rule = "partner_already_accounted"
        remaining.difference_update(members)
        classes.append({"representative": min(members), "members": members, "rule": rule})
    return classes


def build_body(r: int, profile: str) -> dict:
    if not isinstance(r, int) or isinstance(r, bool) or r < 4:
        raise ValueError("r must be an integer >= 4")
    if profile not in PROFILES:
        raise ValueError(f"profile must be one of {PROFILES}")

    q_cap = 3 * r + 2 if profile == "residual-core" else 3 * r - 1
    assumptions = ["RC"] + (["ANCHOR_K8"] if profile == "near-anchor" else [])
    source_list = [RC_SOURCE] + ([ANCHOR_SOURCE] if profile == "near-anchor" else [])
    candidates = [d for d in range(r + 1) if d * (r + 1 - d) <= q_cap]
    rows = []
    for d in range(r + 1):
        lower_bound = d * (r + 1 - d)
        rows.append({
            "d": d,
            "partner": r + 1 - d,
            "lower_bound": lower_bound,
            "q_cap": q_cap,
            "slack": q_cap - lower_bound,
            "admissible_by_necessary_bound": lower_bound <= q_cap,
        })

    instance = {
        "schema": SCHEMA,
        "module_id": "ENDPOINT_DOMAIN_LOWER_BOUND_V1",
        "module_kind": "necessary-domain-pruning",
        "constraint_generation_version": "endpoint-domain-generator-v1.0.0",
        "r": r,
        "profile": profile,
        "statement": (
            "Under the listed assumptions, every legal regular repivot at a maximal-q "
            "state must have integer missing degree d in [0,r] satisfying "
            "d*(r+1-d)<=q_cap. The listed admissible degrees are exactly the solutions "
            "of this necessary inequality; admissibility does not imply graph realizability."
        ),
        "assumption_ids": assumptions,
        "sources": source_list,
        "parameter_domain": {"d_min": 0, "d_max": r, "q_cap": q_cap},
        "variable_map": [
            {"name": "d", "type": "integer", "meaning": "missing degree of a legal regular repivot"},
            {"name": "q", "type": "integer", "meaning": "global maximal-q charge subject to the selected ceiling"},
        ],
        "constraints": [
            {"id": "D_RANGE", "formula": "0 <= d <= r"},
            {"id": "REPIVOT_BASE", "formula": "q >= d*(r+1-d)"},
            {"id": "Q_CAP", "formula": f"q <= {q_cap}"},
            {"id": "DERIVED_DOMAIN", "formula": f"d*(r+1-d) <= {q_cap}"},
        ],
        "arithmetic": {"kind": "exact_integer", "rounding": "none"},
        "source_scope": {
            "r_at_least_12": "conditional reduction interface only; RC/front extraction remains an external gate",
            "r_below_12": "schema/encoding only; no general RC reduction is asserted",
        },
        "promotion_policy": {
            "conditional_module_may_be_certified": r >= 12,
            "eg617_r_promoted_by_this_module": False,
            "reason": "this module proves a necessary scalar domain only, not endpoint closure or graph nonexistence",
        },
    }

    certificate = {
        "domain_rows": rows,
        "candidate_missing_degrees": candidates,
        "reflection_classes": reflection_classes(candidates, r),
        "completeness_claim": "one exact-integer row for every d in {0,...,r}, in ascending order",
        "scope_warning": (
            "The scalar reflection quotient only groups d-values paired by d<->r+1-d "
            "when both are in the legal domain. It does not certify graph-level symmetry."
        ),
    }
    body = {"instance": instance, "certificate": certificate}
    return {
        "body": body,
        "instance_sha256": sha256(instance),
        "certificate_sha256": sha256(body),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("r", type=int)
    parser.add_argument("--profile", choices=PROFILES, default="residual-core")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = build_body(args.r, args.profile)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
