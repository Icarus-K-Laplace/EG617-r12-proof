# Fixed-Class d2 Plateau Skeleton Theorem

Assumptions: hypotheses A+B, `r>=12`, and a pivot p lexicographically maximal in `(q,tau)`.

Fix one d2 shell class

`S={u,v}`

and let Y be **all** regular d2 owners with this shell missing set. For `y in Y`, write

`D_y=N_H(y)`, `|D_y|=2`.

Let

`b=e_M(S) in {0,1}`,

`w_x=kappa_x+e_F(x,S)` for `x in H`,

`mu(D)=1-e_H(D) in {0,1}` for a 2-support D,

and let the class allowance be

`a=b+sigma_u+sigma_v`.

For every owner y the exact repivot identity is

> **`ell_y:=q-q_y=a-[w(D_y)+mu(D_y)]`.**                    (1.1)

At q-maximality, `ell_y>=0`. Hence a row is q-flat iff

> **`w(D_y)+mu(D_y)=a`.**                                   (1.2)

For each core vertex x define the owner-incidence multiplicity

`lambda_x=#{y in Y:x in D_y}`.

Every such incidence contributes a distinct shell target neighbour of x, so

`d_F(x)>=r+kappa_x+lambda_x`.

Therefore

> **`kappa_x+lambda_x>=2  =>  x in X`,**                    (1.3)

where `X={z:d_F(z)>r+1}` is the global decorated set.

Let

`s=|S intersect X| in {0,1,2}`.

Exact tau transport says every q-flat row satisfies

> **`|D_y intersect X|<=s`.**                               (1.4)

These four formulas completely control the low-decoration plateau.

---

# 2. Case s=0

Both shell endpoints u,v are nondecorated. In particular `g_u=g_v=0`.

Use the full common-S family Y and put

`L=A\(S union Y)`.

For each `z in S`, common-S transport gives

`sigma_z=m_L(z)+g_z-|L|>=0`.

Since `g_z=0` and `m_L(z)<=|L|`, necessarily

> `sigma_u=sigma_v=0`.

Therefore

> **`a=b`.**                                                 (2.1)

Now let y be q-flat and x an endpoint of D_y. By (1.4), `x notin X`. Since `lambda_x>=1`, (1.3) forces

`lambda_x=1`, `kappa_x=0`.

Moreover x has its owner y as a shell target neighbour. If `e_F(x,S)>=1`, then

`d_F(x)>=r+1+1=r+2`,

so x would lie in X. Hence

> **every endpoint of every q-flat support has `lambda=1`, `kappa=0`, `e_F(x,S)=0`, hence `w_x=0`.**   (2.2)

Consequences:

- q-flat supports are pairwise disjoint;
- (1.2) and (2.1) give `mu(D_y)=b`.

## 2A. b=0

Then `a=0`, so every legal owner is automatically q-flat: from (1.1), `ell_y=-[w(D_y)+mu(D_y)]>=0` forces `w(D_y)=mu(D_y)=0`.

Thus every D_y is a target edge and all support endpoints have w=0.

For two distinct supports D_i,D_j and `x in D_i`, row closure for D_j gives

`e_H(x,D_j)<=w_x=0`.

Hence there are no target cross-edges between distinct supports.

If four supports existed, choosing one endpoint from each would give an independent 4-set in H, contradicting `alpha(H)<=3`.

Therefore

> **`s=0,b=0 => |Y|<=3`.**                                  (2.3)

This entire class is bounded; no strict-loss rows exist.

## 2B. b=1

Then `a=1`. A q-flat support has `mu=1`, hence is an H-nonedge. Distinct q-flat supports again have no target cross-edges by row closure and (2.2).

Two such supports would therefore form an independent 4-set. Hence

> **the number of q-flat rows is at most 1.**                 (2.4)

Strict rows have `ell=1` and `w(D)+mu(D)=0`, so each strict support is a target edge with both endpoints of w=0. Distinct strict support classes have no target cross-edges, hence there are at most three distinct strict support classes by `alpha(H)<=3`; multiplicity inside a strict repeated class remains a hereditary-packing object.

Thus even the `s=0,b=1` class has only O(1) support **types**.

**Status for s=0:** `PROVED_CONDITIONAL`.

---

# 3. Case s=1

Let P be the set of q-flat rows and regard their distinct core supports as edges of a simple graph Q on H.

By (1.4), every edge of Q contains at most one decorated vertex.

