# Robust exact core: current theorem boundary after the cylinder audit

## Status

- **PROVED_ANALYTIC:** the stability theorem gives (r^2-O(r)) clean transversal blocks.
- **PROVED_CONDITIONAL:** a linear edit charge holds when an ordinary same-group label is represented outside the target hub set in every other block.
- **PROVED_ANALYTIC:** every non-target color graph is (K_6)-free under (\alpha(G_0)\le5).
- **OPEN:** deleting (O(1)) vertices to obtain exact orthogonal partitions.
- **OPEN:** an (O(r))-repair theorem whose every repair conflicts with the coloring constraints.
- **OPEN:** robust nonextension directly from the near-design.

## 1. What the clean-block count actually gives

The frozen theorem retains at least
[
r^2-93r-54
]
size-5 exact transversals, pairwise linear, in partial parallel classes. This is (r^2-O(r)) blocks, not a complete resolvable (TD(5,r)).

The complement may still contain (O(r)) bad ideal blocks and (O(r)) pair-multiplicity defects. Nothing in the count alone proves that these defects meet the target hub set or can be repaired by deleting (O(1)) vertices.

## 2. Cylinder audit: a local one-color shortcut is globally forbidden

For a non-target color (i), a missing pair (uv) in one ideal block can be blocked by adding a star from (u) to all five vertices of a clean transversal block (C). This costs only five added edges and may make (\alpha(G_i)\le r).

But if (C) remains a (K_5) in (G_i), then (C\cup\{u\}) is a (K_6) in (G_i), contradicting (\alpha(G_0)\le5). Thus the target alpha condition forces at least one further missing edge in the cover block. That new defect itself requires protection against an independent transversal.

A previously explored (d_i=6) abstract trap is withdrawn: it did not establish (\alpha(G_i)\le r), because two missing pairs could be selected simultaneously while omitting the special cover block. It must not be used as a counterexample or theorem input.

## 3. Why exactification still does not follow

The current theorem does not yet prove that the defect-propagation chain terminates in a contradiction. It could, in principle, branch or cycle among:
- repeated-group missing pairs;
- target cross edges inside ideal transversal blocks;
- added cross-block edges in non-target colors;
- hub-incident target deletions.

All actual pairs have one color, so a valid proof must track pair ownership exactly. A local repair of one partition can consume a pair already needed by another color; target edges are not free repair resources.

The upstream exact affine/net nonextension theorem applies only once its exact orthogonal-partition hypotheses are established. The current (5r+1)-vertex terminal is not such a structure merely because it is close to a partial TD.

## 4. Minimum missing theorem

The next sufficient result is a **defect-chain cost theorem**:

> Every chain/cycle of missing edges and cylinder covers that keeps each non-target color (K_6)-free has total non-target slack plus target cross-cover cost exceeding the exact global budget, unless it creates an omitted-color ((r+1))-set.

This must count each pair once and cannot assume an affine plane exists. Until this is proved, no exact-core or robust nonextension closure is claimed.


## 5. Alternative terminal closure without exactification

**PROVED_ANALYTIC for (r\ge6212):** the contextual terminal itself is impossible by bounded target-internal defect capacity; an exact net is not needed.

The target stability theorem gives (|X|\le108), every target internal deletion touches (X), and (B_j\setminus X) is a target clique. Each hub has at most four missing target edges to ordinary vertices in its own group. Therefore
[
D\le4|X|+\binom{|X|}{2}\le6210.
]
Some target group has at least (r+1) vertices. Every non-target color must have an edge in a fixed ((r+1))-subset of that group, so unique color ownership requires at least (r-1) distinct target internal deletions. For (r\ge6212), this contradicts (D\le6210).

Thus the exact-core route is no longer necessary to close the **terminal branch** for sufficiently large (r). It remains OPEN as a structural route, and the front-end forcing interface to the terminal remains OPEN. See `JOINT_DEFECT_PROPAGATION.md` for the full proof.
