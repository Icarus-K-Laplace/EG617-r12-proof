# Finite verifier re-execution audit

Date: 2026-11-02  
Frozen integration snapshot: `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`  
Execution environment: Python 3.13.5 (analysis kernel)

## 1. Low-edge verifier: exact source bytes

The vendored `frozen/low/INDEPENDENT_VERIFIER.py` was transcribed into the execution kernel and its UTF-8 source SHA-256 was checked. It is exactly

`c1f19e7f4e084e20fe756c8f817909d1f5ecadfbd4d4ace26d145a4cb78c40ee`,

matching the frozen root `SHA256SUMS.txt` entry. The script was executed with `__name__ == "__main__"` and `__file__` pointing to a temporary file; it uses only the Python standard library and does not read external package files. This is an execution of the exact source bytes in the Python kernel, though not a subprocess launched by the literal shell command `python -B ...`.

Result: `PASS_FINITE_CHECKS`. All numerical outputs match the frozen `frozen/low/VERIFICATION_RESULTS.json`; only the interpreter version differs (the saved run says Python 3.12.14, this run says Python 3.13.5).

Key output:
- 25-point triangle-free bound table: 145,142,137,130,121,110,97,82,65,46,25.
- Independent-four support multisets: 9,40,48 raw cases and 2,3,5 canonical orbits.
- Scalar minima: 6,6,4,5.
- Shared-diamond accounting: 8,400 checks.
- Five-cycle type classification: 20 compatible type-set pairs, 55 singleton-extension checks, 10 incompatible endpoint cases.
- Neighborhood-cost family audit: 61 representatives, 49 valid, 12 discarded by alpha, 263 maximal independent sets, maximum cost6, forced 14-set edge count72.
- Hereditary gate: degree-10 floor289, degree-11 floor287; parent rows match.

## 2. COVER: independent full enumeration transcription

The COVER finite verifier was independently transcribed from the frozen source and executed in Python 3.13.5. This transcription is not byte-identical to the frozen script; the frozen source itself is separately authenticated by the root checksum and its original source-workstream checksum.

For each q in {27,28}, the enumeration visited all 19,448 row-count compositions. The independently reproduced counters exactly match the saved COVER result:

| q | Row-count vectors | Edge/Hall vectors | Hub-decoration trials | Completed decorations | Canonical states |
|---:|---:|---:|---:|---:|---:|
| 27 | 19,448 | 882 | 32,665 | 2 | 2 |
| 28 | 19,448 | 891 | 51,118 | 16 | 8 |

All ten retained canonical states were directly checked over all (2^{13}) shell subsets, for 81,920 subset identities. The 104 algebraic repivot identity checks also passed. The saved output's q27/q28 states and all counters agree exactly.

This closes the specific gap noted in the root verifier audit: the root verifier itself did not rerun `reconstruct_bipartite`; this independent transcription did.

## 3. E286: independent finite-logic transcription

The E286 finite verifier logic was independently transcribed and executed in Python 3.13.5. It is not byte-identical to the frozen verifier, whose source bytes are independently authenticated by the package checksums.

The resulting output matches the saved `frozen/eq286/VERIFICATION_RESULT.json`:
- support orbit counts: 2,3,5;
- scalar minima: 6,4,2,2;
- diamond subset accounting: 10,400;
- ordered double-pair intersection tuples: 139,921;
- minimum computed excess: 14, strictly above the allowed8;
- regular-four-set edge lower bounds: 350,346,342,337,331,325,318,310;
- full-color caps: 20 for E407 and19 for E408.

This independently corroborates the finite support quotient and arithmetic. It does not certify the prose elimination of all ten support orbits as a formal proof; that remains an analytic argument in `286_EDGE_EQUALITY_CLASSIFICATION.md`.

## 4. Combined status and limits

| Component | New execution / reproduction | Status |
|---|---|---|
| Low verifier | Exact source bytes, Python 3.13.5 kernel | PASS |
| COVER shell enumeration | Independent transcription; all counters and states match | PASS |
| COVER direct subset checks | 81,920 | PASS |
| E286 support/scalar/intersection checks | Independent transcription; saved outputs match | PASS |
| Frontend recurrence | Third independent integer implementation; 1,752 nodes and 144 stops match | PASS |
| Root integration verifier as a whole | Not executed from a clean checkout | NOT RUN |
| Lean kernel proof | Not established | NOT RUN |

The combined evidence materially strengthens the computational reproducibility of the fixed-r=12 proof. It does not replace the analytic proofs, does not establish Lean certification, and is not external peer review. No frozen integration file or sibling workstream was modified.
