# Clean-Pair Global Budget — Three-Part Assignment Kernel

Status: **PROVED_CONDITIONAL structural reduction; NONEXTENSION OPEN**.

This note attacks the linear interval left by the Andrasfai-Erdos-Sos (AES) reduction. It uses only the frozen legal-core contract, the hereditary excess cap, and the clean-pair row-closure contract. It never assumes alpha(F)<=3.

## 1. Contract and parameters

Assume A+B and r>=12. Let H be a legal core with

- |H|=3r-1;
- alpha(H)<=3 and omega(H)<=r-1;
- delta(H)>=r;
- K=sum_{x in H}(d_H(x)-r)<=2r-2.

Let U be the union of m pairwise-disjoint clean a=2 blocks P_i={x_i^0,x_i^1}, and suppose

m >= ceil(4r/3+3).

Put

a=m-r+1,  h=|H\U|=3r-1-2m=r+1-2a.

In the nonempty AES interval, m<=floor(3(r-1)/2), so h>=2. The lower threshold gives a>=ceil(r/3)+4 and h<=floor(r/3)-7; in particular a>h+10 and every block-type class below has size >4.

Every clean endpoint x has w_x=1, hence kappa_x=d_H(x)-r in {0,1} and d_H(x)=r+kappa_x.

## 2. The AES partition has no same-part clean block

Let G=overline(H[U]). By alpha(H)<=3, G is K4-free. The previous minimum-degree estimate gives delta(G)>5|U|/8, so AES makes G 3-partite with parts A,B,C. Each part is a clique in H, hence |A|,|B|,|C|<=r-1.

