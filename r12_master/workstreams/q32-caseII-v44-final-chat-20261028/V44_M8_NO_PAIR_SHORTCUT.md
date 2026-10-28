# V44 m=8 alternate closure via the 130-edge no-pair theorem

Date: 2026-10-28
Status: PROVED_CONDITIONAL; alternate to the longer U-pool saturation proof.

Assume the registered Q32 contract with `|U|=44`, `m=8`, and `|W|=3`.

The already-proved normal form and Sections 1.1–1.2 of `V44_M8_CLOSURE.md` establish that, for every `w in W`, the set

`L(w)={D among the three 130-edge nonexact colors: d_D(w)=4 and all D-neighbors of w lie in H}`

has size at least two.

For any distinct `u,v in W`, the two subsets `L(u),L(v)` of the same three-color set must intersect. Choose `D in L(u) intersect L(v)`. Then D has two distinct core-only degree-four vertices, contradicting `Q32_130_NO_TWO_CORE_ONLY_DEG4.md`.

Therefore `|U|=44,m=8` is impossible directly. This shortcut does not need the `(2,2,2)/(3,2,2)/(3,3,2)` split, the 700-edge U-pool saturation, or the final Turan-equality contradiction. The existing longer proof remains as an independent cross-check.

Dependencies: corrected non-full-support multiplicity; source-correct zero-shell special-edge obstruction; the 130-edge minimum-degree-four theorem; the pointwise `|L(w)|>=2` normal form; Kang–Pikhurko Theorems 1 and 4 at `(56,11)`. No exceptional-vertex injectivity or universal degree-nine claim is used.
