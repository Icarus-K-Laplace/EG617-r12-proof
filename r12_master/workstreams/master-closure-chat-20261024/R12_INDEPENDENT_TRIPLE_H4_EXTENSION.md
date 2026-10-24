# R12 independent-triple theorem through total excess four

Status: **PROVED ANALYTIC** under the graph contract H on 35 vertices with alpha(H)<=3, omega(H)<=11, and delta(H)>=12.

This extends the registered independent-triple obstruction from total anchor excess at most three to at most four. The new case is the only pattern (14,13,13); the proof reduces it to an exact three-part transversal count plus the clique-cap correction.

## Theorem

Let H be a graph on 35 vertices with

- alpha(H)<=3;
- omega(H)<=11;
- delta(H)>=12.

Let a_1,a_2,a_3 be pairwise nonadjacent vertices and define

h = sum_i (d_H(a_i)-12),
K = sum_{v in V(H)} (d_H(v)-12) = 2e(H)-420.

If h<=4, then K>=8, equivalently e(H)>=214.

## Proof

Because K is even, it is enough to rule out K<=6. If one anchor has degree12, the registered GLOBAL_INDEPENDENT_TRIPLE_MIN_ANCHOR_THEOREM applies. If all three anchors have positive excess and h<=3, GLOBAL_INDEPENDENT_TRIPLE_H3_THEOREM applies. The only new case is therefore

(d_H(a_1),d_H(a_2),d_H(a_3)) = (14,13,13),

with h=4. Assume K<=6, so the total excess outside the three anchors is at most2.

### 1. Anchor-signature partition

Partition the other 32 vertices into:

- exclusive blocks X_i, adjacent to a_i and to neither of the other two anchors;
- a connector set C of vertices adjacent to at least two anchors.

Let c=|C| and let t be the number of triple-connectors adjacent to all three anchors. Each exclusive block X_i is a clique: two nonadjacent vertices in X_i, together with the other two anchors, would be an independent 4-set. Thus x_i=|X_i|<=10.

Counting anchor incidences gives

40 = (32-c)+2(c-t)+3t = 32+c+t,

so c+t=8 and 4<=c<=8. Also x_1+x_2+x_3=32-c.

Every pair-connector has at least 11-c neighbours in the exclusive blocks, and every triple-connector at least 10-c, because it has at most c-1 connector neighbours and total degree at least12. Hence

E_XC >= (c-t)(11-c)+t(10-c)=12c-c^2-8,

where E_XC counts edges between connectors and exclusive blocks.

Let E_cross count edges between distinct exclusive blocks and let K_X be the excess sum over all exclusive vertices. The exact degree sum over X_1 union X_2 union X_3 is

2 E_cross + E_XC = sum_i x_i(12-x_i)+K_X.

Since K_X<=2,

E_cross <= [sum_i x_i(12-x_i)+2-(12c-c^2-8)]/2.

For fixed sum x_1+x_2+x_3=32-c and x_i<=10, concavity of x(12-x) gives the following upper bounds:

| c | sum x_i | max sum x_i(12-x_i) | lower bound E_XC | upper bound E_cross |
|---:|---:|---:|---:|---:|
| 4 | 28 | 74 | 24 | 26 |
| 5 | 27 | 81 | 27 | 28 |
| 6 | 26 | 86 | 28 | 30 |
| 7 | 25 | 91 | 27 | 33 |
| 8 | 24 | 96 | 24 | 37 |

### 2. A stronger lower bound from the clique cap

Let Z_i be the degree-12 vertices in X_i, and write their sizes in descending order as z_1>=z_2>=z_3. At most two vertices outside the anchors have positive excess, so

z_1+z_2+z_3 >= 30-c.

Also z_1<=10. Therefore

z_2+z_3 >= 20-c >=12.

Since each Z_i is a clique and omega(H)<=11, at least one pair between Z_2 and Z_3 is a nonedge. Fix such a pair b in Z_2 and d in Z_3.

If there were no independent transversal of Z_1,Z_2,Z_3, then every a in Z_1 would be adjacent to at least one of b,d. Since at most z_2 z_3-1 edges run between Z_2 and Z_3, this forces

E_cross >= z_2 z_3 - 1 + z_1.                            (1)

For c<=7, put s=z_2+z_3>=20-c, so s is at least 13,14,15,16 respectively. With z_2<=z_1<=10, minimizing the right side of (1) over z_2+z_3>=s gives the lower bounds 39,49,59,69 for c=7,6,5,4 respectively. Each exceeds the corresponding upper bound 33,30,28,26 in the table. Thus no case with c<=7 can lack an independent transversal.

### 3. The c=8 boundary

Here x_1+x_2+x_3=24, z_1+z_2+z_3>=22, and every z_i<=10. The degree-sum bound above gives E_cross<=37. We show the lower bound (1) is always at least38.

If z_3=2, then (z_1,z_2,z_3)=(10,10,2). The two available positive-excess vertices must both lie in the third block, so the corresponding x-profile is (10,10,4). The upper bound improves to E_cross<=25, while (1) gives at least29.

If z_3=3, the only possible sorted triples are (10,10,3) and (10,9,3). The corresponding x-profiles are (10,10,4) and (10,9,5). The respective lower bounds in (1) are 39 and36, while the corresponding upper bounds are25 and30.

If z_3=4, the possible sorted triples are (10,10,4), (10,9,4), (10,8,4), and (9,9,4). The maximum possible E_cross upper bounds over the corresponding x-profiles are respectively 25,30,33,34 (attained at x-profiles (10,10,4), (10,9,5), (10,8,6), and (9,9,6)). The lower bounds in (1) are respectively 49,45,41,44. Every pair contradicts.

Finally, if z_3>=5, the constraints z_1+z_2+z_3>=22 and z_1<=10 imply z_2+z_3>=12. If z_3=5, then z_2>=7 and the minimum of (1) is44, attained at (10,7,5). If z_3>=6, the minimum is at least45. Both exceed E_cross<=37.

Thus the assumption of no independent transversal is impossible also when c=8.

### 4. Finish

There is therefore an independent transversal z_i in Z_i: three pairwise nonadjacent degree-12 vertices. The registered GLOBAL_THREE_ANCHOR_K6_FULL_CLOSURE then gives K>=8, contradicting K<=6.

This proves the new case h=4. Together with the minimum-anchor and h<=3 theorems, every independent triple of total degree excess at most four forces K>=8. QED.

## Backend consequence

For a d3 common-S family whose missing triple is independent in the target graph, the exact transport theorem gives h_y<=a-3 in every owner-repivot core. The present theorem therefore extends the E-305 three-anchor envelope from allowance a<=6 to **a<=7**. The only triangular allowance not covered by this argument is a=8, where the remaining no-anchor patterns have total excess four or five (the total-four case is now closed; total five remains open).

## Independent finite check

The connector-count arithmetic has been independently enumerated over every nonnegative pair-connector triple with c+t=8, x_i<=10. The aggregate profile bounds in the table are exact. For c=8, the four z_3 subcases above exhaust all sorted degree-12 block sizes allowed by sum z_i>=22 and z_i<=10.
