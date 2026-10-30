# Q33 universal 284-edge core attack — canonical state

Date: 2026-10-30  
Repository: Icarus-K-Laplace/EG617-r12-proof  
Branch: workstream/r12-q33-v47-excess4-universal-core-attack-20261030  
Write scope: r12_master/workstreams/q33-v47-excess4-universal-core-chat-20261030/

## Headline

**Universal core theorem: PROVED under the five explicit graph hypotheses.**

There is no simple graph H satisfying simultaneously

- |V(H)| = 47;
- e(H) = 284;
- delta(H) >= 12;
- alpha(H) <= 4;
- omega(H) <= 11.

The proof is analytic. It uses an independent four-set of degree-12 vertices, four private cliques, a 25-point second-Turan common-neighbor bound, a K11-K11 pair excess obstruction, and an exhaustive support-size reduction for |Z| = 3, 4, 5.

## Status boundary

- Four-set lower-bound calculation: **PROVED**.
- Four-private-clique and Z reduction: **PROVED**.
- Common-neighbor capacity: **PROVED_CONDITIONAL** on Kang-Pikhurko Theorem 1 (primary source checked).
- K11-K11 pair excess >= 6: **PROVED**.
- All support templates: **PROVED**.
- Independent arithmetic/support-shape verifier: **COMPUTATION_CERTIFIED** for the finite checks only.
- Application to the genuine E408/Q33 parent: **PROVED_CONDITIONAL**, because the parent minimum-degree input delta(H) >= 12 is imported from the retained V11 core interface. The current root audit labels V11 independent replay pending.
- Full EG617(r=12): **OPEN / NOT_CERTIFIED**. This workstream does not claim root promotion.

## Parent contract

The Q33 parent produces a 47-point core with 284 edges from E=408 and q=33. It inherits alpha<=4 and omega<=11 from the genuine 61-point h13 residual. The minimum-degree condition is the only nontrivial inherited input and is explicitly isolated in Q33_PARENT_CONTRACT_AUDIT.md.

## Separation

This theorem is for the **284-edge / excess-four Q33 contract**. No conclusion from Astra's 285-edge / excess-six Q32 theorem is used as a premise. The Astra branch was read only as a comparison source.

No sibling workstream or global canonical state was modified.
