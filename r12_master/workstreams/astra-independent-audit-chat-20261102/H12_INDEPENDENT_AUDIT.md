# Independent audit of the h12 terminal and the 48-point floor

Frozen Astra integration snapshot: `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`.

Audit branch: `workstream/r12-astra-independent-audit-20261102`.

## Result

No mathematical counterexample or load-bearing gap was found in the reviewed h12 chain. The proof uses a dedicated order-48 argument; it does not transport the order-47 edge floor.

## 1. The order-48 minimum-degree gate

For (J\in R(4,48)):

- Degree at most10 leaves at least37 nonneighbors, inducing a forbidden (R(3,37)).
- If a vertex has degree11, its 36-core lies in (R(3,36)), hence has at least234 edges. The 11-shell cannot be a clique because the pivot would complete a (K_{12}). Choose two target-nonadjacent shell points (a,b). Each has at most3 neighbors in the 36-core by the 37-point cap. Thus their common antineighborhood has at least (36-6=30) vertices. It has independence number at most2, so any 24 of its vertices would be in (R(2,24)), impossible.

Therefore (delta(J)\ge12). This is independent of any edge-count assumption on (J).

## 2. Charge identities and the q=20 shell lemma

For a degree-12 pivot (p), shell (A=N(p)), core (C=J-N[p]), let (M=\overline{J[A]}), (g_a=d_J(a)-12\ge0), and (t_a=d_M(a)+g_a). Since
[
d_C(a)=d_J(a)-1-d_{J[A]}(a)=d_M(a)+g_a=t_a,
]
the weights are exactly the actual core degrees of shell vertices.

For every (S\subseteq A), direct double-counting gives
[
q=e(M)+\sum_Ag_a
=t(S)-e_M(S)+e_M(A\setminus S)+G_{A\setminus S}.
]
Thus (q\ge t(S)-e_M(S)).

The three shell hypotheses used by the q20 lemma are valid:
- (e(M)\ge11), since (e(J[N[p]])=78-e(M)\le D(13)=67).
- (alpha(M)\le10), since an independent 11-set in (M), together with pivot (p), would give a (K_{12}).
- For every M-edge (ab), (t_a+t_b\ge12): otherwise the common antineighborhood of (a,b) in the core has at least24 vertices and independence number at most2, contradicting (R(2,24)=\varnothing).
- For every M-triangle (T), (t(T)\ge24): the core vertices anticomplete to all of (T) form a clique (otherwise they and (T) give an independent 5-set), so there are at most11 of them in the 35-core.

If M contains a triangle, (q\ge t(T)-3\ge21). If M is triangle-free, (alpha(M)\le10) and (e(M)\ge11) force a 2-matching: a graph with matching number at most1 is a star or a triangle plus isolates, both excluded. A 3-matching would give (q\ge36-9=27), so the matching number is exactly2.

Choose a maximum 2-matching with four endpoints (S). Mantel on the triangle-free four-vertex graph gives (e_M(S)\le4), hence (q\ge24-4=20). At equality:
[
t(S)=24,\qquad M[S]=K_{2,2},\qquad
e(M[A\setminus S])=G_{A\setminus S}=0.
]
So the eight exterior shell vertices are independent and undecorated.

Every exterior vertex can attach only to one side of this (K_{2,2}), by triangle-freeness. Attachments on both sides would give a 3-matching by taking one attachment edge on each side and the opposite unused K2,2 edge. Therefore all attachments meet one fixed two-vertex side (X). The other side (Y) has no exterior attachments.

At least one exterior attachment exists because (e(M)\ge11) while (M[S]) has only four edges. Let the two hub weights be (a). The two (Y)-weights are at least2, and each C4 edge has endpoint weight sum at least12. Since the four edge inequalities sum to (2t(S)=48), each is equality; opposite vertices have equal weights, so (a\le10). An exterior point adjacent to just one hub would have weight1 and force (a\ge11), impossible. Hence every active exterior point attaches to both hubs. Its weight is2, forcing (a\ge10), hence (a=10). The Y-weights are2 and their decorations are zero. If (r) is the total number of degree-2 low vertices (the two Y vertices plus active exterior points), then (e(M)=2r\ge11), so (6\le r\le10). The equality form is exactly
[
M=K_{2,r}\sqcup(10-r)K_1,quad
t(\text{hub})=10,quad t(\text{low})=2,quad
g_{\text{hub}}=10-r.
]

## 3. Independent finite recheck of the equality case

A standalone checker enumerates:
- all (4^8=65,536) attachment patterns of the eight exterior vertices to the two hubs;
- all 7,006,595 decoration allocations compatible with (q=20) and the edge floor;
- all four C4 edge inequalities and all exterior-edge inequalities.

It recovers exactly163 feasible labelled configurations, all of the claimed normal form. Their counts by (r) are (70,56,28,8,1) for (r=6,7,8,9,10), respectively. See `RECHECK_H12_Q20.py` and `RECHECK_H12_Q20.json`.

This is a finite check after the analytic C4 and one-side-attachment reductions; those reductions are justified in Section2 above and are not delegated to the script.

## 4. Inserted-center contradiction

For a leaf (y) in (K_{2,r}), (d_J(y)=12), and its core row has two vertices. Repivoting at (y) removes that row from the old core and inserts the two hubs. Each old hub has exactly10 neighbors in the old core, because its weight (t=d_C) is10. The two hubs are target-adjacent (there is no hub-hub edge in M). Therefore each has at most (10+1=11) neighbors in the new core. This contradicts the minimum-degree-12 theorem for the relevant new core.

The level of the new core matters:
- In the generic (R(4,48)\Rightarrow e\ge310) proof, the new core has35 vertices and lies in (R(3,35)), where the independently proved minimum-degree-12 lemma applies.
- In the T61 h12 contradiction, the new core has48 vertices and lies in (R(4,48)), where the order-48 minimum-degree gate from Section1 applies.

No order-47 floor is transferred to order48.

## 5. The 310-edge floor and the T61 h12 branch

For (J\in R(4,48)), if (delta(J)\ge13), then (e(J)\ge312). Otherwise choose a degree-12 pivot. Its35-core lies in (R(3,35)), has minimum degree12, and has at least211 edges by the AES equality exclusion. The shell has (e(M)\ge11), pair-row charge at least12 on M-edges, and triangle charge at least24 on M-triangles. Thus (q\ge20). Equality is excluded by the inserted-center contradiction in the 35-core. Therefore (q\ge21) and
[
e(J)=78+q+e(C)\ge78+21+211=310.
]

For a genuine T61 graph with (delta(F)=12), every degree-12 pivot has a 48-core in (R(4,48)), so (e(C)\ge310). The shell charge is at least20. Consequently (E\ge78+20+310=408). At (E\le408), equality is forced and the shell is q20. Repivoting at a leaf produces another48-core in (R(4,48)), whose minimum degree must be12, while an inserted hub has degree at most11. Contradiction.

## 6. Scope and remaining certification

The h12 chain is analytically coherent under the stated lower-order inputs. The finite equality enumeration passed. The proof still depends on the separate M1–M5 lower-order theorem and the AES application; this audit reread their exact statements and arithmetic but is not a Lean proof. It also does not establish a clean-room build of the complete K145 proof. No frozen integration files were changed.
