# q36 f=2 far-target-K2 — c=8 no-d2 A=3 multiplicity-four one-edge full closure

Status: `PROVED` under `Q36_F2_FAR_K2_C8_NO_D2_A3_MULT4_ONEEDGE_REDUCTION.md`, common-S row closure, CORE211, q36 lexicographic maximality, and `alpha(H)<=3`.

This closes all three residual owner architectures left by the multiplicity-four one-edge reduction at once.

## 1. Setup

Let D={a,b,c} be the multiplicity-four support with exactly one internal target edge ab. Thus c is target-nonadjacent to both a and b.

The preceding reduction proves:

- `w(D)=0`, where `w_v=kappa_v+e_F(v,S)` and `S=F union {x}`;
- there is a unique support class E disjoint from D;
- E is a repeated target K3 of multiplicity2 or3;
- common-S row closure gives `e_H(D,E)=0`.

In particular

`w_a=w_b=w_c=0`.                                             (1)

Since kappa is nonnegative, (1) gives `kappa_c=0`; hence

`d_H(c)=12`.                                                  (2)

Because c is isolated inside H[D] and D is target-anticomplete to E, c has no target neighbour in `(D union E)\{c}`. Therefore all twelve H-neighbours of c lie in

`L=V(H)\(D union E)`,

which has size29. Thus

> at most12 vertices of L are target-adjacent to c.           (3)

## 2. Every vertex of L has positive common-S weight

Take v in L.

If `w_v=0`, row closure against D and E gives

`e_H(v,D)=e_H(v,E)=0`.

Choose the target-nonedge pair `{a,c}` in D and any e in E. Since D--E is target-anticomplete, the four vertices

`{a,c,e,v}`

would be an independent4-set in H, contradicting `alpha(H)<=3`.

Therefore

> `w_v>=1` for every v in L.                                 (4)

## 3. Every weight-one vertex must meet c

Suppose `w_v=1`.

Row closure gives

`e_H(v,D)<=1`, `e_H(v,E)<=1`.                               (5)

Assume for contradiction that vc is a target nonedge.

For every e in E, the triple `{a,c,e}` is target-independent: ac is a nonedge and D--E has no target edges. To prevent `{a,c,e,v}` from being an independent4-set for all three choices of e, v must either

- be target-adjacent to a, or
- be target-adjacent to every point of E.

The second option is impossible by `e_H(v,E)<=1`. Hence va must be a target edge.

Applying the same argument to the independent triple `{b,c,e}` forces vb to be a target edge.

Then `e_H(v,D)>=2`, contradicting (5).

Therefore

> `w_v=1` implies `vc` is a target edge.                      (6)

By (3), at most12 vertices of L can have weight1.

## 4. Global weight contradiction

The remaining at least

`29-12=17`

vertices of L have weight at least2. Hence

`sum_(v in L) w_v >=12*1+17*2=46`.                         (7)

On the other hand the exact global common-S weight in the c=8 no-d2 A=3 shell is

`sum_(v in H) w_v
 = sum_H kappa_v + e_F(S,H)`.

CORE211 gives `sum_H kappa_v=2`.

The two far rows contribute total core incidence `22-a_F`. For the active decorated vertex x,

`A=nu_x+g_x-a_F=3`

implies its core-row size is

`d_M(x)+g_x=13+a_F-t_x`.

Therefore

`e_F(S,H)=(22-a_F)+(13+a_F-t_x)=35-t_x`,

and so

> `sum_H w_v =37-t_x <=37`.                                 (8)

Equations (7)--(8) contradict each other.

## 5. Conclusion

No corrected-contract c=8 far-K2 no-d2 A=3 state can contain a multiplicity-four one-edge support.

Therefore

> `A=3, multiplicity4, one-edge support` is EMPTY.

This closes simultaneously all `4+3+1` and `4+2+1+1` residual owner architectures from `Q36_F2_FAR_K2_C8_NO_D2_A3_MULT4_ONEEDGE_REDUCTION.md`.