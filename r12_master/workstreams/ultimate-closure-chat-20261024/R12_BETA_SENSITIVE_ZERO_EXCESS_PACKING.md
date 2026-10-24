# Beta-sensitive exact-129 zero-excess component packing

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** on the retained T61 core contract and exact-129 K5 factor theorem. Necessary structure only.

## 1. Contract

Let H be the 47-vertex core in E407 Q32 or E408 Q33, with
\[
\alpha(H)\le4,\quad \delta(H)\ge12,\quad e(H)=284,\quad
\sum_{x\in H}(d_H(x)-12)=4.
\]
Put
\[
X=\{x\in H:d_H(x)>12\}.
\]
Because every positive excess is an integer, |X|≤4.

Let M[S] be the missing-target graph on the three shell hubs S, and let \(\beta=e(M[S])\). For every exact-129 non-target color C, assume the retained equality factor theorem: C[F] has ten vertex-disjoint isolated K5 components and an 11-vertex exceptional gadget.

Each K5 component meeting S can contain only a clique of M[S] among its S-vertices: any pair in the component is C-colored and therefore is a missing target edge.

## 2. Count the B-labelled no-S components

A K5 component avoiding S is either of the form \(\{b\}\cup Q\), with b in B and Q a four-set in H, or the exceptional form \(\{p\}\cup Q\). The latter can occur at most once, since p is a single vertex and is target-adjacent to all shell vertices. A component avoiding both S and p cannot lie wholly in H because \(\alpha(H)\le4\), and it contains at most one B vertex because B is a target clique.

The number of components that can meet S is controlled by \(\omega(M[S])\):
- \(\beta=0\): \(\omega(M[S])=1\), so at most three components meet S. At least seven avoid S, hence at least six are B-labelled after allowing one pivot component.
- \(\beta=1\) or \(2\): \(\omega(M[S])=2\), so at most two components meet S. At least eight avoid S, hence at least seven are B-labelled.
- \(\beta=3\): \(\omega(M[S])=3\), so at most one component meets S. At least nine avoid S, hence at least eight are B-labelled.

Thus each exact-129 color has at least \(w_\beta\) pairwise-disjoint B-labelled witness sets \(\{b\}\cup Q\), where
\[
w_0=6,\qquad w_1=w_2=7,\qquad w_3=8.
\]
Each Q is an independent four-set in H, and b is target-anticomplete to Q.

## 3. Zero-excess strengthening

At most four core vertices lie in X. The B-labelled Q-sets for a fixed color are disjoint because their K5 components are disjoint. Therefore at most four of the \(w_\beta\) sets can meet X. At least
\[
z_\beta=\max(0,w_\beta-4)
\]
are wholly contained in \(H_0=H-X\), so every vertex of each such Q has core degree exactly 12.

Hence
\[
\boxed{z_0=2,\quad z_1=z_2=3,\quad z_3=4}
\]
zero-excess B-labelled component witnesses per exact-129 color.

Across distinct colors, these four-sets form a linear family: two have intersection at most one, since sharing two core vertices would assign their common edge two colors.

## 4. Global floors

The non-target edge totals on the 61-point residual are
\[
1830-407=1423=11\cdot129+4
\]
for E407, and
\[
1830-408=1422=11\cdot129+3
\]
for E408 Q33. Thus E407 has at least seven exact-129 colors and E408 Q33 at least eight.

For E407 Q32, the template parameter is \(\beta=0\) for A/B, \(\beta=1\) for C/D, and \(\beta=2\) for E. Therefore:
- A/B: at least \(7\cdot2=14\) zero-excess B-labelled witnesses;
- C/D: at least \(7\cdot3=21\);
- E: at least \(7\cdot3=21\).

For E408 Q33, conditional on the registered beta value:
- \(\beta=0\): at least \(8\cdot2=16\);
- \(\beta=1\) or \(2\): at least \(8\cdot3=24\);
- \(\beta=3\): at least \(8\cdot4=32\).

These counts strengthen the conservative two-witness-per-color bound from the sibling witness-packing branch. They are actual K5-component witnesses, not arbitrary independent four-sets, so the cross-color linearity statement is valid.

## 5. Hub consequence and limitation

If a B-labelled witness has a full row b, meaning b misses all three hubs, then Q must hit every hub: otherwise Q together with b and an unhit hub is an independent six-set in F. This statement applies to each such witness individually.

The count above does not guarantee that any specified number of the zero-excess witnesses carry full-row labels. It also does not bound how often a core edge can serve Hall matchings for different witness pairs. Therefore no E407 or E408 terminal is excluded by this theorem alone.

The full EG617(r=12) theorem remains OPEN / NOT_CERTIFIED.
