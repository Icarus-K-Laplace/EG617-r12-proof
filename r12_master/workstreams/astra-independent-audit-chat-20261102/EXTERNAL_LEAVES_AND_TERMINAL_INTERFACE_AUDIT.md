# External theorem leaves and terminal-interface audit

Date: 2026-11-03  
Frozen integration audited: `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`  
Audit branch: `workstream/r12-astra-independent-audit-20261102`

## 1. External theorem statements and exact substitutions

### 1.1 Turán

For a graph on n vertices with independence number at most k, its complement is K_{k+1}-free. Turán therefore gives
`e(G) >= p_k(n) = k*binom(q,2)+q*r` for n=kq+r, 0<=r<k.

This is exactly the lower color-class bound used to derive the hereditary caps
`D(n)=binom(n,2)-11*p_12(n)`. The use is standard and all parameters are integer-exact.

### 1.2 Kang–Pikhurko, Theorem 1

The primary paper's Theorem 1 assumes n>=r+3 and r>=2. In the regime r<=(n-1)/2 it gives
`e(L) <= t_r(n)-floor(n/r)+1`
for every K_{r+1}-free graph L that is not r-partite.

Two applications were checked:

- **Contextual 49-set:** n=49,r=12. The hypotheses hold (49>=15 and 12<=24). The Turán graph has part sizes 5,4,...,4, so `p_12(49)=76` and `t_12(49)=1100`. Thus `e(L)<=1100-4+1=1097`; since `binom(49,2)=1176`, the complementary color graph has at least79 edges. This is exactly the 79 used in the 319-versus-307 contradiction.
- **25-set common-neighborhood bound:** n=25,r=2. The hypotheses hold and the theorem gives `e(L)<=t_2(25)-floor(25/2)+1=156-12+1=145`. The low-edge proof also contains an elementary shortest-odd-cycle/Mantel derivation of this same 145 bound. The corrected dependency proposal designates that elementary route for LOW285, so SECOND_TURAN is load-bearing only for CONTEXTUAL49_EMPTY.

The contextual-49 application correctly checks both conditions that can be easy to conflate: L is K13-free because the other color graph has independence at most12; L is not12-partite because a 12-partition would partition that color graph into12 cliques of size at most4, covering at most48 vertices.

### 1.3 Andrásfai–Erdős–Sós, Theorem 1.1

The cited theorem says that a K_s-free graph with
`delta > ((3s-7)/(3s-4))*n`
is (s-1)-partite. At s=4 the threshold is 5n/8.

The CORE211 application is exact: if H in R(3,35) had e(H)=210, its minimum degree is at least12 by M4 and hence exactly12; its complement L is 22-regular, K4-free, on35 vertices. Since `22 > 5*35/8 = 21.875`, AES makes L 3-partite. Then H is the union of three cliques, one of size at least12, contradicting omega(H)<=11. Therefore e(H)>=211. No equality case or stronger AES conclusion is used.

### 1.4 Brooks

If the least color graph G had minimum degree at least12, its edge count at most870 forces every degree to equal12. Every connected component with maximum degree12 is not K13 because omega(G)<=12; components with smaller maximum degree are trivially 12-colorable (including a possible K12 component). Brooks therefore gives a proper vertex 12-coloring of G. One independent color class has at least ceil(145/12)=13 vertices, contradicting alpha(G)<=12. The theorem is used only for this minimum-degree reduction.

## 2. Exact terminal interfaces

| Interface | Required contract | Derived result | Audit |
|---|---|---|---|
| Original coloring -> least color graph | K145, 12 edge colors, every13-set has all colors | e<=870, alpha<=12, omega<=12, all D caps | PASS |
| Contextual R(4,49) | 49-vertex induced subgraph, alpha<=4, omega<=11, D caps | delta>=13; e>=319; other11 colors each >=79, so e<=307 | PASS |
| T61 extraction | Same original induced graph; maximal K12 packing | alpha(F)<=5, omega(F)<=11, caps, 397<=E<=408 | PASS, conditional on recurrence replay and its analytic rules |
| h12 terminal | F has61 vertices, delta12; every pivot core is R(4,48) | D48 gives delta(core)>=12 and e(core)>=310; q>=20; q=20 repivot inserts a vertex of degree<=11 into another R(4,48) core | PASS |
| h13 terminal | F has61 vertices, delta13; every regular pivot core is R(4,47) | GATE47 + LOW285 + EX286 gives e(core)>=287; COVER gives Q>=29; E407/E408 layers contradicted | PASS |
| Other degrees | Same T61 contract | delta<=11 creates contextual R(4,49); delta>=14 gives E>=427 | PASS |

Important scope check: the h13 certificates are applied only after the minimum degree of F has been shown to be13. They are not applied to a graph of minimum degree12 merely because it has some degree13 vertex. The h12 branch uses actual48-cores and the D48 gate; it does not transport the47-point floor.

### 2.1 The 47-point strict floor