If a vertex x lies in two owner supports (even if one of the owners is strict), then `lambda_x>=2`, so x is decorated by (1.3). Therefore:

> a support used by a q-flat row cannot be repeated: if D occurred for two owners, both endpoints would have `lambda>=2`, hence both would be decorated, contradicting (1.4).   (3.1)

Thus q-flat owners and q-flat support edges are in one-to-one correspondence.

If a vertex c has Q-degree at least two, then `lambda_c>=2`, so c is decorated. Hence no Q-edge can join two vertices of Q-degree at least two. It follows that every connected component of Q is either

- an isolated edge; or
- a star.

Now consider a star with center c and at least two leaves `x_1,...,x_k`. The center is decorated. Hence every leaf on a q-flat edge is nondecorated. As above, for such a leaf x,

`lambda_x=1`, `kappa_x=0`, `e_F(x,S)=0`, so `w_x=0`.

For distinct leaves x_i,x_j, row closure for x_i against support `{c,x_j}` gives

`e_H(x_i,{c,x_j})=0`.

Thus x_i is target-nonadjacent to c and to x_j. Therefore

`{c,x_1,...,x_k}`

is independent. Since `alpha(H)<=3`,

> **every q-flat star has at most two support edges.**        (3.2)

Next choose one nondecorated endpoint x_C from each component C of Q. Such an endpoint exists because every q-flat edge contains at most one decorated vertex. For two different components C,C', x_C does not lie in the support chosen from C', and `w_(x_C)=0`. Row closure therefore gives

`e_H(x_C,D_(C'))=0`,

in particular x_C is target-nonadjacent to x_(C').

Four components would yield an independent 4-set. Hence

> **Q has at most three connected components.**              (3.3)

Combining (3.1)--(3.3):

> **`s=1 =>` at most six q-flat owners in the fixed shell class.**   (3.4)

Moreover the q-flat support graph is exactly a disjoint union of at most three components, each an isolated edge or a star with at most two edges.

**Status:** `PROVED_CONDITIONAL`.

---

# 4. Case s=2 — the unique scalable plateau regime

When both u and v are decorated, (1.4) imposes no cardinality restriction on a 2-support D_y. Exact support repetition can therefore remain q-flat, and the preceding star/disjointness argument no longer applies.

Thus:

> **Fixed-Class Plateau Reduction Theorem.** For a fixed d2 shell class S:
>
> - if `|S intersect X|=0`, the class has only O(1) support types; in the b=0 subcase it has at most three owners total, and in the b=1 subcase at most one q-flat owner;
> - if `|S intersect X|=1`, it has at most six q-flat owners, with q-flat supports forming at most three tiny star/edge components;
> - therefore any d2 shell class carrying an unbounded family of q-flat owners must satisfy
>   **`S subset X`**.

In other words, the only scalable equal-q d2 mechanism is the **fully decorated shell-pair regime**.

**Status:** `PROVED_CONDITIONAL`.

---

# 5. Multi-pivot defect sum inside one fixed class

Summing (1.1) over all owners gives the exact identity

> **`L:=sum_y ell_y = N a - sum_x lambda_x w_x - sum_y mu(D_y)`.**   (5.1)

This is the common-S d2 specialization of the general multi-S support-gain identity.

If `F0` denotes the number of q-flat owners, then every other owner loses at least one integer q-unit, so

> `L>=N-F0`.                                                  (5.2)

Hence

> **`sum_x lambda_x w_x + sum_y mu(D_y) <= N(a-1)+F0`.**     (5.3)

For `s<=1`, the theorem supplies the absolute bound `F0<=6` (and sharper bounds above). Thus any large owner class in a non-fully-decorated shell pair must place almost all rows in positive q-loss, with an exact aggregate defect penalty.

The only regime in which the q-flat count can itself scale with r is `s=2`.

---

# 6. Main-theorem impact

The previous six-point shell theorem reduced d2 to at most fifteen shell classes. This theorem reduces the internal plateau behavior of each class further:

- all non-fully-decorated classes have only O(1) q-flat skeletons;
- the only scalable q-flat core-support multiplicity can occur in classes whose two shell endpoints are globally decorated.

Therefore the next blocker is no longer arbitrary fixed-class d2 compatibility. It is specifically:

> **Fully-decorated d2 plateau compatibility:** eliminate or rigidify q-flat repeated/core-support systems for a fixed shell pair `S subset X`.

This is the unique scalable equal-q d2 regime.