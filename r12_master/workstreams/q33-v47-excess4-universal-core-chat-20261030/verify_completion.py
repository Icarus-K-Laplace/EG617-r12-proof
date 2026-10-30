#!/usr/bin/env python3
"""Exact verifier for COMPLETION_CERTIFICATE.csv; no optimizer or floats."""
from fractions import Fraction as Q
from itertools import combinations, product
from pathlib import Path
import csv, json

HERE = Path(__file__).resolve().parent
pairs = list(combinations(range(4), 2))
patterns = [(11, 11, 11, 11), (10, 11, 11, 11)]
expected = set()
for s in patterns:
    for n in product(*(range(1, v + 1) for v in s)):
        if sum(s) - sum(n) != 12:
            continue
        if any(s[i] == s[j] and n[i] > n[j] for i, j in pairs):
            continue
        expected.add((s, n))

seen = set()
per = {s: [0, Q(0)] for s in patterns}
with (HERE / "COMPLETION_CERTIFICATE.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        s = tuple(map(int, row["s"].split(";")))
        n = tuple(map(int, row["n"].split(";")))
        lam = tuple(map(Q, row["lambda_"].split(";")))
        assert (s, n) in expected and (s, n) not in seen
        assert len(lam) == 4 and min(lam) >= 0
        assert all(lam[i] + lam[j] >= Q(1, n[i] * n[j]) for i, j in pairs)
        value = sum(lam[i] * n[i] * (13 - s[i]) for i in range(4)) + 2 * max(lam)
        assert value == Q(row["bound"]) and value < 1
        seen.add((s, n))
        per[s][0] += 1
        per[s][1] = max(per[s][1], value)

assert seen == expected
result = {
    "status": "EXACT_CERTIFICATE_VERIFIED",
    "rows": len(seen),
    "scope": "Weighted union-bound lemma for four cliques of sizes 11^4 or 10,11^3; total excess <=2; a degree-12 vertex incomplete to each clique.",
    "table": [{"s": s, "rows": v[0], "maximum": str(v[1])} for s, v in per.items()],
}
(HERE / "VERIFIED_COMPLETION.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
print(json.dumps(result, indent=2))
