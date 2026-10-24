# Plateau Distance Compression Theorem

Status: `PROVED_CONDITIONAL` / `PROVED_SYMBOLIC` as marked below.

Scope: the remaining fully-decorated distinct-support d2 plateau under the general-r repivot contract.

Dependencies:

- residual-core contract A;
- anchor-excess hypothesis B, hence `q<=3r-1`;
- exact regular repivot set exchange;
- the proved third coordinate `zeta`;
- `alpha(H)<=3`;
- for the scalar matching/allowance bounds only, the inherited hereditary core cap `K<=2r-2`.

Throughout `r>=12`.

---

## 1. Plateau-distance coordinate

For a legal regular pivot p define

`eta(p)`
` = #{ x in A_p : x is regular, d_p(x)=1,`
`      (q_x,tau_x,zeta(x))=(q_p,tau_p,zeta(p)) }`.

Thus eta counts degree-one neighbours of p inside the exact `Phi_3=(q,tau,zeta)` plateau graph.

It is an integer with

`0<=eta<=r+1`.

Therefore

> **`Phi_4=(q,tau,zeta,eta)`**

is a genuine bounded lexicographic potential.

This statement needs no monotonicity theorem: choose a legal pivot maximizing the displayed bounded integer tuple.

**Status:** `PROVED_SYMBOLIC`.

---

## 2. Exact pair-set transition for one common-S d2 family

Fix a d2 common-S family at p, with

`S={s_1,s_2}`

and distinct owners `y_i` having core supports

`D_i=N_H(y_i)`, `|D_i|=2`.

Repivot from p to one owner `y_i`. Then

`H_i=(H\D_i) union S`,

`A_i=(A\(S union {y_i})) union D_i union {p}`.

For another owner `y_j`, `j!=i`, put

`h_ij=|D_i intersect D_j|`.

Because `y_j` was missing exactly S in the old shell and had exactly D_j as its old core-neighbour set, direct set exchange gives

> `S_j^(i)=D_i\D_j`,
>
> `D_j^(i)=D_j\D_i`,
>
> **`d_i(y_j)=2-h_ij`.**                                     (2.1)

Hence:

- identical supports (`h=2`) become d0;
- one-point overlaps (`h=1`) become d1;
- disjoint supports (`h=0`) remain d2, now in the common missing pair D_i.

This is exact and does not use a charge inequality.

**Status:** `PROVED_SYMBOLIC`.

---

## 3. Intersection-to-d1 transport

Now restrict to owners which are `Phi_3`-flat with p.

At `zeta(p)=0`, a `Phi_3`-flat exact class cannot repeat: if a support had multiplicity at least2, the exact zeta update would give positive zeta after repivot and strictly improve `Phi_3`.

So the remaining distinct-support plateau is represented by a simple graph

`G_S`

whose vertices are the support classes D_i and where two supports are adjacent iff they overlap in one core point.

Let

`deg_G(D_i)=#{j!=i:|D_i intersect D_j|=1}`.

Every overlapping owner y_j is, by (2.1), a regular d1 owner in the y_i-view. Since q, tau and zeta are pivot-state invariants and all chosen owners lie on the same `Phi_3` plateau, every such y_j is counted by `eta(y_i)`.

Therefore

> **`eta(y_i)>=deg_G(D_i)`.**                                 (3.1)

At a `Phi_4`-maximal pivot p every legal `Phi_3`-flat repivot satisfies

`eta(y_i)<=eta(p)`.

Consequently

> **Distinct-support overlap bound**
>
> `Delta(G_S)<=eta(p)`.                                      (3.2)

Thus arbitrary d2 overlap is not a new free parameter: every overlap degree is paid for by an already-visible d1 plateau population.

**Status:** `PROVED_SYMBOLIC`.

---

## 4. Matching extraction

Let N be the number of distinct `Phi_3`-flat d2 supports in the fixed class S.

The support-intersection graph G_S has maximum degree at most eta by (3.2). A greedy independent set in G_S therefore has size at least

> **`nu >= ceil(N/(eta+1))`.**                                (4.1)

An independent set of G_S is exactly a pairwise-disjoint family of core 2-supports.

Hence every large distinct-support plateau contains a large disjoint matching unless a comparably large d1 plateau population eta already exists.

**Status:** `PROVED_SYMBOLIC`.

---

## 5. Exact charge bound for a disjoint q-flat subfamily

For the fixed d2 shell pair S write

`w_x=kappa_x+e_F(x,S)`,

`mu(D)=1-e_H(D)`,

and let a be the common allowance.

Every q-flat support satisfies

`w(D)+mu(D)=a`.                                               (5.1)

Take any pairwise-disjoint q-flat subfamily `D_1,...,D_nu`.
Because the supports are disjoint,

`sum_i w(D_i)=w(U)<=W`,

where U is their union and

`W=sum_H w_x=K+2r-2+a+b`,

`b=e_M(S) in {0,1}`.

Also `sum_i mu(D_i)<=nu`. Therefore (5.1) gives

`nu a<=W+nu`,

or

> **`nu(a-1)<=K+2r-2+a+b`.**                                 (5.2)

Using the inherited hereditary core cap

`K<=2r-2`

gives

> **`nu(a-1)<=4r-4+a+b`.**                                   (5.3)

Combining with (4.1), for `a>=2`,

> `ceil(N/(eta+1))(a-1)<=4r-4+a+b`.                          (5.4)

This is the first exact scalar inequality coupling

- distinct-support multiplicity N,
- support-overlap complexity eta,
- and d2 allowance a.

