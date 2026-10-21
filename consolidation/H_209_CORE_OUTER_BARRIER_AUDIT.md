# H-version audit: 209-core floor and r=12 outer barrier

## Status

`SOURCE_RECOVERED / PARTIALLY_AUDITED / NON-CANONICAL_FOR_CORE211`

This note records what H contributes to the current research state without importing historical status labels wholesale.

## 1. Audited historical 35-core floor

H derives, in its r=12 cap-three setting,

`B_12(3,35) >= 209`.

The key historical split is:
- if the 35-point core has minimum degree at least 12, H treats 210 as automatic in that older framework;
- the difficult `delta=11` row is handled by a degree-11 pivot, a 23-point cap-two extremal lower bound `e(K)>=131`, and an equality-cover contradiction excluding the `E=208` endpoint;
- hence the historical safe floor becomes 209.

H explicitly downgrades an earlier `213` claim and isolates `E=209` as the first unresolved equality-core layer.

This is **not** the modern CORE211 theorem. It is a weaker historical floor with a different proof architecture and different inherited dependencies.

## 2. 209-edge equality-core program

Later H sections use the 209 floor inside `e(F)=325` shell decompositions. In alpha-excess-2 shell cases the edge identity forces

`e(core)=209`,

so every such pivot sees a 209-edge extremal member of `F_12(3,35)`. H then starts a compatibility program for overlapping 209-edge cores.

This is useful historical structure, but it does not replace the modern `q=30 + 211-core` equality system.

## 3. r=12 terminal outer barrier

H independently recomputes the old outer recurrence and finds the crucial terminal obstruction:

- terminal row `(d,j)=(11,7)` has outer edge budget 342;
- the hereditary 49-vertex density ceiling is 340;
- strict recurrence closure would require 343.

Therefore a nonempty 49-vertex residual cannot repair the outer recursion by any same-residual scalar edge lower bound. The repair must instead be one of:

1. prove the 49-vertex residual class empty;
2. prove a structural/block exclusion that changes the residual object;
3. alter the outer packing/charging architecture before the terminal cell.

H then generalizes the scalar comparison and shows the same obstruction across the terminal degree rows `d=4,...,11`.

This explains why the historical recurrence architecture failed and is consistent with the modern decision to build a direct front-end reduction to a legal 49-point residual/T61 obstruction instead of relying on a contextual lower-floor rescue.

## 4. Impact on the current project

### Direct canonical upgrade
None. H does not supersede the current CORE211 proof or current T61 reduction.

### Useful recovered facts
- historical safe floor 209 and its equality-core boundary;
- rigorous diagnosis that scalar outer edge-floor strengthening cannot close the r=12 terminal;
- several weighted quotient / endpoint-capacity / codegree rigidity motifs worth mining if modern branches resemble those historical configurations.

### Remaining consolidation gap
The modern repository still needs a standalone clean proof of CORE211. H narrows provenance history but does not fill that gap.
