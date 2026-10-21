# Canonical state — 2026-10-21

## The theorem is not certified

Target: prove the `r=12` case of Erdős Problem 617. Current status: **NOT_CERTIFIED**.

## Backend

For a legitimate residual `F in R(4,49)`, current clean machinery uses a degree-13 pivot `p` with shell `A` of size13 and 35-core `H`:

`e(F)=91+q+e(H)`.

Clean core floor:

`H in R(3,35) => e(H)>=211`.

Reusable repivot assets:

- `q=28`: analytic profitable-repivot mechanism;
- `q=29` plus inherited `delta(H)>=12`: a degree-13 repivot `y` exists with `q_y>=30`; this does **not** require `e(H)=211`.

For E331, CORE211 is applied separately after the repivot to force `q_y<=29`, producing the contradiction.

Current backend lower frontier is `E332`:

- `E329`, `E330`, `E331` are closed in the reconstructed DAG, with the uniform-q27 theorem as a dependency;
- any genuine `E332` survivor admits `(q,e(H))=(30,211)`;
- for `e(H)=211`, the core degree multiset is `14,12^34` or `13^2,12^33`.

Active Line C object:

`E332 : q30 shell + almost-12-regular 211-edge 35-core`.

Higher layers `E333...E340` remain open as Line B.

## Front-end — major 2026-10-21 reduction

The obsolete target `e(F)=325` has been retired. The modern bridge target is simply

`hypothetical K145 counterexample -> legitimate induced F in R(4,49)`.

The new Line A theorem is:

`least-edge colour G -> legitimate induced R(4,49) OR embedded T61 obstruction`.

This dichotomy is **PROVED** and does not use a generic R449 edge lower bound or the backend E332+ theory.

The contextual recurrence is **COMPUTATION_CERTIFIED**:

- 1752 recurrence nodes checked;
- 144 outer stopping comparisons checked;
- two independent integer implementations agree;
- unique nonexcluded outer stop `(d,j,a,n)=(11,6,5,61)`.

The embedded T61 obstruction has:

- minimum-degree anchor `d=11` in the original least-edge colour;
- exactly six genuine K12 blocks in the anchor nonneighbourhood packing;
- a 61-vertex residual `R` with `alpha(R)<=5`, `omega(R)<=11`, inherited caps;
- `397<=e(R)<=408`;
- `delta(R) in {12,13}`;
- exact outer ledger `E+sigma+z+g+x_6+y_6=408`.

Thus the entire front-end is now reduced to one sharply specified task:

`exclude embedded T61 OR extract a legitimate induced R(4,49) from it`.

Important non-implications that remain visible:

- the anchor contributes algebraic 66 but is a genuine seventh K12 only if `z=0`; `z=0` is OPEN;
- T61 is not automatically the `E406, delta13` parent of S31;
- S31 `q<=30` does not itself create another K12;
- T61 is not automatically in the canonical S30 macro contract.

## S30 state

For the specified row-labelled `(5,7,8,8)` branch:

- singleton-triangle case `uv,uw,vw` is analytically closed;
- a new saturation lemma removes eight scalar cases for each of k0 and k1;
- for k1,a0, `tv` is forced and b=3 is eliminated;
- exact remaining necessary scalar cases: 14 for k0 and 13 for k1.

These are scalar necessary cases, not graph survivors or a complete incidence classification.

## Three-line split

- Line A / Astra A: exclude or extract from embedded T61.
- Line B / Astra B: high backend `E333...E340`.
- Line C: eliminate `E332:q30+211`.

## Certification warning

The full EG617 `r=12` theorem remains OPEN. It can be certified only when the T61 bridge and all legitimate `R(4,49)` backend layers are closed.