**Status:** (5.2) `PROVED_SYMBOLIC`; (5.3)--(5.4) `PROVED_CONDITIONAL` on the inherited hereditary cap.

---

## 6. Complete closure of allowance a=0 and a=1

### a=0

Every q-flat support has

`w(D)=0`, `mu(D)=0`.

So it is a target edge with two zero-charge endpoints.

Two distinct supports cannot overlap: if

`D={x,u}`, `E={x,v}`

with all three charges zero, row closure for u against E would require

`e_H(u,E)=0`,

but `ux` is already a target edge. Contradiction.

Thus the supports are disjoint. Between two distinct supports row closure gives no target cross-edge. Four supports would therefore supply an independent 4-set by choosing one endpoint from each support, contradicting `alpha(H)<=3`.

Hence

> **`a=0 => N<=3`.**                                         (6.1)

### a=1

Every q-flat support contains at least one zero-charge endpoint:

- if `mu=1`, then both endpoint charges are zero;
- if `mu=0`, the two charges sum to one.

For a zero-charge vertex z define its support signature

`sig(z)={D_i:z in D_i}`.

Distinct zero signatures are pairwise target-nonadjacent by row closure, so `alpha(H)<=3` permits at most three distinct zero signatures.

Fix one signature Sigma. If `|Sigma|>=3`, all supports in Sigma are distinct 2-sets containing the same zero-charge hub x. Write them

`{x,u_1},...,{x,u_k}`.

For each leaf u_i, q-flatness at allowance1 gives

- `w(u_i)=1` if `xu_i` is a target edge;
- `w(u_i)=0` if `xu_i` is a target nonedge.

Applying row closure to u_i against `{x,u_j}` shows in either case

`u_i u_j` is a target nonedge.

Thus the leaves are pairwise independent, so `k<=3`.

Therefore every zero signature contains at most three support labels. Since every support contains a zero-charge endpoint and there are at most three signatures,

> **`a=1 => N<=9`.**                                         (6.2)

So the distinct-support scalable plateau begins only at allowance at least2.

**Status:** `PROVED_CONDITIONAL` only on the residual core alpha bound; no hereditary cap is used.

---

## 7. d1 scale-transfer bound

The eta population lives in at most five d1 shell classes by the already-proved shell-incidence theorem.

Hence one d1 shell singleton class contains at least

`N_1>=ceil(eta/5)`                                             (7.1)

`Phi_3`-flat owners.

In the neutral-free slice `zeta=0` these singleton supports are distinct. Let c be that fixed d1 class allowance.

For d1, `t_s=r+c`, so the total common-S core charge is

`W_1=K+r+c`.

Every q-flat singleton support u has

`w_u=c`.

Distinctness gives

`N_1 c<=W_1=K+r+c`.

Under `K<=2r-2`,

> **`(N_1-1)c<=3r-2`.**                                     (7.2)

If c=0, row closure makes the distinct support vertices pairwise target-nonadjacent, so `N_1<=3`.

Thus any linear eta population automatically concentrates into a linear d1 class whose allowance is bounded by an absolute constant.

For example, if `eta>=eps*r` and r is large enough that `ceil(eta/5)>=eps*r/5`, then

> `c <= (3r-2)/(eps*r/5-1) = 15/eps + o(1)`.                (7.3)

**Status:** `PROVED_CONDITIONAL` on the hereditary core cap for (7.2)--(7.3).

---

## 8. Asymptotic low-endpoint compression dichotomy

Let a fixed fully-decorated distinct-support d2 class have

`N>=eps*r`

for some fixed `eps>0` along an unbounded sequence of r.

Then exactly one of the following asymptotic routes occurs.

### Route A — d1 concentration

`eta=Omega(r)`.

Then by Section7 one of the at-most-five d1 shell classes has linear size and **O(1) allowance**.

### Route B — large d2 matching

`eta=o(r)`.

Then (4.1) gives

`nu>=N/(eta+1)=omega(1)`.

Equation (5.3) then yields

`a-1 <= (4r-4+a+b)/nu`.

In particular a cannot remain a positive linear fraction of r; otherwise the right side would make nu=O(1). Hence

> **`eta=o(r)` and `N=Omega(r) => a=o(r)`.**                 (8.1)

Equivalently:

> every scalable d2 plateau with linearly large allowance transfers linearly many plateau states into d1; if it does not, its allowance is sublinear.

This is an all-large-r structural compression theorem. It does not yet eliminate the final low-allowance terminal, but it removes the possibility of a simultaneously

- linearly large distinct d2 family,
- linearly large allowance,
- and sublinear d1 correction population.

**Status:** `PROVED_CONDITIONAL` on A+B plus the inherited hereditary core cap.

---

## 9. Surviving terminal after this theorem

The former blocker "arbitrary fully-decorated distinct-support d2 plateau" is replaced by only two scale mechanisms:

1. a **bounded-allowance d1 concentration terminal**;
2. a **sublinear-allowance d2 matching terminal**, with exact matching inequality (5.4).

Additionally, allowance0 and allowance1 d2 distinct-support systems are absolutely bounded (`N<=3` and `N<=9`).

The next single blocker is therefore:

> classify / eliminate the first genuinely scalable low-allowance level `d2, a=2` together with the bounded-allowance d1 terminal.

The natural a=2 clean matching skeleton has pairwise-disjoint target-K2 supports of endpoint charge `(1,1)` except for at most three supports carrying a zero endpoint. Between two clean supports row closure makes the target cross graph a matching of size at most2. This is the next rigid design object to classify.