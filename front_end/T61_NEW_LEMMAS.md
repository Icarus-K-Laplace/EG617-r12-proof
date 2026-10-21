# T61 new lemmas — 2026-10-21

Status policy: every statement below is either `PROVED` or explicitly marked `OPEN`.

## T61 context

Assume the proved front-end dichotomy has entered the embedded terminal class `T61` under the temporary contextual hypothesis that the fixed least-edge colour graph `G` contains no induced member of `R(4,49)`.

Thus:

- `v` has minimum degree 11;
- `A=N_G(v)` has size 11;
- in `U=V(G)\N[v]` there are six inclusion-maximal genuine target `K12` blocks `Q1,...,Q6` and a 61-point residual `R`;
- `alpha(R)<=5`, `omega(R)<=11`, all hereditary `D` caps hold;
- `397<=E=e(R)<=408`, `delta(R) in {12,13}`;
- with `sigma=870-m`, `z=55-e(G[A])`, `g=sum_{a in A}(d_G(a)-11)`, and the six-block cross terms `x6,y6`,

`E + sigma + z + g + x6 + y6 = 408`.

The full theorem is still OPEN; these lemmas only tighten T61.

---

## T61-L1. Residual independence is exactly five — PROVED

Under the contextual no-`R(4,49)` hypothesis,

`alpha(R)=5`.

Proof. We already have `alpha(R)<=5`. If `alpha(R)<=4`, any induced 49-vertex subset of `R` inherits `omega<=11` and all `D` caps, hence is an induced member of `R(4,49)`, contradicting the contextual hypothesis. Therefore `alpha(R)=5`.

---

## T61-L2. Anchor defect elimination: z=0 — PROVED

The anchor closed neighbourhood is a genuine target `K12`:

`z=0`, hence `G[N[v]] = K12`.

Proof. Suppose `z>0` and choose a missing edge `ab` inside `A`. Let `r_a,r_b` be the missing degrees of `a,b` in `A`, and let `g_a=d_G(a)-11`, `g_b=d_G(b)-11`.

Because `a,b` are endpoints of a missing edge,

`r_a+r_b-1 <= z`, hence `r_a+r_b <= z+1`.

The target degree from `a` into `U` is exactly `r_a+g_a`: inside `N[v]` it has `11-r_a` target neighbours and its total target degree is `11+g_a`. Similarly for `b`. Therefore

`d_U(a)+d_U(b) <= z+1+g_a+g_b <= z+1+g`.

From the T61 ledger,

`z+g <= sigma+z+g+x6+y6 = 408-E <= 11`, so

`d_U(a)+d_U(b) <= 12`.

In particular, the union `T=N_R(a) union N_R(b)` has size at most 12. Hence `R-T` has at least 49 vertices. If `alpha(R-T)<=4`, any 49 vertices inside `R-T` would give an induced `R(4,49)`, impossible. Thus `R-T` contains an independent 5-set `S`, and by construction `S` is anticomplete to both `a` and `b`.

For each of the six genuine `K12` blocks `Qi`, every one of the seven vertices in `S union {a,b}` has at most one target neighbour in `Qi`. Hence the avoiding list `Li subset Qi` has size at least `12-7=5`.

Edges between two block lists are still matchings. Apply the proved matching-transversal rigidity theorem to the six lists. If no independent transversal exists, then all six lists have size exactly 5 and every pair of lists is joined by a perfect matching, forcing

`x6 >= 5*C(6,2)=75`.

But the outer ledger gives `x6<=408-E<=11`, contradiction. Therefore an independent transversal `q1,...,q6` exists. Then

`S union {a,b,q1,...,q6}`

is an independent 13-set in `G`, contradicting `alpha(G)<=12`.

Therefore `z=0`.

### Consequences

The T61 ledger simplifies to

`E + sigma + g + x6 + y6 = 408`.

The original anchor block `N[v]` is now a seventh genuine target `K12`, disjoint from the six blocks in `U`. This does **not** yet create an eighth block or a 49-point residual; the residual is still the same 61-point graph `R`.

---

## T61-L3. Modern generic R(4,48) floor is 309 — PROVED

Using the clean `CORE211` theorem, every `C in R(4,48)` satisfies

`e(C)>=309`.

Proof. The already audited 48-point argument gives `delta(C)>=12`. If `delta(C)>=13`, handshake gives `e(C)>=312`.

Otherwise take a degree-12 pivot. Its 35-point core `H` belongs to `R(3,35)`, so modern `CORE211` gives `e(H)>=211`. The audited 12-shell argument gives shell charge `q>=20`. Therefore

`e(C)=78+q+e(H) >= 78+20+211 = 309`.

This strengthens the old seed 308. The old front-end recurrence remains valid as certified; replacing 308 by 309 only strengthens downstream deductions and must be re-run before claiming a new arithmetic certificate.

---

## T61-L4. The minimum-degree-12 row starts at E=407 — PROVED

If a T61 residual has minimum degree 12, then with the usual 12-shell / 48-core decomposition

`E = 78 + q + e(C48)`,

where `q>=20` and, by T61-L3, `e(C48)>=309`. Hence

`E>=407`.

Therefore the previously allowed h=12 row `E=406..408` contracts to

`E in {407,408}`.

More precisely:

- `E=407` forces `(q,e(C48))=(20,309)`;
- `E=408` allows only `(20,310)` or `(21,309)`.

