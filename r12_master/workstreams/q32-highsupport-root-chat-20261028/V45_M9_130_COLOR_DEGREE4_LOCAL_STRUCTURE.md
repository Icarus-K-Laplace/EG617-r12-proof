# Q32 v=45,m=9 — source-correct local structure of a 130-edge color at a degree-four vertex

Date: 2026-10-28  
Status: **PROVED_CONDITIONAL local lemma; no W-pair conclusion.**

This note replaces the unsupported inference that two degree-four vertices in a 130-edge nonexact color must be joined by that color.

## 1. Contract

Let D be a non-target color graph on the 61-point residual with
- e(D)=130;
- alpha(D)<=12;
- omega(D)<=5;
- delta(D)>=4 (from the audited 130-edge minimum-degree theorem).

Let v be any vertex with d_D(v)=4. Write S=N_D(v), |S|=4, and let N be the 56 vertices nonadjacent to v, excluding v.

## 2. Second-Turán lower bound on D[N]

Because v is nonadjacent to every point of N, alpha(D[N])<=11. Also omega(D[N])<=5. Hence J=bar(D[N]) is K12-free.

J is not 11-partite: if it were, D[N] would be a union of eleven D-cliques, each of size at most5, covering at most55 vertices, while |N|=56.

For (n,r)=(56,11), the cited Kang–Pikhurko theorem is in range. The balanced Turán graph has part sizes 6,5^10, so
- C(56,2)=1540;
- t_11(56)=1540-[C(6,2)+10C(5,2)]=1425;
- p_11(56)=t_11(56)-floor(56/11)+1=1421.

Therefore
`e(D[N]) >= C(56,2)-p_11(56)=1540-1421=119.`

## 3. Exact neighborhood ledger

Let a=e(D[S]) and b=e_D(S,N). Since v has exactly four edges to S,
`130 = e(D[N]) + 4 + a + b`.
Thus `a+b<=7`.

Each s in S already has one D-edge to v and must have total D-degree at least4. Summing the remaining degrees over S gives
`2a+b >= 4(4-1)=12`.

Combining,
`a >= 5`.
Since S has four vertices, `a<=C(4,2)=6`. There are exactly two cases:

### Case A: a=5

Then `b=2` and `e(D[N])=119`. The graph D[S] is K4 minus one edge. Its two degree-two vertices (the endpoints of the missing edge) each need exactly one edge to N; the other two vertices have no edge to N. All four vertices of S have degree exactly4 in D.

### Case B: a=6

Then S is K4 and `b in {0,1}`. If b=0, `e(D[N])=120` and `{v} union S` is an isolated D-colored K5. If b=1, `e(D[N])=119` and exactly one vertex of S has one edge to N; the other three have degree4.

No other local pattern is compatible with the 130-edge budget and delta(D)>=4.

## 4. Application to v=45,m=9

At each W-point w_i, the 130-edge nonexact color has degree4 and all four neighbors lie in H. The local lemma says its four-neighbor set is either K4 or K4 minus one edge, with at most one or two edges, respectively, leaving that set for N_D(w_i).

This local lemma **does not** force w_1w_2 to have color D: the Case-A and Case-B neighborhood structures are both compatible with w_1,w_2 being nonadjacent in D. Thus the local lemma alone leaves `e_H(W) in {0,1}` and `e(bar(H[U])) in {730,731}` undetermined. However, that binary variable is no longer load-bearing: Section 6 below gives a direct contradiction at either W-point without deciding the W-pair edge.

## 5. Proof boundary of the local neighborhood lemma

Sections 2–3 are a local consequence of the registered 130-edge contract, the already-audited `delta(D)>=4` theorem, and the source-checked Kang–Pikhurro extremal bound at (56,11). By themselves they do not close a Q32 terminal. The stronger core-only exclusion is the separate argument in Section 6.


## 6. Strengthening when all four neighbors lie in the target core

Assume additionally that S is contained in H and alpha(H)<=4. Then S cannot induce K4: if it did, {v} union S would be a D-colored K5 wholly inside H, hence a target-independent 5-set. So only Case A from Section 3 can occur:
`e(D[S])=5,` `e_D(S,N)=2,` `e(D[N])=119`,
and D[S]=K4-e.

Let a,b be the two endpoints of the missing edge and c,d the two central vertices. The degree ledger forces exactly one S-N edge at each of a,b and none at c,d. Thus a has D-neighborhood {v,c,d,z} for one z in N. The vertices v,c,d form a triangle; z is nonadjacent to v by definition of N and to c,d because c,d have no neighbors in N. Hence D[N_D(a)] is a triangle plus an isolated vertex and has only 3 edges.

But a itself has degree four, so applying the already-proved Section 2 to a requires `e(D[N_D(a)])>=5`, contradiction.

Therefore:
> **No vertex v in H can have d_D(v)=4 with all four D-neighbors in H.**

This is stronger than any W-pair implication. In the v=45,m=9 normal form, it closes the branch as soon as one W-point is forced to be degree four/core-only in the 130-edge color. The unresolved value `e_H(W) in {0,1}` remains correct, but is no longer load-bearing for that closure.
