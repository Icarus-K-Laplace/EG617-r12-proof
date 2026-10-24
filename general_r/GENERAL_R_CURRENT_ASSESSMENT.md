# General-r Current Assessment

Status: **OPEN**, but the all-large-r architecture is now sharply compressed.

## 1. Contextual full-color cap

For a target residual on `kr+1` vertices arising inside the original balanced `r`-coloring, if

`alpha(F)<=k`,

then every non-target color `C_j` on the same vertex set satisfies

- `alpha(C_j)<=r`;
- `omega(C_j)<=k`.

The exact Brouwer/Kang-Pikhurko second-Turán layer gives

`e(C_j)>=p_r(kr+1)+(k-1)`.

Therefore

> **`e(F)<=U_(k,r)`**, where
>
> `U_(k,r)=[k r^2+(k^2-4k+2)r+4k-2]/2`.

This contextual cap is stronger than the old one-color hereditary cap because it remembers that all colors coexist on the same residual.

## 2. The contextual 4r+1 branch is dead

For `k=4`,

`U_(4,r)=2r^2+r+7`.

If a contextual `4r+1` residual has

`delta(F)>=r+1`,

then

`e(F)>=(4r+1)(r+1)/2`,

which exceeds `U_(4,r)` by `(3r-13)/2`.

Hence:

> **For every `r>=5`, the contextual `4r+1` branch is impossible once the minimum-degree contract is available.**

At `r=12`, the existing front-end theorem already proves every genuine contextual `R(4,49)` residual has `delta>=13`; therefore the contextual `R(4,49)` branch is empty outright.

## 3. Why 5r+1 is the first genuine terminal

For `k=5`,

`U_(5,r)=(5r^2+7r+18)/2`.

If `delta(F)>=r+2`, the minimum-degree lower bound exceeds this cap for every `r>=5`.

Thus any surviving contextual `5r+1` terminal with the natural lower minimum-degree source is forced into exactly

> **`delta(F) in {r,r+1}`.**

This explains the r=12 T61 `h=12/13` split as a general full-color stability phenomenon.

## 4. Direct anchor extraction in every 5r+1 terminal for r>=67

`GENERAL_R_5R1_ALL_LARGE_R_ANCHOR_EXTRACTION.md` proves:

> **For every `r>=67`, every contextual `5r+1` terminal contains a direct near-anchor independent triple.**

More precisely:

- if `delta(F)=r`, there is an independent triple `(r,<=r+1,<=r+1)`;
- if `delta(F)=r+1`, there is an independent triple `(r+1,<=r+2,<=r+2)`.

The difficult `delta=r` branch is reduced to a constant-defect anti-neighbourhood system. Deleting vertices with extra defect at least3 removes at most5 points. Liu–Ren–Wang's degree-sensitive AES theorem, together with an actual lower bound on `Delta` coming from a degree-r low vertex, forces the complement to be 4-partite for `r>=67`. The endpoint cases `t=4,5` are then killed by clique-capacity and greedy K4-transversal arguments.

Using only the classical Andrásfai–Erdős–Sós theorem gives the independent fallback threshold `r>=71`.

## 5. Near-anchor common anti-neighbourhood is constant-width

Let T be the extracted independent triple and W its common target anti-neighbourhood.

Because `alpha(F)<=5`,

`alpha(F[W])<=2`.

For every non-target color,

`alpha(C_j[W])<=r`.

Hence

`p_2(|W|)+(r-1)p_r(|W|)<=C(|W|,2)`.

This forces `|W|<=2r+1` for `r>=6`.

The two top layers are then eliminated:

- `|W|=2r+1` is impossible for `r>=4` by the sharp non-bipartite triangle-free edge bound;
- `|W|=2r` is impossible for `r>=11`: the slack ledger forces at least `r-2` non-target perfect matchings, hence the complement has minimum degree at least `r-2`, and triangle-free AES forces bipartiteness, contradicting the target clique cap.

Therefore:

- low terminal layer:

  > **`2r-4 <= |W| <=2r-1`;**

- high terminal layer:

  > **`2r-7 <= |W| <=2r-1`.**

So the remaining downstream geometry has only finitely many size offsets, independent of r.

## 6. Exact top surviving layer |W|=2r-1

At `|W|=2r-1`, total pair-count slack is exactly `r-1`.

