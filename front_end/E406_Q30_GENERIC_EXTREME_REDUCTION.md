# E406 q30 local-maximum: generic extreme-shell reduction

Status: `PROVED` for the reductions stated here. This file is independent of the E332 211-edge core value.

Assume the explicit E406 T61 contract and a degree-13 pivot p with q=30. Assume further that q=30 is globally maximal among degree-13 pivots. Then the 47-core C has e(C)=285 and delta(C)>=12.

Write A=N(p), M=complement(R[A]), decorations g_a=d_R(a)-13, G=sum g, z=e(M)=30-G, and row weights t_a=d_M(a)+g_a. Since z>=22, G<=8.

The independently proved low/middle-charge bridge gives: q<=23 impossible; q24,25,26 promote upward; q27,q28 impossible; q29 has a good repivot to q30. Hence every legal repivot from a q30 local maximum has charge in {24,25,26,29,30}.

## 1. Regular missing degrees

For an undecorated shell vertex y with d=d_M(y), S=N_M(y), the exact repivot lower bound gives

q_y-q >= d(13-d)-[t(S)-e_M(S)].

Since t(S)-e_M(S)<=q=30 and q_y<=30, d in {0,1,2,3,10,11,12}. In particular no regular degree4..9 occurs.

Call regular degree0,1,2 vertices low and regular degree11,12 vertices high. Low regular vertices are pairwise nonadjacent in M by PAIR-13.

## 2. At most two high regular vertices

Let h be the number of high regular vertices.

If h>=5, M[H] contains a triangle. Any missing triangle of high regular vertices has row-weight at least33, so the subset identity gives q>=33-3=30; equality forces all three weights11 and zero outside charge. Any fourth high vertex outside that triangle would then have missing degree at most3, contradiction.

For h=4, M[H] is either K4, K4-e, or K4 minus a matching because every high vertex has M-degree at least11. K4 gives q>=44-6>30. K4-e contains a high triangle and the same equality contradiction. In K4 minus a matching, every high vertex has two high neighbours and therefore at least9 neighbours among the other nine shell vertices. Hence there are at least36 high-to-outside incidences; the outside vertices have capacity at most 2 per low plus 4 per decorated vertex, and with at most8 decorated vertices the required incidence count forces more decoration than G<=8. Contradiction.

For h=3, M[H] cannot be a triangle by the same equality argument. Thus M[H]=K3-e. The middle high requires at least9 outside neighbours and the two endpoints at least10 each, for at least29 high-to-outside incidences. If k outside vertices are decorated, the ten outside vertices have incidence capacity at most 2(10-k)+3k=20+k<=28 because k<=G<=8. Contradiction.

Therefore h<=2.

## 3. Decoration window G>=4

Let D be the decorated set, k=|D|, L the regular low set, and r=h+k. Since L is independent and every low has degree at most2,

z <= C(r,2)+2(13-r).

Because h<=2 and k<=G:

- G=0 gives r<=2 and RHS<=23<30;
- G=1 gives r<=3 and RHS<=23<29;
- G=2 gives r<=4 and RHS<=24<28;
- G=3 gives r<=5 and RHS<=26<27.

Hence G>=4. Together with G<=8:

4<=G<=8.

## 4. Exact support count at G=4

Now z=26. The edge-capacity inequality forces r>=5, while h<=2 and k<=4 give r<=6.

If r=5, equality is forced in the capacity bound, so every low has degree2 and M[H union D]=K5. But five pairwise target-nonadjacent shell vertices require their core rows to cover all47 core vertices: otherwise an uncovered core vertex together with those five shell vertices is an independent6-set. Hence t(S)>=47 on that K5 and

q>=47-C(5,2)=37,

contradiction.

Thus r=6. Since h<=2 and k<=4, necessarily

(h,k,l)=(2,4,7).

For the two high regular vertices a,b, each has at least6 low neighbours, so they share a low u. Then N_M(u)={a,b}. The d=2 repivot at u has q_u>=29, hence its new core has at most286 edges and minimum degree at least12. Applying the exact zero-gap formula in that repivot view forces both a and b to be missing-adjacent to every shell vertex outside {a,b}. Therefore every low has neighbourhood {a,b}, there are no low-decorated missing edges, and the remaining four decorated vertices induce a graph J with 3 or4 edges.

All four decorations equal1. For any J-edge xy, PAIR-13 gives t_x+t_y>=13, whereas t_x=3+d_J(x)<=6 and likewise for y. Impossible. Hence G=4 is empty.

## 5. G=5 and G=6,h=0

The shell proofs in backend/E332_G4_G5_CLOSURE.md and backend/E332_G6_H0_CLOSURE.md use only:

- q=30 and G=5 or6;
- h<=2;
- low independence and degree<=2;
- PAIR/TRIANGLE row coverage;
- the no-rise degree-2 inequality t_i+t_j>=23 when a regular low uses an M-edge pair;
- elementary edge capacity and positive-decoration accounting.

They do not use the 211-edge core degree multiset in the h=0/one-high G5 arguments or in the G6,h=0 argument. In E406 PAIR-13 is at least as strong as the pair bound used there. Replaying those calculations gives:

- G=5: EMPTY;
- G=6,h=0: EMPTY.

No claim is made here about the E332-specific G6,h=2 core-capacity contradiction, which used a 35-point core and does not transfer automatically.

## Consequence

Any E406 q30 local maximum with no regular d3/d10 root is reduced to

- G=6 with h=1 or2;
- G=7 or8 with h=0,1,2.

This is now the complete generic extreme-shell frontier for the plateau-escape bridge.
