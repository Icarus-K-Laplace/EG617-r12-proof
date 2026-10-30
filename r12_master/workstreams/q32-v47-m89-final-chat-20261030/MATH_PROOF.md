# Mathematical results — Q32 full-support m=8,9

## 1. Frozen contract

Assume the source-correct Q32 interface:

`|H|=47`, `e(H)=285`, `alpha(H)<=4`, `delta(H)>=12`, and
`sum_{v in H}(d_H(v)-12)=6`.

There are `m=8` or `m=9` exact non-target colors. For each exact color C, the Type-I source factorization gives twelve disjoint K5 factors partitioning all 60 vertices other than its special point x_C. Each factor meets the 14-point outside set O. The pivot is p=47 and A={48,...,60}; all pA edges have the target color.

For every exact color C, the pivot construction gives a four-set Q_C contained in H and adjacent to p in color C:
- if p != x_C, Q_C is the other four vertices in the unique Type-I K5 factor containing p;
- if p = x_C, Q_C is N_t minus its distinguished vertex y_C.

The four-set Q_C is independent in H. Distinct Q_C are vertex-disjoint because a shared vertex would give its p-edge two different colors. Put Q=union_C Q_C and R=H\Q. Thus |Q|=4m and |R|=47-4m.

## 2. Type-I outside profiles and witness count

Let b_i=|K_i intersect O| for the twelve K5 factors. Every factor meets O, so b_i>=1.

- If x_C is in O, sum b_i=13. The source cap b_i<=2 therefore forces exactly one double-outside factor and eleven single-outside factors.
- If x_C is in H, sum b_i=14. The cap b_i<=3 forces either one triple-outside factor and eleven single-outside factors, or two double-outside factors and ten single-outside factors.

The exceptional factor indices are unrestricted: a legal single-outside witness may be one of the two special K5 factors. No assumption that all ten isolated factors are single-outside is used.

Consequently every exact color supplies at least ten pairwise vertex-disjoint core K4 witnesses. Witnesses of different colors intersect in at most one vertex: if two such K4s shared two vertices, their shared edge would have two owners, contrary to the global edge-coloring.

**Status: PROVED_CONDITIONAL** on the source-correct Type-I interface and unique edge ownership.

## 3. Pivot-pair perfect matchings

For two distinct exact colors C,D, the sets Q_C,Q_D are disjoint independent four-sets in H. The bipartite graph B_CD=H[Q_C,Q_D] has independence number at most four. In a bipartite graph on 4+4 vertices, alpha=8-tau; hence its vertex-cover number is at least four. By Kőnig's theorem it has a matching of size four, necessarily a perfect matching.

Thus
[
e_H(Q_C,Q_D)ge4.
]

This is the correct all-m=8/9 pivot matching statement. It does not assert the aligned m=10 common-P decomposition.

**Status: PROVED_CONDITIONAL.**

## 4. Light-pair matching composition

Call a pivot pair light if e_H(Q_C,Q_D)=4. Its four edges are exactly one perfect matching, hence define a unique bijection f_CD:Q_C -> Q_D.

Suppose C,D,E are distinct and both CD and CE are light. For u in Q_C, put v=f_CD(u), w=f_CE(u). If vw were not an H-edge, then
[
(Q_C\setminus{u})\cup{v,w}
]
would be an independent five-set: the other three vertices of Q_C are unmatched to v and w by uniqueness of the two perfect matchings, and vw is absent. This contradicts alpha(H)<=4. Therefore every composed edge vw belongs to H.

If different common anchors force t distinct perfect matchings between Q_D and Q_E, all t must be contained in B_DE.

**Status: PROVED_CONDITIONAL.**

## 5. Exact K4,4 packing capacity

Let mu_4(t) be the minimum number of edges in a bipartite graph with parts of size four that contains t distinct perfect matchings. Exhaustive enumeration of all 2^16 edge sets gives:

| t | mu_4(t) |
|---:|---:|
| 1 | 4 |
| 2 | 6 |
| 3-4 | 8 |
| 5-6 | 10 |
| 7-9 | 12 |
| 10-11 | 13 |
| 12-14 | 14 |
| 15-18 | 15 |
| 19-24 | 16 |

Hence if t distinct compositions are forced for a pivot pair, its target edge count is at least mu_4(t). The independent script `verify_m89_pivot_matching.py` enumerates all 65,536 bipartite graphs and verifies the table.

**Status: COMPUTATION_CERTIFIED** for this finite K4,4 lookup; its use in the full CSP is **PROVED_CONDITIONAL** by the composition lemma.

## 6. Pivot-block degree ledger

Write
[
e_H(Q_i,Q_j)=4+x_{ij},quad
e_H(Q_i,R)=|R|+y_i,
]
where x_ij,y_i are nonnegative. Set
[
X_i=sum_{j\ne i}x_{ij},qquad
Y_i=y_i,qquad
\epsilon_i=sum_{v\in Q_i}(d_H(v)-12).
]

Since Q_i is independent,
[
sum_{v\in Q_i}d_H(v)
=sum_{j\ne i}e_H(Q_i,Q_j)+e_H(Q_i,R)
=4(m-1)+X_i+|R|+Y_i
=43+X_i+Y_i.
]
The left side is 48+epsilon_i. Therefore
[
oxed{X_i+Y_i=5+\epsilon_i.}
]
Summing over all pivot blocks gives
[
sum_i\epsilon_i=2x+y-5m\le6,
]
where x=sum_{i<j}x_ij and y=sum_i y_i.

This is an exact distribution of the six degree-excess units across the individual pivot blocks, not a new independent edge budget.

**Status: PROVED_CONDITIONAL.**

