# Asymptotic Inequality Ledger

All backend formulas are under an extracted legal `4r+1` residual unless explicitly stated otherwise.

Write

- `E=e(F)`;
- `D=D_r(4r+1)=2r^2+4r+4`;
- `epsilon=D-E>=0`;
- `K=2e(H)-r(3r-1)`;
- `q=e(M)+G_A`.

## 1. Exact master conservation law

From `E=C(r+2,2)+q+e(H)`:

> **`K=6r+6-2epsilon-2q`.**

Equivalently:

> **`q+epsilon=3r+3-K/2`.**

Also `r(3r-1)` is even, so K is always even.

Consequences:

- `K>=7` iff `K>=8`;
- baseline `K>=2` gives `q<=3r+2-epsilon`;
- `K>=8` gives `q<=3r-1-epsilon`.

## 2. Main ledger

| quantity | lower | upper | scalable gap / threshold | dependency |
|---|---:|---:|---|---|
| residual order | `4r+1` | `4r+1` | exact | A_ext extraction |
| residual degree minimum | `r+1` | — | automatic for `r>=17` | extracted residual + hereditary cap |
| residual edges `E` | — | `2r^2+4r+4` | deficit `epsilon` | hereditary cap |
| core order | `3r-1` | `3r-1` | exact | residual theorem |
| core minimum degree | `r` | — | automatic for `r>=17` | extracted residual theorem |
| core excess `K` | `2` baseline; `8` for r>=68 | `2r-2` | linear window | core floor/cap + anchor |
| charge `q` | `0` | `3r+2-epsilon`; with K>=8 `3r-1-epsilon` | slope 3 | master law |
| regular support degree `d` | `0` | `r` | base `d(r+1-d)` | repivot identity |
| medium support base | `4r-12` | q ceiling | slope 4 vs 3 | endpoint collapse |
| common-S owner multiplicity `N` | `0` | hereditary `r-O(1)`; fixed-deficit multicolour `r/2+O_epsilon(1)` | slope halved | multicolour stability |
| zero signatures | `0` | `3` | O(1) | `alpha(H)<=3` |
| zero vertices | `0` | `3r-1` | no global O(1) bound | OPEN |
| d2 one-loss charge `W` | three-class `3r-2` | exact `K+2r-2+a+b` | `K+a+b>=r` | d2 barrier |
| high support complement | — | `<=2` target shell neighbours per high owner | O(1) | endpoint collapse |
| high owners | `0` | `3` | absolute O(1) | sibling repivot |
| high shell kernel | `0` | `9` | absolute O(1) | sibling repivot |
| high core signatures | `1` | `8` | absolute O(1) | sibling repivot |
| decorated shell count `tau` | `[r-3-2epsilon-epsilon sqrt(4epsilon+1)]/2` | `r+1` | slope `1/2` for fixed epsilon | low regular clique cap + high owners<=3 |
| recurrence/extraction depth | `0` | unknown | upstream only | A_ext OPEN |
| exact terminal type count | — | not yet O(1) globally | d2 and d0/d1 remain scalable | C* OPEN |

## 3. Automatic residual contract threshold

A sibling theorem proves that if an induced `4r+1` residual with `alpha<=4`, `omega<=r-1` and the inherited cap exists, then for every `r>=17`:

- `delta(F)=r+1`;
- a legal exact pivot exists;
- `delta(H)>=r`.

The threshold comes from the `3r` exclusion using Andrasfai-Erdos-Sos:

`2r-2 > 5(3r)/8`,

which holds for `r>16`.

Thus the asymptotic front does not need a separate minimum-degree hypothesis.

## 4. Universal medium-degree slope theorem

Suppose `K>=kappa`. Then

`q<=3r+3-epsilon-kappa/2`.

For `4<=d<=r-3`:

`d(r+1-d)>=4(r-3)=4r-12`.

Hence the whole medium interval is impossible whenever

> **`r>15-epsilon-kappa/2`.**

Worst case epsilon=0:

| kappa | first r excluding all medium d |
|---:|---:|
| 2 | 15 |
| 4 | 14 |
| 6 | 13 |
| 8 | 12 |

More generally, `K>=-lambda r-O(1)` with fixed `lambda<2` still gives asymptotic medium-degree collapse.

## 5. Multicolour slope-half obstruction

At deficit epsilon, every regular target clique B satisfies

`2|B| <= r-1+2epsilon+epsilon sqrt(4epsilon+1)`.

For a common-S owner family:

> **`N <= [r-3+2epsilon+epsilon sqrt(4epsilon+1)]/2`.**

For fixed epsilon, owner capacity has slope 1/2.

For d3, the independent fixed-deficit contradiction threshold is

> **`r>11+epsilon sqrt(4epsilon+1)`.**

The sibling repivot workstream gives a stronger all-deficit common-S d3 closure under the residual/anchor setup.

## 6. Decoration-heavy terminal inequality

Low-endpoint regular shell vertices form a regular target clique, so their number is at most

`[r-1+2epsilon+epsilon sqrt(4epsilon+1)]/2`.

The stronger endpoint theorem gives at most three high regular owners. Therefore

> **`tau >= [r-3-2epsilon-epsilon sqrt(4epsilon+1)]/2`.**

For fixed epsilon:

> **`tau>=r/2-O_epsilon(1)`.**

Exact repivot transport is

`tau_y-tau_p=|D_y intersect X|-|S_y intersect X|`.

Hence a fixed-deficit terminal with no tau-improving repivot must support a linear-size balanced decoration incidence system. This is a candidate route to a design-like rigidity theorem.

## 7. d2 synthesis target

For an exact one-loss three-class d2 terminal:

> **`K+a+b>=r`**, `b in {0,1}`.

