# R12 independent-triple theorem through total excess five

Status: **PROVED ANALYTIC** under the 35-core graph contract alpha(H)<=3, omega(H)<=11, delta(H)>=12.

This closes the final total-excess-five equality left by the d3 common-missing-triangle transport. Together with the minimum-anchor, h<=3, and h<=4 theorems, it proves the same K>=8 obstruction for every independent triple whose total degree excess above12 is at most five.

## Theorem

Let H have 35 vertices, alpha(H)<=3, omega(H)<=11, and delta(H)>=12. If H contains an independent triple a_1,a_2,a_3 with

h = sum_i (d_H(a_i)-12) <= 5,

then K=sum_v(d_H(v)-12)=2e(H)-420 >= 8.

## Proof

The cases h<=4 are proved in the registered minimum-anchor, h<=3, and h<=4 theorems. Because K is even, suppose for contradiction K<=6 and consider the only new case h=5.

If any anchor has degree12, the minimum-anchor theorem applies. Otherwise all three anchor excesses are positive integers summing to five, so their degree pattern is either (15,13,13) or (14,14,13). The proof below is uniform in these two patterns.

### 1. Connector and exclusive-block accounting

Partition the other 32 vertices into exclusive blocks X_i (adjacent to exactly anchor a_i among the anchors) and a connector set C (adjacent to at least two anchors). Let c=|C| and t be the number of triple-connectors. Write x_i=|X_i|.

Each X_i is a clique, because two nonadjacent vertices of X_i together with the other two anchors would form an independent 4-set. Therefore x_i<=10 and x_1+x_2+x_3=32-c.

The anchor-degree sum is 36+h=41. Counting anchor incidences from the other vertices gives

41=(32-c)+2(c-t)+3t=32+c+t,

so c+t=9 and 5<=c<=9.

A pair-connector has at least 11-c exclusive neighbours, and a triple-connector at least 10-c. Thus the number E_XC of connector-to-exclusive edges satisfies

E_XC >= (c-t)(11-c)+t(10-c)=12c-c^2-9.

Let E_cross count edges between distinct exclusive blocks. Summing degrees over the exclusive vertices gives

2 E_cross + E_XC = sum_i x_i(12-x_i)+K_X,

where K_X is their total degree excess. The anchors consume five units of the total budget K<=6, so K_X<=1. By concavity of x(12-x), the maximum values for the possible sums x_1+x_2+x_3=32-c are:

| c | sum x_i | max sum x_i(12-x_i) | lower bound E_XC | upper bound E_cross |
|---:|---:|---:|---:|---:|
| 5 | 27 | 81 | 26 | 28 |
| 6 | 26 | 86 | 27 | 30 |
| 7 | 25 | 91 | 26 | 33 |
| 8 | 24 | 96 | 23 | 37 |
| 9 | 23 | 99 | 18 | 41 |

### 2. Clique-cap corrected transversal lower bound

Let Z_i be the degree-12 vertices in X_i and sort their sizes as z_1>=z_2>=z_3. Since at most one vertex outside the anchors has positive excess,

z_1+z_2+z_3 >= 31-c.

As z_1<=10, we have z_2+z_3>=21-c>=12. The sets Z_i are cliques, and omega(H)<=11, so at least one cross-pair between Z_2 and Z_3 is a nonedge. Fix such a pair b,d.

Assume no independent transversal exists across Z_1,Z_2,Z_3. Every a in Z_1 must then be adjacent to b or d. Since at most z_2*z_3-1 edges run between Z_2 and Z_3, we obtain

E_cross >= z_2*z_3 - 1 + z_1.                            (1)

For c=5,6,7,8, the sum s=z_2+z_3 is at least 16,15,14,13 respectively. Using z_2<=z_1<=10, the minimum right-hand side of (1) is respectively 69,59,49,39. These exceed the corresponding upper bounds 28,30,33,37 in the table. Thus c<=8 is impossible.

### 3. The c=9 endpoint

Here x_1+x_2+x_3=23, z_1+z_2+z_3>=22, and z_i<=10. The table gives E_cross<=41. We show that (1) always exceeds the applicable upper bound.

- If z_3=2, then z=(10,10,2). The one allowed positive-excess vertex must be in the third block, so x=(10,10,3). The upper bound improves to 25, while (1) gives 29.
- If z_3=3, the possible sorted z triples are (10,10,3) and (10,9,3). The corresponding upper bounds are at most 25 and 31, while (1) is at least 39 and 36.
- If z_3=4, the possible sorted z triples are (10,9,4), (10,8,4), and (9,9,4). Their maximum corresponding upper bounds are 31,35,36, while (1) is at least 45,41,44.
- If z_3>=5, the constraints z_1+z_2+z_3>=22 and z_1<=10 imply z_2+z_3>=12. If z_3=5, the minimum of (1) is44, attained at z=(10,7,5); if z_3>=6, it is at least45. Both exceed41.

Therefore the assumption of no independent transversal is impossible when c=9 as well.

### 4. Finish

An independent transversal exists, giving three pairwise nonadjacent degree-12 vertices. The registered three-anchor closure then forces K>=8, contradicting K<=6. This proves the h=5 case and hence the theorem. QED.

## Backend consequence

The common-S independent-triple transport identity gives h_y<=a-3 in every owner-repivot core when the common missing triple is independent in the target graph. Since the high-backend ceiling is a<=8 for d=3, the present theorem closes the entire independent-triple branch through a=8. The previous a=8 patterns (1,1,3) and (1,2,2) are now both excluded by the same graph-theoretic theorem.

## Independent finite check

For h=5, the c=5..9 connector count bounds and the c=9 z_3 subcases were checked by exact integer enumeration. Across the two possible anchor degree patterns, no feasible connector profile survives the clique-cap corrected transversal inequality.
