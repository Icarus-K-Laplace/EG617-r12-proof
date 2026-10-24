# Literature Audit — CHAT F

## Erdős--Gyárfás 1999

Primary source: P. Erdős and A. Gyárfás, *Split and balanced colorings of complete graphs*, Discrete Mathematics 200 (1999), 79--86.

Verified from the author-hosted PDF:

- Conjecture 1 is exactly the `K_{r^2+1}` statement.
- They prove the general lower bound `r^2+1 <= g_r(2)` by Turan counting.
- They explicitly state that affine planes of order `r` give balanced colorings on `K_{r^2}` for infinitely many `r`: `r-1` colors from parallel classes and the last color from the union of two classes.
- Their separate upper construction for `g_r(2)<=r^2+r+1` uses a projective plane of order `r+1`; this is a different construction and should not be confused with the `K_{r^2}` sharpness example.

## Modern structural note

A 2026 reproducible note by OutBlade records the edge-disjoint fractional clique-cover product bound

`n <= chi_bar_f(C_i) chi_bar_f(C_j)`

and interprets `r^2` as an MDS/net barrier. This is useful evidence, but the present workstream does not treat that note as a peer-reviewed source.

## Nets / MOLS completion

Classical finite-geometry literature states that a set of `n-2` mutually orthogonal Latin squares of order `n` extends uniquely to a complete set of `n-1` MOLS; equivalently a net of order `n` and degree `n` has a unique affine-plane completion. This is the deficiency-one completion fact used in `EXTREMAL_EXAMPLES.md` and Corollary F4.3.

Before using it in a final master proof, pin a primary source/theorem statement (Bruck/net completion or an equivalent modern reference) and verify the exact hypotheses for all small orders needed.

## Affine-plane existence facts

Safe statements:

- affine/projective planes exist for every prime-power order;
- order 6 is impossible;
- order 10 is impossible;
- no general theorem says every non-prime-power order is impossible.

Therefore all-r arguments must be phrased in abstract-design terms and must not assume a field model.

## 2026 r=5 result

Hai Xia and Stefan Szeider (arXiv:2610.24484, submitted 17 Oct 2026) prove the `r=5` case using a sparse-color extremal reduction and certified computation. Their result reinforces that the full-coloring problem contains structure beyond naive Turan counting; it does not classify all `K_{25}` sharp colorings.