## 7. Scalar pivot frontier (not a contradiction)

Let n=47-4m and p_4(n)=C(n,2)-t_4(n). Write
[
e_H(Q)=4\binom m2+x,quad
e_H(Q,R)=mn+y,quad
e_H(R)=p_4(n)+z.
]
For m=8, n=15 and p_4(n)=21; for m=9, n=11 and p_4(n)=10. Since e(H)=285,
[
x+y+z=32.
]

The degree sums over Q and R give
[
2x+y\ge5m,qquad y+2z\ge D_m,
]
where D_8=18 and D_9=13. The six-unit excess identity is
[
(2x+y-5m)+(y+2z-D_m)=6.
]

Exact integer enumeration gives 79 feasible scalar triples for m=8 and 61 for m=9. Their ranges are recorded in `RUN_LOG.md`. These are relaxations only; neither frontier is empty.

**Status: PROVED** for the arithmetic reduction; **OPEN** for excluding its graph-realizable states.

## 8. Withdrawn shortcuts

- **WITHDRAWN:** `delta(H[R]) >= 12-m` unconditionally. A residual vertex can have more than m target neighbors in Q; the extra cross edges trade against its internal R-degree. Only the summed inequality `y+2z>=D_m` is currently justified without fixing the cross-degree distribution.
- **WITHDRAWN:** `d_H(q,R) >= 13-m` unconditionally for q in Q. A pivot-block vertex can have extra target neighbors in other pivot blocks; those extra internal-Q edges trade against its R-degree.
- **WITHDRAWN as an m=8/9 constraint:** the six common-P factors and residual-signature injectivity from the aligned m=10 3+7 cell. No m=8/9 four-track reduction has been proved in the inspected dependencies.


## 9. Exact source-core accounting and the 69/70 near-Turan normal form

For an exact color C, let \(b_i=|K_i\cap O|\) for its twelve Type-I K5 factors and let \(a=|A_0|\). The source profile gives \(b_i\in\{1,2,3\}\). The K5 interiors contribute exactly
\[
B_C=\sum_{i=1}^{12}\binom{5-b_i}{2}
\]
edges inside H. The only other C-edges are the nine Type-I gadget edges. Their H-H contribution is exactly
\[
G_C^H=
{\bf1}_{x_C\in H}\bigl(|(N_s\setminus A_0)\cap H|+
|(N_t\setminus\{y_C\})\cap H|\bigr)
+{\bf1}_{y_C\in H}|A_0\cap H|.
\]
Thus
\[
\boxed{e_C(H)=B_C+G_C^H.}
\]
The isolated solver encodes this equality directly, independently of the aggregate 69--75 cap.

The source-correct placement cases sharpen it:

- If \(x_C\in O\), the outside profile is \((2,1^{11})\), so \(B_C=69\). All gadget edges incident with \(x_C\) leave H; only \(y_C-A_0\) can contribute H-H edges. Therefore
  \[
  69\le e_C(H)\le69+a\le73.
  \]
- If \(x_C\in H\) and the profile is two-double \((2,2,1^{10})\), then \(B_C=66\). The registered Type-I gadget count gives \(G_C^H\ge6-a\), while at least one gadget edge leaves H, so
  \[
  \max(69,72-a)\le e_C(H)\le74.
  \]
- If \(x_C\in H\) and the profile is triple \((3,1^{11})\), then \(B_C=67\), and the same gadget count gives
  \[
  \max(69,73-a)\le e_C(H)\le75.
  \]

**Status: PROVED_CONDITIONAL** on the source-correct Type-I factorization and the registered gadget-edge placement lemma in \`HIGH_SUPPORT_NEAR_TURAN.md\`.

### 9.1 Near-Turan partition for every non-target color in the 69/70 layer

For any non-target color C, put \(D=C[H]\). Since \(\alpha(C)\le12\), we have \(\alpha(D)\le12\), hence \(\bar D\) is K13-free. Also \(\omega(D)\le4\), because a C-colored K5 inside H would be an independent 5-set in the target graph H.

- If \(e(D)=69\), then \(e(\bar D)=\binom{47}{2}-69=1012=t_{12}(47)\), so Turán equality gives a complete 12-partite complement.
- If \(e(D)=70\), then \(e(\bar D)=1011\). The registered second-Turán bound says a non-12-partite K13-free graph on 47 vertices has at most \(1010\) edges. Hence \(\bar D\) is again 12-partite.

Every part is a D-clique and has size at most four. Since the parts cover 47 vertices, their sizes are exactly
\[
4^{11},3.
\]
The 12 parts contribute exactly \(11\binom42+\binom32=69\) D-edges. There are zero cross-part D-edges in the 69-layer and exactly one in the 70-layer. A D-colored K4 crossing two parts needs at least three cross-part edges (the cheapest split is 3+1), so every D-colored K4 lies wholly in a size-four part.

Thus every non-target color in the 69/70 layer has an \(11K_4+K_3\) partition. For exact colors, every source single-outside witness K4 occupies one of the size-four parts. With ten witnesses, the remaining seven vertices split into one further K4 part and one K3 part; with eleven witnesses, the remaining three vertices are the K3 part.

**Status: PROVED_CONDITIONAL** on the registered second-Turán input. The solver encodes this partition conditionally for every non-target color with 69 or 70 H-edges. For exact colors it additionally forces each source witness K4 into a size-four part; the independent verifier reconstructs the partition from the color graph and checks witness alignment.

### 9.2 What this does not prove

The low-layer partition theorem is a necessary structural reduction for all eleven non-target colors, not a contradiction. The m=8/9 solver still has not been executed to SAT/UNSAT. The full-support terminal remains **OPEN**.
