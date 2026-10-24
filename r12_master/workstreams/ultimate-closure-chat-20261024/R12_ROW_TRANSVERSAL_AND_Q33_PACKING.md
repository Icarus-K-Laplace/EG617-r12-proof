# R12 row-transversal theorem and exact-129 high-k witness packing

Date: 2026-10-25 (local continuation of the 2026-10-24 sprint).  
Status: **PROVED necessary-structure theorem under the frozen T61 / V12 contracts; E407/E408 terminal exclusions remain OPEN.**

## 1. Frozen notation

Let F be the 61-vertex target residual, with alpha(F)<=5 and omega(F)<=11. Choose a regular pivot p, shell A=N_F(p), |A|=13, and core H=V(F)\(A union {p}), |H|=47. For a in A, write

    D_a=N_F(a) intersect H,     t_a=|D_a|.

The shell missing graph is M=bar(F[A]); thus ab in E(M) means a,b are nonadjacent in F. For b in B=A\S, write

    k_b=|N_M(b) intersect S|.

In E407 Q32, B is a regular K10, so t_b=k_b<=3. In E408 Q33/d3, t_b=k_b+g_b and the exact budget is

    beta + X + G_B = 3,
    beta=e(M[S]),  X>=0,  G_B=sum_B g_b.

The retained core interface gives e(H)=284 and sum_H(d_H-12)=4 in E407 Q32 and E408 Q33. E408 Q32 instead has e(H)=285 and core excess6; no excess-4 argument is silently transferred to that layer.

## 2. Row-union theorem

**Lemma 2.1 (PAIR-13 / TRI-24).** Under the retained R(3,35) and R(2,24) exclusions:

1. If ab is a missing shell edge, then |D_a union D_b|>=13.
2. If abc is a missing shell triangle, then |D_a union D_b union D_c|>=24.

**Proof.** If |D_a union D_b|<=12, at least35 core vertices remain anticomplete to both a and b. The retained R(3,35) exclusion supplies an independent 4-set there, which together with a,b is an independent 6-set in F, contradiction. Similarly, if a missing triangle has row union at most23, at least24 core vertices remain anticomplete to all three; R(2,24) supplies an independent 3-set, again producing an independent 6-set. ∎

These inequalities are independent of the E407 enumeration threshold. They apply to the 284-edge E407 Q32 and E408 Q33 cores, and to E408 Q32 provided the same retained hereditary inputs are valid.

## 3. Row-transversal theorem

**Theorem 3.1.** Let a,b be shell vertices with ab in E(M) and t_a<=12. Then X_a=H\D_a has at least35 vertices and alpha(X_a)=4. Every independent 4-set Q in X_a intersects D_b.

**Proof.** Since |X_a|=47-t_a>=35, the retained R(3,35) exclusion gives alpha(X_a)>=4; since alpha(H)<=4, equality holds. If an independent 4-set Q in X_a avoided D_b, it would be anticomplete to both a and b. As ab is a missing shell edge, Q union {a,b} would be an independent 6-set in F, contradiction. ∎

Equivalently, for each shell row a, the family of core rows {D_b : ab in E(M)} is a transversal family for all maximum independent 4-sets of X_a. This quantifies over **every** such independent 4-set, not only a selected witness Q_b.

### Exact template consequences

- If t_a=10 and b is a regular k_b=3 row missing to a, D_b is a 3-vertex transversal of all independent 4-sets in the 37-vertex X_a. No set of at most two vertices can be such a transversal, because deleting it leaves at least35 vertices and hence an independent 4-set.
- If t_a=11 and b is a regular k_b=2 row missing to a, D_b is a minimum 2-vertex transversal in the 36-vertex X_a. No singleton can hit every independent 4-set, because deleting one vertex leaves35 vertices.
- If t_a=12 and b is a regular k_b=1 row missing to a, its singleton D_b is a 1-vertex transversal in the 35-vertex X_a.

This gives the following common support constraints for the five E407 Q32 templates:

