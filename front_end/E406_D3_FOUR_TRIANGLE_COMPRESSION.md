# E406 d=3: four-triangle support compression

Status: `PROVED` under the d=3 q31 platform contract. E406 remains `OPEN`.

This note continues `E406_D3_PURE_SUPPORT_CLASSES.md` and `E406_NEAR284_ROW_UNION_LEMMAS.md`.

Let y be a q31 pivot in one of the seven d=3 q31 platforms. Let B be the 10-point shell clique side and D the 3-point missing-neighbour side. Let n be the number of active degree-3 vertices in B. Thus

- Type A: `n=10-r0`, `r0 in {0,1,2,3}`, shell decoration `G=3r0`;
- Type B: `n=10-r0`, `r0 in {0,1,2}`, shell decoration `G=3r0+1`.

Every active b in B has a 3-point core support U_b. By the q31 support rigidity theorem, each support is one of:

1. a P3 plateau support, with `eps_C(U)=0`, `e_F(D,U)=0`;
2. a pure K3 support giving a q30 child, with `eps_C(U)=0`, `e_F(D,U)=0`;
3. a defective K3 plateau support, with
   `eps_C(U)+e_F(D,U)=1`.

At least one pure K3 support exists: the reverse edge of the q30 -> q31 final rise.

## 1. Distinct support classes are disjoint

Fix two distinct supports U,V.

If U is pure K3, `E406_D3_PURE_SUPPORT_CLASSES.md` already proves U and V are disjoint.

Suppose U is a defective K3 plateau. Repivoting its shell vertex preserves q=31. The three imported U-vertices have new row weights `(11,10,10)`: their old core degrees are 12 plus total support excess, each loses two internal K3 neighbours, and the total `eps_C(U)+e_F(D,U)` equals1.

If `r=|U intersect V|=2`, the V-shell vertex has new core row size1 and is missing-adjacent to at least one imported U-vertex of weight at most11, violating PAIR-13.

If r=1, the V-shell row has size2 and is missing-adjacent to two imported U-vertices. PAIR-13 would force both imported weights to be11, but only one such vertex exists. Contradiction.

Hence a defective K3 class has no proper overlap with any other support.

Now suppose U is a P3 plateau. After its q31-preserving repivot, the imported P3 vertices have weights `(11,10,11)`.

- r=2 is impossible by PAIR-13 (`1+11<13`).
- if r=1, PAIR-13 forces the shared vertex to be the middle of the P3, so the two missing imported vertices are the weight-11 endpoints.

But V is itself P3 or K3 and is connected. At least one vertex of `V\U` is adjacent in the old core to that shared middle vertex. When U is removed, that retained support vertex loses at least one core neighbour. The total compensation available to all retained vertices of V is

`eps_C(V)+e_F(D,V) <=1`.

For a P3/pure-K3 support it is0, immediate contradiction; for a defective K3 support both outside vertices were adjacent to the shared K3 vertex, producing at least two lost incidences but only one unit of compensation. Contradiction.

Therefore every two distinct support classes are disjoint.

## 2. Cross edges between distinct support classes

For a support U define its defect

`delta(U)=eps_C(U)+e_F(D,U)`.

Thus delta is0 for P3 and pure K3 classes, and1 for defective K3 classes.

Repivot at U. Let V be a disjoint retained support. Each v in V changes core degree by

`-d_C(v,U) + d_F(v,D)`.

The new core has minimum degree at least12, so summing over V gives

`e_C(U,V) <= eps_C(V)+e_F(D,V)=delta(V)`.

Repeating with U,V interchanged yields

`e_C(U,V) <= min(delta(U),delta(V))`.

Consequently:

- every zero-defect class is anticomplete to every other class;
- two defective K3 classes have at most one cross edge.

## 3. Class-count upper bound from alpha(C)<=4

There cannot be two distinct P3 classes: two P3 classes are anticomplete and already supply an independent4-set from their endpoints; the mandatory pure K3 class is anticomplete to both and would give an independent5-set.

If one P3 class exists, there are at most two K3 classes in total: three K3 classes always have an independent transversal of size3 (one pure class is anticomplete to the others and the remaining pair has at most one cross edge), which together with the two independent P3 endpoints gives an independent5-set.

Hence a configuration containing a P3 has at most three support classes.

If there is no P3, all classes are K3s. There is at least one pure K3 class P, anticomplete to every other class. If there were at least five K3 classes total, choose four classes other than P. Between every pair of those four classes there is at most one cross edge. Among the `3^4=81` choices of one vertex from each class, any fixed cross edge forbids exactly `3^2=9` choices, and there are at most six class pairs. Thus at most54 choices are forbidden; an independent transversal of size4 exists. Together with any vertex of P this gives an independent5-set in C, impossible.

Therefore the total number c of support classes always satisfies

`c<=4`.   (CLASS-UPPER)

## 4. Global excess forces c=4 and excludes P3 classes

For a support class U of multiplicity m, the contribution of its three vertices to the ambient E406 excess above degree13 is exactly

`3(m-1)+delta(U)`.

Indeed each support vertex has core degree `12+eps`, occurs in m B-rows, and has its D-shell incidences counted by `e_F(D,U)`.

Let d be the number of defective K3 classes. Since all classes are disjoint and their multiplicities sum to n, the support-class vertices contribute

`3n-3c+d`

total ambient excess.

The total ambient excess carried by all 47 core vertices is

`19-G`.

### Type A

Here `G=3r0`, `n=10-r0`, so

`19-G = 3n-11`.

Therefore

`3n-3c+d <= 3n-11`,

hence

`3c-d >=11`.   (A)

### Type B

Here `G=3r0+1`, so

`19-G = 3n-12`.

Thus

`3c-d >=12`.   (B)

Both inequalities imply `c>=4`. Together with CLASS-UPPER:

`c=4`.

A P3 class would force `c<=3`, so **no P3 class exists**.

Thus all four classes are K3s.

In Type B, (B) forces `d=0`: all four are pure K3 classes.

In Type A, (A) gives `d<=1`: at most one class is defective.

Since every pair of classes then includes a zero-defect class unless both are defective, and there is at most one defective class, all four K3 classes are pairwise anticomplete.

Therefore every surviving d=3 q31 platform contains exactly

`T1,T2,T3,T4`,

four pairwise disjoint, pairwise anticomplete K3s in the 284-edge core.

## 5. Exact 35-point remainder ledger

Let T be the union of the four triangles and let H be the remaining35 core vertices.

Let eta be the total internal core excess on the unique possible defective triangle (`eta=0` or1). Then

- `e_C(T)=12`;
- the T-H incidence count is `120+eta`;
- `e(H)=152-eta`;
- the total H-side core excess is `4-eta`.

Every H-vertex is complete to at least one of the four triangles: otherwise choose one missed vertex from each pairwise anticomplete triangle and obtain an independent5-set together with the H-vertex.

Thus the d=3 E406 problem has been reduced to a four-row-triangle core contract with a **35-point remainder of only 151 or152 edges and total excess at most4**.

This is strictly tighter than the historical S30 contract (`e(H)=153`, excess6).

## 6. Remaining task

To close d=3 it is now sufficient to exclude this four-antocomplete-triangle / 35-point remainder contract. Historical S30 row-capacity and pair-overlap lemmas may be reused only after checking their hypotheses against the stronger present ledger; no historical S31 CLOSED label is imported.