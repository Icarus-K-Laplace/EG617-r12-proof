# Global Repeated-Support Dense-Block Theorem

Status: `PROVED_ANALYTIC`.

Dependencies:

- all-pivot regular codegree rigidity;
- the hereditary induced-edge cap `D_cap(t)`;
- the pivot/core decomposition.

This theorem is independent of common missing sets. It gives a direct bridge from support repetition to a forbidden near-clique geometry.

## 1. Setup

Let p be a pivot with shell A and core H.

Let

`D subset H`, `|D|=d>=1`,

be one core support which is used by m distinct regular shell owners

`Y_D={y_1,...,y_m}`.

Thus

`N_H(y_i)=D`

for every owner.

Write

`mu(D)=C(d,2)-e_H(D)`

for the number of target nonedges internal to D.

Assume every induced t-set obeys the hereditary target-edge cap

`e_F(W)<=D_cap(t)`.

Define the hereditary missing-edge requirement

`Delta(t)=C(t,2)-D_cap(t)`.

## 2. Same-support owners form a clique

Take two distinct owners y,z in `Y_D`.

They share the pivot p and every vertex of the nonempty support D as target neighbours.

If yz were a target nonedge, regular nonadjacent codegree rigidity would allow at most one common target neighbour. But y,z have at least

`1+d>=2`

common target neighbours.

Contradiction.

Therefore

> `Y_D` is a target clique.                                  (R1)

Also p is target-adjacent to every owner, so

> `{p} union Y_D` is a target `K_(m+1)`.                     (R2)

## 3. Exact dense-block edge count

Consider

`W_D={p} union Y_D union D`.

Every adjacency inside W_D is known:

- p--owner: all target edges;
- owner--owner: all target edges by (R1);
- owner--D: all target edges because D is the core support of every owner;
- p--D: all target nonedges because D lies in the p-core;
- inside D: exactly `C(d,2)-mu(D)` target edges.

Hence W_D has size

`t=m+d+1`

and exactly

`C(m+1,2)+md+C(d,2)-mu(D)`

target edges.

Equivalently, compared with a complete t-vertex graph, the **only** missing target edges are

- the d pivot--D pairs;
- the `mu(D)` internal nonedges of D.

Therefore

> `C(t,2)-e_F(W_D)=d+mu(D)`.                                (R3)

This is an exact identity.

## 4. Hereditary repetition obstruction

Applying the hereditary cap to W_D gives

`e_F(W_D)<=D_cap(t)`.

Using (R3),

> **Repeated-support defect inequality**
>
> `d+mu(D)>=Delta(m+d+1)`.                                  (R4)

Thus support repetition is possible only if the fixed local defect `d+mu(D)` is large enough to pay the hereditary missing-edge requirement at the resulting dense-block size.

This converts multiplicity into a deterministic local defect lower bound.

## 5. r=12 low-support consequences

For the retained r=12 contract,

`D_cap(t)=C(t,2)-11 p_12(t)`.

In particular

`Delta(13)=11`.

If

`m>=12-d`,

choose any `12-d` owners from the repeated class. The corresponding dense block has size13, so (R4) gives

> `d+mu(D)>=11`.                                             (R5)

Consequently, whenever

`d+mu(D)<=10`,

one has

> `m<=11-d`.                                                 (R6)

For the first low-support sizes this is automatic:

### d=2

`mu(D)<=1`, so `d+mu(D)<=3<11`. Therefore

> **m<=9.**                                                   (R7)

### d=3

`mu(D)<=3`, so `d+mu(D)<=6<11`. Therefore

> **m<=8.**                                                   (R8)

### d=4

`mu(D)<=6`, so `d+mu(D)<=10<11`. Therefore

> **m<=7.**                                                   (R9)

These bounds require neither a common missing set nor a charge witness.

## 6. Why R9 is a natural equality boundary

For d=2, multiplicity9 is the absolute last multiplicity not ruled out by the 13-point hereditary cap.

Thus the historical `R9` phenomenon is not an accidental E333 row count. It is the natural endpoint of a general dense-block theorem:

> a two-point support cannot be repeated ten times in any legal r=12 residual, regardless of the shell family label.

When the support is itself a target K2, the nine owners together with D form a target K11. Hence multiplicity9 is also a clique-saturation equality geometry, explaining why any extra adjacency/excess rapidly creates a contradiction.

## 7. Repeated clique-support corollary

If D is a target K_d, then `mu(D)=0` and the owners are complete to D. Therefore

`Y_D union D`

is a target clique of size `m+d`.

Under clique cap `omega(F)<=omega`,

> `m<=omega-d`.                                              (R10)

For r=12 (`omega=11`):

- repeated K2: `m<=9`;
- repeated K3: `m<=8`;
- repeated K4: `m<=7`.

This recovers the same low-support thresholds from a second, purely clique-theoretic viewpoint when the support is complete.

## 8. Equality rigidity

If equality is close in (R4), then W_D is a near-extremal hereditary-cap set whose entire missing-edge set is concentrated in the fixed star p--D plus the internal defect of D.

Thus a high-multiplicity repeated support does not leave arbitrary freedom: it creates a dense block with an explicitly known complement.

This is exactly the type of equality object required by the Global Support-Compatibility program.

## 9. Parameterized nature

The exact identity (R3) is completely parameterized.

All dependence on r enters only through the hereditary cap function `D_cap(t)` and, for the clique corollary, the clique bound omega.

Therefore (R4) transfers verbatim to any higher-r reduction possessing analogous pivot/core structure and hereditary caps.