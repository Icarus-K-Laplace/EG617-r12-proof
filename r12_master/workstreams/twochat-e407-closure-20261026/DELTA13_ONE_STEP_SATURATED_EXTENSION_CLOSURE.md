# E407 Q32 — delta=13 one-step-to-308 saturated full-core extension closure

Date: 2026-10-27  
Status: **PROVED_CONDITIONAL / EXCLUDED**, conditional on the one-step kernel reduction in `DELTA13_ONE_STEP_SATURATED_REDUCTION.md`. That reduction inherits the unaudited Didin 2026 dependency through the old saturated-kernel classification. Once the classified kernel is fixed, the contradiction below is elementary apart from the registered Brouwer W-side four-partite step for epsilon_U>=1.

## 1. Frozen classified one-step kernel

Use the notation of the reduction file. We have

\[
G'=K_7^A\dot\cup K_7^B\dot\cup\overline J,
\qquad G=G'+a_*v,
\]

where J is the 15-vertex C5 blow-up with parts `X,Y,C,{d0},E` of sizes `5,5,2,1,2`.

The 49 support K4s exhaust every A-B edge and every J-edge of `L'=\overline{G'}`. The unique safe augmentation edge `e=a_*v` is therefore one of fourteen uncovered A/B-J cross edges. Since a J-vertex z has exactly `2(7-d_J(z))` uncovered cross edges and J has degree sequence `7^10,6^4,4^1`,

\[
\boxed{v\in C\cup E\cup\{d_0\}.}
\tag{1.1}
\]

In particular the degree-7 X/Y vertices cannot be the J-endpoint of e.

Let

\[
\epsilon_u=d_H(u)-12,\qquad
\epsilon_U=\sum_{u\in U}\epsilon_u\in\{0,1,2,3\}.
\]

Then

\[
e(H[W])=35-\epsilon_U.
\]

The exact U-to-W degrees needed below are

\[
d_W(a_*)=5+\epsilon_{a_*},\qquad
d_W(a)=6+\epsilon_a\ (a\in A\setminus\{a_*\}),
\]
\[
d_W(b)=6+\epsilon_b\ (b\in B),
\]

and on the four-vertex clique `R_4:=C\cup E`,

\[
d_W(r)=4+\epsilon_r\quad(r\ne v),
\qquad d_W(v)=3+\epsilon_v\quad(v\in R_4).
\]

For d0,

\[
d_W(d_0)=
\begin{cases}
1+\epsilon_{d_0},&v=d_0,\\
2+\epsilon_{d_0},&v\in R_4.
\end{cases}
\tag{1.2}
\]

Recall also that d0 is target-nonadjacent to every vertex of `R_4`, A is target-anticomplete to B and to `R_4` except for the single edge `a_*v`, and B is target-anticomplete to `R_4`.

## 2. Elementary pair rule

We repeatedly use:

> **Pair rule.** If x,y are nonadjacent in H, then their common H-nonneighbours contain no independent triple. Otherwise that triple together with x,y is an independent five-set, contradicting `alpha(H)<=4`.

For epsilon_U>=1, Brouwer forces `\overline{H[W]}` to be four-partite, so W is four target-clique parts with the exact profiles listed in the reduction file.

We also use a small transversal fact. If four target-clique parts have sizes at least three and at most two cross edges, deleting at most two W vertices leaves an independent transversal. If all four parts have size at least four, deleting at most three vertices still leaves an independent transversal even with two cross edges: after deletion the worst remaining sizes are `(1,4,4,4)`, and each cross edge forbids at most one quarter of the Cartesian-product choices, so two edges cannot cover all transversals. With one cross edge, the same argument is stronger.

## 3. epsilon_U=0 is impossible without classifying W

Here `e(H[W])=35` and by (1.2)

\[
|N_W(d_0)|\le2.
\]

Put `S=N_W(d0)`.

