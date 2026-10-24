# Failed Generalizations

## FG-001 — “the sharp affine construction is essentially unique at edge level”

Status: **FALSE**.

The unused affine parallel class may be colored edge-by-edge arbitrarily without destroying balance, provided every color keeps one complete base parallel class.

## FG-002 — “a sharp affine coloring necessarily contains two pure color classes”

Status: **FALSE** for the full sharp family.

Every color may receive extra edges from the leftover parallel class. Arguments requiring a color graph to equal exactly a disjoint union of `r` cliques are therefore too rigid unless purity is separately derived.

## FG-003 — “O(r) or o(r^2) edge-edit stability to one standard affine coloring”

Status: **FALSE**.

The CE-F-001 family can be `Theta(r^3)` recolorings away.

## FG-004 — “K is an independent refinement of q in the repivot potential”

Status: **FALSE**.

At fixed residual graph, `Delta K=-2 Delta q`; the coordinates carry the same information with opposite orientation.

## FG-005 — “Chat A already proved delta(H)>=r”

Status: **FALSE AS STATUS REPORT**.

The audited branch proves only `delta(H)>=r-1` and compresses the remaining degree-`r-1` case. Do not silently strengthen it.

## Surviving corrected targets

The following are not refuted by this round:

- stability to an orthogonal-partition / net skeleton rather than an exact coloring;
- the full three-anchor theorem for `12<=r<=67`;
- a refined termination theorem eliminating all equal-potential d2 plateaus;
- the final `delta(H)>=r` boundary elimination using extra residual-shell information.
