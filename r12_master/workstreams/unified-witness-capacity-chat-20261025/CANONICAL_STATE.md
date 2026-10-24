# Unified witness-capacity workstream — canonical state

Updated: 2026-10-25  
Repository: Icarus-K-Laplace/EG617-r12-proof  
Branch: workstream/r12-unified-witness-capacity-20261025  
Allowed directory: r12_master/workstreams/unified-witness-capacity-chat-20261025/

## Headline

**EG617(r=12): OPEN / NOT_CERTIFIED.** This workstream has proved a reusable conditional labelled-incidence theorem and a finite omission-capacity refinement, but has not excluded the remaining E407/E408 terminal candidates.

## Live source heads read before work

- Emergency sprint: f4c3b06891d29238d4f9cca2588f442004b6dc97
- Ultimate closure / E408 Q32 line: 1aa47d10edd5ece2b73a0891af7ac2ce37ecbb40
- Zero-excess witness line: 07d19abfd6c1c749c7360526e4a04a3eb865fb2e
- E407 Q32 terminal / Cell-B line: 3f42fcce5761ca2372140618adda56f95fcbe253
- Witness-packing line (latest universal E408 Q33 S0>=12 theorem): f5d3daa07403877ede9885e1bd5c2f46b16d81da
- Base master-closure head used to create this branch: e46da35aedce7bbaaf11756b50192bd157956239

The source branches were read-only; no sibling path was edited.

## Canonical mathematical results

1. **Exact-129 labels:** each selected exact-129 color has seven independent four-point witnesses under the retained witness contract, at least six B-labelled. Same-label witnesses across colors are disjoint; all distinct witnesses are linear.
2. **New label-capacity theorem:** a pivot-labelled witness can occur in at most floor(v/4) colors. At E408 Q33, v=31 and c=8, so at least one color has seven B-labelled witnesses. Combining this with total excess four gives at least 17 zero-excess B-labelled witnesses across the eight colors. E407 has at least 14.
3. **Zero-excess graph theorem audited:** for a 284-edge core, after deleting the positive-excess vertices and then any further at most six vertices, an independent four-set remains. This gives a common unlabelled witness for any pair of regular B rows with at most three zero-excess neighbours each. For a 285-edge core the deletion threshold is only four.
4. **Omission-capacity theorem:** at the minimum-support boundary, with r_x witness multiplicity and o_x=c-r_x, e_H(U,W) is at least the sum of max(0,13-v+3(c-o_x)). It gives the verified profile tables in LABELLED_WITNESS_CAPACITY_THEOREM.md; in E408 Q33, Omega=sum binom(o_x,2)<=48 (and Omega<=24 when S0 is 12, 13, or 14).
5. **Edge multiplicity:** the exact crossing-edge load is sum over xy in E(H[U]) of r_x r_y, not the unweighted number of crossing edges. Its lower bound remains compatible with the available upper bound, so it does not close a terminal.

## Status by obligation

- E407 Q32, 49 witnesses / 29 support points: **OPEN**. Inherited S=epsilon_U+2delta>=9, delta>=3, epsilon_U+delta<=16. The labelled omission-capacity table correlates Omega with S but leaves profiles.
- E408 Q33, 56 witnesses / 31 support points: **OPEN**. Inherited universal S0=epsilon_U+2delta>=12, epsilon_U+delta<=17. The new omission bound excludes highly concentrated omission profiles but leaves the S0=12 relaxation.
- E408 Q32, 285-edge / excess-six core: **OPEN** and separate. The zero-excess theorem permits only four further deletions, so the pairwise row-union conclusion does not apply automatically when the union has size five or six.
- Original K145 reduction bridge and full EG617 theorem: **OPEN / NOT_CERTIFIED**.

## Minimum unresolved proposition

A pair of regular rows has a common independent four-set in H0, but this set is not necessarily a monochromatic component of an exact-129 color. The exact-129 label/edge-ownership theorem cannot be applied to an arbitrary independent set. The next advance must prove a label-transfer/component-realization lemma, a sharper hub-capacity theorem, or a finite incidence-design exclusion.

See the four theorem/audit files in this directory and verify_unified_witness_capacity.py.