If `|S|<=1`, then `H[W]-S` has at least 17 vertices and at most 35 edges. A graph on 17 vertices with independence number at most three has at least 40 edges, so `H[W]-S` contains an independent four-set.

If `|S|=2` and `H[W]-S` had independence number at most three, then on 16 vertices it would have at least

\[
\binom62+2\binom52=35
\]

edges. Since the original H[W] has exactly 35 edges, equality would force all 35 edges to survive deletion of S. Thus both vertices of S would be isolated in H[W], and equality gives the balanced three-clique extremal graph on the remaining 16 vertices. Two isolated vertices plus one vertex from each of the three cliques form an independent five-set in H[W], impossible.

Hence in all cases there is an independent four-set in `W\setminus N_W(d0)`. Together with d0 it gives an independent five-set in H. Therefore

\[
\boxed{\epsilon_U=0\text{ is impossible}.}
\tag{3.1}
\]

## 4. epsilon_U=1 is impossible

The W profiles are

- `(3,4,5,6), q=0`;
- `(3,5,5,5), q=1`;
- `(4,4,4,6), q=1`;
- `(4,4,5,5), q=2`.

### 4.1. If v=d0

Then `d_W(d0)=1+epsilon_d0<=2`. The transversal lemma gives an independent W-four-set avoiding its neighbourhood, contradiction.

### 4.2. If v is in C union E

Then `d_W(d0)=2+epsilon_d0<=3`. If `epsilon_d0=0`, the same deletion-two transversal lemma closes the case. Hence `epsilon_d0=1`, all U-excess is on d0, and `d_W(d0)=3`.

The two profiles whose clique parts all have size at least four are excluded by the deletion-three/two-cross-edge transversal lemma. Thus a survivor would have a K3 part. The three neighbours of d0 must be exactly that K3; otherwise all four parts remain available and the zero/one cross-edge system has an independent transversal avoiding them.

Now the special endpoint `v in C union E` has

\[
d_W(v)=3
\]

because all U-excess has already been used by d0. The pair d0,v is nonadjacent in H.

- In `(3,4,5,6),q=0`, outside the d0-K3 there are three disjoint W cliques of sizes 4,5,6. Three neighbours of v cannot exhaust any one of them, so the common nonneighbours of d0,v contain one vertex from each of the three cliques — an independent triple.
- In `(3,5,5,5),q=1`, after deleting at most three v-neighbours each of the three K5 parts has at least two available vertices. A single cross edge cannot block every three-part transversal; choose the endpoints away from that one edge. Again the common nonneighbours contain an independent triple.

Both contradict the pair rule. Hence

\[
\boxed{\epsilon_U=1\text{ is impossible}.}
\tag{4.1}
\]

## 5. epsilon_U=2 is impossible

The W profiles are

- `(3,5,5,5),q=0`;
- `(4,4,4,6),q=0`;
- `(4,4,5,5),q=1`.

### 5.1. Endpoint v=d0

Here `d_W(d0)=1+epsilon_d0<=3`.

For the profiles with all parts of size at least four, an independent transversal avoiding `N_W(d0)` exists, contradiction.

In the `K3+3K5` profile, the only way a three-point neighbourhood can hit every transversal is to be exactly the K3. This forces `epsilon_d0=2`, exhausting all U-excess. Every `r in C union E` then has W-degree four. Since d0 and r are nonadjacent and d0 has no W-neighbour outside the K3, the pair rule would require r to exhaust one of the three outer K5s. Four neighbours cannot do so. Contradiction.

### 5.2. Endpoint v in C union E

If an all-parts-at-least-four profile survived, `N_W(d0)` would have to contain a whole K4. Thus `epsilon_d0=2`, `d_W(d0)=4`, and all U-excess is used by d0. The special endpoint v has `d_W(v)=3`. The pair d0,v is nonadjacent. After removing the d0-K4, v's three neighbours cannot exhaust any of the three remaining W clique parts, and the possible single cross edge cannot block all three-part transversals. The pair rule is violated.

