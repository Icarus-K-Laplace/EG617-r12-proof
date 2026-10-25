# E407 Q32: exclude every 47-core extension of the saturated local model

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL for the explicit local model**, under the retained 47-core/49-witness contract and Brouwer's second-Turán theorem. The general saturated-kernel classification is recorded separately in DELTA14_SATURATED_KERNEL_CLASSIFICATION.md and depends on the external-theorem contract in DELTA14_SATURATED_ALPHA_CRITICAL_REDUCTION.md.

## 0. Audit note

An earlier draft used the false implication `|S_P| <= 11-|P|` for the total common-neighbour set of a clique (P), inferred from (omega(H)le11). That inference is invalid because (S_P) need not be a clique. The earlier draft has been withdrawn. The proof below replaces those cardinality arguments with explicit independent-set and incidence-capacity arguments; it does not use a total common-neighbour bound derived from clique number alone.

## 1. Fixed local model and core ledger

Let
[
H[U]=K_7^Adotcup K_7^Bdotcupoverline J,
qquad |U|=29,quad |W|=18,
]
where (J) is the verified (C_5)-blow-up with cyclic part sizes ((5,5,2,1,2)). Write its 15-vertex block as (X,Y,C,{d_0},E), with sizes (5,5,2,1,2), respectively. The relevant adjacencies in (H[U]) are:
- (A,B) are disjoint (K_7)'s and are anticomplete to one another and to the 15-vertex block;
- (X,Y) are (K_5)'s anticomplete to one another;
- (Ccup E) is a (K_4), anticomplete to (d_0);
- (d_0) is complete to (Xcup Y), and anticomplete to (Ccup E);
- each of (C,E) is anticomplete to one of (X,Y), respectively.

The degree sequence in (H[U]) is (6^{14},7^{10},8^4,10^1), with (d_{H[U]}(d_0)=10). Let
[
epsilon_v=d_H(v)-12,qquad
epsilon_U=sum_{uin U}epsilon_u.
]
The retained core contract gives
[
e(H[W])=34-epsilon_U,quad
0leepsilon_Ule2,quad
d_H(d_0,W)=2+epsilon_{d_0}le2+epsilon_U.
]
Every (uin U) is complete to at least one W clique component whenever (H[W]) is a disjoint union of four cliques: otherwise choosing one non-neighbour from each component together with (u) gives an independent 5-set.

## 2. (epsilon_U=0) is impossible

The exact W-profile audit gives part sizes and cross-edge counts
[
(3,4,5,6),q=0;quad (3,5,5,5),q=1;quad
(4,4,4,6),q=1;quad (4,4,5,5),q=2.
]
All parts are cliques in (H[W]), with at most two cross-edges. Here (d_0) has exactly two W-neighbours.

For any deletion set (Ssubseteq W) with (|S|le2), an independent transversal of the four parts remains after avoiding (S). To see this, count the Cartesian-product transversals: if two deleted vertices lie in one part, each cross-edge forbids at most (1/3) of the choices; if they lie in different parts, each forbids at most (1/4); in either case the total forbidden fraction from at most two edges is strictly below one. The cases (|S|le1) are easier. Apply this with (S=N_W(d_0)). The independent transversal together with (d_0) is an independent 5-set, contradiction.

## 3. (epsilon_U=1) is impossible

The W-edge ledger gives (e(H[W])=33). The exact four-partite/Turán profile audit leaves only (K_3dotcup3K_5), (3K_4dotcup K_6), or (K_4dotcup K_4dotcup K_5dotcup K_5) with one cross-edge.

### 3.1. (3K_4dotcup K_6)

Since (d_H(d_0,W)=2+epsilon_{d_0}le3), (d_0) cannot be complete to any W component, all of which have size at least four. This contradicts the complete-to-a-component property above.

### 3.2. (K_4dotcup K_4dotcup K_5dotcup K_5) with one cross-edge

The four clique parts have sizes at least four. Since (|N_W(d_0)|le3), there is an independent transversal avoiding (N_W(d_0)): after deleting at most three vertices, the remaining part sizes are bounded below by ((1,4,4,4)), ((2,3,4,4)), or ((3,3,3,4)); the single cross-edge forbids at most (1/4), (1/6), or (1/9) of all transversals. Adding (d_0) gives an independent 5-set, contradiction.

### 3.3. (K_3dotcup3K_5)

The vertex (d_0) must be complete to the (K_3), so (epsilon_{d_0}=1). Every vertex of (Ccup E) has W-degree four; to be complete to a W component it must be complete to the (K_3), with exactly one extra edge to a vertex in one of the three (K_5)'s. Thus no K5 vertex is adjacent to (d_0), and at most one K5 vertex can be complete to all four vertices of (Ccup E): each of those four vertices has only one W-neighbour outside the K3.

