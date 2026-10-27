# E407 Q32 — delta=13 one-step-to-308 K5-saturated reduction

Date: 2026-10-27  
Status: **PROVED_CONDITIONAL strict reduction**, conditional on the registered delta=14 saturated-kernel classification, whose alpha-critical component-count step uses the unaudited Didin 2026 theorem. No terminal contradiction is claimed in this file; the extension contradiction is separated into `DELTA13_ONE_STEP_SATURATED_EXTENSION_CLOSURE.md`.

## 1. One-step saturated contract

Let

\[
L=L_U=\overline{H[U]},\qquad |U|=29,\qquad e(L)=307,
\]

be non-four-partite and K5-free. Assume there is exactly one K5-safe augmentation edge `e`, and

\[
L':=L+e
\]

is a non-four-partite 308-edge K5-free K5-saturated graph.

Put

\[
G'=\overline{L'},\qquad G=\overline L=G'+e.
\]

Then

\[
e(G')=98,\qquad e(G)=99.
\]

The 49 selected support blocks are K4s already present in L. Hence they remain 49 pairwise edge-disjoint K4s in L'. Moreover the new edge e is not an edge of any selected support K4.

Because the support K4s themselves give an independent 4-set in G', while L' is K5-free,

\[
\alpha(G')=4.
\]

Thus `(G',L')` satisfies exactly the old 98-edge saturated local-kernel contract.

## 2. Import the registered saturated-kernel classification

Under the same external-theorem firewall as `DELTA14_SATURATED_ALPHA_CRITICAL_REDUCTION.md` and `DELTA14_SATURATED_KERNEL_CLASSIFICATION.md`, every admissible G' is

\[
\boxed{G'=K_7^A\dot\cup K_7^B\dot\cup\overline J,}
\tag{2.1}
\]

where J is the 15-vertex triangle-free saturated non-bipartite C5 blow-up with cyclic part sizes

\[
(5,5,2,1,2).
\]

Write these J-parts as

\[
X,Y,C,\{d_0\},E,
\]

with sizes `5,5,2,1,2`. In G':

- A and B are disjoint K7s, anticomplete to each other and to the 15-vertex block;
- X,Y are K5s and are anticomplete to each other;
- `C union E` is a K4, anticomplete to d0;
- d0 is complete to `X union Y` and anticomplete to `C union E`.

The internal G'-degree sequence on U is

\[
6^{14},\quad 7^{10},\quad 8^4,\quad 10^1,
\]

where d0 is the unique degree-10 vertex.

## 3. The augmentation edge is one of exactly 14 uncovered A/B-J cross edges

In L', every K4 consists of exactly

- one A vertex,
- one B vertex,
- the endpoints of one J-edge.

The 49 selected support K4s are edge-disjoint. Since `|A||B|=49` and `e(J)=49`, they exhaust all 49 A-B edges and all 49 J-edges exactly once.

Each support K4 also uses four A/B-to-J cross edges. Thus the 49 support blocks use

\[
49\cdot4=196
\]

of the

\[
7\cdot15+7\cdot15=210
\]

A/B-J cross edges in L'. Exactly

\[
\boxed{210-196=14}
\tag{3.1}
\]

cross edges are uncovered by the support packing.

Since e is not a support edge and every A-B edge and J-edge is a support edge, e must be one of these fourteen uncovered cross edges. After interchanging A and B if necessary, write

\[
\boxed{e=a_*v,\qquad a_*\in A,\quad v\in V(J).}
\tag{3.2}
\]

Thus the original target graph on U is

\[
G=G'+a_*v.
\]

At a J-vertex z, the support system uses exactly `d_J(z)` distinct A-labels and `d_J(z)` distinct B-labels, so the number of uncovered cross edges incident with z is

\[
2(7-d_J(z)).
\]

Since J has degree sequence `7^10,6^4,4^1`, the fourteen uncovered edges distribute as

- zero at the ten degree-7 J vertices;
- two at each of the four degree-6 J vertices;
- six at d0.

Hence the J-endpoint v of e lies in `C union E` or equals d0; in the explicit labeling a degree-7 X/Y vertex has no uncovered A/B cross edge. This sharpened endpoint localization is useful below. If a different admissible labeling is used, the invariant statement is simply `d_J(v)<7`; under the classified kernel that means `v in C union E union {d0}`.

## 4. Exact U-to-W degrees after restoring e

Let

\[
\epsilon_u=d_H(u)-12,\qquad
\epsilon_U=\sum_{u\in U}\epsilon_u.
\]

For delta=13,

\[
0\le\epsilon_U\le3,
\qquad e(H[W])=35-\epsilon_U.
\tag{4.1}
\]

Restoring the target edge `a_*v` raises the internal G-degree of its two endpoints by one and therefore lowers each corresponding U-to-W degree by one.

The exact W-degrees from U are:

- A: `d_W(a)=6+epsilon_a` for `a!=a_*`, while
  \[
  d_W(a_*)=5+\epsilon_{a_*};
  \]
- B: `d_W(b)=6+epsilon_b`;
- X,Y: `d_W(z)=5+epsilon_z` (but v cannot lie here under the uncovered-edge localization above);
- C,E: `d_W(z)=4+epsilon_z`, except if `z=v`, when
  \[
  d_W(v)=3+\epsilon_v;
  \]
- d0:
  \[
  d_W(d_0)=
  \begin{cases}
  1+\epsilon_{d_0},&v=d_0,\\
  2+\epsilon_{d_0},&v\ne d_0.
  \end{cases}
  \tag{4.2}
  \]

The aggregate cross-edge count is

\[
e_H(U,W)=150+\epsilon_U.
\]

## 5. W-side four-partite profiles for epsilon_U>=1

Since `alpha(H[W])<=4`, the complement of H[W] is K5-free. By (4.1),

\[
e(\overline{H[W]})=153-(35-\epsilon_U)=118+\epsilon_U.
\]

Brouwer's second-Turan bound gives at most 118 edges for a non-four-partite K5-free graph on 18 vertices. Therefore for every

\[
\epsilon_U\ge1
\]

the graph `\overline{H[W]}` is four-partite. Equivalently W is partitioned into four target cliques; any H[W] edges between distinct parts are the small defect q.

The exact integer profiles are:

| epsilon_U | W clique-part sizes | cross edges q |
|---:|---|---:|
| 1 | (3,4,5,6) | 0 |
| 1 | (3,5,5,5) | 1 |
| 1 | (4,4,4,6) | 1 |
| 1 | (4,4,5,5) | 2 |
| 2 | (3,5,5,5) | 0 |
| 2 | (4,4,4,6) | 0 |
| 2 | (4,4,5,5) | 1 |
| 3 | (4,4,5,5) | 0 |

For epsilon_U=0, `e(\overline{H[W]})=118`, so equality with the non-four-partite Brouwer boundary is possible and no four-partite conclusion is imported. The epsilon=0 terminal is instead killed directly by edge-count stability in the extension-closure file.

## 6. Two elementary independent-set rules used by the terminal proof

### Pair common-nonneighbour rule

If `x,y` are nonadjacent in H, then the common H-nonneighbours of x,y induce a graph of independence number at most two. Otherwise an independent triple among those common nonneighbours together with x,y is an independent five-set in H.

### W-transversal blocker rule

Suppose W is split into four target cliques. If a core vertex u has a W-neighbour set S and there is an independent transversal of the four W clique parts avoiding S, then that transversal together with u is an independent five-set. Hence `N_W(u)` must hit every independent transversal.

For a genuine disjoint union of four cliques this means `N_W(u)` contains an entire clique part. With at most one or two W-cross edges, the same conclusion remains valid in the small-degree cases used in the extension proof unless the deleted set empties a part; the finite inequalities are written explicitly there.

## 7. Dependency firewall

The reduction to the C5-blow-up kernel uses the previously registered saturated-kernel classification and therefore inherits the unaudited Didin 2026 dependency, together with Brouwer's theorem.

Everything after the kernel has been fixed — the fourteen uncovered-edge count, degree identities, W profile enumeration, pair common-nonneighbour rule, and transversal arguments — is elementary under the frozen E407 core contract.

No E407-Q32 closure is claimed in this file alone.
