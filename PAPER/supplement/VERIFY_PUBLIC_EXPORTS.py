#!/usr/bin/env python3
"""Verify the standalone T61 row ledger and q27/q28 canonical state-key exports."""
from __future__ import annotations

import hashlib
import json
from itertools import permutations
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    payload = b"blob " + str(len(data)).encode("ascii") + b"\0" + data
    return hashlib.sha1(payload).hexdigest()


def canonical_key(weights, rows):
    candidates = []
    for p in permutations(range(3)):
        permuted_weights = tuple(weights[i] for i in p)
        permuted_rows = tuple(sorted(
            (
                sum(1 << j for j, i in enumerate(p) if mask >> i & 1),
                decoration,
            )
            for mask, decoration in rows
        ))
        candidates.append((permuted_weights, permuted_rows))
    return min(candidates)


def fail(message: str):
    raise SystemExit("FAIL: " + message)


# Exact 61-row scalar recurrence ledger.
front_path = ROOT / "frontend" / "FRONTEND_REPLAY.json"
front = read_json(front_path)
t61_path = ROOT / "frontend" / "T61_H_ROW_LEDGER.json"
t61 = read_json(t61_path)
if t61.get("schema") != "eg617.t61-h-row-ledger.v1":
    fail("unexpected T61 export schema")
if t61.get("source", {}).get("git_blob_sha1") != git_blob_sha1(front_path):
    fail("T61 source Git-blob provenance mismatch")
if t61.get("rows") != front.get("T61_rows"):
    fail("T61 exported rows differ from FRONTEND_REPLAY.json")
rows = t61["rows"]
if len(rows) != 61 or [row.get("h") for row in rows] != list(range(61)):
    fail("T61 export must contain exactly h=0,...,60")

# Exact q27/q28 state export and S3 canonicality.
cover_path = ROOT / "cover" / "VERIFICATION_RESULT.json"
cover = read_json(cover_path)
verifier_path = ROOT / "cover" / "INDEPENDENT_VERIFIER.py"
states_path = ROOT / "cover" / "Q27_Q28_CANONICAL_STATE_KEYS.json"
export = read_json(states_path)
if export.get("schema") != "eg617.cover.q27-q28-canonical-state-keys.v1":
    fail("unexpected q27/q28 export schema")
sources = export.get("sources", {})
if sources.get("verification_result", {}).get("git_blob_sha1") != git_blob_sha1(cover_path):
    fail("q27/q28 result Git-blob provenance mismatch")
if sources.get("canonicalizer", {}).get("git_blob_sha1") != git_blob_sha1(verifier_path):
    fail("q27/q28 canonicalizer Git-blob provenance mismatch")

source_records = {record["q"]: record for record in cover.get("bipartite", [])}
if set(source_records) != {27, 28}:
    fail("source result must contain exactly q=27 and q=28")
if export.get("state_counts") != {"27": 2, "28": 8}:
    fail("export state-count declaration mismatch")

for q in (27, 28):
    source_states = source_records[q]["states"]
    exported_states = [x for x in export.get("states", []) if x.get("q") == q]
    if len(source_states) != len(exported_states):
        fail(f"q={q}: exported state count mismatch")
    source_keys = []
    for state in source_states:
        weights = state["hub_weights"]
        rows = state["rows"]
        key = canonical_key(weights, rows)
        if key != (tuple(weights), tuple(tuple(row) for row in rows)):
            fail(f"q={q}: source state is not in canonical S3 form")
        source_keys.append({"hub_weights": weights, "rows": rows})
    export_keys = [x.get("canonical_key") for x in exported_states]
    if export_keys != source_keys:
        fail(f"q={q}: exported canonical keys differ from source verifier output")

if len(export.get("states", [])) != 10:
    fail("combined q27/q28 export must contain ten states")

print("PASS: T61 h-row ledger (61 rows, h=0..60)")
print("PASS: q27/q28 canonical state keys (2 + 8 states)")
print("PASS: Git-blob provenance and S3 canonicality")
