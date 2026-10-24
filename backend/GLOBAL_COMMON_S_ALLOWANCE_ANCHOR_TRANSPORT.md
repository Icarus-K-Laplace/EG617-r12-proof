# Global Common-S Allowance Localization and Anchor-Transport Theorem

Status: **PROVED_ANALYTIC** under the standard legal high-backend contract and the all-pivot 35-core minimum-degree-12 theorem.

This theorem refines `GLOBAL_COMMON_S_CROSS_BUDGET_D5_ESCAPE_CLOSURE.md`.  It identifies the common-S ambient allowance exactly as a local missing/slack budget on S and shows that zero transport slack creates degree-12 anchors after every owner repivot.

The result is intended as a forcing bridge from higher-slack support geometry to the global three-anchor envelope.

---

## 1. Setup

Fix a maximum-q regular pivot p with 13-point shell A and 35-core H.  Let

- Y be a family of regular shell vertices sharing the same shell missing set S;
- `|S|=d`, `|Y|=N`;
- `L=A\(S union Y)`, `|L|=r=13-d-N`;
- for `s in S`, let `m_L(s)=d_M(s,L)`;
- `g_s=d_F(s)-13`;
- `D_s=N_H(s)` be the old-core row of s.

For an owner `y in Y`, let `D_y=N_H(y)` be its d-point support.  Let

`a := q-d(13-d)-B`

be the standard common-S ambient allowance, where

`B=e_M(A\S)+G_(A\S)`.

Because owners are regular and are pairwise target-adjacent and target-adjacent to every leftover, here

`B=e_M(L)+G_L`.

---

## 2. Transport slack

Define, for every s in S,

> `sigma_s := m_L(s)+g_s-r`.                              (AT1)

The cross-budget lemma from `GLOBAL_COMMON_S_CROSS_BUDGET_D5_ESCAPE_CLOSURE.md` proves

`m_L(s)+g_s>=r`,

so

> **`sigma_s>=0`.**                                       (AT2)

Equivalently, since `e_F(s,L)=r-m_L(s)`,

`sigma_s = g_s-e_F(s,L)`.

Thus sigma measures exactly the decoration of s not already spent on target adjacency from s to the leftover set.

---

## 3. Exact allowance localization

The exact shell residual identity gives

`q-d(13-d)`
`=e_M(S)+e_M(L)+(G_S-e_F(S,L))+G_L`.

Subtracting

`B=e_M(L)+G_L`

yields

> **`a=e_M(S)+G_S-e_F(S,L)`.**                            (AT3)

Using `G_S-e_F(S,L)=sum_(s in S) sigma_s`, we obtain the exact localization

> **`a=e_M(S)+sum_(s in S) sigma_s`.**                    (AT4)

Therefore every unit of common-S allowance has only two possible sources:

1. a target missing edge internal to S;
2. one unit of positive transport slack on a point of S.

There is no hidden allowance elsewhere in the shell.

Immediate equality consequences include:

- `a=0` iff S is a target clique and every sigma_s=0;
- if `a=e_M(S)`, then every sigma_s=0;
- for fixed a, large internal missing density in S forces many zero-sigma points.

---

## 4. Exact anchor-transport identity

Fix an owner y in Y and a point s in S.

Because sy is a target nonedge, s moves into the new core H_y after repivoting y.

Inside H_y, the neighbours of s are exactly

1. its target neighbours inside `S\{s}`, numbering `d-1-m_S(s)`;
2. its old-core neighbours outside D_y, numbering `|D_s\D_y|`.

Hence

`d_(H_y)(s)`
`=d-1-m_S(s)+|D_s|-|D_s intersect D_y|`.

But

`|D_s|=d_M(s)+g_s`
`=N+m_S(s)+m_L(s)+g_s`.

Using `N+d-1=12-r`, we get the exact identity

> **`d_(H_y)(s)-12 = sigma_s-|D_s intersect D_y|`.**      (AT5)

Since every legal owner repivot core has minimum degree at least12,

> **`|D_s intersect D_y|<=sigma_s`.**                     (AT6)

This is an exact multi-pivot compatibility constraint.

---

## 5. Zero-slack points become universal owner-core anchors

If `sigma_s=0`, then (AT5)--(AT6) force

- `D_s intersect D_y=empty`;
- `d_(H_y)(s)=12`.

And this holds for **every** owner y in Y.

Therefore:

> **Zero-Slack Anchor Transport.**
>
> Every point `s in S` with `sigma_s=0` becomes a degree-12 vertex in every owner-repivot core H_y, with its old core row disjoint from every owner support D_y.

Now suppose three zero-sigma points `s1,s2,s3 in S` are pairwise target-nonadjacent.  Their mutual adjacencies are unchanged when they move into H_y.  Thus in every H_y they form three pairwise nonadjacent degree-12 anchors.

Applying `GLOBAL_THREE_ANCHOR_K6_FULL_CLOSURE.md` and `GLOBAL_THREE_ANCHOR_BACKEND_ENVELOPE.md` gives

> **`q_y<=E-305`**                                        (AT7)

for every owner y.

Equivalently, if `ell_y=q-q_y` is the q-loss of y,

> **`ell_y>=q-(E-305)`.**                                 (AT8)

So a zero-slack missing triangle automatically pushes every owner into the global three-anchor loss envelope.

---

## 6. d3 corollary

Take `d=3` and suppose S itself is a target-independent triple, i.e.

`e_M(S)=3`.

Then (AT4) gives

`a=3+sigma_1+sigma_2+sigma_3`.

In particular, in the first-high-slack layer `a=3`,

`sigma_1=sigma_2=sigma_3=0`.

Hence every owner repivot core contains S as three pairwise nonadjacent degree-12 anchors, and therefore every owner satisfies

> **`q_y<=E-305`.**

Thus the `d3 / a=3 / missing-triangle` equality geometry is not an independent sunflower case: it is automatically a three-anchor configuration after any owner repivot.

More generally, whenever three pairwise nonadjacent points of S exhaust zero transport slack, the same conclusion holds for any d.

---

## 7. Relation to the forcing-to-master bridge

The forcing-to-master programme previously separated

- zero-signature / sunflower support geometry;
- the three-anchor branch.

The present theorem gives a direct transport mechanism between them:

> **internal missing density of S + allowance saturation -> zero transport slack -> degree-12 anchors in every owner core.**

Therefore higher-slack equality states should first be tested using the localized budget (AT4).  If their allowance is already consumed by internal missing edges of S, zero-slack points are forced and the state can enter the three-anchor envelope without any support multiplicity classification.

Only equality states whose allowance contains genuine positive sigma mass remain in the collapsed-signature support branch.

This shrinks the shallow-loss Bridge B to a local distribution problem on at most d support-missing vertices.

---

## 8. Portability

The proof is parameterized by shell size and the minimum degree of every repivot core.  The exact cancellation in (AT5) comes from the r=12 values shell size13 and core minimum degree12; in a larger-r analogue the same calculation produces a shifted transport-slack identity.

The conceptual statement survives unchanged: unused decoration/cross-adjacency slack on the common missing set measures exactly how far its vertices are from becoming minimum-degree anchors after owner repivot.