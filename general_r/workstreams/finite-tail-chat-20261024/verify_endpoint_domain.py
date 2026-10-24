#!/usr/bin/env python3
"""Independent verifier for endpoint-domain certificates.

This file intentionally does not import the producer. It independently rebuilds
the exact integer rows, reflection classes, hashes, and theorem scope.
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


def expected_reflection_classes(candidates: list[int], r: int) -> list[dict]:
    remaining = set(candidates)
    result = []
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
            if partner not in candidates:
                raise AssertionError("reflection does not preserve necessary-bound domain")
            members = [d]
            rule = "partner_already_accounted"
        remaining.difference_update(members)
        result.append({"representative": min(members), "members": members, "rule": rule})
    return result


def independently_derive_body(r: int, profile: str) -> dict:
    if type(r) is not int or r < 4:
        raise AssertionError("invalid r")
    if profile not in PROFILES:
        raise AssertionError("unknown profile")

    q_cap = 3 * r + 2 if profile == "residual-core" else 3 * r - 1
    assumptions = ["RC"] if profile == "residual-core" else ["RC", "ANCHOR_K8"]
    sources = [RC_SOURCE] if profile == "residual-core" else [RC_SOURCE, ANCHOR_SOURCE]
    candidates = []
    rows = []
    for d in range(0, r + 1):
        value = d * (r + 1 - d)
        allowed = value <= q_cap
        if allowed:
            candidates.append(d)
        rows.append({
            "d": d,
            "partner": r + 1 - d,
            "lower_bound": value,
            "q_cap": q_cap,
            "slack": q_cap - value,
            "admissible_by_necessary_bound": allowed,
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
        "sources": sources,
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
        "reflection_classes": expected_reflection_classes(candidates, r),
        "completeness_claim": "one exact-integer row for every d in {0,...,r}, in ascending order",
        "scope_warning": (
            "The scalar reflection quotient only groups d-values paired by d<->r+1-d "
            "when both are in the legal domain. It does not certify graph-level symmetry."
        ),
    }
    return {"instance": instance, "certificate": certificate}


def verify(path: Path) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    if set(obj) != {"body", "instance_sha256", "certificate_sha256"}:
        raise AssertionError("unexpected certificate envelope fields")
    body = obj["body"]
    instance = body["instance"]
    r = instance["r"]
    profile = instance["profile"]
    expected = independently_derive_body(r, profile)
    if body != expected:
        raise AssertionError("certificate body differs from independent exact derivation")
    if obj["instance_sha256"] != sha256(instance):
        raise AssertionError("instance SHA256 mismatch")
    if obj["certificate_sha256"] != sha256(body):
        raise AssertionError("certificate SHA256 mismatch")

    rows = body["certificate"]["domain_rows"]
    if len(rows) != r + 1 or [row["d"] for row in rows] != list(range(r + 1)):
        raise AssertionError("domain rows are not complete and ordered")
    verifier_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return {
        "status": "PASS",
        "module_id": instance["module_id"],
        "r": r,
        "profile": profile,
        "instance_sha256": obj["instance_sha256"],
        "certificate_sha256": obj["certificate_sha256"],
        "verifier_sha256": verifier_sha,
        "rows_checked": len(rows),
        "candidate_missing_degrees": body["certificate"]["candidate_missing_degrees"],
        "reflection_classes_checked": len(body["certificate"]["reflection_classes"]),
        "conditional_module_applicable": r >= 12,
        "eg617_r_proved": False,
        "warning": "PASS certifies the exact necessary scalar domain under listed assumptions only",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()
    print(json.dumps(verify(args.certificate), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
