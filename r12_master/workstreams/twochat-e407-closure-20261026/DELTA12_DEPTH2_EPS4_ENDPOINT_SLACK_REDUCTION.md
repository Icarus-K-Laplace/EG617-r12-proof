# E407 Q32 — delta=12 depth-2 epsilon_U=4 endpoint-slack reduction

Date: 2026-10-28  
Status: **PROVED_CONDITIONAL strict reduction** under the registered 308-edge depth-2 kernel classification and the delta=12 low-W-degree lemma. Three equality-slack endpoint profiles are excluded; four aggregate profiles remain OPEN. E407 Q32 remains OPEN.

## 1. Setup

Work in the depth-2 C5-blowup kernel at
\[
\epsilon_U=4.
\]
Then
\[
H[W]=K_4^P\dot\cup K_4^Q\dot\cup K_5^R\dot\cup K_5^T
\]
with no W-cross edges.

Let `d0` be the unique degree-4 point of J and let `C4=C\cup E` be the four degree-6 J-points. Let

- `t0` = number of the two restored target edges incident with d0;
- `epsilon0` = core excess at d0;
- `E_C=sum_{c in C4} epsilon_c`;
- `E_rest=4-epsilon0-E_C`.

Then
\[
d_W(d_0)=2+\epsilon_0-t_0,
\qquad d_W(c)=4+\epsilon_c-t_c,
\]
with
\[
t_0+\sum_{c\in C4}t_c=2.
\]
Every U-point has W-degree at least three.

The pure pair rule says that if two core vertices are H-nonadjacent, their common W-nonneighbours contain no independent triple. Since W is four disjoint cliques, the union of their W-neighbourhoods must completely cover at least two W-components.

## 2. Exact endpoint-slack inequality

The point d0 is H-nonadjacent to every c in C4. The two smallest W-components have total size eight. Therefore
\[
d_W(d_0)+d_W(c)\ge8
\]
for all four c.

Summing yields
\[
4(2+\epsilon_0-t_0)+\sum_c(4+\epsilon_c-t_c)\ge32.
\]
Using `sum_c t_c=2-t0`,
\[
\boxed{4\epsilon_0+E_C\ge10+3t_0.}\tag{2.1}
\]
Together with `epsilon0+E_C+E_rest=4`, nonnegativity, `t0 in {0,1,2}`, and the three-neighbour floor, the complete aggregate survivor list is

| t0 | epsilon0 | E_C | E_rest | d_W(d0) | pair-sum slack |
|---:|---:|---:|---:|---:|---:|
| 0 | 2 | 2 | 0 | 4 | 0 |
| 0 | 3 | 0 | 1 | 5 | 2 |
| 0 | 3 | 1 | 0 | 5 | 3 |
| 0 | 4 | 0 | 0 | 6 | 6 |
| 1 | 3 | 1 | 0 | 4 | 0 |
| 1 | 4 | 0 | 0 | 5 | 3 |
| 2 | 4 | 0 | 0 | 4 | 0 |

Here pair-sum slack is
\[
\sum_{c\in C4}(d_W(d0)+d_W(c))-32.
\]
The verifier independently enumerates the integer ledger.

## 3. Equality-slack structure

Consider one of the three rows with slack zero:
\[
(0,2,2,0),\quad(1,3,1,0),\quad(2,4,0,0).
\tag{3.1}
\]
In all three,
\[
d_W(d0)=4.
\]
Since all four pair inequalities sum exactly to equality, every c in C4 has W-degree four and every pair `(d0,c)` has neighbourhood-union size exactly eight. The only two W-components with total size eight are K4^P and K4^Q. Hence for one fixed eight-set
\[
R_8=K_4^P\dot\cup K_4^Q,
\]
we have
\[
N_W(c)=R_8\setminus N_W(d0)
\quad\text{for every }c\in C4.
\tag{3.2}
\]
The two sets are disjoint four-sets.

Put
\[
x=|N_W(d0)\cap K_4^P|.
\]
Then the complementary four-set has `4-x` P-points and x Q-points.

## 4. Every non-d0-partner is K5-complete

Let v lie in one of the two K7 components and suppose v is not a restored neighbour of d0. In every equality-slack row all excess outside `d0\cup C4` is zero, so
\[
d_W(v)=6-r_v\le6.
\]
Choose any c in C4 to which v is nonadjacent; such a c always exists because there are only two restored edges.

The pair `(v,c)` and the pair `(v,d0)` must each cover two W-components.

A direct four-case calculation gives:

- x=2 is impossible: both pairs can use the two K4s only by forcing v to contain both complementary four-sets, requiring eight neighbours;
- x=1 or3 is impossible: the only possible K4+K5 alternatives on the two pairs require one K5 plus one missing point from each distinct K4, requiring at least seven neighbours;
- x=0 or4 is possible only when v is complete to one of the two K5 components.

Thus
\[
\boxed{x\in\{0,4\},}
\tag{4.1}
\]
and every non-d0-partner v has a binary label R or T according to the K5 component it sees completely.

Two labelled vertices on opposite K7 sides cannot have the same label. They are H-nonadjacent; if both are complete to the same K5, each has at most one W-neighbour outside it, so their union has at most two outside vertices and cannot completely cover any second W-component. Therefore cross-K7 labels are opposite.

## 5. Exclude the three equality rows

### t0=0

There is no d0-partner. All seven vertices on each K7 are labelled. Opposite-label forcing makes one whole K7 complete to a K5, producing K12. Contradiction.

### t0=1

There is at most one d0-partner exception. Hence one of the two K7s still has all seven vertices labelled uniformly by one K5. Again K7+K5 gives K12.

### t0=2

If the two d0-edges share an A/B endpoint, there is only one exception and the previous K12 argument applies. The only remaining endpoint pattern has one d0-partner in each K7, leaving six labelled vertices on each side with opposite K5 labels.

Let a0,b0 be the two exceptions. Since every c has the complementary K4 neighbourhood, the pair `(a0,c)` forces a0 either

1. to be complete to the other K4, or
2. to be complete to one K5.

If a0 takes the K5 used by the six labelled vertices on its own K7 side, that side becomes seven K5-complete vertices and gives K12. If it takes the opposite K5, its pair with a labelled vertex on the opposite K7 side has the same label and violates the pair rule. Hence a0 must be complete to the other K4. The same argument forces b0 to be complete to that same K4.

But then the nonadjacent pair `(a0,b0)` covers that K4 and has at most two vertices outside it, so it cannot cover a second component. Contradiction.

Therefore all three slack-zero rows in (3.1) are impossible.

## 6. Exact remaining epsilon_U=4 aggregate frontier

Only four aggregate endpoint/excess profiles remain:
\[
\boxed{
( t_0,\epsilon_0,E_C,E_{rest})\in
\{(0,3,0,1),(0,3,1,0),(0,4,0,0),(1,4,0,0)\}.
}
\tag{6.1}
\]

These are necessary aggregate profiles, not asserted realizations. They require a further neighbourhood-level analysis; the current theorem does not close epsilon_U=4.

## 7. Dependency audit

The reduction uses:
1. the registered 308-edge depth-2 kernel classification;
2. the delta=12 low-W-degree lemma;
3. pure graph alpha(H)<=4, omega(H)<=11, exact degree/excess accounting and the nonadjacent-pair rule.

It does not use Didin. The finite verifier checks the aggregate ledger and equality-case binary endpoint arithmetic only; it does not re-prove the external kernel classification.
