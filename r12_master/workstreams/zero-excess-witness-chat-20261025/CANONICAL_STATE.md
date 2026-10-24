# Canonical state — R12 zero-excess witness workstream

Date: 2026-10-25  
Repository: \`Icarus-K-Laplace/EG617-r12-proof\`  
Branch: \`workstream/r12-zero-excess-witness-20261025\`  
Scope: fixed \(r=12\) only. This line does not modify sibling workstreams.

## Headline

**EG617(r=12) remains OPEN / NOT_CERTIFIED.**

## New theorem

\`R12_ZERO_EXCESS_WITNESS_THEOREM.md\` proves analytically:

- For a 47-point core \(H\) with \(\alpha(H)\le4\), \(\delta(H)\ge12\), and \(e(H)=284\), let \(H_0\) be obtained by deleting all vertices with \(d_H>12\). Then \(\alpha(H_0-T)=4\) for every \(T\) of at most six vertices.
- For \(e(H)=285\), the same holds for every \(T\) of at most four vertices.
- Therefore each regular shell row with at most three core neighbours has an independent four-set witness entirely in \(H_0\), and in the 284-edge core every pair of such rows has a common witness.
- Under the retained exact-129 factor theorem, each exact-129 color in E407 Q32 and E408 Q33 has at least one no-S K5 component whose four core vertices all have degree 12 in \(H\). This yields at least seven such colored witnesses for E407 Q32 and at least eight for E408 Q33.

The graph lemma is **PROVED_ANALYTIC**. The exact-129 component corollary is **PROVED_CONDITIONAL** on the retained Kang–Pikhurko equality/factor theorem and the contextual color caps.

## Remaining blocker

This supplies necessary witness structure but does not eliminate any E407/E408 terminal. The open step is a joint labelled-overlap/capacity contradiction using the actual 284-edge core and unique color ownership. No sum of local costs may be taken over overlapping witnesses without an explicit multiplicity bound.

## Repository discipline

Only \`r12_master/workstreams/zero-excess-witness-chat-20261025/\` is modified by this branch. The sprint/master/ultimate-closure branches were read-only references.
