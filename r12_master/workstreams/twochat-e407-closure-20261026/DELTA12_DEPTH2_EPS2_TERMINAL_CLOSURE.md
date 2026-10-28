# E407 Q32 — delta=12 depth-2 epsilon_U=2 terminal closure

Date: 2026-10-28  
Status: **PROVED_CONDITIONAL / CLOSED** under `DELTA12_DEPTH2_EPS2_TERMINAL_REDUCTION.md` and the registered 308-edge saturated-kernel classification. This closes only this terminal; E407 Q32 remains OPEN / NOT_CERTIFIED.

## 1. Frozen terminal

Work in the unique survivor produced by `DELTA12_DEPTH2_EPS2_TERMINAL_REDUCTION.md`.

After two K5-safe augmentations the classified graph is
\[
G_2=K_7^A\dot\cup K_7^B\dot\cup \overline J,
\]
where the original target graph `H[U]` is obtained from `G_2` by restoring exactly two target edges from `A\cup B` to two distinct vertices
\[
c_1,c_2\in C\cup E.
\]
The unique degree-4 point of `J` is `d_0`. The preceding reduction proves:

1. all U-excess equals two and is concentrated at `d_0`;
2. the two J-endpoints `c_1,c_2` are distinct;
3. `H[W]=K_3\dot\cup K_4\dot\cup K_5\dot\cup K_6`;
4. `N_W(d_0)=K_4`;
5. `N_W(c_1)=N_W(c_2)=K_3`;
6. every point of `C\cup E` is complete to the same `K_3`.

The only unresolved choice is the pair of endpoints of the restored edges on the `A\cup B` side: they may be distinct or may coincide.

We use the frozen pair rule:

> if `x,y` are nonadjacent in `H`, then their common W-nonneighbours contain no independent triple.

Because `H[W]` is a disjoint union of four cliques, this has the following equivalent consequence.

### Lemma 1.1 — component-cover form of the pair rule

If `x,y` are nonadjacent in H, then
\[
N_W(x)\cup N_W(y)
\]
contains every vertex of at least two of the four components `K3,K4,K5,K6`.

**Proof.** If the union failed to cover three of the four components completely, the common W-nonneighbour set would meet at least three distinct components. Choosing one point from each gives an independent triple, contradicting the pair rule. QED.

## 2. W-degrees on the two K7 parts

Let `v\in A\cup B`, and let `r_v\in\{0,1,2\}` be the number of restored target edges incident with `v`.

All U-excess is on `d_0`, so `epsilon_v=0`. In `H[U]`, the vertex `v` has its six neighbours inside its own K7 plus exactly `r_v` restored neighbours. Therefore
\[
\boxed{d_W(v)=6-r_v\le6.}\tag{2.1}
\]

Every such v is H-nonadjacent to d0, since the two restored edges avoid d0. Hence Lemma 1.1 applied to the pair `(v,d0)`, together with `N_W(d0)=K4`, forces `N_W(v)` to contain one whole component among
\[
K_3,K_5,K_6.\tag{2.2}
\]

Now fix v which is not simultaneously the restored A/B-side endpoint of both c1 and c2. Then v is nonadjacent to at least one of c1,c2. For such a ci, Lemma 1.1 and `N_W(ci)=K3` force `N_W(v)` to contain one whole component among
\[
K_4,K_5,K_6.\tag{2.3}
\]

If (2.2) were satisfied only by K3 and (2.3) only by K4, then `d_W(v)>=3+4=7`, contradicting (2.1). Therefore every such v is complete to K5 or K6.

Since `d_W(v)<=6`, it cannot be complete to both K5 and K6. Thus every non-exceptional v receives a unique label
\[
\ell(v)\in\{5,6\},
\]
where `ell(v)=j` means v is complete to the W-component Kj.

There is at most one exceptional vertex: it occurs only if both restored target edges have the same A/B-side endpoint. If the restored endpoints are distinct, all fourteen vertices of A union B are labelled.

## 3. Opposite-label theorem across A and B

### Lemma 3.1

If `a\in A` and `b\in B` are both labelled, then
\[
\boxed{\ell(a)\ne\ell(b).}\tag{3.1}
\]

**Proof.** The pair a,b is H-nonadjacent because the two K7 components are disconnected in G2 and no restored edge is of A-B type.

If both labels are 5, then each vertex is complete to K5 and, by dW<=6, has at most one W-neighbour outside K5. Thus their union has at most two vertices outside K5. It cannot cover any of K3,K4,K6 completely. Hence their union covers only one W-component, K5, contradicting Lemma 1.1.

If both labels are 6, completeness to K6 already uses all six allowed W-neighbours, so both W-neighbourhoods equal K6. Again the union covers only one W-component, contradicting Lemma 1.1.

Therefore their labels are opposite. QED.

A binary complete bipartite opposite-label condition immediately implies that all labelled vertices on one K7 side have one common label and all labelled vertices on the other side have the opposite label.

## 4. Terminal contradiction

### Case 1 — distinct restored A/B-side endpoints

Then every vertex of A and B is labelled. Lemma 3.1 forces A to be monochromatic in the label and B to have the opposite label.

- If A has label 5, the K7 A is complete to the W-clique K5, giving a K12 in H.
- If A has label 6, the K7 A is complete to K6, giving a K13 in H.

Both contradict `omega(H)<=11`.

### Case 2 — both restored edges share one A/B-side endpoint

Let the common endpoint be z. By symmetry suppose `z\in A`. Then all seven B vertices and the six vertices `A\setminus\{z\}` are labelled. Lemma 3.1 forces `A\setminus\{z\}` to have one common label L and all of B the opposite label.

- If L=6, the six-vertex clique `A\setminus\{z\}` is complete to the W-clique K6, producing K12.
- If L=5, all seven vertices of B have label 6, so the K7 B is complete to K6, producing K13.

Again `omega(H)<=11` is contradicted. The case `z\in B` is symmetric.

Thus no restored-edge endpoint pattern is possible.

## 5. Conclusion

\[
\boxed{
\delta=12,\ \epsilon_U=2,\ \text{non-four-partite depth-2 terminal}\Longrightarrow\bot.
}
\]

This closes the unique epsilon_U=2 depth-2 terminal from the previous reduction.

## 6. Dependency and scope audit

The proof uses:

1. `DELTA12_AUGMENTATION_FRONTIER.md` and the registered 308-edge saturated-kernel classification to reach the depth-2 C5-blowup model;
2. `DELTA12_DEPTH2_EPS2_TERMINAL_REDUCTION.md` for the unique W-terminal data;
3. the pure graph constraints `alpha(H)<=4`, `omega(H)<=11` and the derived nonadjacent-pair common-nonneighbour rule;
4. exact degree/excess accounting inside H.

It does **not** use the Didin 2026 component-count theorem. Didin is used in separate depth-0/depth-1 saturated exclusions and remains unaudited there.

This theorem does **not** close:
- depth-2 epsilon_U in {0,1,3,4};
- depth-3;
- delta=12 four-partite U;
- delta<=11;
- the five-template same-core global compatibility problem;
- E407 Q32 as a whole;
- EG617(r=12).
