# EG617 fixed r=12 — root promotion receipt after fail-close

Updated: 2026-10-27
Receipt class: **branch-local source-freeze / fail-closed promotion audit**
Current theorem status: **OPEN / NOT_CERTIFIED**
Unique currently identified live graph terminal: **E408 / h13 / Qmax=32 / e(H)=285 / excess6**

## 1. Promotion withdrawal

The earlier branch-local receipt promoted `EG617(r=12)` to `PROVED_CONDITIONAL + COMPUTATION_CERTIFIED`. That promotion is withdrawn.

Primary-source verification of the Kang--Pikhurko Type-I equality construction refuted a load-bearing premise used by the former E408 whole-layer closure: there is no color-degree9 exceptional vertex. See `KP_DEGREE9_RETRACTION_AND_E408_Q32_REOPEN.md`.

Fail-closed rule therefore reopens E408-Q32 and blocks the root theorem.

## 2. Front-end gate — still valid

`front_end/FRONTEND_BRIDGE_THEOREM.md`, blob `52b2f4af102ceba1671dc7d0e7ed36a512458e77`:

`balanced K145 counterexample -> contextual R(4,49) OR embedded T61`.

Line-A computation certificate:

- package SHA256 `8f34097f195f53a6aac2999a655d3dc6a4ebc7c74f5764aedea65a79235a98ac`;
- 1,752 recurrence nodes;
- 144 stopping comparisons;
- 73 manifest files, 0 errors;
- unique no-R449 stop `(11,6,5,61)`, `397<=E<=408`;
- independent replay PASS.

Contextual R449 remains excluded by `front_end/CONTEXTUAL_R449_FULL_COLOR_IMPOSSIBILITY.md`, blob `dd072ce9ef703b56e9184f2ede992988fce9f86e`, relative to its named extremal input.

## 3. T61 low layers — still valid

Registered closures remain in force for:

- h12;
- h13 E397--E400;
- E401--E404;
- E405;
- E406.

The source-freeze of every individual low-layer theorem remains a publication-audit task, but no new defect was found in these layers during the KP audit.

## 4. E407 — still closed

### Q31
V10/V11 independent replay and analytic capacity remain unaffected.

- V10 archive SHA256 `e83e2907d541b38304746e855af52b5e21b6500a35cb0fdb676a4f6a7601303a`;
- V11 archive SHA256 `27ecec92d43a27fb132c60aa7b374131a860547c236d8ed3d83d3cf0eab9f0a4`;
- V11 certificate SHA256 `0baffc39ee481b27af53fda36a8fe40b8cd8c527103b5126060857c4eaacd09b`.

### Q32
V12 coverage remains computation-certified:

- archive SHA256 `0c3c69a7baf94a816eff29f3a079b97ac7750d0e8b8fd2773330469c4b8c5e36`;
- certificate SHA256 `cab4e67bc501fe51c06f8fc008443b870aebf8794528af1a3045e83be7d6db30`;
- 8,677 kernel weights;
- 17,957 count states;
- 1,984 necessary shells;
- 554 survivors, all mapped to five templates.

Read-only sibling freeze:

- branch head observed `b36538e27dce89dfcba2aa2bfdfc29d6611a96ec`;
- `FIVE_TEMPLATE_GLOBAL_COMPATIBILITY.md` blob `8b95bbf59e7a9232eff6cc27c9f50177533e5e21`;
- `SUPPORT_BLOCK_ANCHOR_IDENTITY.md` blob `50447a9931b9b51a21a979dc61d834389abd4e3a`;
- `PROOF_DEPENDENCY_AUDIT.md` blob `4b6c8ef85dce38003591c1aa712b7f9b637a68cb`.

The shortest terminal contradiction remains:

`49*C(4,2)=294` selected complement edges on U,
`e(overline(H[U]))<=310`,
and one unselected non-target color contributes at least `p_12(29)=22`, so

`294+22=316>310`.

This does not use the false degree9 premise.

## 5. Kang--Pikhurko exact-129 source gate — factorization PASS, degree9 FAIL

The primary-source audit confirms:

- complement equality at `(n,r)=(61,12)`;
- optimal sequences exactly `(5^12)`, `(4,5^10,6)`, `(4,4,5^8,6,6)`;
- clique cap leaves only `(5^12)`;
- hence exact color factorization `10 isolated K5 + G11`.

It refutes:

- any universal degree9 exceptional vertex.

Correct variable degrees are `(4+a,9-a)` for `a in {1,2,3,4}`.

Source audit: `KANG_PIKHURKO_EXACT129_SOURCE_AUDIT.md`.
Companion arithmetic/sequence verifier: `verify_kp_exact129_instance.py`.
Retraction: `KP_DEGREE9_RETRACTION_AND_E408_Q32_REOPEN.md`.

## 6. E408 charge gates after correction

### Q31 — PASS_CONDITIONAL + COMPUTATION_CERTIFIED
The V11 route remains valid under its named inputs.

### Q33 — PASS_CONDITIONAL
The load-bearing Q33 route does not use degree9:

- `Q33_M10_EXACT_COLOR_CAPACITY_EXCLUSION.md`: component witness packing excludes m=10;
- `Q33_NONEXACT_U_RESERVE_CLOSURE.md`: m=8/9 are excluded by nonexact-color U reserve.

### Q32 — OPEN / FAIL-CLOSED
Retracted Q32 closure files:

- `Q32_GLOBAL_EXCEPTIONAL_INJECTIVITY.md`;
- `Q32_EXACT_COLOR_COUNT_COLLAPSE.md`;
- the injectivity-dependent closure in `Q32_NONFULL_SUPPORT_SHELL_CAPACITY.md`;
- `E408_WHOLE_LAYER_EXACT_COUNT_CLOSURE.md` as a whole-layer theorem.

These files remain historical artifacts only.

## 7. E408-Q32 surviving theorem interface

Read-only source branch:

`workstream/r12-e408-q32-excess6-20261025`

Key source:

`CORE285_CAPACITY_THEOREM.md`, blob `3555748eefa810049bbd5fa6796462ea83a7002a`.

Valid necessary structure:

- 47-core H with285 edges, alpha<=4, min degree>=12;
- total core excess6;
- exact-color count m in `{8,9,10}`;
- each exact color yields at least ten pairwise-disjoint independent core4 witnesses;
- cross-color witness system is pairwise linear;
- total support v satisfies `v>=44` after the low-support triple-pair refinement;
- exact capacity
  `6N <= C(v,2)-p_4(47-v)-12v+285-E_U`.

No closure at `v=44..47` is yet certified.

## 8. Current root composition

Closed relative to named inputs:

- contextual R449;
- T61 h12;
- h13 E397--E406;
- E407 Q31/Q32;
- E408 Q31/Q33.

Open:

- E408 Q32.

Therefore

`EG617(r=12) = OPEN / NOT_CERTIFIED`.

## 9. Promotion condition

Root promotion is permitted only after a valid theorem excludes E408-Q32 without using exceptional degree9 or an illicit excess-four transfer.

Any new source mismatch automatically reopens the affected gate.
