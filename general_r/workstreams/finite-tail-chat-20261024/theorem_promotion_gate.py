#!/usr/bin/env python3
"""Theorem-promotion gate for finite-tail endpoint-domain certificates.

A verified conditional lemma may be promoted as conditional. This gate never
promotes EG617(r) from a necessary-domain module, even if its arithmetic passes.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MODULES = {
    "ENDPOINT_DOMAIN_LOWER_BOUND_V1": {
        "generator": ROOT / "generate_endpoint_domain.py",
        "verifier": ROOT / "verify_endpoint_domain.py",
    },
    "D1_SHELL_CLASS_BOUND_V1": {
        "generator": ROOT / "generate_d1_shell_bound.py",
        "verifier": ROOT / "verify_d1_shell_bound.py",
    },
}
DEFAULT_LEDGER = ROOT / "ASSUMPTION_LEDGER.md"


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_status_line(ledger: str, assumption_id: str) -> str:
    prefix = f"- {assumption_id}:"
    for line in ledger.splitlines():
        if line.strip().startswith(prefix):
            return line.strip()[len(prefix):].strip()
    return "UNKNOWN"


def status_applies(status_text: str, r: int) -> bool:
    if status_text == "PROVED_ANALYTIC":
        return True
    match = re.search(r"PROVED_ANALYTIC for r>=(\d+)", status_text)
    if match:
        return r >= int(match.group(1))
    match = re.search(r"PROVED_ANALYTIC for all r>=(\d+)", status_text)
    if match:
        return r >= int(match.group(1))
    return False


def gate(certificate_path: Path, ledger_path: Path) -> dict:
    envelope = json.loads(certificate_path.read_text(encoding="utf-8"))
    instance = envelope["body"]["instance"]
    module_id = instance.get("module_id")
    module_tools = MODULES.get(module_id)
    if module_tools is None:
        raise AssertionError(f"unknown module ID: {module_id}")
    verifier_path = module_tools["verifier"]
    generator_path = module_tools["generator"]
    verification = subprocess.run(
        [sys.executable, str(verifier_path), str(certificate_path)],
        check=True, capture_output=True, text=True,
    )
    verified = json.loads(verification.stdout)
    if verified.get("status") != "PASS" or verified.get("module_id") != module_id:
        raise AssertionError("independent verifier did not certify the expected module")
    r = instance["r"]
    ledger = ledger_path.read_text(encoding="utf-8")
    assumption_status = {}
    for assumption_id in instance["assumption_ids"]:
        status_text = read_status_line(ledger, assumption_id)
        assumption_status[assumption_id] = {
            "ledger_status": status_text,
            "proved_for_this_r": status_applies(status_text, r),
        }

    source_supported = r >= 12
    all_assumptions_known = all(x["ledger_status"] != "UNKNOWN" for x in assumption_status.values())
    all_assumptions_proved = all(x["proved_for_this_r"] for x in assumption_status.values())
    if not all_assumptions_known:
        conditional_module_status = "BLOCKED_UNKNOWN_ASSUMPTION_ID"
        module_gate = "BLOCKED_UNKNOWN_ASSUMPTION_ID"
    elif not source_supported:
        conditional_module_status = "SCHEMA_ONLY"
        module_gate = "BLOCKED_SOURCE_REDUCTION_NOT_APPLICABLE"
    else:
        conditional_module_status = "CONDITIONAL_LEMMA_CERTIFIED"
        module_gate = "PASS_CONDITIONAL_MODULE"

    # This module gives a necessary domain only, never a contradiction or graph closure.
    eg617_promotion_status = "BLOCKED_MODULE_IS_ONLY_NECESSARY_DOMAIN"
    if not all_assumptions_known:
        eg617_reason = "one or more assumption IDs are absent from the machine-readable ledger"
    elif not all_assumptions_proved:
        eg617_reason = "one or more analytic assumptions are not proved for this r"
    else:
        eg617_reason = "even with assumptions discharged, endpoint-domain pruning is not a graph nonexistence proof"

    return {
        "gate_schema": "eg617-theorem-promotion-gate-v1",
        "status": module_gate,
        "module_status": conditional_module_status,
        "module_id": module_id,
        "r": r,
        "profile": instance.get("profile", "not-applicable"),
        "assumption_status": assumption_status,
        "assumptions_all_known": all_assumptions_known,
        "assumptions_all_proved_for_r": all_assumptions_proved,
        "instance_sha256": verified["instance_sha256"],
        "certificate_sha256": verified["certificate_sha256"],
        "generator_path": generator_path.name,
        "generator_sha256": sha256_file(generator_path),
        "verifier_path": verifier_path.name,
        "verifier_sha256": verified["verifier_sha256"],
        "gate_sha256": sha256_file(Path(__file__)),
        "replay_command": f"python {verifier_path.name} {certificate_path}",
        "conditional_lemma_promotion": "PASS" if source_supported and all_assumptions_known else "BLOCKED",
        "eg617_promotion_status": eg617_promotion_status,
        "eg617_r_proved": False,
        "eg617_promotion_reason": eg617_reason,
        "scope": "conditional necessary-domain lemma only; no endpoint closure, graph-level symmetry, or EG617(r) theorem is certified",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--ledger", type=Path, default=DEFAULT_LEDGER)
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    result = gate(args.certificate, args.ledger)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.receipt:
        args.receipt.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
