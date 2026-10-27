# Progress log — E407 Q32 two-chat closure workstream

Date: 2026-10-27  
Branch: `workstream/r12-twochat-e407-closure-20261026`

Historical Rounds 1–15 are preserved in prior commits. This current log records the newest mathematically substantive advances. E407 Q32 remains OPEN / NOT_CERTIFIED.

## Round 16 — actual selected hub-complete support blocks

Commit: `49d86aee7a4c89400fffd94b5616845281257d13`

Added:
- `SELECTED_SUPPORT_HUB_COMPLETENESS.md`
- `S_ANCHOR_CROSS_LOAD_REFINEMENT.md`
- `verify_selected_support_global_forcing.py`

Results:
1. If a V12 template contains a full B row f (k_f=3), every selected B-anchored block that is not hub-complete must meet D_f. Since |D_f|=3 and same-color selected blocks are disjoint, each exact color has at least b_c-3>=2 actual selected hub-complete support blocks.
2. A/B/C/D always have a full row. E either has one or its row constraints force n0=n1=n3=0,n2=10, i.e. all ten B rows are P3 ends-pair rows.
3. Hence A/B/C/D and E-full have at least14 actual selected hub-complete B-blocks globally. E-no-full has at least35 actual selected B-blocks hitting both P3 endpoint rows.
4. If sigma is the number of selected S-anchor occurrences, every exact color owns at least one exact-colored S-B shell edge and an S-anchored exact color owns at least two. Therefore
   |E_exact(S,B)| >= max(14-beta, 7+sigma).

These theorems finally move the old auxiliary-component witness forcing onto the actual 49 selected support blocks.

## Round 17 — common-core full-row linearity capacity

Commit: `5e6d6d311860a412dccab1a5b0a7b2d513d28f1b`

Added:
- `FULL_ROW_LINEARITY_CAPACITY.md`
- `verify_full_row_linearity_capacity.py`

Let h be the number of full B rows and N_bad the global number of selected B-blocks that are not hub-complete. For u in U let d(u) count full rows whose D_b contain u. Then sum d(u)<=3h.

Pointwise anchor injectivity gives z(u)<=min(7,10-d(u)) for the number of bad blocks through u. Every bad block must hit all h full rows. Pairwise block linearity gives the quadratic capacity inequality
\[
N_{bad}h^2\le D^2+\sum_u(\min(7,10-d(u))-1)d(u)^2.
\]
Using `(min(7,10-d)-1)d^2 <=20d` and D<=3h yields
\[
N_{bad}\le\min\{21,\lfloor9+60/h\rfloor\}.
\]
Thus A/C, with h>=6, now force at least16 actual selected hub-complete support blocks, rising to18,19,20 for h=7,8,9.

This is a genuine same-core theorem using shell rows, actual selected blocks, support linearity, and anchor injectivity simultaneously.

## Round 18 — delta=13 epsilon_U=0 reduced to five KP W-kernels

Commit: `ffc2b514fe66ce5cfa6a3f9202cc857454e9fd45`

Added:
- `DELTA13_EPS0_KP_KERNEL_REDUCTION.md`
- `verify_delta13_eps0_kp_kernel.py`

At delta=13, epsilon_U=0, L_U four-partite:
- U has parts 7,7,7,8 and exactly eight D-to-small H[U] cross edges;
- e(H[W])=35;
- J=bar(H[W]) is K5-free on18 vertices with118 edges;
- J cannot be four-partite because no positive four-part size sequence summing18 has target clique-edge total35;
- 118 is exactly the Brouwer non-four-partite bound, so the registered Kang-Pikhurko equality theorem applies.

The equality part-size conditions leave only base sequences
\[
(3,4,5,5),\qquad(4,4,4,5),
\]
and the proper subset parameter leaves exactly five target W-kernels:
\[
(3,4,5,5;a=1,2),\quad(4,4,4,5;a=1,2,3).
\]

This was a strict finite reduction, not yet closure.

## Round 19 — close delta=13 epsilon_U=0 four-partite-U

Commit: `fa73d6b2e81c7c501c03bb5cfa5244ca0c0ff9a5`

Added:
- `DELTA13_EPS0_KP_KERNEL_CLOSURE.md`
- `verify_delta13_eps0_kp_closure.py`

New analytic mechanism:
1. Every U vertex has at least one W neighbour because alpha(H[W])=4 and alpha(H)<=4.
2. Therefore each D point has at most four H[U] cross-neighbours.
3. If a W vertex is not complete to any U part, independent-5 avoidance forces its U-degree at least10.
4. Every low W vertex with U-degree<=9 therefore has a unique U-part label.
5. Two low vertices with the same label must be adjacent in H: otherwise their common U-neighbourhood has size at least7 while the registered nonadjacent-pair inequality gives at most4.
6. The four label classes are H-cliques. With U-part sizes 7,7,7,8 and omega(H)<=11, their capacities are 4,4,4,3. Hence at least three of the 18 W vertices must be high.
7. A high vertex of W-degree d costs at least d-2 units of W excess. The total excess is only four.
8. For each of the five KP kernels this permits only a tiny high-set list. Direct analytic colouring arguments on the KP base parts show the remaining low graph cannot fit into capacities 4,4,4,3. An independent finite verifier enumerates all high sets of cost<=4 and confirms no capacitated 4-colouring.

Conclusion:
\[
\boxed{\delta=13,\epsilon_U=0,\ L_U\text{ four-partite is excluded}.}
\]
Combined with the previously registered epsilon_U=1,2,3 closures, the entire delta=13 four-partite-U branch is now excluded.

## Current frontier after Round 19

Global:
- A–E five-template same-core compatibility: OPEN.
- A/C now have >=16 actual selected hub-complete blocks; B/D/E-full >=14; E-no-full >=35 endpoint-complete selected blocks.
- exact S-B cross-load >=max(14-beta,7+sigma).

Local core:
- delta=16: closed.
- delta=15: closed under registered contracts.
- delta=14 four-partite: closed; saturated non-four-partite remains conditional on Didin.
- delta=13 four-partite: **fully closed**.
- delta=13 non-four-partite: OPEN.
- delta<=12: OPEN.

Minimum-slack:
- slack-one branch reduced to exact kernel;
- no-slack-one branch OPEN.

Root:
- E407 Q32 OPEN / NOT_CERTIFIED.
- EG617(r=12) OPEN / NOT_CERTIFIED.

## Highest-priority next attacks

1. Use the strengthened actual selected hub-complete family together with support multiplicities, target-excess concentration, and B colour-premium to close A–E globally.
2. Independently attack delta=13 non-four-partite L_U at e(L_U)=307; no four-partite result is extrapolated.
3. Replace or independently discharge the delta=14 Didin-dependent saturated branch before any unconditional E407 claim.