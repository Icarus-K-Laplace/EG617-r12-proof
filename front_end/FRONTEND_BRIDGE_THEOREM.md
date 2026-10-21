# EG617-r12 — Line A front-end bridge

Date: 2026-10-21. Project conclusion: **OPEN**.

The target is an induced member of R(4,49), with no prescribed edge layer. Nothing in this package studies E332 or E333–E340. The new reduction does not use a 49-vertex edge lower bound, a 49-vertex emptiness theorem, or a 325-edge assumption.

## F0. Definitions — PROVED

For n=ak+b, 0<=b<a, put p_a(n)=a*binom(k,2)+kb, and D(n)=binom(n,2)-11*p_12(n). R(a,n) denotes simple n-vertex graphs with alpha<=a, omega<=11, and e(J[W])<=D(|W|) for every W.

A hypothetical balanced colouring means every 13-set contains every colour; it does not mean colour edge counts are equal. Choose a least-edge colour graph G. Then |G|=145, e(G)=m<=870, alpha(G)<=12, omega(G)<=12. Every induced target subgraph has the D caps: each of the other eleven colour graphs has independence number at most12 and therefore at least p_12(n) edges on an n-set.

For a target K12 Q, an outside vertex has at most one target neighbour in Q, since e(Q union {v})<=D(13)=67. Thus pairwise disjoint target K12 blocks have matching cross-edges. All blocks below are genuine target cliques.

## F1. Matching-transversal rigidity — PROVED

Let k>=2 parts each have at least k-1 vertices, and let edges between each pair of parts form a matching. If no independent transversal exists, every part has exactly k-1 vertices and every pair matching is perfect. In fact the cross graph consists of k-1 disjoint K_k's.

If some part has at least k vertices, put it last and greedily choose. If a vertex in one (now size k-1) part misses another part entirely, preselect it, choose the other k-2 parts, and put the untouched part last. This proves perfect matching. Fix a vertex in the first part and remove its one neighbour from every other part. The remaining parts have no transversal; applying the already proved perfect-matching assertion to them shows that all the removed vertices are matched to one another. They form a K_k with the fixed vertex. Vary the fixed vertex to partition the parts. The k=2 case is immediate.

## F2. Equality rotation saturates ALL twelve cross slots — PROVED

Suppose k target K12 blocks coexist with an independent set I outside them of size s+1, where s=13-k. Suppose that for every s-subset S of I, its avoiding lists in the k blocks have no independent transversal. They then have size exactly k-1 by F1.

Each S sends exactly s edges with distinct endpoints into each block. Vary S: every vertex of I has a target neighbour in every block, and these s+1 neighbours are distinct (s>=2 in the applications). Every block vertex avoids at least one S: omit its unique neighbour in I, if it has one; if it has none, choose any S. In that avoiding list the vertex must have a matched neighbour in every other block by F1. Thus the original matching between EVERY pair of blocks is perfect on ALL twelve vertices.

Consequently x=12*binom(k,2) and y>=k(s+1). This conclusion concerns actual edges. It is stronger than taking the union of a few numerical lower bounds on x.

## F3. Eight genuine blocks give alpha(Y)<=4 — PROVED

Eight blocks leave49 vertices Y. If Y has independent S of size5, alpha(G)<=12 prohibits its extension by a transversal of the eight blocks. F1 gives x>=7*28=196 and y>=40. Exact accounting gives e(Y)<=870-528-196-40=106.

But p_5(49)=216, so Y has an independent6-set I. Apply F2 to all five-subsets of I: x=12*28=336 and y>=48. Hence

    m >=528+336+48=912>870,

a contradiction.

## F4. Seven genuine blocks give alpha(Y)<=5 — PROVED

Seven blocks leave61 vertices. Independent6 would, by F1, give x>=6*21=126 and y>=42, hence e(Y)<=240. Since p_6(61)=280, independent7 then exists. F2 now gives x=12*21=252, y>=49, hence e(Y)<=107. Yet alpha(Y)<=12 implies e(Y)>=p_12(61)=125. Contradiction.

If the seven-block packing is maximal, omega(Y)<=11, so this is a legitimate R(5,61) with e(Y)+x+y+(870-m)=408. It is NOT automatically the 406-edge, minimum-degree13 parent of S31.

## F5. Eight-block packings are maximal; the 49 contract — PROVED

There cannot be ten disjoint blocks: an independent3 in their25-vertex residual would, by F1, require405 cross edges, while at most210 edges remain after the ten internal cliques. Hence the residual has alpha<=2. Its nonneighbourhoods are cliques of size at most12, so delta>=12 and e>=150>D(25)=146.

There cannot be nine: their37-residual contains no K12 by the preceding argument. Independent4 would require288 cross edges, whereas x<=870-594=276. Thus it belongs to R(3,37), which is empty by seed L3 in ASSUMPTION_LEDGER.md.

Therefore eight genuine blocks always leave F in R(4,49), by F3 and maximality. The exact ledger is

    e(F)=m-528-x-y.

For ANY such F, degrees<=11 are impossible by R(3,37). Degree12 would give a36-core with at least234 edges. Its12-shell contains a nonedge uv; their core-neighbourhood union has size>=13 by R(2,24). The induced38-set comprising that core and u,v would have at least247 edges>D(38)=241. Thus delta(F)>=13. D(49)=340 forces delta(F)=13 and at least686-2e(F)>=6 degree13 vertices.