The sharp non-bipartite triangle-free theorem forces the target excess to be at least `r-2`, leaving exactly two integer cells.

### Cell A

- target excess `r-1`;
- all non-target colors are exact near-perfect matchings.

### Cell B

- target excess `r-2`;
- total non-target excess1;
- the complement of the target on W attains equality in the non-bipartite triangle-free extremal theorem.

Hence

> **`bar(F[W]) = S(K_(r-1,r-1))`,**
>
> a single-edge subdivision of the complete bipartite graph.

Moreover Cell B has a canonical genuine coloring obtained from a 1-factorization of `K_(r-1,r-1)` by subdividing one factor edge and assigning both subdivision edges the same factor color.

Thus Cell B is a real local design extremizer, not a numerical artefact.

## 7. Latin / rainbow extension reduction

For an ordinary non-target factor color j in Cell B,

`C_j[W]=M_j + isolated w`.

For an outside color-j-independent set S, the exact extension condition is

`1_(w in N_j(S)) + # {factor edges e subseteq N_j(S)} >= |S|`.

Consequences:

- a single outside vertex must either use its w-edge as a one-edge certificate or cover both endpoints of a factor edge;
- across different colors, the chosen factor edges for one outside vertex are pairwise vertex-disjoint;
- hence the minimum extension pattern is a large rainbow matching / Latin partial transversal;
- for three anchors, in almost every factor the three selected certificates must be distinct.

Therefore the sharp Cell B nonextension problem is a three-fold near-complete Latin partial-transversal extension problem, not arbitrary graph casework.

## 8. Pointwise cross bound in Cell B

For every outside vertex o in Cell B, the certificate constraints force at least `2r-4` of its `2r-1` edges into W to be non-target.

Hence

> **`d_F(o,W)<=3` for every outside vertex o.**

This is an exact pointwise target-cross bound.

## 9. High Cell B has only 22 defect units

In the high terminal layer `delta(F)=r+1`, let A,B be the two `(r-1)` target cliques inside W and w the subdivision vertex.

Inside W:

- every A/B vertex has target degree `r-1`;
- w has target degree `2r-4`.

Write

`d_F(s,O)=2+a_s` for side vertices,

`x_w=d_F(w,O)`,

and

`kappa_o=d_F(o)-(r+1)` for outside vertices.

The contextual edge cap gives total excess above `r+1` at most `r+17`, while w already contributes unavoidable excess `r-5` internally.

Therefore

> **`x_w + sum_s a_s + sum_o kappa_o <=22`.**

Thus the high Cell B extension is a **22-defect problem independent of r**.

In particular:

- `x_w<=22`;
- total side over-incidence is at most22;
- all but at most22 outside vertices have exact target degree `r+1`;
- every outside vertex has at most3 target neighbours in W.

This is the strongest current downstream normal form.

## 10. New all-large-r logical DAG

The preferred architecture is now

`hypothetical counterexample`

`-> contextual extraction theorem`

`-> 4r+1 or 5r+1`

`-> 4r+1 dies immediately`

`-> 5r+1 has delta in {r,r+1}`

`-> r>=67 gives direct near-anchor triple`

`-> common anti-neighbourhood has constant size offset`

`-> top cell is explicit subdivided-factorization design`

`-> high cell has only22 extension defects`

`-> uniform nonextension theorem`

`-> contradiction`.

The old d2/d3 backend machinery remains valuable for fixed-r and finite-tail certification but is no longer the most direct all-large-r route.

## 11. Load-bearing missing theorems

Only two major all-large-r ingredients remain:

1. **upstream contextual extraction:** force every hypothetical counterexample into the `4r+1 / 5r+1` dichotomy;
2. **downstream design nonextension:** exclude the bounded-offset near-anchor survivors, in particular the Cell B subdivided-factorization extension.

For `r>=67`, the terminal anchor extraction itself is no longer open.

## 12. r=12 implication

For the fixed r=12 project, contextual `R(4,49)` is already impossible, so the front-end recurrence may treat no-49-extraction as a theorem. The only original front obstruction is T61.

The surviving T61 branch has `delta=13`, i.e. precisely the high terminal layer. Therefore if its near-anchor common anti-neighbourhood enters Cell B, it inherits the same 22-defect extension ledger.

This does not yet certify the full r=12 proof, but it gives a new cross-check and a much more structured route for the remaining high T61 states.