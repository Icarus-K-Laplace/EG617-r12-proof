# Independent universal Q32 attack — canonical state

Date: 2026-10-30.  
Branch: workstream/r12-astra-q32-v47-universal-attack-20261030.  
Exclusive write directory: r12_master/workstreams/astra-q32-v47-universal-attack-chat-20261030/.

## Headline theorem U6 — PROVED CONDITIONAL ON THE CORE CONTRACT

There is no simple graph H satisfying all five conditions:

    |V(H)|=47, e(H)=285, delta(H)>=12, alpha(H)<=4, omega(H)<=11.

The proof is analytic. It uses ordinary Turan and Kang–Pikhurko Theorem 1 at n=25,r=2. The total degree excess is forced to be six. The proof reduces every candidate to two support templates:

- P: 12,13,13,24,24, requiring at least 8 excess units;
- D: 12,13,14,23,24, requiring at least 10 excess units.

Both contradict the available six. The detailed independent proof audit is Q32_UNIVERSAL_THEOREM_INDEPENDENT_AUDIT.md.

## Parent application — NOT CERTIFIED

The genuine T61/Q32 parent directly supplies four of the five core conditions:

- |H|=47;
- e(H)=285;
- alpha(H)<=4;
- omega(H)<=11.

The remaining condition delta(H)>=12 is inherited through E406_CORE_MINDEG_288.md and the lower-order R(3,35) minimum-degree seed. INTEGRATED1_CORE211_AUDIT.md explicitly records that the seed's 23-neighbourhood / cap-two exclusion still lacks a standalone proof/certificate or exact bibliographic dependency in the audited source set. Therefore the parent implication is not yet independently certified.

Do not report Q32 as closed until Q32_PARENT_CONTRACT_MAPPING.md's minimum-degree dependency is recovered and audited. The frozen Q32 contract is not itself a proof of its own parent coverage.

## Mechanism and verification

The mechanism is independent of m, witness support U, source-color placements and exceptional-point locations. The 25-point common-antineighborhood contradiction gives the universal common-neighbor bound; private-clique rotation and pointwise excess accounting leave P and D only.

Independent JavaScript replay confirmed:
- support orbit counts 2,3,5 for h=3,4,5;
- P mixed-pair minimum 4 over 90 legal cases;
- D mixed-pair minimum 5 over 90 legal cases;
- direct recount of both retained failed-search graphs.

The committed Python verifier receipt remains in verification_log.txt and verification_results.json. Failed search is diagnostic only; no solver UNSAT or exhaustive 47-vertex graph enumeration is claimed.

## Scope and firewall

If the parent minimum-degree input is certified, U6 excludes every Q32 support row |U|=44,45,46,47 and every m=8,9,10 at once. Until then, these remain conditional at parent level. Sibling low-support closures remain their own conditional results; no sibling theorem is imported into U6.

Q33 (284 edges, excess four), E407, E408 Q31, and the original EG617(r=12) root are outside U6. No global root or sibling file has been modified.
