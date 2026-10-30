# Mathematical results — Q32 full-support m=8,9

> **AUDIT STATUS: NOT A VALID EG617 CLOSURE.** This file's source-labelled exact-color model assumes every exact-129 color is Type I and its final obstruction additionally assumes omega(H)<=5. The actual balanced-coloring problem supplies only alpha(C),omega(C)<=12 and the Q32 core has omega(H)<=11. Both extra clique restrictions are absent. The previous m=8/9 analytic-closure claim and the e_C(H)>=71 global floor are withdrawn. See AUDIT_RETRACTION_BALANCED_PREMISES.md. The pivot arithmetic and Hall lemmas below remain conditional local results, not a complete Q32 model.

## 1. Frozen contract

Assume the registered Q32 core interface:

`|H|=47`, `e(H)=285`, `alpha(H)<=4`, `delta(H)>=12`, and
`sum_{v in H}(d_H(v)-12)=6`.

The source-labelled construction below is restricted to the **augmented Type-I subcase** in which each exact color is separately known to have twelve disjoint K5 factors partitioning all 60 vertices other than x_C. This Type-I coverage is not established for every exact color under balancedness, which only gives alpha(C),omega(C)<=12. The pivot is p=47 and A={48,...,60}; all pA edges have the target color.

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


### 9.3 Orthogonality of simultaneous low-layer color partitions

If two distinct non-target colors C,D both lie in the 69/70 layer, let P_C,P_D be their 11K4+K3 partitions. Any part of P_C is a C-clique and any part of P_D is a D-clique. Their intersection has size at most one: two common vertices would make their shared edge both C- and D-colored.

Thus the two partitions are orthogonal. For k non-target colors in the low layer, label each vertex by its part index in each partition. Any two distinct vertices agree in at most one coordinate, so these 47 label-vectors form a 12-ary code of length k and minimum Hamming distance at least k-1.

Each coordinate contributes exactly
\[
11\binom42+\binom32=69
\]
agreeing vertex-pairs. Since no pair agrees in two coordinates,
\[
69k\le\binom{47}{2}=1081,
\]
so \(k\le15\). This bound does not exclude k=8 or9 (or even all eleven non-target colors); the partition code by itself is therefore not a closure theorem.

The solver now encodes pairwise orthogonality explicitly:
\[
P_C(u)=P_C(v)\ \Longrightarrow\ P_D(u)\ne P_D(v)
\]
whenever both colors are in the 69/70 layer. The independent verifier checks the same condition on reconstructed partitions.

**Status: PROVED_CONDITIONAL** for the orthogonality statement; the explicit CSP cuts are necessary consequences of unique edge ownership.


### 9.4 Complete source-triangle alignment and special-gadget localization

A double-outside factor leaves a C-triangle in H. In the 69/70 partition, every C-triangle lies in one part because there is at most one cross-part C-edge.

- If x is outside O, the unique double factor's K3 occupies the size-three part after the eleven single-outside K4 witnesses fill all size-four parts. The exact core identity reduces to
  \[
  e_C(H)=69+{\bf1}_{y_C\in H}|A_0\cap H|.
  \]
  Hence the y--A0 gadget contributes zero or one H-edge in the low layer.
- If x is in H with two-double profile, the two disjoint K3s occupy the remaining size-four and size-three parts. The size-four part contains x and one K3. Since x's only source C-neighbors in H lie in \(N_s\setminus A_0\) and \(N_t\setminus\{y_C\}\), this K3 must be special. It cannot be the Ns K3: the other special factor Nt would then contribute at least two cross-part x--Nt edges, whether Nt is double or single. Thus it is the Nt K3. Necessarily \(|N_t\cap O|=2\), \(y_C\in O\), and all three H vertices of Nt share the part of x. The remaining x--Ns edges are cross-part, so
  \[
  e_C(H)=66+3+|(N_s\setminus A_0)\cap H|
        =69+|(N_s\setminus A_0)\cap H|,
  \]
  with the last term at most one.
- If x is in H with triple profile, the eleven K4 witnesses fill all size-four parts and the size-three part is x plus the two H vertices of the triple factor. The triple factor cannot be isolated (x has no source edges to it) or Ns (then Nt is single and contributes at least three cross-part x--Nt edges). It must be Nt. Necessarily \(|N_t\cap O|=3\), \(y_C\in O\), and both H vertices of Nt share x's part. Again
  \[
  e_C(H)=67+2+|(N_s\setminus A_0)\cap H|
        =69+|(N_s\setminus A_0)\cap H|,
  \]
  with the last term at most one.

