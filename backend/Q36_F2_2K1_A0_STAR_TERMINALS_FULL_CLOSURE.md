# q36 f=2, 2K1 far, a_F=0 — full closure of all remaining star terminals

Status: `PROVED` under the q36 CORE211 parent contract, `Q36_F2_2K1_A0_C2_REPEATED_STAR_REDUCTION.md`, `Q36_F2_2K1_A0_C1_STAR_REDUCTION.md`, row closure, and `alpha(F)<=4`.

This closes the last three equality terminals of the entire `2K1, a_F=0` branch.

## 1. Global q36 / CORE211 budget

In the q36 E338 parent state,

- the 35-core H has `e(H)=211` and `delta(H)>=12`;
- writing `kappa_v=d_H(v)-12`, one has `sum_H kappa_v=2`;
- the 49-point graph has total degree excess over13

`sum_(v in F)(d_F(v)-13)=2*338-49*13=39`.

Let the two far regular shell vertices be `a,b`. Their 12-point core supports A,B are disjoint by the regular missing-edge zero-gap theorem. Every d2 low support D lies in

`R=H\(A union B)`.

For a core vertex `r in R\D`, the d2 row closure reads

`e_H(r,D)<=kappa_r+e_F(r,{a,b})`.

But r lies outside the two far supports, so `e_F(r,{a,b})=0`. Hence every core-regular such r satisfies

`e_H(r,D)=0`.                                               (1)

Since total core excess is only2, among the nine vertices of `R\D` at least seven are core-regular. Fix any such r.

## 2. Independent-five forcing against a star terminal

Fix an endpoint d of D and a decorated shell vertex x in X with `dx` a target nonedge.

If also `rx` were a target nonedge, then

`{a,b,d,x,r}`

would be an independent5-set:

- `ab` is a target nonedge;
- the far vertices are target-anticomplete to X and to R in the `2K1,a_F=0` branch;
- `d` lies in R, hence is target-nonadjacent to a,b;
- `dr=0` by (1);
- `dx=0` by choice;
- `rx=0` by assumption.

This contradicts `alpha(F)<=4`.

Therefore every core-regular `r in R\D` is target-adjacent to every X-vertex that is target-nonadjacent to d. Consequently, if d has at least s nonneighbours in X, then

`d_F(r)>=d_H(r)+s=12+s`.                                  (2)

Thus r contributes at least `s-1` units of global degree excess above13.

## 3. c=2 repeated-support K1,4 terminal

By `Q36_F2_2K1_A0_C2_REPEATED_STAR_REDUCTION.md`:

- `|X|=9`;
- `M[X]=K1,4 disjoint_union 4K1`;
- both endpoints of the repeated pure K2 support D are target-adjacent in X exactly to the missing-star centre h.

Hence either endpoint d of D has exactly eight target nonneighbours in X. Taking `s=8` in (2), each of the at least seven core-regular vertices of `R\D` has

`d_F(r)>=20`,

so contributes at least7 units of global excess. These seven vertices alone contribute at least

`7*7=49>39`,

contradicting the global excess budget.

Therefore the c=2 repeated star terminal is EMPTY.

## 4. c=1, nu=2 terminal

By `Q36_F2_2K1_A0_C1_STAR_REDUCTION.md`:

- `|X|=10`;
- `M[X]=K1,2 disjoint_union 7K1`;
- both endpoints of the pure K2 support D are target-adjacent in X exactly to the star centre.

Thus each endpoint has nine X-nonneighbours. In particular `s>=8`, so the same seven-vertex excess argument yields at least49 units of global excess, impossible.

Hence the c=1, nu=2 terminal is EMPTY.

## 5. c=1, nu=3 terminal

Here

- `M[X]=K1,3 disjoint_union 6K1`;
- both D-endpoints are adjacent to the star centre;
- there is at most one additional D--X target edge in total.

Therefore each D-endpoint has at most two target neighbours in X, hence at least eight target nonneighbours in X. Again `s>=8`, and the seven core-regular vertices of `R\D` contribute at least49 units of global excess, contradicting39.

Hence the c=1, nu=3 terminal is EMPTY.

## 6. Conclusion

All three remaining `2K1,a_F=0` equality terminals are impossible. Combined with the previously proved c>=3 closures and the c=2 distinct-support closure:

> the entire q36 f=2 far-2K1 branch with `a_F=0` is EMPTY.

No statement is made here about the `a_F=1` branch or the far-target-K2 topology.