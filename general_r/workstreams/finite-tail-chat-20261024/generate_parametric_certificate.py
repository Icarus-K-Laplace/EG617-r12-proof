#!/usr/bin/env python3
"""Unified parameterized certificate-family entry point.

This wrapper reuses the frozen endpoint-domain and d1 generators/verifiers.
It does not reimplement either mathematical module. Admission is checked
against the independently validated parameter matrix before generation.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MODULES = {
    "ENDPOINT_DOMAIN_LOWER_BOUND_V1": {
        "generator": ROOT / "generate_endpoint_domain.py",
        "profiles": {"residual-core", "near-anchor"},
    },
    "D1_SHELL_CLASS_BOUND_V1": {
        "generator": ROOT / "generate_d1_shell_bound.py",
        "profiles": {"not-applicable"},
    },
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--module", required=True, choices=sorted(MODULES))
    parser.add_argument("--r", required=True, type=int)
    parser.add_argument("--profile", choices=["residual-core", "near-anchor", "not-applicable"])
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--receipt", required=True, type=Path)
    args = parser.parse_args()

    if args.r < 4:
        parser.error("r must be an integer >= 4")
    module = MODULES[args.module]
    profile = args.profile or "not-applicable"
    if profile not in module["profiles"]:
        parser.error(f"profile {profile!r} is invalid for {args.module}")

    admission_command = [
        sys.executable, str(ROOT / "parameter_admission_verifier.py"),
        str(ROOT / "PARAMETER_ADMISSION_MATRIX.json"),
        "--query-r", str(args.r), "--module", args.module,
    ]
    if profile != "not-applicable":
        admission_command.extend(["--profile", profile])
    admission_run = subprocess.run(
        admission_command, check=True, capture_output=True, text=True,
    )
    admission_payload = json.loads(admission_run.stdout)
    admission = admission_payload["query"]
    if not admission["source_applicable"]:
        print(json.dumps({
            "status": "BLOCKED_SOURCE_REDUCTION_NOT_APPLICABLE",
            "r": args.r,
            "module_id": args.module,
            "profile": profile,
            "reason": admission["reason"],
            "matrix_sha256": admission_payload["matrix_sha256"],
            "eg617_r_proved": False,
        }, indent=2, sort_keys=True))
        raise SystemExit(2)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.receipt.parent.mkdir(parents=True, exist_ok=True)
    generator_command = [sys.executable, str(module["generator"]), str(args.r)]
    if args.module == "ENDPOINT_DOMAIN_LOWER_BOUND_V1":
        generator_command.extend(["--profile", profile])
    generator_command.extend(["--output", str(args.output)])
    subprocess.run(generator_command, check=True)

    gate_command = [
        sys.executable, str(ROOT / "theorem_promotion_gate.py"),
        str(args.output), "--receipt", str(args.receipt),
    ]
    subprocess.run(gate_command, check=True)
    print(json.dumps({
        "status": "CERTIFICATE_FAMILY_MEMBER_GENERATED",
        "module_id": args.module,
        "r": args.r,
        "profile": profile,
        "admission_status": admission["admission_status"],
        "required_assumption_ids": admission["required_assumption_ids"],
        "source_ids": admission["source_ids"],
        "matrix_sha256": admission_payload["matrix_sha256"],
        "certificate_path": str(args.output),
        "receipt_path": str(args.receipt),
        "eg617_r_proved": False,
        "warning": "A generated and replayed conditional module certificate is not an EG617(r) proof.",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
