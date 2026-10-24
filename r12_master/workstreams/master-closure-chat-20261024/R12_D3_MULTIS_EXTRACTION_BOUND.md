# R12 d3 multi-S extraction and allowance localization through q=38

Status: **PROVED ANALYTIC** under the standard legal R(4,49) backend contract and the all-pivot 35-core minimum-degree-12 contract.

Purpose: extend the q32 d3 multi-S extraction theorem to the full high-backend charge ceiling q<=38, without falsely claiming that every resulting common-S class is already closed.

## Theorem

Let p be a maximum-q degree-13 pivot in a legal 49-point residual F, with shell A, |A|=13, and core H. Let Y be any family of regular shell vertices such that every y in Y has

`|S_y|=|D_y|=3`,

where `S_y=N_M(y)` and `D_y=N_H(y)`. Write `N=|Y|), assume `q<=38`, and partition Y into common-missing-triple classes

`Y_S={y in Y:S_y=S}`,

with class size `n=|Y_S|).

Then:

1. Y is a target clique and `N<=10`.
2. For each class Y_S, its common-S allowance
   `a_S=q-30-B_S`, where `B_S=e_M(A\S)+G_(A\S)`, satisfies the exact bound
   [
   0\le a_S\le q-30-N+n.
   ]
3. Consequently every nonempty class satisfies
   [
   n\ge N+30-q.
   ]
   The number of distinct missing-triple classes is therefore at most
   [
   \min\left\{\binom{13-N}{3},\left\lfloor\frac{N}{N+30-q}\right\rfloor\right\}
   ]
   whenever the denominator is positive.
4. More sharply, a class of size n enters the already-classified common-S allowance regimes whenever its actual `a_S` is at most3; the formula above shows exactly when that is forced by N, q and n.

## Proof

### Step 1: all d3 owners are adjacent

By the nonadjacent regular zero-gap identity in `backend/HIGH_LAYER_V3_JOINT_CANONICAL.md`, if two regular shell vertices y,z are target-nonadjacent, then

`S_y union S_z=A`.

But `|S_y union S_z|<=6<13=|A|`. This is impossible. Hence Y is a target clique. Since p is adjacent to every vertex in A, `{p} union Y` is a target clique of size N+1. The legal residual has `omega(F)<=11), so N<=10.

### Step 2: missing triples live in the small complement

Every y in Y is adjacent to every other owner z. Therefore no other owner lies in S_y, and

`S_y subset Q:=A\Y`, `|Q|=13-N`.

Fix a class Y_S of size n and put

`T=A\(S union Y_S)`.

For each z in Y\Y_S, choose `x_z in S_z\S`, which is nonempty because S_z and S are distinct triples. Since x_z lies in T and z lies in T, `x_z z` is a missing edge of M[T]. Different z give different edges, so

`e_M(T)>=N-n`.

Also `G_T>=0). There are no missing edges from Y_S to T, because every owner in Y_S is adjacent to every point outside its common missing triple. Hence

`B_S=e_M(A\S)+G_(A\S)=e_M(T)+G_T>=N-n`.

### Step 3: allowance localization

For any y in Y_S, the exact exchange formula from `HIGH_LAYER_V3_JOINT_CANONICAL.md` reads

`q_y=30+B_S+kappa(D_y)+mu(D_y)+e_F(S,D_y)`.

Every term after B_S is nonnegative. Maximality gives `q_y<=q), so

`0<=a_S:=q-30-B_S`.

Using `B_S>=N-n` gives

`a_S<=q-30-N+n`.

Rearranging `a_S>=0) gives `n>=N+30-q). The number of classes is bounded both by the number `binom(13-N,3)` of possible triples in Q and by the sum of their sizes N. This proves the theorem.

## Immediate consequences for the current frontier

The formula is useful because it localizes the remaining multi-S problem by **class size**, not by historical E-layer.

- **N=10:** Q has exactly three vertices, so all rows have the same missing triple.
- **N=9, q<=34:** every occurring class has size at least5; two such classes would require at least10 owners. Thus all nine rows share one missing triple.
- **N=9, q=35:** every occurring class has size at least4, so at most two classes occur. Each class has allowance `a_S<=n-4`; classes of size4 or5 are subcritical (`a_S<=1)).
- **N=9, q=36:** every class has size at least3 and at most three classes occur. Classes of size at most5 have `a_S<=2); only a class of size at least6 can reach first-high-slack allowance3.
- **N=9, q=37:** every class has size at least2; `a_S<=n-2). Classes of size at most4 are subcritical.
- **N=9, q=38:** `a_S<=n-1). Classes of size at most3 are subcritical, and a size-4 class has allowance at most3.
- For smaller N, the same exact formula applies. For example, at N=8 and q<=35, each class has `a_S<=n-3`; small classes are forced into subcritical or first-high-slack regimes.

Whenever a class has `s=|S intersect X|<3`, these allowance bounds place it in the existing subcritical / first-high-slack / loss-layer machinery. If `s=3`, the lexicographic strict-loss argument is unavailable and the fully-decorated branch must be handled separately; this theorem does not silently apply the `s<3` lemmas to it.

## What this theorem does not prove

It does **not** close every d3 shell:

- the owner count may be below7;
- classes with `s=3` are not covered by the non-fully-decorated support decomposition;
- a size-4 or larger class can still land in the higher-slack shallow-loss window;
- the theorem says nothing by itself about d2 multi-S systems or the d4/d9 non-common-S extraction problem.

The result is a genuine extraction/allowance theorem, not a final E335--E340 contradiction.
