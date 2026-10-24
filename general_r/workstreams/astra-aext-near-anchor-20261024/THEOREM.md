# Exact target and clean-room partial theorems
Overall status: PARTIAL; A_ext* is OPEN.

## 0. Exact target (not redefined here)
Verbatim from CHAT E, SUFFICIENTLY_LARGE_R_THEOREM.md, commit aa7fbbda16ff0170c9bf7c440ca961a7a8aab3c0:
> Every hypothetical counterexample produces either:
> 1. a contextual legal 4r+1 residual with alpha ≤ 4, omega ≤ r−1, and inherited full-colour cap; or
> 2. an anchored contextual 5r+1 terminal with alpha=5, omega ≤ r−1, delta ≥ r, inherited full-colour cap, and no legal 4r+1 residual.
>
> This is OPEN.

The input's word "legal" retains its upstream contract. The results below do not silently equate an arbitrary induced subgraph with that complete contract.

## 1. Definitions and external dependencies
All graphs are finite simple undirected graphs. Set
p_k(n)=k*binom(floor(n/k),2)+(n mod k)*floor(n/k).
This is the minimum number of edges in an n-vertex graph with alpha<=k, by Turan applied to its complement.

Use Brooks' theorem componentwise: maximum degree Delta>=3, with no complete component K_(Delta+1), implies chromatic number at most Delta (components of lower degree are harmless).
Use the exact second-Turan bound: if J is K_(k+1)-free, not k-partite, k>=2 and n>=2k+1, then
e(J)<=t_k(n)-floor(n/k)+1.
This regime is verified in Kang--Pikhurko, Theorem 1 (2005):
https://opikhurko.warwick.ac.uk/E/KangPikhurko05ms.pdf
Brooks reference: Catlin (1978), introductory statement,
https://doi.org/10.1016/0012-365X(78)90167-X
No D_low, near-anchor exclusion, or conjectural C* is used below.

## 2. Original-colouring constraints — PROVED
Assume r>=3 and an r-colouring of K_(r^2+1) in which every (r+1)-set contains all colours.
Each colour graph has alpha<=r and omega<=r. For every induced n-set, each colour has at least p_r(n) edges. Therefore every colour also has the hereditary upper cap
D_r(n)=binom(n,2)-(r-1)p_r(n).
The least colour G has m<=mu=r(r^2+1)/2.

If Q is a target K_r, an outside vertex has at most one target neighbour in Q: all r-1 other colours must occur among its r incident edges into Q. Thus interblock target edges are matchings.

There is a minimum-degree anchor v with d<=r-1. Otherwise the average-degree bound makes G r-regular, while alpha<=r forces chi>=r+1. Brooks contradicts this, since K_(r+1) components are forbidden. Set s=r-d, 1<=s<=r.

Let A=N_G(v), B=V(G)\N_G[v]. Define z=binom(d,2)-e(G[A]) and g_x=d_G(x)-d for x in A. All g_x>=0 and exact counting gives
m=binom(d+1,2)+q+e(G[B]), q=z+sum_A g_x>=0.
Indeed e(A,B)=sum_A(d_G(x)-1)-2e(A).

## 3. Normalization and exact deletion ledger — PROVED
For 1<=a<=r-1 define
B_s(a)=[a*r^2-a*r+r^2+2*r*s-r-s^2+s]/2,
B_a=B_1(a)=r*((a+1)*r-a+1)/2.
The anchor nonneighbourhood starts at a=r-1 and has ar+s vertices, alpha<=a, e<=B_s(a).

An induced (ar+1)-subset with e<=B_a exists by averaging. The exact, unscaled identity is
B_1(a)*binom(ar+s,2)-B_s(a)*binom(ar+1,2)
= r*(s-1)/4 * [a^2*r*(s-2)+2*a*r^2+a*r*s+r*s+s].
It is nonnegative for every integer s>=1. This explicitly distinguishes the unscaled identity from the doubled expression used in the source.

If R_a contains a target K_r Q, put R_(a-1)=R_a-Q. Exactly
e(R_(a-1))=e(R_a)-binom(r,2)-e_G(Q,R_(a-1)).
Thus e<=B_(a-1); no cross term is dropped as an equality.
An independent a-set in R_(a-1) forbids at most a<r vertices of Q, hence would extend to an independent (a+1)-set. Therefore alpha(R_(a-1))<=a-1.

The integer potential a strictly decreases. This proves termination, NOT termination at a<=5. At the first K_r-free stop, 1<=a<=r-1 and omega<=r-1. a=1 is impossible. Results excluding smaller terminal types require their separate hypotheses.