It remains to consider `K3+3K5`. Again `N_W(d0)` must contain the K3.

- If `epsilon_d0=1`, then d0 has exactly the K3 and only one U-excess unit remains. The special v has W-degree at most four, still too small to exhaust an outer K5 as required by the pair rule.
- If `epsilon_d0=2`, then d0 has the K3 plus at most one outer neighbour and no U-excess remains. The special v has W-degree three. Even together with the single outer neighbour of d0, the pair can cover at most four vertices of one outer K5, not all five. Again the pair rule fails.

Therefore

\[
\boxed{\epsilon_U=2\text{ is impossible}.}
\tag{5.1}
\]

## 6. epsilon_U=3 is impossible

Here

\[
H[W]=K_4\dot\cup K_4\dot\cup K_5\dot\cup K_5
\]

with no cross edges.

### 6.1. Endpoint v=d0

Now `d_W(d0)=1+epsilon_d0<=4`. To hit every independent four-part transversal, d0 must contain an entire W clique part in its neighbourhood. Therefore

\[
epsilon_{d_0}=3,
\qquad N_W(d_0)=P_0\cong K_4,
\]

and every other U vertex has zero excess.

Each `c in C union E` has W-degree four and is nonadjacent to d0. By the pair rule, `N_W(c)` must exhaust one of the three W parts outside P0. The only part small enough is the other K4, say P1. Hence

\[
N_W(c)=P_1\quad\text{for every }c\in C\cup E.
\tag{6.1}
\]

Because e joins `a_*` to d0, let `A_0=A\setminus\{a_*\}`, a K6. Every vertex w in the two K5 parts P2,P3 is nonadjacent to d0 and to every vertex of `C union E`. If w were not complete to A0 and not complete to B, choose nonneighbours `a in A0`, `b in B`, and `c in C union E`; then

\[
\{d_0,a,b,c,w\}
\]

would be independent. Thus every vertex of P2 union P3 is complete to A0 or complete to B.

Let `a_i` and `b_i` be the numbers of vertices of Pi, `i=2,3`, complete to A0 and B respectively. Then

\[
a_i+b_i\ge5.
\tag{6.2}
\]

Since B is a K7 and Pi is a K5, `b_i<=4`, so `a_2,a_3>=1`.

Fix `c in C union E`. For every `z in A0 union B`, z and c are nonadjacent and `N_W(c)=P1`. The pair rule therefore forces every such z to be complete to at least one of `P0,P2,P3`; otherwise one common nonneighbour can be chosen from each of these three disjoint W cliques.

Every A0 vertex has W-degree six. If `a_2+a_3<=2`, then (because both are positive) `a_2=a_3=1`, and (6.2) forces `b_2,b_3>=4`, impossible because the seven B vertices have only 42 W-incidences and eight B-complete W vertices would already require 56 incidences. Hence `a_2+a_3>2`, so no A0 row can use P0: P0 would cost four edges in addition to more than two forced A0-complete P2/P3 vertices.

If both P2 and P3 were used as saturation parts by different A0 rows, feasibility would force simultaneously `a_2<=1` and `a_3<=1`, again impossible. Therefore all six A0 rows saturate the same K5, say P2. Then all five vertices of P2 are complete to A0, while feasibility of those rows forces `a_3=1`.

By (6.2), at least four vertices of P3 are complete to B. For a B row, four forced neighbours in P3 prevent saturation of P0 or P2; the pair rule therefore forces every B row to saturate P3. Hence all five vertices of P3 are complete to the K7 B, creating a target K12, contradicting `omega(H)<=11`.

Thus the endpoint-d0 branch is impossible.

### 6.2. Endpoint v in C union E and epsilon_d0=2

Here `d_W(d0)=4`; its neighbourhood must be a K4 part P0. One U-excess unit remains.

