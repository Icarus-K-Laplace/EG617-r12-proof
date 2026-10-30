# V12 archive inventory

Date: 2026-10-30

Source: ChatGPT Library `/T61_H13_V12.zip`
Library file ID: `file_00000000fa1881f4bfbef443ae0fe03d`
Archive size: **190,249 bytes**
Archive SHA-256: `0c3c69a7baf94a816eff29f3a079b97ac7750d0e8b8fd2773330469c4b8c5e36`
Archive entries: **29 files**

The archive was recovered from Library; it is not present as a raw file in the inspected GitHub branch trees. The original ZIP is retained in Library and is not duplicated in this workstream.

| Path inside ZIP | Bytes |
|---|---:|
| `T61_H13_V12/E407_D3_RHO1_EXCLUSION.md` | 4,301 |
| `T61_H13_V12/E407_Q32_CERTIFICATE.json` | 2,374,602 |
| `T61_H13_V12/E407_Q32_FULL_CLOSURE.md` | 3,032 |
| `T61_H13_V12/E407_Q32_SCREEN.json` | 456,376 |
| `T61_H13_V12/E408_Q32_EXTENSION.md` | 1,645 |
| `T61_H13_V12/INDEPENDENT_Q32_REPLAY.json` | 2,141 |
| `T61_H13_V12/INPUTS/COMPLETION_LIFT_V11.md` | 4,107 |
| `T61_H13_V12/INPUTS/CORE_INTERFACE_V6.md` | 4,433 |
| `T61_H13_V12/INPUTS/EXCHANGE_V8.md` | 11,301 |
| `T61_H13_V12/INPUTS/PAIR_ROW_CAPACITY_V11.md` | 4,663 |
| `T61_H13_V12/INPUTS/Q32_Q33_SLACK_V10.md` | 2,691 |
| `T61_H13_V12/INPUTS/TASK_V12.txt` | 6,255 |
| `T61_H13_V12/INPUT_SOURCE_HASHES.json` | 1,920 |
| `T61_H13_V12/K9_PAIR_ROW_COMPLETION.md` | 4,215 |
| `T61_H13_V12/NEAR_K12_CAPACITY_EXTENSION.md` | 4,000 |
| `T61_H13_V12/Q32_COMMON_K10_CAPACITY.md` | 5,141 |
| `T61_H13_V12/Q32_KERNEL_CASE_TABLE.csv` | 229,271 |
| `T61_H13_V12/Q32_KERNEL_COVERAGE.md` | 10,080 |
| `T61_H13_V12/Q32_ONE_DEFECT_LOCALIZATION.md` | 3,155 |
| `T61_H13_V12/Q32_SLACK_SENSITIVITY_AUDIT.md` | 3,023 |
| `T61_H13_V12/Q33_TWO_DEFECT_CLASSIFICATION.md` | 2,026 |
| `T61_H13_V12/README.md` | 1,795 |
| `T61_H13_V12/SHA256SUMS.txt` | 2,577 |
| `T61_H13_V12/T61_DEPENDENCY_DAG_V12.md` | 3,328 |
| `T61_H13_V12/T61_H13_MASTER_V12.md` | 6,415 |
| `T61_H13_V12/build_package.py` | 3,176 |
| `T61_H13_V12/enumerate_q32_kernels.py` | 5,540 |
| `T61_H13_V12/screen_q32.py` | 2,183 |
| `T61_H13_V12/verify_q32_certificate.py` | 9,773 |

The package contains the certificate, screen, kernel case table, input copies, source manifest, original generator, original verifier, screen program, analytic notes, and SHA256 manifest. See `V12_HASH_AUDIT.md` for per-file hashes and source-copy checks.


## Duplicate and V11 provenance recheck

The canonical Library file /T61_H13_V12.zip (file ID file_00000000fa1881f4bfbef443ae0fe03d) and duplicate paths /T61_H13_V12(1).zip (file ID file_00000000fb708211927e41bf90bd1b08) and /T61_H13_V12(2).zip (file ID file_00000000bbe882079e6f1608dd8de985) are all 190,249 bytes, byte-identical, and share the archive SHA-256 above.

The V11 source archive is /T61_H13_V11.zip (file ID file_00000000bd708243a192cac79752b2a3), 62,298 bytes, SHA-256 27ecec92d43a27fb132c60aa7b374131a860547c236d8ed3d83d3cf0eab9f0a4. Its 22/22 SHA256SUMS entries pass. The five V12 files marked CONDITIONAL in INPUT_SOURCE_HASHES.json were each byte-compared with their mapped V11 source files; all five comparisons pass.