The `(20,308)`, `(21,308)`, `(22,308)` channels are eliminated.

---

## T61-L5. Exact equality structure of a 309-edge R(4,48) core — PROVED

Let `C in R(4,48)` have `e(C)=309`. Then `delta(C)=12`. Take a degree-12 pivot `p`, let `A` be its 12-shell, `H` the 35-core, `M=overline{C[A]}`, `z=e(M)`, and `g_a=d_C(a)-12`.

The identity is

`309 = 78 + q + e(H)`, `q=z+sum g`.

By the shell floor `q>=20` and `CORE211`, `e(H)>=211`; hence equality forces

`q=20`, `e(H)=211`.

The 13-point cap gives `z>=11`. The audited shell matching lemma gives a 2-matching in `M`. Since the q=20 equality cannot use the triangle alternative, `M` is triangle-free.

Choose any two disjoint missing edges. The standard q-floor proof gives

`q >= 24 - e(M[S])`,

for their four endpoints `S`, with `e(M[S])<=4` by triangle-freeness. Equality `q=20` forces equality in every term:

- the four endpoints induce a `C4` in `M`;
- `M[A\S]` has no edges;
- all decorations outside `S` vanish;
- for each chosen matching edge, its two core rows are disjoint and have union size exactly 12.

Varying the chosen 2-matching classifies the missing graph completely:

`M = K_{2,r} disjoint_union (10-r) K1`, with `6<=r<=10`.

The two vertices on the 2-side are the centres. Each centre has decoration `10-r`; every leaf and isolated shell vertex has decoration zero. Core-row sizes are:

- centre row: 10;
- leaf row: 2;
- isolated row: 0.

For every centre-leaf missing edge, the corresponding 10-row and 2-row are disjoint and their union has size 12.

Reason for `r>=6`: `z=2r>=11`. Reason for the decorations: a leaf has `t=2`, while pair equality gives centre weight 10, so each centre has `g=10-r`.

---

## T61-L6. CORE211 forces almost-clique 12-row unions — PROVED

Continue in T61-L5. Let `D1,D2` be the two 10-vertex centre rows in the 211-edge core `H`. For any leaf shell vertex let `P` be its 2-vertex core row. Then `P` is disjoint from both `D1,D2`.

For each `i=1,2`, put `Ui=Di union P`, so `|Ui|=12`. The common nonneighbour set `H\Ui` has 23 vertices. If it contained an independent 3-set, together with the corresponding missing shell edge (centre, leaf) it would form an independent 5-set in `C`, impossible. Hence `H\Ui` belongs to `R(2,23)` and has at least 131 edges.

The 211-core has total degree excess 2 above degree 12. If `eps(Ui)=sum_{u in Ui}(d_H(u)-12)`, then

`e(H\Ui)=211-(144+eps(Ui)-e_H(Ui)) = 67-eps(Ui)+e_H(Ui)`.

Since the left side is at least 131,

`e_H(Ui) >= 64 + eps(Ui)`.

Because `omega(H)<=11`, `Ui` cannot be a `K12`, so `e_H(Ui)<=65`. Consequently

`eps(Ui)<=1`, and each `Ui` is a 12-vertex graph missing at most `2-eps(Ui)` edges.

In particular each centre row induces at least 43 of its possible 45 edges.

---

## T61-L7. The two centre rows overlap in at least seven core vertices — PROVED

Continue in T61-L6. Let

`s=|D1 intersect D2|`.

For a leaf row `P={u,w}`, write `p=e_H(P)` and `eps(P)=sum_{x in P}(d_H(x)-12)`.

From `e_H(Ui)>=64+eps(Ui)` and `e_H(Di)<=45`,

`e_H(P,Di) >= 19 + eps(Ui) - p`.

Therefore

`d_H(u)+d_H(w) >= 2p + e(P,D1 union D2)`

`>= 38 + eps(U1)+eps(U2) - 2s`.

The 211-core degree multiset is either `14,12^34` or `13^2,12^33`. Also `eps(Ui)<=1`, so a leaf row cannot contain the degree-14 vertex, nor both degree-13 vertices. Hence

`d_H(u)+d_H(w) <=25`.

Thus

`25 >= 38 - 2s`, so `s>=7`.

A sharper bookkeeping form is

`2s >= 14 + eps(U1)+eps(U2)-eps(P)`.

Therefore `s=7` can occur only in a zero-excess channel; any captured excess typically forces `s>=8`.

---

## Current h=12 terminal after these lemmas — OPEN

The minimum-degree-12 branch has been reduced to:

1. `E=407`: outer equality `(q,e(C48))=(20,309)` and the 309-core contains the exact `K_{2,r}` q20 shell over a 211-edge 35-core described above;
2. `E=408`: either `(q,e(C48))=(20,310)` or `(21,309)`; every 309 subchannel inherits the same inner q20/211 structure.

The strongest current inner geometry for a 309-core is:

- `M=K_{2,r} + isolates`, `6<=r<=10`;
- two 10-rows `D1,D2` with overlap at least 7;
- every leaf 2-row is disjoint from both centre rows;
- each 12-set `Di union P` is missing at most two core edges;
- the 211-core has only two units of total degree excess.

A contradiction from this geometry has not yet been completed. This is a preferred target for Astra A.
