# Independent universal Q32 attack - canonical state

Date: 2026-10-30.
Branch: workstream/r12-astra-q32-v47-universal-attack-20261030.
Exclusive write directory: r12_master/workstreams/astra-q32-v47-universal-attack-chat-20261030/.
Base: global workstream b0459807acd4b7e386148056ddf77d7998918893.

## Headline theorem - PROVED

There is no simple graph H with

    |H|=47, e(H)=285, delta(H)>=12, alpha(H)<=4, omega(H)<=11.

Hence genuine full-support E408/Q32 configurations with this core contract do not exist, uniformly for m=8,9,10. The proof is analytic and uses ordinary Turan and the published second-Turan theorem. No sibling theorem, source placement, exact-color partition or random-search failure is a proof premise. This does not close Q33, E407 or EG617(r=12) as a whole.

## Mechanism

The global excess sum(d(v)-12) is six. An independent degree12 four-set gives private cliques and at most five shared-neighbor points. A 25-point common-antineighborhood bound forbids two exterior vertices both complete to a K10. Rotation and degree accounting reduce all cores to cliques K10,K10,K11,K11 and five pair-supported points, with only two intermediate support multisets:

- D: 12,13,14,23,24;
- P: 12,13,13,24,24.

Both are now excluded. In P, two disjoint mixed-clique blockers require at least 4+4=8 excess units. In D, simultaneous incidence accounting requires at least 5+5=10. Both exceed six. Complete K10 attachments are explicitly retained and bounded, never assumed absent.

Full proof: UNIVERSAL_Q32_THEOREM.md, steps1-8, conclusion U6.

## Verification and adverse search

INDEPENDENT_VERIFIER.py independently checks the support orbits, all finite integer inequalities, the D local accounting inequality including zero missing sets, source parameters and all 90 aggregate source occupancies. It also directly recounts every independent5 and K12 in the two retained failed search graphs. The latest execution receipt is verification_log.txt; exact results are verification_results.json. The script checks finite proof ingredients and diagnostics; the logical graph proof is in the theorem document.

The two executed 30,000-proposal searches predate the final obstructions. Neither produced a valid core. Their failure is not a nonexistence argument; no solver or unrun background computation is claimed.

## Read-only source audit

- Global: b0459807acd4b7e386148056ddf77d7998918893; default main separately recorded at 278639de8572ffab12fe859d36f776fbb88fc4f0.
- A: f78ac022d70647e9c87580bbc595c2306cfda26c; old K6-free closure retracted.
- B: initial 43f22404cbcc15b13fb8a12d003e60e9fef9bde7; final audit refreshed to db515bab1a203ccae131c3953ffe2a8ecef539a6. Its K4-e/Z4 slice is reported closed; its remaining full-support frontier remains open in that branch. No B theorem is imported.
- C: ca088347124f4ea7706a63129d7ed63d4e4090d7; Q33 promotion open.
- D: 0b48d1f768e3d3c1d3137e0c3ec12f1ff618bb91; parent support bridge remains conditional.

The actual T61 parent supplies target alpha(F)<=5, hence non-target omega(C)<=5. The target core uses only omega(H)<=11. No sibling, previous Astra directory, root state or default branch is modified.

## Promotion boundary

U6 is ready for independent mathematical review and import wherever all five CORE hypotheses have been established. Source profiles and exceptional positions impose no further case split because their common core projection is already impossible. Root integration and global EG617 closure are outside this write scope and are not claimed.
