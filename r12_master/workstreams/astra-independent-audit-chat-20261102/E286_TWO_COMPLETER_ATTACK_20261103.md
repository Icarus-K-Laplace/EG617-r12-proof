# E286 focused adversarial attack: two completers and shared-center charges

Date: 2026-11-03  
Frozen theorem source: `frozen/eq286/286_EDGE_EQUALITY_CLASSIFICATION.md` at integration commit `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`.  
Audit branch: `workstream/r12-astra-independent-audit-20261102`.

## Verdict

**NO GAP FOUND in the two-completer argument.** A stronger statement follows from the same hypotheses: no two vertices can both complete the same K10. This is an additional analytic observation, not a correction to the frozen proof.

The finite support enumeration and scalar/pointwise checks are independently reproduced by `E286_TWO_COMPLETER_ATTACK.py`; its output is `E286_TWO_COMPLETER_ATTACK_RESULTS.json`.

## 1. Exact common-antineighborhood lemma

Let H have 47 vertices, e(H)=286, minimum degree at least12, independence number at most4, clique number at most11. Write d(x)=12+epsilon(x), so
`sum epsilon = 2e-12*47 = 8`.

For nonadjacent u,v, let c=|N(u) intersect N(v)| and let U be their common antineighborhood, excluding u,v. Then
`|U| = 45 - (d(u)+d(v)-c) = 21+c-epsilon(u)-epsilon(v).`
Any three independent vertices in U together with u,v would be an independent 5-set, so alpha(H[U])<=2.

The frozen 25-point lemma is exact: if W has 25 vertices and alpha(H[W])<=2, then its complement F is triangle-free. F cannot be bipartite, since H[W] would be the union of two cliques, each of order at most11, covering at most22 vertices. For a triangle-free non-bipartite graph on25, take a shortest odd cycle C_(2k+1). It is chordless; each outside vertex has at most k neighbors on C (its C-neighborhood is independent), and the outside graph has at most floor((24-2k)^2/4) edges by Mantel. Hence
`e(F) <= 2k+1 + k(24-2k) + floor((24-2k)^2/4) <= 145`.
Therefore e(H[W])>=300-145=155. But
`2e(H[W]) <= sum_(x in W)d_H(x) <= 25*12+8=308`,
so e(H[W])<=154, contradiction. Thus no such W exists.

## 2. Stronger two-K10-completer exclusion

Suppose u,v both complete a K10 clique Q. They are nonadjacent, since otherwise Q union {u,v} is a K12, contrary to omega(H)<=11. Thus c(u,v)>=10.

- If epsilon(u)+epsilon(v)<=6, then |U|>=21+10-6=25, contradicting the 25-point lemma.
- The only remaining possibilities are epsilon(u)+epsilon(v)=7 or8, since the total excess is8. In either case |U|>=23. If the sum is7, at most one unit of excess remains anywhere outside {u,v}; among at least24 vertices of U there are at least23 zero-excess vertices. If the sum is8, every other vertex has zero excess and U has at least23 vertices. In either case choose W subset U with |W|=23 and epsilon(x)=0 for every x in W.

Now F=complement of H[W] is triangle-free because alpha(H[W])<=2. For each x in W, d_H(x)=12 and d_H[W](x)<=12, so
`d_F(x)=22-d_H[W](x)>=10 > 2*23/5=9.2`.
The triangle-free case r=2 of Andrásfai–Erdős–Sós therefore forces F to be bipartite. Its two independent parts are cliques in H[W], each of order at most11. This would give |W|<=22, contradicting |W|=23.

Consequently **no pair of vertices can both complete the same K10** under the E286 hypotheses. In particular, the frozen weaker estimate epsilon(u)+epsilon(v)>=7 is valid, and can be strengthened to an outright impossibility.

## 3. Why the D-support zero-completer branch is still valid

In D={01,02,03,12,13}, each K10 is incident with one K10/K10 point P and two mixed K10/K11 points. The opposite missing-set sizes for the two mixed points are positive, because a mixed point cannot complete a K11. The opposite missing-set size for P may be zero, but this is the only possible negative increment at a K10.

For a K10 vertex missing a subset S of its three incident support points, the degree lower bound is
`d(x)>=12 + sum_(i in S)(a_i-1)`,
where at most one a_i can be zero and the other two are at least1. Hence
`max(0,sum_(i in S)(a_i-1)) >= sum_(i in S)max(0,a_i-2)`.
For a K11 with its two incident mixed points, the same inequality holds for arbitrary opposite missing sizes a,b>=0:
`max(0,(a-1)+(b-1)) >= max(0,a-2)+max(0,b-2)`.

The script exhausts all allowed integer values and every missing subset: zero counterexamples at K10 and K11. Thus the center charges for two noncompleting mixed points sharing K10/K11 cliques are additive, including the case where P completes the opposite K10. Each noncompleting mixed point contributes at least5 by formula (5), whose exact finite minimum is5 at (a,b)=(2,2). If a K10 has zero mixed completers, both mixed points are noncompleting and contribute at least10; if it has one completer, the other point contributes at least5; if it had two, the stronger exclusion in Section2 rules it out. This closes the D-support counting without assuming a separate completer-existence lemma.

## 4. Double-pair and K9 shared-center equality attacks

The small-budget double-pair lemma uses:
- f_(9,11) minimum2, uniquely at (2,4);
- f_(10,10) minimum2, uniquely at (3,3).

At equality all two units sit on the selected mixed point, leaving both clique centers and the companion at excess0. The companion cannot miss both cliques, hence completes a clique missed by the selected point (it cannot complete a K11). A missing vertex then has degree at least 8+4+1=13 or 9+3+1=13, contradiction.

For the K9 center with two K9-completers, let A,A' be the two missing subsets and b,b'>=1 the opposite K11 missing sizes. A vertex x in A only has degree at least 8+2+b+1=11+b; in A' only, at least 11+b'; in A cap A', at least 8+2+b+b'=10+b+b'. Therefore its excess pays additively for (b-1) and (b'-1) contributions. The independent check covers all b,b' in1..11 with zero counterexamples. The resulting scalar formula (4) has minimum5; the three-star formula (3) has minimum6.

## 5. Independent finite checks

- Support orbits from the incidence constraints: h=3 gives2; h=4 gives3; h=5 gives5; total10, matching the theorem table.
- K10 pointwise inequality: all a0 in0..10, a1,a2 in1..11, and all eight missing subsets; zero failures.
- K11 pointwise inequality: all a,b in0..10 and all four missing subsets; zero failures.
- Scalar minima: f11=6 at(2,2); f10,11=4 at(2,3); f9,11=2 at(2,4); f10,10=2 at(3,3); formula(5)=5 at(2,2); formula(4)=5 at(2,1)..(7,1); formula(3)=6 at(2,1)..(8,1).
- Triangle-free non-bipartite edge bounds from the shortest-odd-cycle/Mantel calculation: n=19 ->82; n=23 ->122; n=24 ->133; n=25 ->145.

## 6. Scope and disposition

This pass found no counterexample in the two-completer, D-support pointwise, double-pair, or K9 shared-center arguments. The stronger no-two-K10-completers lemma uses the triangle-free AES case r=2; the frozen proof does not need this strengthening because its weaker excess bound already suffices.

This does not certify the whole E286 theorem, COVER, T61 extraction, full root build, or Lean formalization. It is a focused audit of the stated subclaims only.
