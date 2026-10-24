# Independent V11/V12 replay record

Date: 2026-10-24. This records a fresh local replay of the Library-delivered archives, not a claim that the analytic completion theorems or retained lower-order inputs have been re-proved.

## Archive identity

| Archive | SHA-256 |
|---|---|
| T61_H13_V11.zip | 27ecec92d43a27fb132c60aa7b374131a860547c236d8ed3d83d3cf0eab9f0a4 |
| T61_H13_V12.zip | 0c3c69a7baf94a816eff29f3a079b97ac7750d0e8b8fd2773330469c4b8c5e36 |

For each extracted package, SHA256SUMS verification returned all entries OK.

## Commands actually run

V11:
- cd .../T61_H13_V11
- sha256sum -c SHA256SUMS.txt
- python -B verify_kernel_certificate.py

V12:
- cd .../T61_H13_V12
- sha256sum -c SHA256SUMS.txt
- python -B verify_q32_certificate.py

Both verifiers use Python's standard library; neither invokes a SAT/ILP solver or imports the generator as the verifier.

## Replay results

### V11

- Status: COMPUTATION_CERTIFIED
- Kernel weight assignments: 684
- Outside-count states: 349
- Labelled necessary shells: 259
- Family A: 252
- Family B: 7
- Completed parent graphs claimed: 0
- Certificate SHA-256: 0baffc39ee481b27af53fda36a8fe40b8cd8c527103b5126060857c4eaacd09b

### V12 E407 Q32

- Status: COMPUTATION_CERTIFIED
- Energy: 407; maximum charge Q=32
- Kernel weight vectors: 8,677
- Count states: 17,957
- Labelled necessary shells: 1,984
- Screen: 90 excluded by D3/rho=1, 1,192 by near-K12 capacity, 148 by K9 pair-row completion, 554 remain open
- Candidate-free family count records: F1 has seven patterns; F2 has two patterns
- Completed parent graphs claimed: 0
- Certificate SHA-256: cab4e67bc501fe51c06f8fc008443b870aebf8794528af1a3045e83be7d6db30

## What this independently certifies

The finite kernel certificate and the screen's labelled-state coverage replay as supplied. In particular, the 554 remaining entries are covered by the five rho=0 regular-d3 templates described in Q32_KERNEL_COVERAGE.md.

## What it does not certify

- It does not construct or exclude a completed 61-vertex parent graph for any remaining template.
- It does not independently prove the analytic rules applied by the screen; those retain their explicit hypotheses and lower-order dependencies.
- It does not close the common regular K11 / 284-edge core compatibility theorem.
- It says nothing that closes E408 Q32 or Q33: V12's E408 sections explicitly retain OPEN status and do not claim exhaustive E408 coverage.

Accordingly, the V11/V12 finite enumeration status is now COMPUTATION_CERTIFIED / INDEPENDENTLY REPLAYED in this workstream, while the E407 and E408 terminal exclusion remains OPEN.


## Checksum-order note

The pristine ZIPs were re-extracted into fresh directories and every entry in each SHA256SUMS.txt passed **before** the verifier was run. The verifier intentionally rewrites its own replay JSON, and the V12 verifier also regenerates Q32_KERNEL_CASE_TABLE.csv. Running sha256sum -c again in that mutated working directory will therefore report those generated outputs as changed. This is expected; it is not an archive-integrity failure. Re-extract the original ZIP to repeat the clean pre-run checksum check.
