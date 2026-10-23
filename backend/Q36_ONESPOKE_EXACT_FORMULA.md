# q36 candidate coverage — exact nonadjacent one-spoke formula

Status: `PROVED` under the standard legal backend contract and CORE211 q36 top channel.

This supplies the core-rich half of `Q36_CANDIDATE_COVERAGE_CLUSTER_REDUCTION.md`.

## 1. Setup

Let p be a q36 top-channel pivot with shell A and 211-edge core H.

Let v be a legal degree-13 pivot lying in H with exactly one target neighbour `a in A`. Then

- `d_H(v)=12`;
- `N_F(v)={a} union D`, where `D=N_H(v)` has size12;
- put `Z=H\(D union {v})`, so `|Z|=22`.

The new shell at v is exactly

`A_v={a} union D`.

For `u in H` write

`kappa_u=d_H(u)-12`.

Put

`m(D)=C(12,2)-e_H(D)=66-e_H(D)`.

## 2. Exact charge formula

Directly from the new 13-shell,

`q_v = 78-e_H(D)-e_F(a,D)+g_a+sum_(u in D)g_u`.            (1)

For `u in D`, if `r_u=e_F(u,A)` is its old shell incidence, then

`g_u=d_F(u)-13=kappa_u+r_u-1`.

Summing over the twelve vertices of D,

`sum_D g_u=kappa(D)+e_F(D,A)-12`.

Substitute into (1). The `a--D` term cancels, giving

> `q_v=m(D)+kappa(D)+g_a+e_F(D,A\{a})`.                    (2)

Every term on the right is nonnegative.

## 3. Equivalent 22-point anti-neighbourhood formula

Partition the old 211-core as

`{v} disjoint_union D disjoint_union Z`.

Since v has exactly the twelve neighbours D,

`211 = 12 + e_H(D)+e_H(Z)+e_H(D,Z)`.                        (3)

Also

`kappa(D)=sum_(u in D)(d_H(u)-12)`
`=12+2e_H(D)+e_H(D,Z)-144`
`=2e_H(D)+e_H(D,Z)-132`.

Therefore

`m(D)+kappa(D)`
`=66-e_H(D)+2e_H(D)+e_H(D,Z)-132`
`=e_H(D)+e_H(D,Z)-66`
`=133-e_H(Z)`

by (3).

Hence (2) is equivalently

> `q_v=133-e_H(Z)+g_a+e_F(D,A\{a})`.                       (4)

## 4. The 22-point anti-neighbourhood is near Mantel-extremal

Because every vertex of Z is target-nonadjacent to v, an independent triple in H[Z] together with v would be an independent4-set in H. But every legal 35-core has `alpha(H)<=3`. Therefore

`alpha(H[Z])<=2`.

Equivalently the complement of H[Z] is triangle-free. Mantel gives

`e_H(Z)>=C(22,2)-floor(22^2/4)`
`=231-121`
`=110`.                                                     (5)

There is also a useful upper bound from the inherited 13-point density cap.

The induced set `{v} union D` has13 vertices and exactly

`12+e_H(D)`

target edges. Since `D(13)=67`,

`e_H(D)<=55`,

so

`m(D)>=11`.                                                 (6)

As `kappa(D)>=0`, the identity `m(D)+kappa(D)=133-e_H(Z)` gives

`e_H(Z)<=122`.                                              (7)

Thus every legal one-spoke pivot carries a 22-point anti-neighbourhood satisfying

> `110<=e_H(Z)<=122`, `alpha(H[Z])<=2`.                     (8)

In complement language, `overline{H[Z]}` is triangle-free with between109 and121 edges, i.e. within12 edges of the Mantel extremum.

## 5. D14 refinement

The full closed neighbourhood of v is the 14-set

`{v,a} union D`.

It has

`13+e_H(D)+e_F(a,D)`

target edges. The inherited `D(14)=69` cap gives

`e_H(D)+e_F(a,D)<=56`,

or

> `m(D)>=10+e_F(a,D)`.                                     (9)

Combining (2) and (9),

`q_v>=10+kappa(D)+g_a+e_F(D,A)`.                           (10)

This inequality will be useful when several one-spoke pivots share or interact with shell rows.

## 6. Candidate-coverage consequence

If a q36 shell has no low regular part, `Q36_CANDIDATE_COVERAGE_CLUSTER_REDUCTION.md` proves that it has at most two adjacent regular pivots.

The CORE211 pivot-abundance theorem guarantees at least seven other legal pivots. Hence at least five are nonadjacent one-spoke pivots of the form treated here.

Therefore the shell-poor branch is not arbitrary: it contains at least five degree-12 core vertices v_i whose 22-point anti-neighbourhoods Z_i all satisfy the near-Mantel window (8), together with the exact charge identity (4).

The remaining task in this branch is a simultaneous stability/compatibility theorem for these at least five near-Mantel anti-neighbourhoods.