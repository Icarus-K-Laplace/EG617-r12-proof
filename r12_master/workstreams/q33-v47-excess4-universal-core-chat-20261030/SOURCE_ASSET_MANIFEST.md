# Q33 source asset manifest

Date: 2026-10-30

## Original retained archives

| Archive | SHA256 | Use |
|---|---|---|
| FRONTEND_LINE_A_V1.zip | 8f34097f195f53a6aac2999a655d3dc6a4ebc7c74f5764aedea65a79235a98ac | Primary strict-descent and lower-order seed source |
| BACKEND49_FIRST_PRINCIPLES_AUDIT_V1.zip | 3801a02fa8e9f53b19c5d289d14deb2f9ef7923e8c63497ca829ad998b433315 | Inspected; not a dependency |
| HIGH_LAYER_BACKEND_V8.zip | 8c05b4490a4c0cdaf08be20180902ec2b5e126f5f275c35f2f12ff353bb825da | Inspected; not a dependency |
| T61_H13_V11.zip | 27ecec92d43a27fb132c60aa7b374131a860547c236d8ed3d83d3cf0eab9f0a4 | Inspected and finite kernel replayed; not a dependency |

## Primary source paths and hashes inside FRONTEND_LINE_A_V1.zip

| Internal source path | SHA256 |
|---|---|
| SOURCES/S31_AUDIT/STRICT_DESCENT_PROOF.md | d91e44a2d9a9cf17d8766f9b0b3c442d8e6bb0818b45a9657618c9119fc306ae |
| SOURCES/S31_AUDIT/SEED_AND_CORE_AUDIT.md | ed2c98b85c82ce7ed439506b6828593639face53c87b2a78225dcba2f84565bc |
| SOURCES/S31_AUDIT/inputs/five_block_v2/S31_FIVE_BLOCK_TERMINAL_CLOSURE_V2/core_audit/SEED_NEIGHBOURHOOD_EXCERPT.md | b287b12026c4e7968d8acd1800c570b6c4ea2a2aaedd24f5083396da0a466ec0 |
| SOURCES/S31_AUDIT/inputs/five_block_v2/S31_FIVE_BLOCK_TERMINAL_CLOSURE_V2/core_audit/SEED_TRIANGLE_FREE_EXCERPT.md | 713b2163617650ee96e7e315f02a273a4873b8e87843e4ca90149991f007ef33 |
| SOURCES/S31_AUDIT/inputs/five_block_v2/S31_FIVE_BLOCK_TERMINAL_CLOSURE_V2/core_audit/CORE_FLOOR_284_PROOF.md | 0ebf37349c7e1c9fdfef54c95b9cb42363b9daa6c32e870cc9a4b5eca5bb837d |

## Exact certificate retained directly in this workstream

- COMPLETION_CERTIFICATE.csv — 127 rows; original SHA256 2603ef814d77fb34f2f13569d64ed15ca40bc4c9d9b85518b41e83da8feaecd9.
- verify_completion.py — exact Fraction verifier; original SHA256 094d2ea62847af6a28fec136ca2990e13ec32f7cb9beaac8a25ea51e7f39ba32.
- VERIFIED_COMPLETION.json — exact output, 32+95 rows, maxima 773/1089 and39/44.
- Q33_SOURCE_COMPLETE_REPLAY.py — additional standard-library arithmetic/support replay, including an optional exact Fraction certificate parser.

The original archive assets remain retained in the user's uploaded file library. The branch contains the proof reconstruction, the full 127-row CSV, both replay scripts, and the exact verifier output.