For any (w) in a K5 component, the set ({a,b,c,d_0}) is independent for every (ain A), (bin B), and (cin Ccup E). If (w) were not complete to any of (A,B,Ccup E), choose a non-neighbour from each of these three sets; together with (d_0) and (w), this would be an independent 5-set. Therefore each of the 15 K5 vertices must be complete to (A), or complete to (B), or complete to all of (Ccup E).

Each vertex of (A) has exactly six W-neighbours, so there are (42) A–W edges total; a K5 vertex complete to (A) consumes seven of these. Hence at most (lfloor42/7floor=6) K5 vertices are complete to (A). The same bound holds for (B). As shown above, at most one K5 vertex is complete to all of (Ccup E). Consequently at most (6+6+1=13) K5 vertices can satisfy the required condition, but there are 15. Contradiction.

All three W profiles are excluded, so (epsilon_U
e1).

## 4. (epsilon_U=2) is impossible

Turán equality forces
[
H[W]=P_0dotcup P_1dotcup P_2dotcup P_3
=K_4dotcup K_4dotcup K_5dotcup K_5,
]
with no cross-edges. Since (d_0) has at most four W-neighbours and must be complete to a W component, (epsilon_{d_0}=2) and (d_0) is complete to one K4, called (P_0). All other U-excess is zero. Thus W-degrees are six for A/B vertices, five for X/Y, four for C/E, and four for (d_0). Every U vertex is complete to a unique W part. Each C/E vertex must be complete to (P_0) or (P_1), and therefore has no neighbours in either K5 part.

### 4.1. A/B assignments

For any (ain A,bin B), the triple ({d_0,a,b}) is independent. If (a,b) are both assigned to the same W part, or if either is assigned to (P_0), their extra-edge budgets outside their assigned parts are too small to cover two of the other parts among (P_1,P_2,P_3). Therefore there are two distinct components among (P_1,P_2,P_3) each containing a vertex nonadjacent to both (a,b); these two vertices together with (d_0,a,b) form an independent 5-set. Hence A and B have disjoint assignment supports, and neither uses (P_0).

Because A and B are each cliques, the number of their vertices assigned to a part (P) is at most (11-|P|). The assignment capacities on ((P_1,P_2,P_3)) are therefore ((7,6,6)) for each side separately. Since each side has seven vertices and their supports are disjoint, one side must assign all seven vertices to (P_1), and the other side must split its seven vertices between (P_2) and (P_3), with both groups nonempty. Assume A fills (P_1).

Each A vertex has exactly two W-neighbours outside (P_1), so there are at most (14) A-edges into (P_2cup P_3). Any K5 vertex complete to A consumes seven such edges. Thus at most two vertices in (P_2cup P_3) can be complete to A.

Let (B_i) be the B vertices assigned to (P_i), for (i=2,3). Both (B_2,B_3) are nonempty. Each B vertex has five neighbours in its assigned K5 and only one extra W-neighbour outside it. At most one vertex of (P_2) can be complete to B: otherwise any vertex in (B_3) would need two extra W-neighbours. Similarly, at most one vertex of (P_3) can be complete to B. Hence at most two K5 vertices can be complete to B.

### 4.2. Final independent-set contradiction

Fix any (win P_2cup P_3). It is nonadjacent to (d_0) and to every vertex of (Ccup E). For every (ain A,bin B,cin Ccup E), the set ({a,b,c,d_0}) is independent. If (w) were not complete to A and not complete to B, choosing non-neighbours (a,b) and any (cin Ccup E) would produce an independent 5-set. Thus every one of the ten K5 vertices in (P_2cup P_3) must be complete to A or complete to B.

But at most two are complete to A and at most two are complete to B, giving at most four such vertices, not ten. Contradiction.

## 5. Conclusion and scope

For the explicit local model, all three possible values (epsilon_Uin{0,1,2}) are excluded, so it has no full 47-core extension under the retained core contract. DELTA14_SATURATED_KERNEL_CLASSIFICATION.md further identifies every admissible saturated kernel (J) with this blow-up, conditionally on the alpha-critical reduction and its external-theorem dependencies. Therefore the general (delta=14), non-four-partite, (K_5)-saturated terminal is conditionally excluded.

This does not close the (deltale13) cases, all five shell templates as a global compatibility problem, or the original (K_{145})-to-T61 bridge. E407 Q32 and EG617((r=12)) remain OPEN / NOT_CERTIFIED overall.