Thus survival requires linear core excess or allowance. Any theorem

> **`K+a <= (1-c)r+O(1)`**

for fixed c>0 kills the three-class d2 terminal for all sufficiently large r.

Alternative: prove owner demand above `(1/2+c)r-O(1)` and contradict the multicolour owner capacity.

## 8. Full-colour slack

For `n=r^2+1`, if `s_i=e(G_i)-p_r(n)>=0`, then exactly

> **`sum_i s_i=r^2(r-1)/2`.**

Average slack is `C(r,2)`. Ordinary single-colour stability therefore leaves `Theta(r^2)` edits per colour; the front/design route needs a genuinely multicolour compatibility gain.


## 8. Exact d2 scalar-boundary audit: the proposed linear margin is not derivable

The current exact one-loss d2 identities are
\[
W=K+2r-2+a+b,\qquad W\ge3r-2,
\]
hence (K+a+b\ge r), with (b\in\{0,1\}). The inherited scalar bounds also include
\[
K\le2r-2,\quad q+\epsilon=3r+3-K/2,
\]
and, in the d2 view,
\[
q=2r-2+a+B,\qquad
K\le2r+10-2a-2B.
\]

For every even (r\ge68), the following integer parameter family satisfies all of those recorded scalar constraints:
\[
\epsilon=0,\quad a=2,\quad b=0,\quad
K=r-2,\quad B=r/2+4,\quad q=5r/2+4.
\]
Checks:
- (q=2r-2+a+B=5r/2+4);
- (q+\epsilon=3r+3-K/2=5r/2+4);
- (W=K+2r-2+a+b=3r-2), exactly the required lower bound;
- (2r+10-2a-2B=r-2=K), equality in the recorded K upper bound;
- (8\le K\le2r-2) and (q\le3r-1) for (r\ge10);
- (K+a=r).

Therefore no fixed (c>0) and fixed (C) can make
\[
K+a\le(1-c)r+C
\]
a consequence of the current scalar ledger: the displayed family violates it for all sufficiently large even (r).

**Boundary of this audit:** this is a parameter-level near-counterfamily, not a constructed legal graph or a disproof of a stronger graph-theoretic theorem. A valid proof of the desired margin must use a structural condition not included in the scalar identities.

## 9. Owner-demand/capacity fallback

Define (N) as the number of owners in one common-S family in a legal residual. The proved multicolour capacity is
\[
N_{\mathrm{capacity}}(r,\epsilon)
\le\left\lfloor
\frac{r-3+2\epsilon+\epsilon\sqrt{4\epsilon+1}}2
\right\rfloor,
\]
so (N_{\mathrm{capacity}}=r/2+O_\epsilon(1)) for fixed residual deficit (epsilon).

The missing input is an owner-demand theorem forcing some common-S family to have
\[
N_{\mathrm{required}}>(1/2+c)r-O_\epsilon(1)
\]
for a fixed (c>0), or a comparable strict gap. No such demand theorem is currently proved. The older hereditary sunflower bounds (N\le r-3+o(1)) for d2 and (N\le r-4+o(1)) for d3 have slope one and do not contradict a linear demand. Thus this fallback remains OPEN rather than a completed alternative.

For the a=2 clean-pair block family, the block count (m) is a different quantity from common-S owner multiplicity (N); no identification between them is assumed. The current clean-pair capacity interval (4r/3+3\le m\le\lfloor3(r-1)/2\rfloor) is nonempty.

## 10. Common weighted transversal-cover theorem

**Lemma (TCC).** Let (G) be a graph and (B_1,\ldots,B_s) pairwise disjoint nonempty vertex sets. If every transversal (x_i\in B_i) contains at least one edge of (G), then
\[
1\le\sum_{1\le i<j\le s}
\frac{e_G(B_i,B_j)}{|B_i||B_j|}.
\]
Proof: choose each (x_i) independently and uniformly. The number of selected cross-edges is at least one for every outcome; its expectation is the right-hand side.

**Defect-pair variant.** If (uv\notin E(G)), (alpha(G)\le s+1), and (B_1,\ldots,B_s) are disjoint from ({u,v}), then every set ({u,v,x_1,\ldots,x_s}) contains an edge, so
\[
1\le\sum_{i=1}^s
\frac{d_G(u,B_i)+d_G(v,B_i)}{|B_i|}
+
\sum_{i<j}\frac{e_G(B_i,B_j)}{|B_i||B_j|}.
\]

### Exact C/D mappings

- **Clean pair exchange (C):** take four clean blocks (P_i) of size two. Since (alpha(H)\le3), every one-endpoint transversal has an edge. TCC gives at least four cross-edges on each four-block subsystem. The exact 2-SAT audit strengthens this to **six** cross-edges. Double-counting gives (E_{\mathrm{cross}}\ge\binom m2). This remains compatible with the known linear capacity interval and does not close clean-pair nonextension.
- **TD(5,r) terminal (D):** for a target-missing pair (uv) inside one target group, take one point from each of the other four groups. Since (alpha(G_0)\le5), the defect-pair TCC applies. With group sizes at least (L) and total target cross-edge budget (A), it gives
  \[
  d_{\mathrm{cross}}(u)+d_{\mathrm{cross}}(v)\ge L-A/L.
  \]
  This is the existing cylinder lower bound and bounded-hub concentration theorem. It does not by itself prove global defect-chain cost; that remains OPEN.
- **Residual-core pivot (C common-S):** the support-transition identity (d_i(y_j)=2-|D_i\cap D_j|), owner-capacity theorem, and exact repivot transport are separate valid inputs. No theorem currently identifies the full core support system with the TD(5,r) blocks, so no such identification is made.

The C/D transversal-cover interface is now precise and reusable, but the global terminal contradiction remains OPEN.
