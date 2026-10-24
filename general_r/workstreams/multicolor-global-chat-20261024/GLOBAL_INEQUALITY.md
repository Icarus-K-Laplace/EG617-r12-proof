# Multicolor Global Inequality

Status: **I1 ACHIEVED — proved genuine multicolor non-rainbow/variance inequality**.

Let `n=r^2+1`, `r>3`, and suppose an r-edge-coloring of `K_n` is a counterexample to Problem 617: every `(r+1)`-set sees every color. Write `G_i` for color i and `d_i(v)` for its degree at v.

The proof below genuinely uses the simultaneous color partition; it is not a theorem about a single color graph.

## 1. Local avoidance sets

For each vertex v and color i define

`W_i(v)=V\({v} union N_i(v))`.

Then

`|W_i(v)|=r^2-d_i(v)`.

### Lemma 1

`alpha(G_i[W_i(v)])<=r-1`.

Proof. If `W_i(v)` contained r vertices independent in color i, those r vertices together with v would form an `(r+1)`-set with no color-i edge, contradicting the counterexample property. QED.

Hence

`e_i(W_i(v)) >= p_(r-1)(r^2-d_i(v))`,

where `p_a(m)` is the balanced a-clique Turan-complement floor.

## 2. Exact non-rainbow counting identity

For fixed v define

`Q(v)=C(r^2,2)-sum_i e_i(W_i(v))`.

A pair `{x,y}` in `V\{v}` fails to be counted in the sum exactly when the color of xy equals the color of vx or vy.

Classify triangles by their edge-color pattern:

- `T_R`: three distinct colors (rainbow);
- `T_2`: exactly two colors, one repeated twice;
- `T_3`: monochromatic.

A rainbow triangle contributes 0 to `sum_v Q(v)`, a two-color triangle contributes 2, and a monochromatic triangle contributes 3. Therefore

> **Exact identity**
>
> `sum_v Q(v)=2 T_2+3 T_3`.

This identity is intrinsically multicolor.

## 3. Convex lower bound on the simultaneously avoided edges

At every vertex,

`sum_i d_i(v)=r^2`,

because the r color neighborhoods partition the other `r^2` vertices. Therefore

`sum_i |W_i(v)|=r^2(r-1)`,

so the average `|W_i(v)|` is `r(r-1)`.

The function `p_(r-1)(m)` is discrete convex. Hence

`sum_i p_(r-1)(r^2-d_i(v))`
`>= r p_(r-1)(r(r-1))`
`= r^2 (r-1)^2/2`.

Define the nonnegative convexity penalty

`P(v)=sum_i p_(r-1)(r^2-d_i(v)) - r^2(r-1)^2/2 >=0`,

and `P=sum_v P(v)`.

Since `C(r^2,2)-r^2(r-1)^2/2=r^2(r-1)`, Lemma 1 gives

> **Theorem A — non-rainbow budget**
>
> `2T_2+3T_3 <= n r^2(r-1)-P`.

Consequently the number of non-rainbow triangles satisfies

`T_2+T_3 <= [n r^2(r-1)-P]/2`,

and therefore

> **Rainbow supersaturation**
>
> `T_R >= C(n,3)-[n r^2(r-1)-P]/2`.

In particular, asymptotically all but `O(1/r)` of all vertex-triples must be rainbow in any hypothetical counterexample.

## 4. Degree-variance consequence

Let

`V=sum_(v,i) (d_i(v)-r)^2`.

The number W of same-color wedges is

`W=sum_(v,i) C(d_i(v),2)`.

Trianglewise,

`W=T_2+3T_3`:

a two-color triangle contains exactly one same-color wedge, a monochromatic triangle contains three, and a rainbow triangle contains none.

Because `W<=2T_2+3T_3`, Theorem A gives

`W<=n r^2(r-1)-P`.

Using `sum_i d_i(v)=r^2`,

`W=n r^2(r-1)/2 + V/2`.

Therefore

> **Theorem B — simultaneous color-degree variance bound**
>
> `V+2P <= n r^2(r-1)`.

This is a global near-regularity constraint that is unavailable from any one color in isolation.

## 5. Explicit penalty in terms of variance

For `a=r-1`, the balanced-clique floor satisfies

`p_a(m) >= m^2/(2a)-m/2`.

Equality holds at the balanced point `m=r(r-1)`. Since the `|W_i(v)|` have fixed sum,

`P(v) >= [sum_i (d_i(v)-r)^2]/[2(r-1)]`.

Thus

`P >= V/[2(r-1)]`.

Substituting into Theorem B yields the explicit corollary

> `V <= n r (r-1)^2`.

Equivalently the RMS deviation of the `nr` color-degrees from r is at most `r-1`.

The explicit constant is not yet strong enough for a contradiction, but it is a genuine multicolor moment inequality and a quantitative starting point for stability.

## 6. What this does and does not prove

Achieved:

- a nontrivial global inequality using all colors simultaneously;
- an `O(r^5)` upper budget on repeated-color triangle incidences versus `Theta(r^6)` total triangles;
- a global color-degree variance bound with a convexity penalty.

Not yet achieved:

- I2: forcing one color into a sharply smaller/slacker structural class beyond the known averaging statement;
- I3: sufficiently-large-r contradiction;
- I4: all-r proof.

The next leverage point is to combine the near-total rainbow requirement with the near-Turan clique-partition structure of the color graphs. Those two demands should impose incompatible pair/intersection matrices if the stability errors are small enough.
