# Progress log — E407 Q32 two-chat closure workstream

Date: 2026-10-28  
Branch: `workstream/r12-twochat-e407-closure-20261026`

Historical Rounds 1–37 are preserved in prior commits. E407 Q32 remains OPEN / NOT_CERTIFIED.

## Round 38 — close delta=12 depth-2 epsilon_U=2 terminal

Primary proof: `DELTA12_DEPTH2_EPS2_TERMINAL_CLOSURE.md`  
Independent finite audit: `verify_delta12_depth2_eps2_terminal_closure.py`

Starting point: `DELTA12_DEPTH2_EPS2_TERMINAL_REDUCTION.md` had reduced the depth-2, epsilon_U=2 branch to one W-terminal:

- `H[W]=K3 dotcup K4 dotcup K5 dotcup K6`;
- `N_W(d0)=K4`;
- the two distinct restored J-endpoints c1,c2 satisfy `N_W(c1)=N_W(c2)=K3`;
- both excess units are concentrated on d0;
- the restored A/B-side endpoints may be distinct or may coincide.

New contradiction:

1. Every point v in the two K7 components has `d_W(v)=6-r_v<=6`, where r_v is its restored-edge incidence.
2. The pair `(v,d0)` is nonadjacent, so the common-nonneighbour rule forces v to contain one entire W-component among K3,K5,K6.
3. Unless v is the unique possible common restored endpoint for both c1,c2, it is nonadjacent to at least one ci; that pair forces v to contain one entire component among K4,K5,K6.
4. Since `d_W(v)<=6`, v cannot simultaneously cover K3 and K4. Hence every non-exceptional v is complete to exactly one of K5,K6.
5. Any labelled pair a in the first K7 and b in the second K7 is nonadjacent. If both labels are K5, their neighbourhood union cannot fully cover a second W-component; if both labels are K6, the union is just K6. Hence cross-K7 labels must be opposite.
6. If the restored A/B endpoints are distinct, all 14 points are labelled, making each K7 uniformly K5- or K6-complete and producing K12 or K13.
7. If both restored edges share one A/B endpoint, the other six points on that K7 and all seven on the opposite K7 remain labelled. Opposite-label forcing gives either a K6+K6=K12 or a K7+K6=K13.

Thus the unique terminal is impossible under `omega(H)<=11`.

Status:

- delta=12 / non-four-partite / depth2 / epsilon_U=2: **PROVED_CONDITIONAL / CLOSED**;
- dependency: registered 308-edge saturated-kernel classification plus the preceding terminal reduction;
- Didin: **not used** in this terminal closure;
- delta=12 as a whole: OPEN;
- E407 Q32: OPEN;
- EG617(r=12): OPEN.

## Current highest-priority frontier

1. delta=12 depth-2 epsilon_U=3,4, where W is already four-clique structured;
2. delta=12 depth-3 equality terminals;
3. delta=12 four-partite-U and delta<=11;
4. five-template same-core labelled incompatibility;
5. independent discharge/replacement of the Didin-dependent saturated branches.