Every degree13 pivot has an actual13-shell and35-core H in R(3,35). With M the shell complement, g_a=d_F(a)-13>=0, t_a=|N_H(a)|=d_M(a)+g_a, q=e(M)+sum g, exact counting gives e(F)=91+q+e(H). The14-point cap gives e(M)>=22. For any shell subset S,

    q=t(S)-e(M[S])+e(M[A\S])+sum_(A\S)g.

An M-edge, triangle and K4 have core-row unions of size at least12,24,35 respectively, by the R(2,24) exclusion, omega(H)<=11, and alpha(F)<=4. Thus all corresponding weighted inequalities and the exact repivot identities are inherited. No binary-g assumption is made. Delta(F)<=14 and a complement-core minimum degree20 are not part of this derived contract.

## F6. A different route already suffices: an anchor and seven blocks — PROVED

Let v be a minimum-degree vertex of G, d=d_G(v), A=N_G(v), U=V(G)\N_G[v]. Average degree is at most12. If d=12, G is12-regular; Brooks' theorem componentwise would colour it with12 vertex colours, since no component is K13 and the maximum degree is12. That would give alpha(G)>=ceil(145/12)=13. Thus d<=11.

Choose an inclusion-maximal packing of j genuine target K12's in U; its residual is R. Greedy representatives show alpha(R)<=11-j. Also j<=11. Maximality gives omega(R)<=11. Therefore

    R belongs to R(11-j,144-d-12j).

Put sigma=870-m, z=binom(d,2)-e(G[A]), g=sum_(a in A)(d_G(a)-d), x_j=sum of edges between the j blocks, and y_j=edges from those blocks to R. Then

    e_G(A,U)=2z+g,
    e(G[N[v]])=binom(d+1,2)-z,
    e(R)=870-binom(d+1,2)-66j-(sigma+z+g+x_j+y_j).    (ANCHOR)

This partitions every edge exactly once. All charges are nonnegative.

At d=11,j=7, R has49 vertices and alpha<=4; all the F5 contracts follow. N[v] need NOT be a clique. Seven anchored blocks, not eight unanchored blocks, already suffice for the target.

## F7. Contextual no-extraction reduction — PROVED

Assume for contradiction to the desired BRIDGE that this fixed G has NO induced subgraph in R(4,49). Let C_G(a,n) consist only of the induced subgraphs of this fixed G which have alpha<=a and omega<=11. This family is closed under every induced-subgraph operation used below, and C_G(4,n) is empty for n>=49 under this temporary assumption.

Apply the explicit finite recurrence with only these inputs:

    maximum orders 11,23,36,48 for a=1,2,3,4;
    floors (2,23):131; (3,35):210; (3,36):234;
           (4,47):284; (4,48):308.

There is no R449 edge seed, P562 seed, E325 assumption, or invocation of S27/S30/S31 in this calculation.

The exact certificate covers1752(a,n) nodes and all144(d,j) stopping comparisons. Two independent integer transcriptions agree on EVERY node. After maximality and (ANCHOR), the ONLY nonexcluded outer stop is

    d=11, j=6, R in C_G(5,61), 397<=e(R)<=408.       (T61)

The no-extraction hypothesis implies delta(R)>=12; the408 budget gives delta(R)<=13. The full two-row terminal interface is

|actual minimum degree h|core order|core floor|shell q floor|allowed edge range|
|---:|---:|---:|---:|---:|
|12|48|308|20|406..408|
|13|47|284|22|397..408|

At h12 the exact identity is E=78+q+e(C48), so the total slack over406 is at most2. At h13 it is E=91+q+e(C47). Decorations are nonnegative integers measured from the actual minimum degree.

## F8. The single terminal obstruction — OPEN

It remains to exclude the precisely specified embedded class T61, or prove it contains a legal induced49-set:

* G is the least-edge colour of a balanced K145 colouring, m<=870, with no induced R(4,49).
* v has minimum degree11 in G. In its nonneighbourhood, an inclusion-maximal packing has exactly six genuine target K12 blocks.
* The remaining induced R has61 vertices, alpha<=5, omega<=11, all inherited D caps, and delta(R)=12 or13 with the two exact rows of F7.
* With A=N(v), z=55-e(G[A]), g=sum_A(d_G(a)-11), the actual embedding satisfies

      E+sigma+z+g+x_6+y_6=408,
      e_G(A,U)=2z+g,
      0<=sigma+z+g+x_6+y_6<=11.

* The original eleven other colours still complete this SAME graph.

Thus the proved dichotomy is:

    Balanced K145 / least-edge colour G
      => an induced F in R(4,49), OR an embedded T61 obstruction.

T61 emptiness remains OPEN.

## F9. First unproved implications and exact S31/S27 interfaces

**OPEN:** converting T61 into seven genuine unanchored blocks. The natural candidate N[v] is a K12 iff z=0; the ledger only gives z<=11.

**RETRACTED:** treating the scalar408 outer budget as e(R)=406 or as an actual removed-clique edge count.

**PROVED:** if E=406 and delta(R)=13, the audited S31 theorem applies to the SAME induced R and supplies a degree13 pivot with q<=30, hence a47-core with e>=285. It neither changes E nor constructs a K12.

**CONDITIONAL:** S27 excludes a47-core with e=288 AND minimum degree11. Merely q=27 in a406-edge parent establishes e=288, not the required minimum degree11.

**OPEN:** every T61 state reduces to the currently studied S30 macro contract. In particular E!=406, h12, or q<30 are not assigned to S30 without an interface proof.