Thus, for every exact color in the 69/70 layer with x in H:
\[
|N_t\cap O|=2\text{ (two-double) or }3\text{ (triple)},\quad
y_C\in O,\quad
|(N_s\setminus A_0)\cap H|\le1,
\]
and the entire H-interior of Nt lies in the same part as x.

**Status: PROVED_CONDITIONAL.** The isolated solver now encodes these source-placement implications and the exact \(e_C(H)=69+|(N_s\setminus A_0)\cap H|\) identity. The independent verifier independently checks them in its full alpha-validating pass. For x outside O it checks the unique double K3 alignment and \(e_C(H)=69+1_{y_C\in H}|A_0\cap H|\).

### 9.5 A 253-edge target matching skeleton and 32-edge residual

Fix any non-target color in the 69/70 layer and its 11K4+K3 partition. Every part is independent in H. For any pair of size-four parts A,B, Hall's condition holds in the target bipartite graph H[A,B]: if some S subset A had fewer than |S| neighbors in B, then \(S\cup(B\setminus N(S))\) would be an independent set in H of size at least five. The same argument on the size-three side shows that every 4-by-3 pair has a matching saturating the size-three part.

Choose a perfect matching for each of the 55 pairs of size-four parts and a saturating matching for each of the 11 pairs involving the size-three part. Since each edge joins a unique pair of parts, all choices are edge-disjoint. Their union M has
\[
e(M)=55\cdot4+11\cdot3=220+33=253.
\]
Exactly 36 vertices have \(d_M=11\), and 11 vertices have \(d_M=10\).

Write \(d_H(v)=12+s_v\), where \(s_v\ge0\) and \(\sum s_v=6\). For F=H\setminus M:
\[
e(F)=285-253=32,
\]
\[
d_F(v)=
\begin{cases}
1+s_v,&d_M(v)=11,\\
2+s_v,&d_M(v)=10.
\end{cases}
\]
At most six vertices have \(s_v>0\). Therefore at least 30 of the 36 vertices with \(d_M=11\) are leaves of F.

**Status: PROVED_CONDITIONAL** on the low-layer partition and \(\alpha(H)\le4\). The matchings are existential choices, independently made for each pair of parts. This theorem is not yet encoded with explicit matching-choice variables in the CSP and is not a contradiction by itself.


### 9.6 Exact leaf-core decomposition of the 32-edge residual

Let A be the 36 vertices with \(d_M=11\), and B the 11 vertices with \(d_M=10\). Write \(s_v=d_H(v)-12\), with total six. Let
\[
q=|\{v\in A:s_v>0\}|\le6,
\]
and let t be the number of components of F that are isolated K2s (both endpoints are degree-one vertices in A with s=0).

The degree formulas imply that F has exactly \(L=36-q\) leaves, all in A. The non-leaf core is
\[
W=B\cup\{v\in A:s_v>0\},\qquad |W|=11+q.
\]
After removing the t isolated K2 components, the remaining \(L-2t\) leaves each attach to W. If \(e_W=e(F[W])\), summing degrees over W gives
\[
28+q=(L-2t)+2e_W=(36-q-2t)+2e_W.
\]
Therefore
\[
\boxed{e_W=q+t-4,\qquad q+t\ge4.}
\]

So the residual is exactly t isolated K2 components, at least 30 leaves attached to a core of at most 17 vertices, and a core-edge count fixed by q+t-4 (at most t+2). This is an exact decomposition of every chosen matching skeleton, not merely an average-degree estimate.

**Status: PROVED_CONDITIONAL.** It is a further structural description of F, but no contradiction with the K6-free and cross-color constraints has yet been derived.


### 9.7 Exclusion of the entire 69/70 near-Turán layer

Assume H has 47 vertices, 285 edges, minimum degree at least 12, \(\alpha(H)\le4\), and \(\omega(H)\le5\). Suppose H is partitioned into eleven independent 4-sets and one independent 3-set.

For each pair of parts, Hall's theorem gives a perfect matching (or a matching saturating the 3-set). Their union M has
\[
e(M)=4\binom{11}{2}+3\cdot11=253.
\]
Let F=H\setminus M, so \(e(F)=32\). Each 4-part has three vertices with M-degree 11 and one with M-degree 10, hence its F-degree sum is at least \(3+2=5\). The 3-part has F-degree sum at least 3. Summing over all parts gives
\[
\sum_{i=1}^{11}(\rho_i-5)+(\rho_{12}-3)
=2e(F)-58=6.
\]
Therefore at least five 4-parts are tight, with F-degree sum exactly five. In a tight part P the F-degree profile is exactly \((1,1,1,2)\); call its three leaves \(u_1,u_2,u_3\).