The special endpoint v has W-degree `3+epsilon_v`. Since d0,v are nonadjacent, the pair rule requires v to exhaust one of the three W parts outside P0. This forces

\[
epsilon_v=1,\qquad N_W(v)=P_1\cong K_4,
\]

and exhausts all U-excess. The other three vertices of `C union E`, each of W-degree four, are forced in the same way to have W-neighbourhood P1.

Thus every vertex of the two K5 parts P2,P3, being nonadjacent to d0 and to (say) any nonspecial `c in C union E`, must be complete to A or complete to B; otherwise `d0,a,b,c,w` is an independent five-set.

Let `a_i,b_i` count A-complete and B-complete vertices in Pi. Since B is K7, `b_i<=4`, so at least one vertex of each K5 is A-complete. The special vertex `a_*` has W-degree five. The pair `a_*,c` is nonadjacent for a nonspecial c, so the pair rule forces `a_*` to saturate one of P0,P2,P3. But `a_*` is already adjacent to every A-complete vertex in both P2 and P3, at least one in each. Saturating P0 would therefore require at least `4+1+1=6` W-neighbours, while saturating either K5 would require its five vertices plus at least one forced A-complete vertex in the other K5, again at least six. This contradicts `d_W(a_*)=5`.

Hence this branch is impossible.

### 6.3. Endpoint v in C union E and epsilon_d0=3

Now `d_W(d0)=5` and no U-excess remains for any other vertex. The special v has W-degree three.

If d0 is complete to a K5, then outside that K5 the remaining W parts have sizes 4,4,5. The three neighbours of v cannot exhaust any one of them, violating the pair rule for d0,v.

Therefore d0 is complete to a K4 P0 and has one additional W-neighbour w in another part. To make the pair d0,v satisfy the pair rule, this additional vertex must lie in the other K4 P1, and v must be adjacent to the other three vertices of P1:

\[
N_W(v)=P_1\setminus\{w\}.
\tag{6.3}
\]

For every `b in B`, the pair b,v is nonadjacent. The same is true for every `a in A\setminus\{a_*\}`. Suppose such a vertex z were not adjacent to w. Then the common nonneighbours of z and v would include w, plus vertices from the three W parts `P0,P2,P3` not hit by z. In order to avoid an independent triple, z would have to exhaust at least two of those three parts. The two smallest have sizes 4 and 5, requiring at least nine W-neighbours, but every such z has W-degree six. Contradiction.

Therefore w is adjacent to all seven vertices of B and all six vertices of `A\setminus\{a_*\}`, as well as to d0. Thus w has at least fourteen neighbours in U. Since w lies in the K4 P1 it also has three W-neighbours, so

\[
d_H(w)\ge17.
\]

But the whole 47-core has total degree excess only four over degree twelve, so every vertex has degree at most sixteen. Contradiction.

This closes the last epsilon_U=3 branch.

## 7. Conditional closure of the one-step saturated fork

Sections 3–6 exclude every possible `epsilon_U in {0,1,2,3}`. Therefore, under the registered saturated-kernel classification,

\[
\boxed{
\delta=13,\quad L_U\text{ non-four-partite},\quad
L_U+e\text{ 308-edge K5-saturated for the unique safe }e
\Longrightarrow\bot.
}
\]

The dependency is exactly the old saturated-kernel classification (and its Didin+Brouwer firewall); the full-core extension contradiction itself introduces no new external theorem.

Combining this result with:

1. the unconditional/registered closure of the two-step augmentable branch, and
2. `DELTA13_SATURATED_307_CONDITIONAL_CLOSURE.md` for the already-saturated 307-edge branch,

all non-four-partite delta=13 forks are excluded **conditionally on the stated external-theorem ledger**. Together with the already closed four-partite delta=13 branch, the entire delta=13 layer is conditionally closed.

E407 Q32 as a whole remains OPEN because delta<=12 and the global five-template/shell compatibility obligations remain.
