# Global common-S cross-budget theorem and decorated d5 escape closure

Status: **PROVED_ANALYTIC** under the standard legal high-backend contract and the all-pivot 35-core minimum-degree-12 theorem.

This theorem closes the unique decorated `(d_M,g)=(5,1)` equality escape left by `GLOBAL_LARGE_SUPPORT_MULTI_LEFTOVER_DEGREE_DESCENT.md`.  More importantly, it gives an exact common-S shell residual identity that is independent of the historical E-layer labels.

Dependencies:

- the 13-point shell/common-S setup;
- every owner in `Y` is regular (degree 13);
- every owner has the same shell missing set `S` of size `d`;
- every legal regular-owner repivot has a 35-core of minimum degree at least 12;
- the exact shell charge `q=e(M)+G_A`;
- for the final d4/d9 corollary only: `d(13-d)=36` and `q<=38`.

No solver is used.

---

## 1. Setup

Fix a maximum-q regular pivot p with shell A, |A|=13.  Let

- `Y` be a common-S regular owner family;
- `S` be the common shell missing set, `|S|=d`;
- `N=|Y|`;
- `L=A\(S union Y)` be the leftover set, `|L|=r=13-d-N`.

Because every owner y has missing set exactly S,

- Y is a target clique;
- every owner is target-adjacent to every leftover vertex;
- the only shell missing edges are owner--S, inside S, between S and L, and inside L.

For a shell vertex v write `g_v=d_F(v)-13`, and put `G_T=sum_(v in T) g_v`.

---

## 2. Cross-budget lemma

Take any `s in S` and any owner `y in Y`.

Since sy is a target nonedge, repivoting the regular owner y moves s into the new 35-core `H_y`.  By the all-pivot theorem,

`d_(H_y)(s)>=12`.

Let

- `m_S(s)=d_M(s,S)`;
- `m_L(s)=d_M(s,L)`.

In the original p-view, s misses all N owners, so its old core-neighbourhood size is

`|D_s|=d_M(s)+g_s=N+m_S(s)+m_L(s)+g_s`.

In the y-core, s has exactly

`d-1-m_S(s)`

target neighbours inside S, while its surviving old-core neighbours are at most `|D_s|`.  Hence

`12 <= d-1-m_S(s)+N+m_S(s)+m_L(s)+g_s`.

Using `r=13-d-N`, this simplifies to

> `m_L(s)+g_s >= r`.                                      (CB1)

Equivalently the number of target edges from s to L satisfies

> `e_F(s,L)=r-m_L(s) <= g_s`.                             (CB2)

Summing over s in S gives the global cross-budget inequality

> **`e_F(S,L) <= G_S`.**                                  (CB3)

This is a structural consequence of simultaneous legal repivots; it does not require S to be fully decorated.

---

## 3. Exact common-S shell residual identity

The shell missing edges split exactly as

`e(M)=dN+e_M(S)+e_M(S,L)+e_M(L)`.

Since

`e_M(S,L)=dr-e_F(S,L)`

and all owners are regular (`G_Y=0`),

`q=e(M)+G_A`
` =dN+dr+e_M(S)+e_M(L)-e_F(S,L)+G_S+G_L`.

Because `N+r=13-d`, we obtain the exact identity

> **`q-d(13-d)`**
> **`= e_M(S)+e_M(L)+(G_S-e_F(S,L))+G_L`.**               (CB4)

By (CB3), every term on the right is nonnegative.

Thus the complete common-S slack is localized into only four nonnegative quantities:

1. missing edges inside S;
2. missing edges inside the leftover set L;
3. unused decoration capacity on S after paying for target S--L edges;
4. decoration on L.

This is strictly sharper than the earlier multi-leftover inequality whenever simultaneous owner repivots are available.

---

## 4. d4/d9 consequence at q<=38

For `d in {4,9}`,

`d(13-d)=36`.

Hence (CB4) gives

> **`e_M(S)+e_M(L)+(G_S-e_F(S,L))+G_L <=2`.**              (CB5)

In particular

- `e_M(L)<=2`;
- `G_L<=2`.

We now close the only escape left by `GLOBAL_LARGE_SUPPORT_MULTI_LEFTOVER_DEGREE_DESCENT.md`.

---

## 5. Closure of the d4 decorated d5/g1 escape

The previous degree-descent theorem showed that a fully decorated repeated d4 family at q<=38 either produces a leftover of missing degree at most four, or—in the only unresolved low-owner layers—its extracted minimum-defect leftover x satisfies

