# q36 shell-poor — simultaneous one-spoke interface

Status: `PROVED REDUCTION` under the q36 CORE211 top-channel contract, `Q36_CANDIDATE_COVERAGE_CLUSTER_REDUCTION.md`, `Q36_ONESPOKE_EXACT_FORMULA.md`, inherited D14, CORE211, and the parent `alpha(F)<=4` contract.

This couples the at-least-five one-spoke pivots in the shell-poor regime. It does not close the regime by itself.

## 1. Global shell/core decoration ledger

Let p be the q36 pivot, A its 13-shell, M the shell missing graph, and H the 35-core. Put

`G=sum_(a in A) g_a`.

Since `q=e(M)+G=36` and inherited D14 gives `e(M)>=22`,

`G<=14`.                                                     (1)

In the shell-poor regime at most two shell vertices are globally regular. Every other shell vertex is decorated and contributes at least one unit, hence

`G>=11`.                                                     (2)

Thus

> `11<=G<=14`.                                               (3)

The total shell-core incidence is

`I=sum_(a in A)(d_M(a)+g_a)=2e(M)+G=72-G`.                 (4)

For a core vertex u write `kappa_u=d_H(u)-12`. CORE211 gives

`sum_H kappa_u=2`.

If r_u is the number of target shell neighbours of u, then

`13+g_u = (12+kappa_u)+r_u`,

so

`r_u=1+g_u-kappa_u`.

Summing over H and comparing with (4),

`33+sum_H g_u =72-G`.

Therefore

> `G_H:=sum_(u in H)g_u =39-G`.                              (5)

Combining with (3),

> `25<=G_H<=28`.                                             (6)

## 2. Decoration localization for one one-spoke pivot

Let v be a nonadjacent one-spoke legal pivot:

- `d_H(v)=12`;
- `g_v=0`;
- v has exactly one target neighbour a in the old shell A.

Put

`D=N_H(v)`, |D|=12,
`Z=H\(D union {v})`, |Z|=22.

The exact one-spoke formula is

`q_v=m(D)+kappa(D)+g_a+e_F(D,A\{a})`.                       (7)

For u in D, its shell incidence is `1+g_u-kappa_u`. Summing over D and removing the incidences to a gives

`e_F(D,A\{a})=12+g(D)-kappa(D)-e_F(a,D)`.                  (8)

Substituting (8) into (7),

`q_v=m(D)+12+g_a+g(D)-e_F(a,D)`.                            (9)

Inherited D14 for the closed neighbourhood of v gives

`m(D)>=10+e_F(a,D)`.                                        (10)

Therefore

`q_v>=22+g_a+g(D)`.                                         (11)

The old pivot p is q36-maximal, so every legal repivot has `q_v<=36`. Hence

> `g_a+g(D)<=14`.                                           (12)

Using (5), `g_v=0`, and `H={v} union D union Z`,

`g(Z)=G_H-g(D)>=39-G-(14-g_a)`.

Thus

> `g(Z)>=25-G+g_a`.                                         (13)

Since G<=14,

> `g(Z)>=11+g_a>=11`.                                       (14)

So every one-spoke anti-neighbourhood carries at least eleven units of core decoration.

## 3. Complement-core formulation

Let

`J=overline(H)`.

CORE211 gives

`e(J)=C(35,2)-211=384`.

The H-degree multisets imply J-degrees in `{20,21,22}`, and every ordinary degree-12 core vertex has J-degree22.

For a one-spoke v,

`Z=N_J(v)`.

Since H has alpha at most3, J is K4-free. Consequently `J[Z]` is triangle-free. This recovers the near-Mantel viewpoint of `Q36_ONESPOKE_EXACT_FORMULA.md` in a simultaneous global graph J.

## 4. A core nonedge gives a two-label shell triangle cover

Let v,w be two one-spoke pivots, with unique old-shell target neighbours a_v,a_w.

Assume vw is a target nonedge in H, equivalently `vw in E(J)`.

Take any three shell vertices T contained in

`A\{a_v,a_w}`.

Both v and w are target-anticomplete to every vertex of T, because each has only its own unique shell target neighbour.

If T were target-independent in the parent graph, then

`T union {v,w}`

would be an independent5-set, contradicting `alpha(F)<=4`.

Therefore

`alpha(F[A\{a_v,a_w}])<=2`.                                 (15)

Equivalently, a target-independent shell triple is a triangle in the shell missing graph M. Thus:

> every triangle of M meets `{a_v,a_w}`.                    (16)

If `a_v=a_w`, every triangle of M contains that single common label.

Hence every J-edge among one-spoke pivots produces a size-at-most-two transversal of all shell-missing triangles.

## 5. Shell-poor simultaneous frontier

By the existing cluster reduction, the shell-poor regime contains at least five nonadjacent one-spoke pivots.

For each such pivot v we now simultaneously have:

1. a 22-point J-neighbourhood `Z_v` whose induced J-graph is triangle-free;
2. core-decoration mass `g(Z_v)>=11+g_(a_v)`;
3. for every J-edge vw among these pivots, the two labels `{a_v,a_w}` hit every triangle of M.

Thus the remaining shell-poor problem is no longer five independent near-Mantel problems. It is a joint system coupling

- a K4-free 35-point complement-core J with 384 edges and degrees 20--22;
- at least five degree-22 one-spoke vertices;
- 25--28 units of total core decoration;
- a 13-point shell missing graph with 22--25 edges;
- and the triangle-cover constraints (16).

The next targets are:

- derive a lower bound on J-edges among the one-spoke pivots, forcing several incompatible two-label triangle covers of M; or
- use the decoration lower bounds on the overlapping sets Z_v to exceed the global budget `G_H<=28`.

No external extremal classification is assumed in this file.