No clean block can have both endpoints in one part. If P_i={x,x'} lies in A, then no other block can touch A: any A-endpoint y of another block would create both target edges xy and x'y in the cross graph between the two blocks, violating its matching property. If another block were contained in B or C, the same argument would prevent all remaining blocks from touching that part, leaving at most three blocks in total. Thus, for m>r, all other blocks would have to be BC blocks, forcing |B|=|C|=m-1>r-1, a contradiction.

Consequently every block meets two different parts. Let

- x be the number of AB blocks;
- y be the number of AC blocks;
- z be the number of BC blocks.

Then m=x+y+z and

|A|=x+y, |B|=x+z, |C|=y+z.

The clique cap yields

x,y,z >= a=m-r+1.

Write n_A=|A|=r-1-s_A and similarly for B,C. Then

s_A=z-a, s_B=y-a, s_C=x-a,

and

s_A+s_B+s_C = h-2.                                      (2.1)

## 3. Six type classes and the exact cross-edge alphabet

Partition the vertices of U into six type classes:

| Type class | Meaning | Size | Part |
|---|---|---:|---|
| A0 | A-endpoints of AB blocks | x | A |
| A1 | A-endpoints of AC blocks | y | A |
| B0 | B-endpoints of AB blocks | x | B |
| B1 | B-endpoints of BC blocks | z | B |
| C0 | C-endpoints of AC blocks | y | C |
| C1 | C-endpoints of BC blocks | z | C |

The cross-part H edges are exactly of three forms:

1. **Block matching edges:** A0--B0, A1--C0, B1--C1. Each is a matching.
2. **Optional edges:** A0--C1, A1--B1, B0--C0. These are the non-shared-endpoint edges allowed by a two-block matching rule.
3. **Forbidden type pairs:** A0--B1, A1--B0, A0--C0, A1--C1, B0--C1, B1--C0 have no H edges.

For x in part i, let t_x be its number of optional H-neighbours (not counting its block mate). Since the part itself is a clique and the block mate is one additional neighbour,

d_H[U](x)=n_i+t_x.

Therefore its outside-core degree is exactly

d_H(x,H\U)=1+s_i+kappa_x-t_x <= s_i+2.                  (3.1)

The right-hand inequality uses kappa_x in {0,1}.

## 4. Outside-neighbour transversal lemma

The two triples of type classes

T0=(A0,B1,C0),    T1=(A1,B0,C1)

have no H edges between any two of their three classes. Thus any choice of one vertex from each triple is an independent triple in H.

Fix o in O=H\U. If o failed to be adjacent to every vertex of at least one class in T0, it would have a non-neighbour in each of A0,B1,C0. Those three vertices together with o would be an independent 4-set in H. Hence o is H-adjacent to an entire class from T0. The same holds for T1.

For each o choose one witness class in T0 and one in T1. For a type class T in part i, let N_T be the number of outside vertices assigned to T. Every such outside vertex is adjacent to every x in T, so by (3.1),

N_T <= d_H(x,O) <= s_i+2 for every x in T.

Define the nonnegative integer slack

u_T=s_i+2-N_T.

Since |O|=h and each of T0,T1 receives exactly one assignment per outside vertex,

sum_{T in T0} u_T = sum_{T in T1} u_T
= (s_A+s_B+s_C)+6-h = 4.                                (4.1)

Thus every u_T is at most 4. For x in T, (3.1) and d_H(x,O)>=N_T give the exact inequality

t_x <= kappa_x+u_T-1.                                     (4.2)

In particular, every optional cross degree is at most 4. If u_T=0, then every x in T has kappa_x=1 and t_x=0. If u_T=1 and kappa_x=0, then t_x=0.

## 5. Every outside vertex must see an entire part

We now show that the two witness classes chosen for o cannot belong to different parts.

There are six off-part witness pairs. In each case, the remaining class triple has two pair relations that are respectively an empty H-pair and a block matching, and its third relation is an optional graph of maximum degree at most 4. Since x,y,z>=a>4, an H-independent transversal of that remaining triple exists:

| Witness pair | Remaining triple | Independent-transversal choice |
|---|---|---|
| A0,B0 | A1,B1,C1 | choose b in B1; choose a in A1 outside its at-most-4 optional neighbours; choose c in C1 other than b's block mate |
| A0,C1 | A1,B1,C0 | choose a in A1; choose b in B1 outside its optional neighbours; choose c in C0 other than a's block mate |
| B1,A1 | A0,B0,C0 | choose b in B0; choose a in A0 other than b's block mate; choose c in C0 outside b's optional neighbours |
| B1,C1 | A1,B0,C0 | choose c in C0; choose a in A1 other than c's block mate; choose b in B0 outside c's optional neighbours |
| C0,A1 | A0,B0,C1 | choose a in A0; choose b in B0 other than a's block mate; choose c in C1 outside a's optional neighbours |
| C0,B0 | A0,B1,C1 | choose b in B1; choose c in C1 other than b's block mate; choose a in A0 outside c's optional neighbours |

Each chosen triple is pairwise H-nonadjacent. The outside vertex o is nonadjacent to every vertex in the two unchosen type classes, because it was assigned to the other witness classes in T0 and T1. Thus o plus the triple would be an independent 4-set in H, a contradiction.

Therefore the two witness classes must be the two type classes of the same part. We have proved:

> **Outside-neighbour transversal theorem.** Every o in O is adjacent in H to every vertex of at least one entire part A, B, or C.

This uses alpha(H)<=3, not alpha(F)<=3.

## 6. Three-part assignment kernel and no-double-counting identity

Assign each o in O to one part it sees completely. Let O_i be the assigned outside vertices for part i, g_i=|O_i|, and

u_i=s_i+2-g_i.

By (3.1), g_i<=s_i+2. Since sum_i g_i=h and sum_i s_i=h-2,

u_i>=0,   sum_i u_i=4,   g_i=s_i+2-u_i.                  (6.1)

If s_i=0, then g_i=0: otherwise an outside vertex adjacent to all of the size-(r-1) clique U_i would create a target clique of size r.

For x in U_i define rho_x to be its number of neighbours in O\O_i (foreign-assignment incidences). Because all O_i vertices are adjacent to all of U_i,

d_H(x,O)=g_i+rho_x.

Combining with (3.1) gives the exact resource split

t_x+rho_x = kappa_x+u_i-1.                               (6.2)

This counts each optional U-edge twice over its endpoints and each foreign O-U edge once over its U endpoint. Summing (6.2) over U yields

2 e_opt + E_foreign
= K_U + sum_i n_i(u_i-1),                                 (6.3)

where e_opt is the number of optional H-edges inside U, E_foreign=sum_{x in U}rho_x, and K_U=sum_{x in U}kappa_x. No edge is double-counted across the two terms.

Consequences:

- Every optional cross degree t_x is at most u_i<=4.
- If u_i=0, then every x in U_i has kappa_x=1 and t_x=rho_x=0.
- If u_i=1 and kappa_x=0, then t_x=rho_x=0.
- For every clique Q in H[O_i], U_i union Q is a clique, so omega(H[O_i])<=s_i.
- Since sum u_i=4, the high-density terminal is reduced to a three-part assignment with only four total units of assignment slack, optional degree at most four, and the exact budget (6.3).

## 7. What this does and does not close

This is stronger than the previous AES reduction: it proves that every outside-core vertex sees an entire part, not merely that U is three-partite. It also makes the optional cross-edge graph bounded-degree and couples the assignment deficits to excess exactly.

It is **not yet a contradiction**. The remaining kernel can still have h=Theta(r), with s_A+s_B+s_C=h-2 and u_A+u_B+u_C=4. The exact budget (6.3) does not by itself contradict K_U+K_O<=2r-2; the residual degrees and clique/independence constraints inside O must still be used.

A small endpoint consequence is immediate: h=2 is impossible, because then all s_i=0, hence all g_i=0 by the clique cap, contradicting sum g_i=h. The h=3 case is addressed in COUNTEREXAMPLE_SEARCH.md; its remaining subcase requires an additional degree/excess argument and is not promoted here unless separately verified.

Status: AES-to-three-part reduction and outside-neighbour transversal theorem **PROVED_CONDITIONAL**; global clean-pair nonextension **OPEN**.
