# q36 f=2 far-target-K2 — c=8, one d2 row, A=3, m_E=2 exact reduction

Status: `PROVED REDUCTION` under `Q36_F2_FAR_K2_C8_D2_A3_REPEATED_K3_SIGNATURE_REDUCTION.md`, common-S row closure, q36 lexicographic maximality, and `alpha(H[U])<=2`.

This reduces the m_E=2 terminal to one exact common-E-pair state.

## 1. Setup

D and E are disjoint target K3 supports with multiplicities3 and2 respectively. The signature reduction proves

- `u(D)=u(E)=2`;
- there are exactly two remaining owner supports T1,T2;
- each T_i meets D in exactly one point;
- each T_i has signature `(1,1,1)` or `(1,2,0)` relative to `(D,E,outside)`.

All d3 owners belong to the same allowance-three class with active missing vertex x; the other two decorated shell vertices are retained under any d3 repivot.

## 2. Every remaining T has exact defect two

Each T contains at least two globally decorated core vertices:

- one vertex from repeated D;
- and either one or two vertices from repeated E.

If T had full defect3, its repivot would stay at q36, remove x, retain the two inactive decorated shell vertices, and insert at least two globally decorated core vertices. The new shell would have strictly larger tau than the original q36 shell, contradicting lexicographic maximality.

Thus `Delta(T)<=2`.

Since T properly overlaps D, the proper-overlap cost is2, so `Delta(T)>=2`. Hence

> `Delta(T)=2` for every remaining T.                         (1)

## 3. Signature (1,1,1) is impossible

Let

`T={d,e,v}`

with `d in D`, `e in E`, and `v outside D union E`.

The D--E target-nonedge bipartite graph has vertex-cover number3. Since alpha(H[U])<=2, v must cover all those nonedges, so

`e_H(v,D)+e_H(v,E)>=3`.

Row closure against D and E gives each term at most `w_v`, hence

`w_v>=2`.                                                    (2)

Using `Delta(T)=2`, all terms are nonnegative, so equality forces

- `w_v=2`;
- `w_d=w_e=0`;
- `m(T)=0`.

Thus T is a target K3 and in particular de is a target edge.

But `e outside D` and `w_e=0`. Row closure against D gives

`e_H(e,D)<=w_e=0`,

contradicting the target edge de.

Therefore

> signature `(1,1,1)` is impossible.                          (3)

## 4. Exact structure of signature (1,2,0)

Let

`T={d,e1,e2}`

with `d in D` and `e1,e2 in E`.

Because E is a target K3, e1e2 is a target edge. Put

`k_pair = e_H(d,{e1,e2})`,
`k = e_H(d,E)`.

Then `k>=k_pair`, and the internal missing count of T is

`m(T)=2-k_pair`.

Row closure against E gives

`k<=w_d`.

Using the exact defect equation (1),

`2 = m(T)+w_d+w_e1+w_e2`
`  >= 2-k_pair+k+w_e1+w_e2`
`  >= 2`.

Thus equality holds throughout:

- `k=k_pair`;
- `w_d=k_pair`;
- `w_e1=w_e2=0`.                                            (4)

Now e1 and e2 lie outside D. Row closure against D and (4) give

`e_H(e_i,D)<=w_ei=0`.

Therefore neither e1 nor e2 is target-adjacent to d, so `k_pair=0`. Hence (4) sharpens to

> `w_d=w_e1=w_e2=0`,
> `e_H(d,E)=0`,
> `m(T)=2`.                                                  (5)

Thus T has exactly one internal target edge, namely e1e2, and its three vertices carry zero common-S weight.

## 5. The two T supports use the same E-pair

By (3), both T1,T2 have signature `(1,2,0)` and satisfy (5).

Suppose they used two distinct two-subsets of the three-point set E. Any two distinct 2-subsets of a 3-set have union E. Every E vertex would then lie in one of the selected pairs and therefore have w=0 by (5).

Hence

`u(E)=sum_(e in E)w_e=0`,

contradicting the already proved exact repeated-support defect

`u(E)=2`.

Therefore the two T supports use one common E-pair P={e1,e2}. Let e3 be the third E vertex. Then

- `w_e1=w_e2=0`;
- `w_e3=2`;
- both T supports are of the form `{d_i,e1,e2}`;
- every selected d_i has w=0 and is target-anticomplete to E;
- each T has exactly the one target edge e1e2.

## 6. Current m_E=2 terminal

Only one binary choice remains:

1. the two T owners use the same D vertex d, so the same one-edge support `{d,e1,e2}` has multiplicity2;
2. they use two distinct D vertices d1,d2, giving two distinct one-edge supports sharing the E-pair.

The next task is to eliminate these two equality states by q35 secondary-shell / D14 saturation.