Each leaf has only one F-neighbor, so among the ten other 4-parts at most three contain any F-neighbor of these leaves. At least seven 4-parts Q are clean. The perfect matching M[P,Q] sends the three leaves to three distinct vertices of Q. As Q is clean, those are the leaves' only H-neighbors in Q. Its fourth vertex \(w_Q\) is therefore nonadjacent to all three leaves.

For any two clean parts Q,R, if \(w_Qw_R\) is absent then \(\{u_1,u_2,u_3,w_Q,w_R\}\) is an independent 5-set. Since \(\alpha(H)\le4\), all seven selected \(w_Q\) must be pairwise adjacent, yielding a K7. This contradicts \(\omega(H)\le5\).

Thus every 11K4+K3 partition forces \(\alpha(H)\ge5\) or \(\omega(H)\ge7\). The registered 69/70 near-Turán theorem supplies such a partition whenever a non-target color C has \(e_C(H)\le70\), since \(\alpha(C[H])\le12\) and \(\omega(C[H])\le4\). Consequently
\[
\boxed{e_C(H)\ge71\quad\text{for every }c=1,\ldots,11.}
\]
Combining with the 37-unit gap ledger gives
\[
\boxed{\sum_{c=1}^{11}(e_C(H)-71)=15.}
\]

**Status: PROVED.** This removes the entire 69/70 layer for both m=8 and m=9. It does not close the 71+ source-placement cases.


## 10. Analytic exclusion of every exact Type-I color

The preceding low-layer argument is now superseded by a stronger source-partition obstruction. It does not require \(e_C(H)\le70\), or even the 69--75 source-core gap accounting.

Every exact-129 Type-I color C has twelve disjoint monochromatic K5 factors \(B_i\) partitioning \(K_{61}\setminus\{x_C\}\). Each factor meets O, because otherwise its five vertices would be an independent 5-set in H. Let \(b_i=|B_i\cap O|\).

- If \(x_C\in O\), then \(\sum b_i=13\) and all \(b_i\ge1\), so the profile is \((2,1^{11})\). The H-interiors of the factors partition H into eleven independent 4-sets and one independent 3-set.
- If \(x_C\in H\), then \(\sum b_i=14\). The profile is either \((2,2,1^{10})\), giving ten independent 4-sets, two independent 3-sets and the singleton \(\{x_C\}\); or \((3,1^{11})\), giving eleven independent 4-sets, one independent 2-set and \(\{x_C\}\).

The unified tight-part lemma proved in V47_TYPEI_PARTITION_OBSTRUCTION.md excludes all three partition shapes. For clarity, its matching skeletons have the following exact ledgers:

| Shape | \(e(M)\) | \(e(F)\) | Baseline F-degree sum | Total F-degree sum | Tight 4-parts |
|---|---:|---:|---:|---:|---:|
| \(11\cdot4+3\) | 253 | 32 | 58 | 64 | at least 5 |
| \(10\cdot4+3+3+1\) | 250 | 35 | 64 | 70 | at least 4 |
| \(11\cdot4+2+1\) | 253 | 32 | 58 | 64 | at least 5 |

For each tight 4-part P, the three vertices of smallest residual degree have total F-degree at most three. At least \(r-4\ge6\) of the other \(r-1\) four-parts are clean. Their fourth vertices are pairwise adjacent, or else two of them together with the selected triple form an independent 5-set. Thus H contains either an independent 5-set or a K6, contradicting \(\alpha(H)\le4\) and \(\omega(H)\le5\).

Therefore no exact-129 Type-I non-target color can occur on a valid Q32 core:
\[
\boxed{\text{exact-129 Type-I color}\ \Longrightarrow\
\text{one of three forbidden H-partitions}\ \Longrightarrow\ \bot.}
\]

This conclusion is conditional on the Type-I factorization for every exact color and the additional omega(H)<=5 cap. Neither dependency follows from the actual EG617 balanced-coloring/Q32 contract. Therefore this section does **not** exclude m=8 or m=9; both full-support branches remain OPEN. It does not use the 37-unit edge-gap ledger, near-Turan second-extremal theorem, pivot-pair composition, or m-specific reserve inequalities.

The independent candidate verifier now reconstructs the induced partition from each exact color's twelve source K5 factors, selects Hall matchings by augmenting paths, computes F, finds a tight 4-part, and returns an explicit independent 5-set or a clique of size at least six. Its self-test exercises all three partition shapes.

**Status: PROVED_CONDITIONAL** on the registered Type-I factorization and Q32 core contract. The full SMT model was not run; it is no longer needed for this terminal.
