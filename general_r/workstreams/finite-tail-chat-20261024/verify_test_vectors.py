#!/usr/bin/env python3
"""Replay the frozen finite-tail V1 regression vectors.

This checker uses the independent payload derivation in verify_instance.py and
never imports generate_instance.py.  Passing this file checks deterministic
encoding/hash stability only; it is not an EG617 theorem certificate.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from verify_instance import canonical_bytes, expected_payload

ROOT = Path(__file__).resolve().parent


def main() -> None:
    fixture = json.loads((ROOT / "TEST_VECTORS.json").read_text(encoding="utf-8"))
    assert fixture["schema"] == "eg617-finite-tail-test-vectors-v1"
    checked = []
    for row in fixture["vectors"]:
        payload = expected_payload(int(row["r"]), str(row["profile"]))
        digest = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        assert digest == row["payload_sha256"], (row["r"], row["profile"], digest)
        assert payload["candidate_missing_degrees"] == row["candidate_missing_degrees"]
        assert payload["symmetry"]["orbit_representatives"] == row["orbit_representatives"]
        checked.append(
            {
                "r": row["r"],
                "profile": row["profile"],
                "payload_sha256": digest,
            }
        )
    print(
        json.dumps(
            {
                "status": "PASS",
                "vectors_checked": len(checked),
                "checked": checked,
                "warning": "regression encoding only; no EG617(r) theorem is asserted",
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
