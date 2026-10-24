#!/usr/bin/env python3
"""Independent validator and query interface for PARAMETER_ADMISSION_MATRIX.json.

This file intentionally does not import any certificate generator. It rebuilds
source metadata, the range partition, and every explicit parameter row from
the frozen theorem-admission policy. It distinguishes source applicability from
assumption discharge and never promotes EG617(r).
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
SCHEMA = "eg617-parameter-admission-matrix-v1"
REPO = "Icarus-K-Laplace/EG617-r12-proof"
BRANCH = "workstream/general-r-finite-tail-20261024"
EXPECTED_BASE_HEAD = "3d27693d9f9d5bf2586e0f0178228563d96de22b"

SOURCE_REGISTRY = [
    {
        "source_id": "RC_Q_CEILING",
        "theorem_statement": "For every integer r>=12, assuming a legal 4r+1 residual F with the inherited hereditary cap, a degree-(r+1) pivot, and the residual-core contract, e(F)<=2r^2+4r+4, q<=3r+2, and each regular repivot of missing degree d satisfies q_y>=d(r+1-d).",
        "parameter_applicability": {"min_r": 12, "max_r": None},
        "proof_type": "PROVED_SYMBOLIC_CONDITIONAL_ON_RC",
        "assumption_ids": ["RC"],
        "terminal_contract": "legal 4r+1 residual plus complete residual-core contract; does not prove global extraction",
        "source_branch": "workstream/general-r-architecture-20261024",
        "source_commit": "a922c4d7646eb8d0087bde8547562c8aace02ee2",
        "source_path": "general_r/GENERAL_R_Q_CEILING_AND_MISSING_DEGREES.md",
        "source_blob_sha": "85d6ef9d4bf283a35f842fc1e1bf0993f26097b8",
        "theorem_status": "CONDITIONAL"
    },
    {
        "source_id": "RC_FROM_EXTRACTED_RESIDUAL",
        "theorem_statement": "For every integer r>=17, if an induced 4r+1 residual F satisfies alpha(F)<=4, omega(F)<=r-1, and the inherited least-colour cap, then delta(F)=r+1 and a degree-(r+1) pivot yields a core H on 3r-1 vertices with alpha(H)<=3, omega(H)<=r-1, delta(H)>=r.",
        "parameter_applicability": {"min_r": 17, "max_r": None},
        "proof_type": "PROVED_ANALYTIC_CONDITIONAL_ON_RESIDUAL_EXTRACTION",
        "assumption_ids": ["EXTRACTED_4R_PLUS_1_RESIDUAL"],
        "terminal_contract": "an induced 4r+1 residual already exists; extraction/stopping from the original counterexample remains OPEN",
        "source_branch": "workstream/general-r-residual-core-extraction-20261024",
        "source_commit": "614a956a7e964f42c0818eca05e3ca9e26a6458a",
        "source_path": "general_r/workstreams/residual-core-extraction-chat-20261024/RESIDUAL_BRANCH_CLOSURE.md",
        "source_blob_sha": "0cf72df5a7e0e59649713adbec1f41c2b75e7408",
        "theorem_status": "CONDITIONAL_ON_EXTRACTION"
    },
    {
        "source_id": "ANCHOR_K8_NEAR",
        "theorem_statement": "In the broad near-anchor context recorded by the asymptotic synthesis, the anchor-excess floor K_r>=8 is proved analytically for every integer r>=68; it must not be downcast to 12<=r<68.",
        "parameter_applicability": {"min_r": 68, "max_r": None},
        "proof_type": "PROVED_ANALYTIC_FOR_STATED_NEAR_ANCHOR_CONTEXT",
        "assumption_ids": ["RC", "NEAR_ANCHOR_TERMINAL_CONTRACT"],
        "terminal_contract": "broad near-anchor contract of the asymptotic synthesis; not interchangeable with the exact-three-independent-degree-r-anchor theorem",
        "source_branch": "workstream/general-r-asymptotic-20261024",
        "source_commit": "aa7fbbda16ff0170c9bf7c440ca961a7a8aab3c0",
        "source_path": "general_r/workstreams/asymptotic-chat-20261024/CANONICAL_STATE.md",
        "source_blob_sha": "f4b8741a8d6c78044a81dccee229d2c5e4eb0ea8",
        "theorem_status": "PROVED_ANALYTIC_FOR_R_GE_68"
    },
    {
        "source_id": "EXACT_THREE_ANCHOR_K8",
        "theorem_statement": "For every integer r>=12, if H has 3r-1 vertices, alpha(H)<=3, omega(H)<=r-1, delta(H)>=r, and contains three pairwise nonadjacent vertices of degree exactly r, then K=2e(H)-r(3r-1)>=8.",
        "parameter_applicability": {"min_r": 12, "max_r": None},
        "proof_type": "INDEPENDENTLY_VERIFIED_ANALYTIC_AUDIT",
        "assumption_ids": ["CORE_CONTRACT", "THREE_PAIRWISE_NONADJACENT_DEGREE_R_ANCHORS"],
        "terminal_contract": "exact three-anchor configuration only; does not by itself establish the broader near-anchor K8 hypothesis when the three-anchor premise is absent",
        "source_branch": "workstream/general-r-three-anchor-20261024",
        "source_commit": "a934c3ccc22b6991cca5ba82f49ac9f3400748f0",
        "source_path": "general_r/workstreams/three-anchor-chat-20261024/PUBLICATION_VERSION.md",
        "source_blob_sha": "ef1e93744dc14b7f3fdb474df8e0c98590676806",
        "theorem_status": "PROVED_FOR_EXACT_ANCHOR_HYPOTHESES"
    },
    {
        "source_id": "D1_SHELL_CLASS_BOUND",
        "theorem_statement": "Under hypotheses A+B and every integer r>=12, each distinct d1 missing-partner shell class contributes at least r incidences while the total shell incidence is at most 6r-2; hence the number N of distinct d1 shell classes satisfies N<=5.",
        "parameter_applicability": {"min_r": 12, "max_r": None},
        "proof_type": "CONDITIONAL_ANALYTIC_LEMMA_PLUS_EXACT_INTEGER_CERTIFICATE",
        "assumption_ids": ["RC", "ANCHOR_K8"],
        "terminal_contract": "d1 shell-class count only; does not bound owner multiplicity within a class and does not close d1 nonextension",
        "source_branch": "workstream/general-r-repivot-termination-20261024",
        "source_commit": "35fec3eaaab70b31e10b41065634b35b02a28e6",
        "source_path": "general_r/workstreams/repivot-termination-chat-20261024/ENDPOINT_CLASSIFICATION.md",
        "source_blob_sha": "7665a0dafec0e163f47255cdd5efc92d6e9e71f7",
        "theorem_status": "CONDITIONAL_ON_RC_AND_ANCHOR_K8"
    },
    {
        "source_id": "R12_FRONTEND_REC",
        "theorem_statement": "At r=12, the finite contextual recurrence arithmetic has a replayed certificate (1752 nodes and 144 outer comparisons), but the bridge from the recurrence contract to the original graph problem remains OPEN.",
        "parameter_applicability": {"min_r": 12, "max_r": 12},
        "proof_type": "COMPUTATION_CERTIFIED_ARITHMETIC_ONLY",
        "assumption_ids": ["R12_CONTEXTUAL_RECURRENCE_BRIDGE"],
        "terminal_contract": "fixed-r=12 recurrence arithmetic only; not graph nonexistence and not EG617(12)",
        "source_branch": "workstream/general-r-architecture-20261024",
        "source_commit": "a922c4d7646eb8d0087bde8547562c8aace02ee2",
        "source_path": "certificates/frontend_line_a_v1/VERIFICATION_RECEIPT.json",
        "source_blob_sha": "2b414301e2db36031b707dc1c0d5f546c02b89da",
        "theorem_status": "ARITHMETIC_CERTIFIED_BRIDGE_OPEN"
    }
]

RANGES = [
    {"range_id": "R4_TO_R11", "min_r": 4, "max_r": 11, "meaning": "No certified general-r residual-core reduction source applies; module use is schema-only unless a parameter-specific reduction is attached."},
    {"range_id": "R12_TO_R16", "min_r": 12, "max_r": 16, "meaning": "Conditional q-ceiling/backend source applies under RC; no extracted-residual theorem source for the complete core contract; broad near-anchor K8 remains open below 68."},
    {"range_id": "R17_TO_R67", "min_r": 17, "max_r": 67, "meaning": "Core contract follows analytically once a legal 4r+1 residual has been extracted; global extraction remains open; broad near-anchor K8 remains open."},
    {"range_id": "R68_PLUS", "min_r": 68, "max_r": None, "meaning": "Broad near-anchor K8 source applies, but RC/front extraction and endpoint/design terminal closure remain open; no unconditional all-large-r theorem."}
]

MODULE_REGISTRY = [
    {"module_id": "ENDPOINT_DOMAIN_LOWER_BOUND_V1", "generator": "generate_endpoint_domain.py", "generator_version": "endpoint-domain-generator-v1.0.0", "verifier": "verify_endpoint_domain.py", "profiles": ["residual-core", "near-anchor"], "source_ids": ["RC_Q_CEILING", "ANCHOR_K8_NEAR"], "scope": "necessary missing-degree scalar domain only"},
    {"module_id": "D1_SHELL_CLASS_BOUND_V1", "generator": "generate_d1_shell_bound.py", "generator_version": "d1-shell-bound-generator-v1.0.0", "verifier": "verify_d1_shell_bound.py", "profiles": ["not-applicable"], "source_ids": ["D1_SHELL_CLASS_BOUND"], "scope": "conditional d1 shell-class count N<=5 only"}
]


def expected_row(r: int) -> dict[str, Any]:
    if type(r) is not int or r < 4:
        raise ValueError("r must be an integer >= 4")
    supported = r >= 12
    extracted_core = r >= 17
    broad_anchor = r >= 68
    medium = [d for d in range(4, r - 2) if d * (r + 1 - d) <= 3 * r + 2] if supported else []
    baseline = {
        "q_cap_formula": "3*r+2",
        "medium_degree_interval": [4, r - 3] if supported else None,
        "medium_degree_candidates_under_necessary_inequality": medium,
        "interpretation": "conditional scalar necessary-domain only; not a graph-level exclusion beyond the stated inequality"
    }
    anchor = {
        "q_cap_formula": "3*r-1",
        "degree_4_and_symmetric_partner_excluded_if_assumptions_hold": supported,
        "required_assumptions": ["RC", "ANCHOR_K8"],
        "broad_anchor_k8_source_applies": broad_anchor,
        "broad_anchor_k8_assumption_state": "PROVED_ANALYTIC_FOR_R_GE_68" if broad_anchor else "OPEN",
        "exact_three_anchor_specialized_theorem_applies": supported,
        "exact_three_anchor_specialized_theorem_scope": "only when three pairwise nonadjacent degree-r anchors are established"
    }

    def module_status(ids: list[str]) -> dict[str, Any]:
        return {
            "source_applicable": supported,
            "admission_status": "CONDITIONAL" if supported else "BLOCKED_SOURCE_REDUCTION_NOT_APPLICABLE",
            "required_assumption_ids": ids,
            "assumption_states": {
                assumption_id: (
                    "PROVED_ANALYTIC_FOR_R_GE_68" if assumption_id == "ANCHOR_K8" and broad_anchor
                    else "OPEN"
                )
                for assumption_id in ids
            },
            "eg617_promotion_status": "OPEN",
            "reason": "general residual-core source is stated for r>=12; no parameter-specific reduction is registered for r<12" if not supported else "module implication may be certified conditionally, but this does not discharge the listed assumptions or prove EG617(r)"
        }

    return {
        "r": r,
        "source_admission": {
            "general_rc_q_ceiling": "APPLICABLE_CONDITIONAL_ON_RC" if supported else "BLOCKED_SOURCE_REDUCTION_NOT_APPLICABLE",
            "core_contract_given_extracted_residual": "PROVED_ANALYTIC_CONDITIONAL_ON_EXTRACTION" if extracted_core else "NO_APPLICABLE_SOURCE_BELOW_R17",
            "global_residual_extraction": "OPEN",
            "broad_near_anchor_k8": "PROVED_ANALYTIC_SOURCE_APPLIES" if broad_anchor else "OPEN_FOR_THIS_PARAMETER",
            "exact_three_anchor_k8": "PROVED_FOR_EXACT_ANCHOR_HYPOTHESES" if supported else "NO_APPLICABLE_SOURCE_BELOW_R12",
            "asymptotic_r0": "NOT_AVAILABLE",
            "fixed_r12_recurrence": "COMPUTATION_CERTIFIED_ARITHMETIC_ONLY_BRIDGE_OPEN" if r == 12 else "NOT_APPLICABLE"
        },
        "module_admission": {
            "ENDPOINT_DOMAIN_LOWER_BOUND_V1": {
                "residual-core": module_status(["RC"]),
                "near-anchor": module_status(["RC", "ANCHOR_K8"])
            },
            "D1_SHELL_CLASS_BOUND_V1": module_status(["RC", "ANCHOR_K8"])
        },
        "scalar_boundary_audit": {
            "baseline_profile": baseline,
            "near_anchor_profile": anchor,
            "candidate_domain_note": "no theorem-level domain admitted" if r < 12 else ("baseline profile excludes all d in [4,r-3] under q<=3r+2" if r >= 15 else "baseline profile leaves only the boundary candidates d=4 and d=r-3 within [4,r-3]"),
            "theorem_level_warning": "scalar candidate-domain simplification is conditional on the selected q ceiling and is not a proof that surviving states are realizable or that the original graph problem is solved"
        },
        "global_status": {
            "asymptotic_r0": "NOT_AVAILABLE",
            "eg617_r_status": "OPEN",
            "full_finite_tail_admitted": False
        }
    }


def canonical_json(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("ascii")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def verify_matrix(matrix_path: Path) -> dict[str, Any]:
    raw = matrix_path.read_bytes()
    matrix = json.loads(raw.decode("utf-8"))
    if matrix.get("schema") != SCHEMA:
        raise AssertionError("unknown matrix schema")
    if matrix.get("repository") != REPO or matrix.get("branch") != BRANCH:
        raise AssertionError("repository/branch identity mismatch")
    if matrix.get("expected_base_head") != EXPECTED_BASE_HEAD:
        raise AssertionError("unexpected expected-base-head metadata")
    if matrix.get("domain") != {"min_r": 4, "max_r": None, "integer_only": True}:
        raise AssertionError("parameter domain mismatch")
    if matrix.get("source_registry") != SOURCE_REGISTRY:
        raise AssertionError("source registry differs from frozen theorem provenance")
    if matrix.get("range_partition") != RANGES:
        raise AssertionError("range partition mismatch")
    if matrix.get("module_registry") != MODULE_REGISTRY:
        raise AssertionError("module registry mismatch")
    explicit = matrix.get("explicit_rows", {})
    if explicit.get("min_r") != 4 or explicit.get("max_r") != 100 or explicit.get("count") != 97:
        raise AssertionError("explicit-row coverage metadata mismatch")
    rows = explicit.get("rows")
    if not isinstance(rows, list) or len(rows) != 97:
        raise AssertionError("matrix must contain all explicit rows r=4,...,100")
    for expected_r, row in zip(range(4, 101), rows):
        if row != expected_row(expected_r):
            raise AssertionError(f"row mismatch at r={expected_r}")
    if matrix.get("admission_policy") != {
        "blocked_status": "BLOCKED_SOURCE_REDUCTION_NOT_APPLICABLE",
        "conditional_status": "CONDITIONAL",
        "no_unconditional_eg617_promotion": True,
        "rc_global_status": "OPEN",
        "anchor_k8_broad_status_by_range": [
            {"min_r": 12, "max_r": 67, "status": "OPEN"},
            {"min_r": 68, "max_r": None, "status": "PROVED_ANALYTIC_FOR_R_GE_68"}
        ],
        "exact_three_anchor_theorem_not_substitutable_for_broad_anchor_k8": True,
        "asymptotic_r0": "NOT_AVAILABLE"
    }:
        raise AssertionError("admission policy mismatch")
    return {
        "status": "PASS",
        "schema": SCHEMA,
        "explicit_rows_checked": 97,
        "range_partition_checked": len(RANGES),
        "source_records_checked": len(SOURCE_REGISTRY),
        "matrix_sha256": sha256_bytes(raw),
        "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "global_eg617_promotion": "BLOCKED",
        "asymptotic_r0": "NOT_AVAILABLE"
    }


def query_admission(r: int, module_id: str, profile: str | None) -> dict[str, Any]:
    row = expected_row(r)
    if module_id == "ENDPOINT_DOMAIN_LOWER_BOUND_V1":
        if profile not in ("residual-core", "near-anchor"):
            raise ValueError("endpoint-domain module requires profile residual-core or near-anchor")
        result = row["module_admission"][module_id][profile]
    elif module_id == "D1_SHELL_CLASS_BOUND_V1":
        if profile not in (None, "not-applicable"):
            raise ValueError("D1 shell-bound module has no profile")
        result = row["module_admission"][module_id]
    else:
        raise ValueError(f"unknown module ID: {module_id}")
    return {
        "r": r,
        "module_id": module_id,
        "profile": profile or "not-applicable",
        **result,
        "source_ids": (
            ["RC_Q_CEILING"] if module_id == "ENDPOINT_DOMAIN_LOWER_BOUND_V1" and profile == "residual-core"
            else ["RC_Q_CEILING", "ANCHOR_K8_NEAR"] if module_id == "ENDPOINT_DOMAIN_LOWER_BOUND_V1"
            else ["D1_SHELL_CLASS_BOUND"]
        ),
        "eg617_r_proved": False
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("matrix", nargs="?", type=Path, default=ROOT / "PARAMETER_ADMISSION_MATRIX.json")
    parser.add_argument("--query-r", type=int)
    parser.add_argument("--module", choices=["ENDPOINT_DOMAIN_LOWER_BOUND_V1", "D1_SHELL_CLASS_BOUND_V1"])
    parser.add_argument("--profile", choices=["residual-core", "near-anchor", "not-applicable"])
    parser.add_argument("--audit-range", nargs=2, type=int, metavar=("START", "END"))
    args = parser.parse_args()
    audit = verify_matrix(args.matrix)
    if args.audit_range:
        start, end = args.audit_range
        if start < 4 or end < start:
            raise ValueError("invalid audit range")
        for r in range(start, end + 1):
            expected_row(r)
        audit["query_range_audited"] = [start, end]
        audit["query_rows_recomputed"] = end - start + 1
    if args.query_r is not None:
        if args.module is None:
            raise ValueError("--module is required with --query-r")
        query = query_admission(args.query_r, args.module, args.profile)
        audit["query"] = query
    print(json.dumps(audit, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