The target independence number is exactly a for any canonical state with a>=2: the continuous Turan lower bound for alpha<=a-1 exceeds B_a by at least
[r^2+a*r+r-a+2]/[2(a-1)]>0.

## 4. Simultaneous second-Turan ledger — PROVED
Let 2<=a<=r-1 be a K_r-free canonical stop, n=ar+1.
Write x_0=e(G_0)-p_a(n), and x_i=e(G_i)-p_r(n) for i>0.
Counting all edges gives
x_0+sum_(i>0)x_i=(binom(a,2)-1)*r+a.

For i>0, alpha(G_i)<=r and omega(G_i)<=a. The latter holds because a monochromatic non-target clique is target-independent.
The complement of G_i cannot be r-partite: its independent parts would be G_i-cliques of size <=a, covering at most ar<n vertices.
Second-Turan with k=r gives x_i>=a-1.

The target complement cannot be a-partite either: its parts would be target cliques of size <=r-1 and cover at most a(r-1)<n.
Second-Turan with k=a gives x_0>=r-1.
Both uses satisfy n>=2k+1.

Consequently the shifted nonnegative excesses
u_0=x_0-(r-1), u_i=x_i-(a-1)
obey the exact identity
u_0+sum_(i>0)u_i
= L_a(r):=r*(binom(a-1,2)-2)+2a.

In particular L_6(r)=8r+12>0 for every r.
The corresponding contextual upper cap is
U_(a,1)=p_a(ar+1)+r*(binom(a-1,2)-1)+2a-1.
This proves that this strengthened edge-count comparison alone cannot exclude a=6 at ANY increased threshold.

## 5. Sharp single-colour obstruction — PROVED
For all a>=3 and r>=2 construct H_(a,r) on ar+1 vertices:
take r disjoint a-cliques B_1,...,B_r; choose u in B_1 and v in B_2.
Add a new vertex w adjacent to every vertex in (B_1 union B_2) except u,v.
Add the edge uv. There are no other inter-clique edges.

Then
alpha(H)=r, omega(H)=a,
e(H)=r*binom(a,2)+2a-1=p_r(ar+1)+(a-1),
Delta(H)=2a-2.
Proof: the gadget on B_1 union B_2 union {w} has alpha=2. A triple without w repeats one clique; a triple with w would need both u and v, which are adjacent. It has an independent pair. Its largest clique has size a: a clique containing w lies in one B_j minus its distinguished vertex, while the only cross-clique edge uv does not meet w. Other components are K_a. Count the two sets of a-1 w-edges and uv.

Furthermore, if r>=2a(a-1)+2, H satisfies e(H[Z])<=D_r(|Z|) for EVERY vertex subset Z.
For n=|Z|<=r this is the trivial cap binom(n,2).
For n>=r, D_r(n) is nondecreasing: D_r(n+1)-D_r(n)=n-(r-1)floor(n/r)>=0.
Thus D_r(n)>=binom(r,2).
Meanwhile e(H[Z])<=(a-1)n<=(a-1)(ar+1)<=binom(r,2);
the last inequality follows from r-1-2a(a-1)>=1 and r/2>=a-1.
This is an all-r analytic argument, not an enumeration.

At a=6 this holds for every r>=62. Thus the NON-TARGET floor used by the contextual cap is sharp even with all single-colour hereditary caps at every r>=67.
This H is NOT the target graph and NOT an edge partition into r compatible colour graphs. It is NOT a counterexample to P(r) or A_ext*. Its role is to rule out a proposed improvement based only on these one-colour constraints.

## 6. Exact unresolved extraction obligation — OPEN
Uniform high-stop extraction (sufficient remaining input):
For every r>=67 and every normalized first K_r-free stop R_a actually arising from the original colouring, 6<=a<=r-1, construct one of the TWO EXACT outputs in section 0, including contextual and anchoring legality, or contradict the original colouring.

This weaker, bypass-allowing version suffices; proving nonexistence of every such stop would also suffice. It must cover both:
- a<=r-2: at least one genuine removed K_r provides a predecessor interface;
- a=r-1: the initial normalized residual may already be K_r-free and has NO predecessor block.

CONDITIONAL conclusion: combine this obligation with the pinned a<=5 endpoint theorems to obtain A_ext*(r). The endpoint theorems, including full legal-core scope, have not all been independently re-proved in this round; they remain explicit inputs to that conditional statement.

No uniform threshold for this obligation has been established. Neither recursion termination nor a fixed-a asymptotic design approximation supplies it.
