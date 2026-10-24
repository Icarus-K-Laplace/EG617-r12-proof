#!/usr/bin/env python3
"""Independent verifier for D1_SHELL_CLASS_BOUND_V1.

Does not import the producer. It rebuilds the exact incidence-cap rows and
checks that the arithmetic certificate proves the conditional N<=5 implication.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

SCHEMA = "eg617-d1-shell-bound-certificate-v1"
SOURCE = {
    "branch": "workstream/general-r-repivot-termination-20261024",
    "commit": "35fec3eaaab70b31e10b41065634b35b02a28e6c",
    "path": "general_r/workstreams/repivot-termination-chat-20261024/ENDPOINT_CLASSIFICATION.md",
    "theorem": "Under A+B and r>=12, every d1 missing partner has t_s>=r and sum_A t_s<=6r-2; therefore at most five d1 shell classes exist",
    "applicability": "conditional on hypotheses A+B; r>=12",
}


def canonical_bytes(obj: object) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("ascii")


def sha256(obj: object) -> str:
    return hashlib.sha256(canonical_bytes(obj)).hexdigest()


def derive(r: int) -> dict:
    if type(r) is not int or r < 4:
        raise AssertionError("invalid r")
    cap = 6 * r - 2
    rows = []
    for n in range(0, 7):
        minimum = n * r
        rows.append({
            "class_count": n,
            "minimum_total_incidence": minimum,
            "incidence_cap": cap,
            "slack": cap - minimum,
            "feasible_under_budget": minimum <= cap,
        })
    instance = {
        "schema": SCHEMA,
        "module_id": "D1_SHELL_CLASS_BOUND_V1",
        "module_kind": "endpoint-shell-class-capacity",
        "constraint_generation_version": "d1-shell-bound-generator-v1.0.0",
        "r": r,
        "statement": (
            "Assuming the conditional shell-incidence lemmas from the cited endpoint theorem, "
            "each distinct d1 missing-partner shell vertex contributes at least r to the incidence "
            "sum, while the total is at most 6r-2. Therefore N*r<=6r-2 and N<=5 for r>=12."
        ),
        "assumption_ids": ["RC", "ANCHOR_K8"],
        "sources": [SOURCE],
        "parameter_applicability": {"minimum_r": 12},
        "variable_map": [
            {"name": "N", "type": "integer", "meaning": "number of distinct d1 shell classes"},
            {"name": "r", "type": "integer", "meaning": "EG617 parameter"},
            {"name": "t_s", "type": "integer", "meaning": "shell incidence of a d1 missing-partner vertex"},
        ],
        "constraints": [
            {"id": "D1_PARTNER_FLOOR", "formula": "t_s >= r for each distinct d1 shell class"},
            {"id": "SHELL_INCIDENCE_BUDGET", "formula": "sum_A t_s <= 6*r-2"},
            {"id": "COUNTING", "formula": "N*r <= sum_A t_s <= 6*r-2"},
            {"id": "INTEGER_CAP", "formula": "N <= floor((6*r-2)/r) = 5 for r>=12"},
        ],
        "arithmetic": {"kind": "exact_integer", "rounding": "none"},
        "promotion_policy": {
            "conditional_module_may_be_certified": r >= 12,
            "eg617_r_promoted_by_this_module": False,
            "reason": "this proves a shell-class count bound only; bounded-allowance d1 nonextension remains open",
        },
    }
    cert = {
        "class_count_rows": rows,
        "maximum_feasible_class_count": 5,
        "first_impossible_class_count": 6,
        "exact_contradiction_at_six": {
            "required": 6 * r,
            "cap": cap,
            "gap": 6 * r - cap,
            "identity": "6*r-(6*r-2)=2",
        },
        "completeness_claim": "all candidate class counts N=0,...,6 are checked; every N>=7 is also impossible because N*r is increasing",
        "scope_warning": "The arithmetic certificate verifies the counting consequence of the cited conditional shell lemmas; it does not independently prove those graph-theoretic lemmas or close the d1 terminal.",
    }
    return {"instance": instance, "certificate": cert}


def verify(path: Path) -> dict:
    envelope = json.loads(path.read_text(encoding="utf-8"))
    if set(envelope) != {"body", "instance_sha256", "certificate_sha256"}:
        raise AssertionError("invalid certificate envelope")
    body = envelope["body"]
    instance = body["instance"]
    r = instance["r"]
    expected = derive(r)
    if body != expected:
        raise AssertionError("certificate body differs from independent exact derivation")
    if envelope["instance_sha256"] != sha256(instance):
        raise AssertionError("instance SHA256 mismatch")
    if envelope["certificate_sha256"] != sha256(body):
        raise AssertionError("certificate SHA256 mismatch")
    if r >= 12 and body["certificate"]["maximum_feasible_class_count"] != 5:
        raise AssertionError("expected N<=5 for r>=12")
    verifier_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return {
        "status": "PASS",
        "module_id": instance["module_id"],
        "r": r,
        "instance_sha256": envelope["instance_sha256"],
        "certificate_sha256": envelope["certificate_sha256"],
        "verifier_sha256": verifier_sha,
        "rows_checked": len(body["certificate"]["class_count_rows"]),
        "maximum_feasible_class_count": body["certificate"]["maximum_feasible_class_count"],
        "first_impossible_class_count": body["certificate"]["first_impossible_class_count"],
        "conditional_module_applicable": r >= 12,
        "eg617_r_proved": False,
        "warning": "PASS verifies the exact arithmetic consequence under the cited conditional shell lemmas; it does not independently prove those lemmas",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()
    print(json.dumps(verify(args.certificate), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
