# Audit of the bounded target-defect capacity attempt

Date: 2026-10-24  
Branch: `workstream/general-r-design-terminal-20261024`

## Status

**DISPROVED as a proof route.** The proposed conclusion “no contextual terminal for (r\ge6212)” is **withdrawn**. The fatal step claimed that a hub has at most four target-nonneighbors in the ordinary part of its group. That reverses the relevant graph logic: the ordinary part is a clique, not an independent set.

No terminal nonexistence theorem follows from this attempt. The front-end and terminal nonextension statuses remain OPEN.

## 1. Valid inherited facts

For (r\ge1000), the established target stability/hub theorem gives a set (X) with:
- (|X|\le114);
- every target-internal deletion touches (X);
- (G_0[B_j\setminus X]) is a clique for each target ideal group (B_j);
- (|B_j|\in[r-26,r+27]).

Also, the contextual coloring contract gives (alpha(G_i[W])\le r) for every non-target color (i).

These facts are retained.

## 2. The exact error

The withdrawn proof asserted:
> If (v\in X\cap B_j) has five nonneighbors (y_1,\ldots,y_5\in B_j\setminus X), then ({v,y_1,\ldots,y_5}) is an independent six-set.

This is false. The five (y_k) lie in a clique, so the set contains many edges among the (y_k). The condition (alpha(G_0)\le5) does not bound the number of nonneighbors of a hub in the ordinary clique.

The clique cap (omega(G_0)\le r-1) gives a bound in the opposite direction: a hub has at most (r-2) neighbors in (B_j\setminus X), since (r-1) such neighbors together with the hub would form a (K_r). It does not give a constant upper bound on missing edges from the hub.

### Local obstruction to the claimed constant bound

Let (O) be a clique of size (r-1), and let (x,y) be adjacent to each other but nonadjacent to every vertex of (O). On (B=O\cup\{x,y\}), we have
[
|B|=r+1,\qquad \alpha(G_0[B])=2,\qquad \omega(G_0[B])=r-1.
]
All (2(r-1)) missing edges of the ideal clique (K(B)) touch (X=\{x,y\}). Thus a bounded exceptional set and the alpha/clique caps alone do **not** imply (O(1)) internal deletions. This is a local target-side obstruction, not a claimed full terminal coloring.

## 3. A valid lower bound that survives

Choose a target ideal group (B_h) with (|B_h|\ge r+1), which exists because (sum_j|B_j|=5r+1). Fix (S\subseteq B_h), (|S|=r+1). For every non-target color (i), (alpha(G_i[W])\le r) forces at least one color-(i) edge inside (S). The edges chosen for distinct colors are distinct and are all target-internal deletions. Hence
[
\boxed{D_h:=\left|\binom{B_h}{2}\setminus E(G_0)\right|\ge r-1.}
]
This is **PROVED_ANALYTIC**, but it is compatible with the existing (O(r)) total edit budget and does not yield a contradiction.

A trivial upper bound from hub concentration is only
[
D_h\le |X\cap B_h|\,|B_h\setminus X|+\binom{|X\cap B_h|}{2}
\le108(r+27)+\binom{108}{2}
]
when the sharper (|X|\le108) estimate is available. This is (O(r)), not (O(1)), and does not contradict (D_h\ge r-1).

## 4. Corrected frontier

- Bounded hub concentration: **PROVED_ANALYTIC** under the existing theorem.
- Lower bound (D_h\ge r-1) in an oversized target group: **PROVED_ANALYTIC**.
- Constant target-internal defect cap: **DISPROVED**.
- Terminal nonexistence for (r\ge6212): **OPEN**; the earlier claim is withdrawn.
- Multi-block cover-network shared-edge theorem: **OPEN**.
- Literal robust Hub Propagation: **OPEN**.
- Full front-end forcing to a terminal: **OPEN**.

The next valid attack must combine the (D_h\ge r-1) color-ownership requirement with the (O(r)) cross-edge budget and the actual hub neighborhoods. It cannot rely on a constant bound for the number of nonneighbors of a hub.
