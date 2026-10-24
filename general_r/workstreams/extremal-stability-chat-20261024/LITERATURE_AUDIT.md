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


## F-002 — growing-parameter stability inputs

### Füredi partition lemma

Source: J. Balogh, F. C. Clemen, M. Lavrov, B. Lidický and F. Pfender, “Making \(K_{r+1}\)-free graphs \(r\)-partite,” *Combinatorics, Probability and Computing* 30 (2021), 609–618, DOI [10.1017/S0963548320000590](https://doi.org/10.1017/S0963548320000590).

The paper states Füredi's lemma: if \(H\) is an \(n\)-vertex \(K_{q+1}\)-free graph with \(e(H)\ge T_q(n)-t\), then there is a partition \(V(H)=V_1\cup\cdots\cup V_q\) with
\[
\sum_a e(H[V_a])\le t,\qquad
\sum_{a<b} e^c(V_a,V_b)\le 2t.
\]
This is the exact form used in F-002. The constants 1 and 2 are retained; no fixed-\(q\) asymptotic stability theorem is substituted.

### Brouwer non-partite Turán bound

For \(m\ge2q+1\), a \(K_{q+1}\)-free graph that is not \(q\)-partite satisfies
\[
e(H)\le T_q(m)-\lfloor m/q\rfloor+1.
\]
A checked restatement and the relevant attribution are recorded in the public verification note [Brouwer–Kang–Pikhurko audit](https://github.com/nwinter/erdos-617-r5/blob/main/papers/brouwer-kang-pikhurko.md). The F-002 uses apply it with \(q=r-1\) and \(m=r^2-d\), \(0\le d<r\), so the size hypothesis holds for \(r\ge4\).

### Kang–Pikhurko equality classification

M. Kang and O. Pikhurko, “Maximum \(K_{r+1}\)-free graphs which are not \(r\)-partite,” *Matematychni Studii* 24 (2005), 12–20, DOI [10.30970/ms.24.1.12-20](https://doi.org/10.30970/ms.24.1.12-20).

For \(m\ge2q+1\), the extremal non-\(q\)-partite \(K_{q+1}\)-free graphs attaining Brouwer's bound have the explicit construction described in that paper: deleting one vertex leaves a complete \(q\)-partite graph on \(m-1\) vertices. In the F-002 boundary case \(q=r-1\), \(m=r^2-2\), the remaining \(m-1=r^2-3\) vertices cannot fit into \(r-1\) independent parts of size at most \(r\) when \(r\ge4\). Thus equality in Brouwer's bound is excluded by \(\alpha(H_i[B_i])\le r\), yielding the one-edge improvement used in the \(d_i=2\) argument.

These are explicit external graph-theoretic dependencies; the workstream does not claim to reprove them.