For an actual R(4,47) core C:
- if e(C)<=286, M6 proves delta(C)>=12;
- if e(C)<=285, the abstract LOW285 theorem contradicts this;
- if e(C)=286, E286 contradicts this.

Hence e(C)>=287. This is the exact three-premise chain used by E407/E408. M6 alone does not say that every R(4,47) graph has minimum degree12; the edge threshold is essential.

### 2.2 The 48-point floor and q20 repivot

For J in R(4,48), the independent D48 gate gives delta(J)>=12. If delta>=13 then e(J)>=312. If delta=12, the35-core is R(3,35), has delta>=12 and e>=211 by CORE211. The12-shell has q>=20. Equality q=20 has the K_(2,r) plus isolates form, 6<=r<=10. Repivoting at a low leaf replaces its two core neighbors by the two hubs; each inserted hub has at most10 old-core neighbors plus the edge to the other inserted hub, hence degree at most11. The new35-core is still R(3,35), contradicting its minimum-degree12 theorem. Therefore q>=21 and e(J)>=78+21+211=310.

For the T61 h12 branch, the same q20 shell occurs over a48-core, and the repivoted object is another actual R(4,48) core. D48, not the47-point theorem, gives its minimum degree12. The inserted-hub contradiction is therefore at the correct order.

### 2.3 Explicit completion of the K2,2 attachment step

The h12 equality proof says all exterior attachments to the K2,2 meet one fixed side. The justification is short but worth making explicit.

Let the cycle be K_{2,2} with sides X={x1,x2}, Y={y1,y2}; the eight exterior vertices are independent. Since z>=11 and the cycle contributes4 edges, there are at least7 exterior-to-cycle edges. Triangle-freeness immediately implies that no exterior vertex can attach to both sides: every X-Y pair is an edge of K_{2,2}, so such two attachments would form a triangle. If there were attachments on both sides, they would therefore come from two distinct exterior vertices. Choose one attachment edge to X and one to Y; they are disjoint, and the two unused cycle vertices form the opposite X-Y edge. These three edges are a 3-matching, contradiction. Hence all exterior attachments meet one fixed side. The subsequent weight argument rules out a one-hub attachment and forces every active exterior vertex to meet both hubs.

This expands a compressed sentence in H12 Section2; it does not change the theorem.

## 3. Dependency-map status

The frozen integration `PROOF_DAG.json` is acyclic but is not a complete semantic crosswalk. The isolated corrected proposal adds:
- `GATE47` to the47-point floor;
- `D48` to the48-point floor and h12 closure;
- `LOWER_ORDER` as a Q20 dependency;
- `SHELL_MATCHING_BOUNDS` as a dependency of Q20, COVER q>=29, and the recurrence.

The corrected proposal is acyclic with all parent references resolving and every node reachable from K145_EMPTY. It remains an audit proposal; the frozen integration branch was not edited. The root verifier checks graph syntax/acyclicity, not theorem-ledger completeness or the truth of every edge. The external theorem leaves BROOKS, TURAN, AES and SECOND_TURAN should receive exact statement/hypothesis rows in a final public ledger.

## 4. Current disposition

No concrete counterexample or parameter mismatch was found in the external theorem applications or the h12/h13 terminal interfaces checked here. This materially supports the fixed-r=12 proof chain, but it is not a certification of the entire theorem package:

- the frozen root verifier has not been run from a clean local checkout in this audit session;
- the root verifier does not rerun the full COVER shell enumeration or the separate E286 verifier (component-level independent reproductions are recorded in the earlier audit files);
- the frozen proof DAG remains semantically incomplete until the corrected proposal is promoted;
- no Lean kernel certification of K145 and no external referee review have been established.

The mathematical scope remains only the fixed r=12 statement: K145,12 colors,13-vertex subsets. No all-r solution is claimed.


## 5. Fresh finite cross-checks added in this pass

I independently enumerated the four-seed support multisets, up to all 24 seed relabelings, from the defining constraints:
- h in {3,4,5};
- each support has size2,3,or4;
- every seed incidence degree is at least2;
- the total incidence count is h+5;
- no seed incidence degree exceeds4.

The resulting orbit counts are exactly h=3:2, h=4:3, h=5:5, for ten total. The h=5 orbits split into one degree pattern (4,2,2,2) and four patterns (3,3,2,2), matching the ten support cases in the E286 table. This checks the combinatorial exhaustiveness of the support table independently of its verifier.

I also exhaustively evaluated the displayed scalar functions over their finite positive missing-set domains. The exact minima are:
- f11: 6, uniquely at (2,2);
- f10,11: 4, uniquely at (2,3);
- f9,11: 2, uniquely at (2,4);
- f10,10: 2, uniquely at (3,3);
- the E286 three-star, two-K9-completer, and additional-K10-completer functions: minima 6,5,5, respectively, with equality sets matching the source's stated boundary cases.

Finally, the E286 independent-four-set lower bound was recalculated for q=1,...,8 and gives 350,346,342,337,331,325,318,310; all exceed286. These are finite arithmetic cross-checks only; the analytic blocker and shared-leaf arguments remain the proof.
