# Canonical state — E407 Q32 terminal workstream

Date: 2026-10-25  
Repository: Icarus-K-Laplace/EG617-r12-proof  
Branch: workstream/r12-e407-q32-terminal-20261025  
Directory: r12_master/workstreams/e407-q32-terminal-chat-20261025/

## Headline

**EG617(r=12): OPEN / NOT_CERTIFIED. E407 Q32: OPEN.**

## Live sibling heads read

- emergency sprint: f4c3b06891d29238d4f9cca2588f442004b6dc97
- ultimate closure: 1aa47d10edd5ece2b73a0891af7ac2ce37ecbb40
- witness packing: f5d3daa07403877ede9885e1bd5c2f46b16d81da
- zero-excess witness: 07d19abfd6c1c749c7360526e4a04a3eb865fb2e
- Astra dlow terminal: c71b29d3c5b661cdcf00404e545933893c44598b
- Astra aext near-anchor: ad6e4ebe152e3918b9c5fe67f461ba402b1445d8
- base main at branch creation: 3f42fcce5761ca2372140618adda56f95fcbe253

These are the latest heads observed in the repository at the time of this update; they are provenance references, not merged dependencies.

## Established under retained contracts

- The E407 Q32 boundary has 49 linear independent 4-set witnesses on a 29-point support, with \(e(H)=284\), \(\alpha(H)\le4\), \(\delta(H)\ge12\), and total core excess 4.
- The exact ledger gives \(3\le\delta\le16\), \(\delta+\epsilon_U\le16\), and the sibling transversal/excess lemma gives \(\epsilon_U+2\delta\ge9\).
- If \(\delta=16\), \(L=\overline{H[U]}\) is four-partite because it has 310 edges, exceeding the non-four-partite Brouwer threshold 309. The resulting \(7,7,7,8\) core is narrowed but **not excluded**: the \(4+1\) and \(3+2\) endpoint splits are impossible, while the \(5+0\) split remains open because the three non-endpoint \(D\)-vertices already meet the endpoint \(K_4\) and each has only one additional \(W\)-neighbour.
- In that case, \(U\)-part sizes are \(7,7,7,8\), \(H[W]=K_5\cup K_5\cup K_4\cup K_4\), and the five cross edges in \(H[U]\) form a matching between the 8-part and the three 7-parts.
- A reverse-saturation lemma additionally proves every vertex of W is adjacent to all vertices of exactly one U-part; this is needed for the endpoint-split argument.
- The five 8-part endpoints all have the same \(K_4\) as their exact \(W\)-neighbourhood; this \(K_4\) is complete to \(D\). Each vertex in the remaining \(K_4,K_5,K_5\) components is complete to some 7-part, but the full-part labels may vary vertex-by-vertex; no component-wide bijection has been proved.

## Status by case

| Case | Status |
|---|---|
| E407 template A | OPEN |
| E407 template B | OPEN |
| E407 template C | OPEN |
| E407 template D | OPEN |
| E407 template E | OPEN |
| \(\delta=16\) four-partite extreme | OPEN; reduced to the labelled \(5+0\) endpoint kernel |
| \(\delta=14,15\) four-partite | W-part profiles classified, compatibility OPEN |
| \(\delta\le15\) non-four-partite | OPEN |
| E407 Q32 overall | OPEN / NOT_CERTIFIED |
| EG617(r=12) | OPEN / NOT_CERTIFIED |

## Verification status

The local arithmetic/terminal audit script is named verify_e407_delta16_kernel.py. It checks the exact ledgers and finite excess-budget contradictions. It is a consistency check, not a graph-realization certificate; the \(5+0\) endpoint kernel remains OPEN; the verifier does not certify graph realizability.
