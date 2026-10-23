# Global Hereditary Support-Packing Theorem

Status: `PROVED_ANALYTIC`.

This theorem abstracts the recurring D13/D14/D17/common-K10 arguments into one parameterized dense-base inequality.

## 1. Setup

Let G be any graph satisfying a hereditary induced-edge cap

`e_G(W)<=D(|W|)`

for every vertex set W in the relevant size range.

Let B be a fixed base vertex set, `|B|=b`, with known target-edge count

`e_G(B)=E_B`.

Let

`D_1,...,D_k`

be pairwise disjoint support sets outside B, with `|D_i|=d_i`.

For each i suppose the support D_i has

- owner multiplicity `m_i` inside B;
- every owner is target-adjacent to every point of D_i, giving at least `d_i m_i` forced base-support edges;
- `c_i>=0` additional certified base-support target edges not already included in the owner incidences;
- internal target-edge count `e_i=e_G(D_i)`.

Write

`c_ij=e_G(D_i,D_j)`

for cross target edges between distinct support blocks.

No assumption is made that these are all edges in the induced set; omitted edges only strengthen the inequality below.

## 2. Exact hereditary packing inequality

Apply the hereditary cap to

`W=B union D_1 union ... union D_k`.

The induced target edges include at least

`E_B`
` + sum_i (d_i m_i+c_i+e_i)`
` + sum_(i<j) c_ij`.

Therefore

> **Hereditary support-packing inequality**
>
> `sum_i d_i m_i`
> ` + sum_i(c_i+e_i)`
> ` + sum_(i<j)c_ij`
> ` <= D(b+sum_i d_i)-E_B`.                                  (H1)

This is a deterministic analytic inequality.

## 3. Uniform d-support consequence

If all supports have size d, then

> `d sum_i m_i`
> ` + sum_i(c_i+e_i)`
> ` + sum_(i<j)c_ij`
> ` <= D(b+kd)-E_B`.                                        (H2)

Dropping nonnegative terms gives the crude but universal owner-capacity bound

> `sum_i m_i <= floor((D(b+kd)-E_B)/d)`.                    (H3)

If every support is a target clique K_d, then `e_i=C(d,2)`, so

> `d sum_i m_i + k C(d,2)`
> ` <= D(b+kd)-E_B`,                                        (H4)

before counting any cross or extra base-support edges.

## 4. Equality rigidity

Suppose equality holds in H1. Then every omitted possible contribution must vanish. In particular, once the certified terms already exhaust the hereditary cap:

- no additional B--D_i target edge may exist;
- no additional D_i--D_j target edge may exist beyond the certified c_ij;
- every internal support edge count is exact;
- the induced set W saturates the hereditary cap D(|W|).

Thus a scalar capacity equality automatically becomes a global adjacency/nonadjacency prescription.

This is precisely the mechanism behind many previously separate equality cases.

## 5. Recovery of the corrected q36 D17 theorem

In the corrected far-K2 c=8 no-d2 geometry:

- `B={p} union C union Y`;
- `b=11`;
- `E_B=55-rho`;
- two disjoint supports have `d=3`;
- `D(17)=81`.

H2 becomes

`3(r+s)+e_H(D)+e_H(E)+e_H(D,E)+e_F(Y,D union E)<=26+rho`,

which is exactly `Q36_F2_FAR_K2_C8_NO_D2_MULTISUPPORT_D17_CAPACITY.md`.

Thus D17 is not a special q36 trick; it is a direct instance of H1.

## 6. D13/D14 multiplicity bounds as one-support instances

For k=1, H1 gives

`d m+c_1+e_1 <= D(b+d)-E_B`.                                (H5)

All repeated-support D13/D14 inequalities used in the backend are instances of this formula with different dense bases B and support sizes d.

The equality states in those arguments should therefore be classified through Section 4 rather than re-derived separately for each E-layer.

## 7. Multi-support equality principle

The strongest use of H1 is not the crude multiplicity bound H3, but simultaneous saturation.

If several support classes have large multiplicities, then the owner terms `d_i m_i` nearly exhaust the cap. Consequently:

- support internal edges are forced to their minimum compatible with the local row allowance;
- support cross edges are forced to zero or a tiny exact value;
- inactive-base incidences are forced to zero;
- the base itself must be extremal or near-extremal.

Combining this with `GLOBAL_SUPPORT_REPETITION_CHARGING_THEOREM.md` gives the desired dichotomy:

1. too much incidence/charge => improving repivot;
2. otherwise the hereditary cap is nearly saturated => rigid equality geometry.

This is the analytic mechanism intended for the final Global Support-Compatibility Bridge.

## 8. Parameterization and r>=13

H1 depends only on:

- the hereditary cap function D;
- base size and edge count `(b,E_B)`;
- support sizes;
- owner multiplicities;
- certified internal/cross/base-support incidences.

It does not depend on the labels E333,...,E340 or on the numerical value r=12.

Therefore, whenever an r>=13 reduction supplies an analogous hereditary cap and dense pivot base, the same support-packing theorem applies verbatim.