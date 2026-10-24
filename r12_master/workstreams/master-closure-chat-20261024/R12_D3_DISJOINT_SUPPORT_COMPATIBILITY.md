# R12 d3 disjoint-support compatibility through q=38

Status: **PROVED ANALYTIC** under the legal R(4,49) backend contract, the all-pivot 35-core minimum-degree-12 contract, and lexicographic maximum-q pivot choice.

This theorem extends the q<=32 multi-S extraction interface to every disjoint-support subsystem up to the backend ceiling q<=38. It does not claim that every d3 owner system is itself a matching, nor does it close the repeated-common-S shallow-loss cases.

## Theorem

Fix a maximum-q degree-13 pivot p in a legal 49-vertex residual F. Let A be its 13-vertex shell, H its 35-vertex core, and M the shell missing graph. Let Y be any family of regular shell vertices with

- S_y=N_M(y), |S_y|=3;
- D_y=N_H(y), |D_y|=3;
- q<=38.

Let D_{y_1},...,D_{y_m} be pairwise-disjoint support blocks from this family.

Then:

1. Every pair of owners in Y is target-adjacent, and |Y|<=10.
2. For any i!=j with D_{y_i} disjoint from D_{y_j}, the missing triples satisfy |S_{y_i} intersect S_{y_j}|>=2.
3. If these two missing triples are distinct, then
   [
   e_H(D_{y_i},D_{y_j}) le q-36.
   ]
   In particular, distinct missing triples cannot occur across disjoint supports when q<=35.
4. A pairwise-disjoint support family in which all S_{y_i} are distinct has size at most:
   - 3 if q=36 or q=37;
   - 6 if q=38.
5. Consequently, in any pairwise-disjoint support family, the number of distinct missing-triple types is at most 1 for q<=35, at most 3 for q in {36,37}, and at most 6 for q=38.

## Proof

### 1. Owner adjacency

If two regular shell owners y,z were target-nonadjacent, the exact nonadjacent zero-gap theorem would force S_y union S_z=A. But |S_y union S_z|<=6<13. Hence Y is a target clique. Since p is adjacent to every vertex of A, {p} union Y is a target clique, so |Y|<=10 under omega(F)<=11.

### 2. Pairwise missing-set intersection

Fix i!=j with D_i intersect D_j empty. Put

- o=|S_{y_i} intersect S_{y_j}|;
- h=|D_{y_i} intersect D_{y_j}|=0.

The exact third-viewpoint formula gives the support size of y_j after repivoting at y_i:

`d_{y_j}^{y_i}=6-o-h=6-o`.

The exact exchange formula in that view is

`q_{y_j}^{y_i}=d_{y_j}^{y_i}(13-d_{y_j}^{y_i})+P_{y_j}^{y_i}`,

where every term in P is nonnegative. Since p is maximum-q, q_{y_j}^{y_i}<=q<=38.

If o<=1, then d_{y_j}^{y_i} is 5 or 6, and the base term is respectively 40 or 42, both greater than38. Therefore o>=2.

### 3. Distinct missing triples force low cross-density

If S_{y_i} and S_{y_j} are distinct triples, o=2, so d_{y_j}^{y_i}=4 and the base exchange term is 4(13-4)=36. Thus

`P_{y_j}^{y_i}<=q-36`.

In the repivoted view, the new shell support S_{y_j}^{y_i} contains D_{y_i}, and the new core support D_{y_j}^{y_i} contains D_{y_j}. Hence the nonnegative cross-edge term `e_{F_{y_i}}(S_{y_j}^{y_i},D_{y_j}^{y_i})` contains every edge between D_{y_i} and D_{y_j}. It follows that

`e_H(D_{y_i},D_{y_j})<=q-36`.

If q<=35 this inequality is impossible for distinct triples because its left side is nonnegative. Thus all supports in a pairwise-disjoint family share the same missing triple when q<=35.

For q=36,37,38 the cross-edge upper bounds are respectively 0,1,2.

### 4. Transversal capacity

Suppose all m support blocks are pairwise disjoint and their missing triples are pairwise distinct. Every block pair has at most c target cross-edges, where c=q-36.

The Global Block-Transversal Theorem applies because alpha(H)<=3:

`C(m,2)-floor(m^2/3) <= (c/9) C(m,2)`.

For c=0, any transversal is independent, so m<=3. For c=1 the theorem's exact integer inequality fails for every m>=4, so m<=3. For c=2 it fails for every m>=7, so m<=6. These are exactly the claimed bounds for q=36,37,38.

Finally, choose one block for each distinct missing-triple type in an arbitrary pairwise-disjoint support family. The selected blocks remain pairwise disjoint and have pairwise distinct missing triples, so the same capacity bounds the number of types. This proves item 5.

## Exact scope and open boundary

This theorem concerns **pairwise-disjoint core supports**. It does not imply that all supports in Y are disjoint, and it does not bound the multiplicity of support blocks sharing one missing triple. In particular:

- q<=35: every disjoint-support subsystem is common-S, but its repeated-common-S shallow-loss/equality contract still must be closed;
- q=36 or37: a disjoint-support subsystem has at most three distinct missing-triple types, with cross-edge count at most1 between different types;
- q=38: it has at most six distinct missing-triple types, with cross-edge count at most2 between different types.

The remaining universal forcing theorem must still handle intersecting supports, lower owner counts, fully decorated rows, and the unresolved common-S shallow-loss windows. No E335--E340 or original EG617 closure is claimed.
