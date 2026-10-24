# Defect-cover incidence matrix and shared-edge accounting

Date: 2026-10-24  
Branch: `workstream/general-r-design-terminal-20261024`

## Status

- **PROVED_ANALYTIC:** exact weighted cover inequality for every missing ideal-block pair in a non-target color with (r) nonempty ideal blocks.
- **PROVED_ANALYTIC:** for block sizes at least five, a cover using at most 24 cross-block additions cannot be remote-only; at least one edge must meet a defect endpoint.
- **PROVED_ANALYTIC:** a clean (K_5) block allows at most four neighbors from any outside vertex in a non-target color, by (K_6)-freeness.
- **OPEN:** a global bound showing the total defect-cover load exceeds the (O(r)) budget.
- **OPEN:** terminal nonextension; the attempted (r\ge6212) closure was withdrawn (see `JOINT_DEFECT_PROPAGATION.md`).

## 1. Exact setup

Fix a non-target color (i), with an ideal clique partition
[
Q_i=\bigcup_{a=1}^r K(C_a),
]
where all (C_a) are nonempty. Let
[
F_i=E(G_i[W])\setminus E(Q_i)
]
be its cross-block additions. A **defect pair** is (d=(a,{u,v})) with (u,v\in C_a) and (uv\notin E(G_i)).

For each defect pair, the product space is
[
\Omega_d=\prod_{b\ne a} C_b.
]
Every (omega=(x_b)_{b\ne a}\in\Omega_d) yields the ((r+1))-set ({u,v}\cup\{x_b:b\ne a}). Since (uv\notin E(G_i)) and (alpha(G_i[W])\le r), this set must contain an edge of color (i). All such possible edges are cross-block additions in (F_i).

## 2. Defect-cover incidence matrix

For a defect (d=(a,{u,v})) and edge (e\in F_i), define the weight (w_{d,e}) by
[
w_{d,e}=\begin{cases}
1/|C_b|,& e=uz\text{ or }vz,\ z\in C_b,\ b\ne a,\\
1/(|C_p||C_q|),& e\in E(C_p,C_q),\ p,q\ne a,\\
0,&\text{otherwise.}
\end{cases}
]
Here the first case means the edge's endpoint in the defective block is exactly (u) or (v); an edge from another vertex of (C_a) has weight zero for this defect.

Choose one (x_b\in C_b) independently and uniformly for each (b\ne a). Let (Z_d) be the number of (G_i)-edges among the selected vertices and (u,v). Every outcome has (Z_d\ge1). Linearity of expectation gives the exact inequality
[
\boxed{\sum_{e\in F_i}w_{d,e}=\mathbb E Z_d\ge1.}
]
This accounts for every possible multi-block cover network, not just a single cylinder or star.

## 3. Shared-edge load and unique ownership

For a family (mathcal D_i) of defect pairs, define the load of a single actual edge
[
L_i(e)=\sum_{d\in\mathcal D_i}w_{d,e}.
]
Summing the valid inequalities gives
[
\boxed{|\mathcal D_i|\le\sum_{e\in F_i}L_i(e).}
]
This is the correct shared-edge accounting identity. It explicitly allows one edge to serve several defect obligations within the **same** color. Across different colors, edge ownership is unique, so an edge in (F_i) cannot be an addition in (F_j) for (i\ne j).

The inequality alone is not a global contradiction: the load (L_i(e)) can exceed one because an edge between two non-defective blocks contributes (1/(|C_p||C_q|)) to every defect in a third block. Any valid summation argument must bound these loads or exploit additional structure.

### Quantitative load bound for a matching of defects

Suppose every block has size at least five and (mathcal D_i) is a matching (its defect pairs are vertex-disjoint). An edge (e) between blocks (C_p,C_q):
- contributes at most (1/5) to a defect in (C_p), and at most (1/5) to a defect in (C_q), because an endpoint can belong to at most one matching pair in its block;
- contributes at most (1/25) to each defect in every other block.

Therefore, writing (q=|\mathcal D_i|),
[
\boxed{L_i(e)\le\frac25+\frac q{25}.}
]
For (q\le24), this gives (L_i(e)\le34/25). This is a rigorous capacity estimate, but it is not strong enough alone: (24) additions can still have total weighted load above (q). Defects sharing endpoints require a separate, explicitly multiplicity-aware bound.

## 4. The (K_6)-free constraint on endpoint stars

The contextual target cap (alpha(G_0)\le5) implies (G_i) is (K_6)-free for every (i>0). If (C_b) is a **clean actual (K_5)** in (G_i), then any outside vertex (z) has
[
d_{G_i}(z,C_b)\le4,
]
because five neighbors would make (C_b\cup\{z\}) a (K_6).

Consequently, for a fixed defect pair (uv), a cover that uses only edges from (u,v) into a clean (K_5) block (C_b) must have
[
N_{G_i}(u,C_b)\cup N_{G_i}(v,C_b)=C_b
]
and uses at least five edges. (K_6)-freeness does not forbid this: a split star with four neighbors from (u) and one from (v) is locally possible. Thus “every cheap cover creates another defect” is false without extra target-label or pair-ownership input.

## 5. Remote-only cover corollary

Assume all ideal blocks have size at least five and (|F_i|\le24). If none of the additions in (F_i) is incident to (u) or (v), then every (w_{d,e}\le1/25), so
[
\sum_{e\in F_i}w_{d,e}\le\frac{|F_i|}{25}\le\frac{24}{25}<1,
]
contradicting the exact cover inequality. Therefore a low-edit color cannot protect a defect pair by a remote-only network; at least one addition must meet an endpoint of the defect pair.

This is a strict reusable sublemma for the exact-size regime. It does not rule out a mixed network or the known nine-edge two-coordinate barrier.

## 6. Exact remaining obstruction

The missing global statement is a **target-labelled load bound** that handles all of:
1. repeated defect endpoints within a block;
2. edges shared across many defect rows in the same color;
3. remote edges reused by defects in other blocks;
4. the target group label of each endpoint and the fact that ordinary same-group pairs are target-colored;
5. (K_6)-free constraints on every clean block;
6. unique actual edge ownership across colors.

Neither (sum_d 1\le\sum_eL_i(e)) nor the (K_6)-free degree cap alone implies that the total edit budget is exceeded. No robust Hub Propagation or terminal nonextension theorem is claimed here.
