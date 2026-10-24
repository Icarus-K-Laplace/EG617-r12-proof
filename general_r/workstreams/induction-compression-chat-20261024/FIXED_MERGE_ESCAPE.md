# Fixed-Merge Escape: What Hypergraph Data Can and Cannot Prove

Status: **No fixed-merge escape theorem proved; a pure-hypergraph obstruction is explicit.**

## Exact comparison

For fixed c != j,

\[
\mathcal H_{c,j}
=
\left(\bigcup_{i\notin\{c,j\}}\mathcal I_i\right)
\cup(\mathcal I_c\cap\mathcal I_j)
\subseteq
\mathcal H_{-c}=\bigcup_{i\ne c}\mathcal I_i.
\]

Therefore \(\tau(\mathcal H_{c,j})\le\tau(\mathcal H_{-c})\), but the inequality gives no upper bound of \(2r-1\) on the left. Failure of every robust shell, \(\tau(\mathcal H_{-c})\ge2r\), does not logically imply that any fixed merge succeeds.

A fixed merge c -> j succeeds exactly when \(\tau(\mathcal H_{c,j})\le2r-1\). This remains distinct from unrestricted adaptive recoloring.

## Pure-hypergraph obstruction

Let A and B be disjoint sets of size \(2r-1\), and let F consist of every r-subset of A and every r-subset of B. Add any remaining vertices of V as isolated points of F.

Then:

\[
\nu(F)=2,\qquad \tau(F)=2r.
\]

Indeed, an r-uniform family of all r-subsets of a \((2r-1)\)-set has matching number one and transversal number \(r\); the two components are disjoint, so the matching numbers add to two and the transversal numbers add to \(2r\).

If one formally assigns \(\mathcal I_i=F\) for every color i, then both \(\mathcal H_{-c}\) and every \(\mathcal H_{c,j}\) equal F. Thus no purely hypergraph argument from \(\tau\ge2r,\nu=2\) can force a successful fixed merge.

## Why this is not a graph-level counterexample

This construction cannot be the family of independent r-sets of a genuine edge-coloring. If every r-subset of A were independent in every color, then any pair of vertices of A (for r>=2) would lie in an r-subset with no available edge color, contradicting that every edge has exactly one color. The construction is only a pure-hypergraph obstruction; it does not refute the desired graph-level fixed-merge theorem.

## Current graph-level route

The new Case B residual budget and color dichotomy are in ALIGNMENT_FREE_WITNESS_RIGIDITY.md. They may constrain any genuine obstruction through:
- \(\sum_{i\ne c}b_i\le\binom{r-1}{2}\);
- a repeated low-excess witness color with residual clique-transversal structure, or a color with at least four private witnesses;
- perfect matchings on symmetric differences of same-color witnesses.

No implication that a fixed merge must succeed has yet been derived from these graph constraints.


## Exact private-witness criterion for dropping one shell vertex

Let X be a minimum transversal of H_{-c} with |X|=2r. For v in X, define its private-witness family

\[
\mathcal P(v)=\{T\in\mathcal H_{-c}:T\cap X=\{v\}\},
\]

and for a private witness T define its full missing-color set

\[
D(T)=\{i:T\text{ is independent in color }i\}.
\]

For a fixed merge c->j, the set X minus {v} is a successful shell **if and only if**

\[
\boxed{D(T)=\{j\}\quad\text{for every }T\in\mathcal P(v).}
\]

Reason: because X is a transversal, X minus {v} can fail to hit H_{c,j} only on a private witness T in P(v). Such T survives in H_{c,j} exactly if it is independent in some untouched color k not in {c,j}, or is independent in both c and j. Thus all private witnesses must be independent in color j only: not in c and not in any other color.

This is an exact criterion for deleting one vertex from the tight 2r-point transversal, not a proof that such a vertex exists. Failure of every fixed merge means that for every j and every v there is at least one private witness whose missing-color set is not the singleton {j}. This may be due to multi-color witnesses; the current hypergraph data do not rule that out.

## Updated status

The alignment-free residual theorem now also extracts a q-net with at least ceil(q/2) directions in Case B for q=r-1>=3; see ALIGNMENT_FREE_WITNESS_RIGIDITY.md, Theorem J.W5. This is useful geometric structure but does not imply a fixed merge or a shell of size 2r-1.