| Template | Mandatory transversal system |
|---|---|
| A: M[S] empty, weights (12,10,10) | At least six full-S rows are 3-transversals simultaneously for both 10-row hub cores. Their D_b are disjoint from each 10-row hub support by PAIR-13. Any singleton row missing to the 12-row hub has its singleton support disjoint from that hub. |
| B: M[S] empty, weights (11,11,10) | At least eight B rows have k_b>=2. Pair rows are 2-transversals for both 11-row hub cores and disjoint from those hub supports; full rows are 3-transversals, including for the 10-row hub. |
| C: one missing S-edge, weights (12,11,10) | At least six full-S rows are 3-transversals for the 10-row hub and disjoint from its support. For each such row, if x,y are its intersections with the 12- and 11-row hub supports, then x<=2, y<=1, x+y<=2. The missing triangle on the S-edge and b gives this last joint bound. |
| D: one missing S-edge, all weights 11 | At least seven B rows have k_b>=2. Each pair-type row is a 2-transversal for the two hubs it misses and is disjoint from both. For each full row b, with x,y its intersections with the two endpoints of the S missing edge and z their mutual intersection, PAIR-13/TRI-24 give x<=1, y<=1 and x+y+z-w<=1, where w is the triple intersection. Thus a full row cannot intersect both endpoint supports. |
| E: M[S]=P3, weights (12,11,11) | At least five B rows have k_b>=2. Center-singleton rows are singleton transversals for the 12-row hub and disjoint from it. Pair-of-ends rows are 2-transversals for both 11-row hubs and disjoint from each. Full rows satisfy the joint bound x_center+x_end+z-w<=2 for each center-end missing triangle. |

The count floors used above are exactly those in Q32_KERNEL_COVERAGE.md: A/C have n3>=6; B has n2+n3=10-n0>=8; D has na+nb+n3=10-n0>=7; E has n2+n3>=5. For E, equality n2+n3=5 forces the unique count profile (n0,n1,n2,n3)=(0,5,0,5).

These constraints are not a claim that the row supports are equal or disjoint unless the stated theorem proves that relation.

## 4. Stronger exact-129 component packing for E408 Q33

Assume the retained exact-129 factor theorem and seven-block equality system. For each exact-129 non-target color C, C[R] has ten isolated K5 components and an 11-vertex gadget U with alpha(C[U])=2.

**Lemma 4.1.** Every exact-129 color has at least six K5 components containing a B vertex and no S vertex.

**Proof.** At most three K5 components can contain any S vertex, because there are only three S vertices and the components are disjoint. Hence at least seven K5 components contain no S vertex.

A K5 component cannot contain two B vertices: B is a target clique in F, so the edge between any two B vertices is target-colored, not C-colored. A K5 component with no S, no B, and no pivot p would consist of five vertices of H, forming an independent 5-set in H, contradicting alpha(H)<=4. At most one no-S component can contain p without B. Thus at least six of the at least seven no-S components contain a B vertex. ∎

So at most four of the ten B labels can lie outside the no-S K5 components of any exact-129 color.

**Lemma 4.2 (high-k witness packing).** In the E408 Q33/d3 shell, at least five B vertices have k_b>=2. Therefore, for every exact-129 color, at least one no-S K5 component has the form {b} union Q with k_b>=2 and Q subset H, |Q|=4. If beta is 0 or 1, at least two such components exist per exact-129 color.

**Proof.** The exact budget gives c_S=sum_B k_b>=22-beta. If h is the number of B vertices with k_b>=2, then c_S<=10+2h, hence h>=ceil((12-beta)/2), which is at least6 for beta in {0,1} and at least5 for beta in {2,3}. By Lemma 4.1 at most four B labels lie outside no-S components, so at least h-4 high-k labels occur in no-S components. ∎

For each such component, Q is independent in H and anticomplete to b. Because b is missing to at least two vertices of S, Q must hit at least two S rows; otherwise Q plus b and an unhit missing hub would form an independent 6-set. By Lemma 2.1 / the universal shell-support lemma, Q hits at least three distinct shell rows in total.

There are at least eight exact-129 colors because sum_C s_C=3. Therefore the E408 Q33/d3 interface supplies:
- at least **eight** labelled high-k, no-S independent-4 witnesses across distinct colors;
- at least **sixteen** if beta is 0 or 1;
- each selected witness hits at least two S rows and at least three shell rows total.

The selected Q sets have pairwise intersections at most one across distinct colors: otherwise their K5 components would share an edge assigned two different colors. If two selected components use the same B label, their Q sets are disjoint.

This is a labelled packing theorem, not a contradiction by itself. It must be combined with the actual H adjacency and the 62-unit global duplicate system; no scalar-capacity contradiction is asserted here.

## 5. What this closes and what remains open

**Proved under the stated contracts:**
1. PAIR-13 / TRI-24 row-union bounds.
2. The all-independent-4-set transversal property for every missing shell edge.
3. The template-specific support restrictions in Section 3.
4. At least six no-S B-components per exact-129 color, and the high-k witness packing in Section 4.

**Still OPEN:**
- simultaneous labelled 47-core completion for any of the five E407 Q32 templates;
- E408 Q32 exhaustive coverage at the required repivot threshold 29;
- E408 Q33 joint compatibility of the high-k witness packing, all core rows, and the seven-block duplicate system.

No proof status is promoted to EG617(r=12) complete.
