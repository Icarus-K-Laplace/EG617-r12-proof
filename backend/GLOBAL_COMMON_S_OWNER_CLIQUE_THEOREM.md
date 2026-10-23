# Global Common-S Owner-Clique Theorem

Status: `PROVED_ANALYTIC`.

Purpose: record a basic structural fact that is easy to use implicitly but is essential for the global support bridge. It also fixes the scope of any attempt to identify a multi-view system with one common-missing-set family.

## 1. Setup

Let `p` be a pivot with shell `A=N_F(p)` of size `h`. Let

`M=complement(F[A])`.

For a regular shell vertex `y`, write

`S_y=N_M(y)`

for its shell missing set.

Let `Y` be a family of distinct regular shell vertices with one common missing set

`S_y=S`

for every `y in Y`.

Put `N=|Y|` and `d=|S|`.

## 2. Owners are pairwise target-adjacent

Take distinct `y,z in Y`.

Because the missing graph has no loops,

`z notin S_z`.

But `S_z=S`, so

`z notin S`.

Since `S_y=S`, we also have

`z notin S_y`.

Therefore `yz` is not an edge of the shell missing graph M, hence it is a target edge of F.

Thus

> **every common-S owner family Y is a target clique.**

## 3. Pivot extension

The pivot `p` is target-adjacent to every shell vertex. Hence

`{p} union Y`

is a target clique of size

`N+1`.

Consequently, in any parent contract with target clique number at most `omega`,

> `N<=omega-1`.                                               (C1)

For the current r=12 residual contract, `omega(F)<=11`, so

> **N<=10.**                                                  (C2)

This bound is independent of support size, core excess, hereditary caps, and row allowance.

## 4. Dense base outside the common missing set

Let

`T=A\(S union Y)`.

Then

`|T|=h-d-N`.

Every owner `y in Y` is target-adjacent to every vertex of T, because T is disjoint from S and from y itself. Also Y is a target clique and p is adjacent to `Y union T`.

Therefore the base

`B={p} union Y union T`

has size

`|B|=h-d+1`,

independent of N, and contains at least

`e(B) >= (h-d) + C(N,2) + N(h-d-N)`                         (C3)

target edges. Equality in (C3) occurs exactly when T is target-independent.

For the r=12 backend with `h=13,d=3`, the base always has size 11 and

`e(B)>=10+C(N,2)+N(10-N)`.                                  (C4)

In particular:

- N=10: `e(B)=55`;
- N=9: `e(B)=55`;
- N=8: `e(B)>=54`;
- N=7: `e(B)>=52`.

These are the dense bases used by the sharp d=3 capacity theorem.

## 5. Same-support owners are also a clique without common S

There is a second useful fact which does **not** require the owners to share S.

Suppose regular shell vertices `y,z` have the same nonempty core support

`D_y=D_z=D`.

If y and z were target-nonadjacent, the all-pivot codegree rigidity theorem would give at most one common target neighbour. But y and z already have

- the pivot p, and
- every vertex of the nonempty support D

as common target neighbours.

Thus they have at least two common target neighbours, contradiction.

Therefore:

> **all regular owners of one fixed nonempty core support form a target clique.**   (C5)

This is the multi-S analogue of the owner-clique mechanism and is useful for repeated-support hereditary packing.

## 6. Scope correction for the E334 eleven-view language

The phrase `eleven-view system` must not be silently identified with eleven owners sharing one missing triple.

If eleven regular owners really shared one common S, then (C2) would already give an immediate contradiction.

Therefore any genuine unresolved eleven-view object must either

1. involve several different missing sets, or
2. use `view` in a sense different from one common-S owner row.

Any application of the common-S compatibility theorem to that system requires an explicit extraction/partition bridge first.

This is a proof-scope condition, not a cosmetic distinction.

## 7. Parameterized nature

The owner-clique proof only uses

- the shell missing-set definition;
- the fact that a vertex is not missing from itself;
- pivot adjacency to the shell.

Thus (C1) is completely independent of the numerical r=12 constants and transfers verbatim to any analogous pivot reduction.