`d_M(x)=5`, `g_x=1`,

so its local defect is

`lambda_x=d_M(x)+g_x=6`.

Because x was an extracted minimum-defect leftover, every z in L satisfies

`lambda_z>=6`.                                             (D4-1)

For d4, any regular leftover z has

`d_M(z)<=d+e_M(L)<=4+2=6`

by (CB5).  But the exact regular exchange gap at q<=38 forbids regular missing degrees 5 and 6.  Therefore every regular leftover would have `d_M(z)<=4`, contradicting (D4-1).

Hence every leftover vertex must be decorated.  Thus

`G_L>=|L|`.

But (CB5) gives `G_L<=2`.  Therefore

`|L|<=2`.                                                  (D4-2)

The only d4 layers in which the old multi-leftover descent allowed the `(5,1)` escape had owner count N=2 or3, i.e.

`|L|=13-4-N in {7,6}`,

contradicting (D4-2).

Therefore:

> **No fully decorated repeated d4 family at q<=38 realizes the decorated `(d_M,g)=(5,1)` escape.**

Every such d4 family descends to an actual leftover with `d_M<=4`.

---

## 6. Closure of the d9 decorated d5/g1 escape

The only d9 escape left by the old degree-descent theorem is

- q=38;
- N=2 owners;
- r=2 leftovers, say L={x,z};
- x has `(d_M,g)=(5,1)` and is a minimum-defect leftover.

Thus `lambda_z>=6`.

For d9, full decoration of S gives

`G_S>=9`.                                                  (D9-1)

By (CB5), since `g_x=1`, there are two possibilities for z.

### Case A: z is decorated

Then `G_L>=2`.  Equation (CB5) forces

`e_M(S)=e_M(L)=0`,

`G_S=e_F(S,L)`.

In particular xz is a target edge.  Since `d_M(x)=5`, x has exactly four target neighbours in S.  Also `G_L<=2` forces `g_z=1`; from `lambda_z>=6` we get `d_M(z)>=5`, so z has at most four target neighbours in S.

Therefore

`e_F(S,L)<=8`,

contradicting `G_S=e_F(S,L)` and (D9-1).

### Case B: z is regular

The regular degree gap at q<=38 and `lambda_z=d_M(z)>=6` imply

`d_M(z)>=9`.                                               (D9-2)

If xz is a missing edge, then x has five target neighbours in S and z has at most one; hence

`e_F(S,L)<=6`.

If xz is a target edge, then x has four target neighbours in S and (D9-2) leaves z with no target neighbour in S; hence

`e_F(S,L)<=4`.

In either subcase

`G_S-e_F(S,L)>=3`,

while `G_L>=1`, contradicting the total residual bound (CB5), whose right side is only two.

Therefore:

> **The d9/q38/two-owner decorated `(d_M,g)=(5,1)` escape is impossible.**

---

## 7. Large-support Bridge C is closed

Combining Sections 5 and 6 with `GLOBAL_LARGE_SUPPORT_MULTI_LEFTOVER_DEGREE_DESCENT.md` yields:

> **Fully-decorated large-support descent theorem.**
>
> For d in {4,9} and q<=38, every repeated common-S regular owner family produces a leftover shell vertex of missing degree at most four.
>
> The previously unique decorated d5/g1 equality escape does not occur.

Together with the existing subcritical theorem for non-fully-decorated d4/d9 families, there is no longer a genuinely new large-support geometry at q<=38.

Thus the old forcing-to-master **Bridge C is analytically closed**.

---

## 8. Remaining global bridge

After this theorem, the high-backend forcing programme has only:

1. common-S extraction (or direct three-anchor forcing);
2. finite shallow-loss d2/d3 equality windows above first high slack.

The fully-decorated d4/d9 multi-leftover branch no longer requires a separate K4,9-style or medium-support classification.

---

## 9. Portability

The cross-budget argument itself is parameterized.

For a shell of size h, a common-S regular owner family of size N, common missing-set size d, and leftover size r=h-d-N, if every owner repivot places S into a core of minimum degree at least delta_core, the same comparison gives a linear lower bound on `m_L(s)+g_s`.  In the r=12 problem `h=13` and `delta_core=12`, yielding the exact cancellation `m_L(s)+g_s>=r` and hence (CB3)--(CB4).

This is a reusable simultaneous-repivot compatibility theorem, not an E-layer-specific contradiction.
