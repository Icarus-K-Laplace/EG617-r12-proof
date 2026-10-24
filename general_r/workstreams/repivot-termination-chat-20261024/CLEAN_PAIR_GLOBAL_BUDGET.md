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

lambda=m-r+1,  h=|H\U|=3r-1-2m=r+1-2lambda.

In the nonempty AES interval, m<=floor(3(r-1)/2), so h>=2. The lower threshold gives lambda>=ceil(r/3)+4 and h<=floor(r/3)-7; in particular lambda>h+10 and every block-type class below has size >4.

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

x,y,z >= lambda=m-r+1.

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

## 5. Off-part witnesses force high excess

The witness pair chosen for an outside vertex o consists of one class from T0 and one from T1. If the two classes belong to the same part, o sees that entire part. If they belong to different parts, the remaining type classes contain a triple whose three pair relations are: one optional graph of maximum degree at most 4, one block matching, and one empty H-pair.

For that residual triple, any set of fewer than lambda-4 neighbours of o cannot hit all independent transversals. Indeed, after deleting those neighbours, each of the three classes still has at least five vertices. Choose a vertex in the endpoint class of the optional relation, a non-neighbour of it in the other optional class (possible because the optional degree is at most 4), and a vertex in the matching class other than the unique block mate. The resulting triple is pairwise H-nonadjacent and also nonadjacent to o, contradicting alpha(H)<=3.

Therefore, for any cross-part witness pair,

d_H(o,U) >= 2a+(a-4)=3a-4.

Since lambda>=ceil(r/3)+4,

kappa_o=d_H(o)-r >= 3lambda-4-r >= 8.                       (5.1)

Call o **exceptional** if it has no pair of fully-seen witness classes from the same part. Every nonexceptional outside vertex sees an entire part; every exceptional outside vertex satisfies (5.1).

If X is the number of exceptional outside vertices, the inherited excess cap gives

X(3lambda-4-r) <= K_O <= 2r-2-K_U,                             (5.2)

so

X <= floor((2r-2-K_U)/(3lambda-4-r)) <= floor((2r-2)/8).

Since h=r+1-2lambda, the denominator has the exact form

3lambda-4-r=(r-3h-5)/2,

and hence

X <= floor((4r-4-2K_U)/(r-3h-5)).

The denominator is at least 16 throughout the stated high-density branch.

This is a genuine dichotomy, but X can still be linear when lambda is close to r/3.

## 6. Shell-incidence lower bound and strengthened exceptional budget

For every clean endpoint x in U, the clean weight equation is

kappa_x+e_F(x,S)=1,

so kappa_x=1-e_F(x,S), with e_F(x,S) in {0,1}. The total incidence of the old shell pair is

e_F(S,H)=2r+b,  b in {0,1}.

Therefore at most 2r+b endpoints of U have zero excess, and

K_U=sum_{x in U}kappa_x >= 2m-(2r+b).                       (6.1)

The exceptional set O_exc is disjoint from U. Combining (5.1) with (6.1) gives the stronger joint budget

2m-2r-b + X(3lambda-4-r) <= K_U+K_O <= 2r-2,

or

X(3lambda-4-r) <= 4r-2-2m+b.                                    (6.2)

Since 2m=3r-1-h and 3lambda-4-r=(r-3h-5)/2, this becomes

X <= floor(2(r-1+h+b)/(r-3h-5)).                            (6.3)

The denominator r-3h-5 is at least 16 in the high-density branch. At the lower AES threshold, (6.3) gives X<=r/6+O(1), improving the earlier parameter-free X<=r/4+O(1). The exceptional set may still be linear, so this is not a contradiction.

## 7. Part-seeing vertices and the global no-double-counting identity

Assign every nonexceptional outside vertex to one part it sees completely. Let O_i be the assigned vertices for part i, g_i=|O_i|, and define

u_i=s_i+2-g_i.

Then g_i<=s_i+2, u_i>=0, and

sum_i u_i = (h-2)+6-(h-X)=4+X.                            (6.1)

If s_i=0, then g_i=0, because a vertex adjacent to all of the size-(r-1) clique U_i would create a target clique of size r.

For x in U_i let rho_x be the number of its neighbours in O\O_i, including neighbours in other assigned groups and in the exceptional set. Since every vertex of O_i is adjacent to every vertex of U_i,

d_H(x,O)=g_i+rho_x.

Combining this with (3.1) gives the exact resource split

t_x+rho_x = kappa_x+u_i-1.                               (6.2)

Let e_opt be the number of optional H-edges inside U, and E_foreign=sum_{x in U}rho_x. Each optional edge is counted twice by sum t_x, while each foreign O-U edge is counted once by sum rho_x. Thus

2 e_opt + E_foreign
= K_U + sum_i n_i(u_i-1).                                 (6.3)

This is a no-double-counting identity. It couples the optional-edge budget, the outside assignment, and the core excess. It does not by itself close the remaining terminal because X can be positive and the part-assignment slack then sums to 4+X.

The class-witness slacks u_T from Section 4 remain distinct from the part-assignment slacks u_i. The former always sum to 4 and give the unconditional optional-degree bound t_x<=4. The latter sum to 4+X.

For each assigned group O_i, every clique Q in H[O_i] combines with U_i into a clique, so omega(H[O_i])<=s_i.

## 8. What this does and does not close

The new structural result is an **outside-neighbour dichotomy**, not a theorem that every outside vertex sees an entire part. It proves:

- every optional cross degree is at most four;
- every outside vertex either sees a whole part or has excess at least 3lambda-4-r>=8;
- the number X of exceptional vertices obeys (5.2);
- the part-seeing subpopulation has a three-part assignment with total slack 4+X and exact budget (6.3).

The remaining terminal can still have X=Theta(r) near the lower AES threshold, although the shell-incidence budget sharpens its coefficient to at most about 1/6 in that regime. Thus the full linear interval is not eliminated.

Boundary audit:
- If h=2, all s_i=0, so no outside vertex can see a whole part; hence X=2 and (5.1) gives K_O>=r-11. This does not contradict the total budget by itself.
- If h=3, the deficit vector is a permutation of (1,0,0). The case X=0 is impossible: all outside vertices would be assigned to the unique part with deficit one, making O independent; then e_H(U,O)>=5r-8 and K_O>=2r-8, while K_U>=r-2, contradicting K<=2r-2 for r>=12. But exceptional vertices have not been excluded, so h=3 remains open.

Status: AES-to-three-part reduction, class-slack bound, off-part excess lemma, and identity (6.3) **PROVED_CONDITIONAL**; global clean-pair nonextension **OPEN**.
