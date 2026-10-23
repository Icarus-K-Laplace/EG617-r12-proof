# q36 f=2, 2K1 far, a_F=0 — c=7 allowance-three reduction

Status: `PROVED REDUCTION` under the preceding a_F=0 d3-capacity theorems, CORE211, row closure, and lexicographic q36 maximality.

This treats the all-d3, single-missing-class c=7 channel.

## 1. Allowance is forced to three

For c=7, an all-d3 survivor with two missing classes is already excluded by `Q36_F2_2K1_A0_LOW_ALLOWANCE_D3.md` for c>=7. Hence all seven rows miss the same decorated vertex x.

The common-S allowance is

  A=c+nu_x+g_x-7=nu_x+g_x.

Allowance0/1 cannot support seven rows by the low-allowance theorem, and allowance2 cannot support seven rows by `Q36_F2_2K1_A0_ALLOWANCE2_D3_CAPACITY.md`. Thus

  A=3.                                                       (1)

Hence

  nu_x+g_x=3.                                                (2)

The core row of x has size

  |N_H(x)|=A+9=12.                                          (3)

## 2. Exact decorated-shell equality

Since all seven low rows are d3, the shell ledger gives

  G=13-c-nu=6-nu.

There are r=4 decorated shell vertices. The three decorated vertices other than x contribute at least one unit each, so

  G-g_x>=3.

Using G=6-nu and g_x=3-nu_x from (2),

  3-nu+nu_x>=3,

so `nu_x>=nu`. Since always `nu_x<=nu`, equality is forced:

  nu_x=nu,
  g_x=3-nu.                                                  (4)

Therefore every missing edge of M[X] is incident to x, and each of the other three decorated shell vertices has decoration exactly1.

Because G>=r, nu<=2. Thus initially nu belongs to {0,1,2}.

## 3. The x-row is large inside the 11-point remainder

Let A,B be the two disjoint 12-point far supports and

  R=H\(A union B), |R|=11.

Both far regular shell vertices are target-nonadjacent to x and have missing degree12. The regular/decorated zero-gap inequality gives for each far support

  |N_H(x) intersect A|<=g_x-1,
  |N_H(x) intersect B|<=g_x-1.

Since |N_H(x)|=12,

  e_F(x,R)>=12-2(g_x-1).

Using (4),

> e_F(x,R)>=8+2nu.                                         (5)

### nu=2 is impossible

Then (5) gives e(x,R)>=12>|R|=11. Contradiction.

Hence

  nu in {0,1}.                                               (6)

## 4. Supports cannot lie entirely in N_R(x)

Every low support D has size3 and defect

  delta(D)=kappa(D)+m(D)+e_F(x,D)<=3,

with repivot charge

  q_D=33+delta(D).

If all three vertices of D are adjacent to x, then `e_F(x,D)=3`, so necessarily

- delta(D)=3;
- kappa(D)=0;
- m(D)=0;
- H[D]=K3;
- q_D=36.

But every D-vertex has two old shell neighbours: its owner and x. Thus all three inserted vertices are globally decorated. The repivot removes x but retains the other three old decorated shell vertices, so the new q36 shell has at least6 decorated vertices versus the old tau=4. Contradiction.

Therefore

> every support D contains at least one vertex of R\N_H(x). (7)

## 5. nu=1 is impossible

By (5), x has at least10 neighbours in R, so there is at most one non-neighbour z in R. By (7), every one of the seven supports contains z.

Each support therefore has exactly two x-neighbours. Hence

  e_F(x,D)=2.

If kappa(D)+m(D)=1, then delta(D)=3 and q_D=36. The two x-neighbour support vertices are globally decorated, so after retaining the other three old decorated shell vertices the new tau is at least5>4. Thus plateau is impossible and

  kappa(D)=m(D)=0.

Therefore every support is a pure K3 of core-degree12 vertices and repivots to q35.

Write each support as

  {z,p_i,q_i}.

A petal p_i is adjacent to x and its owner, has core degree12, and is therefore globally decorated; this does not affect q35 maximality. Row closure against another support D_j gives

  e_H(p_i,D_j)<=kappa_(p_i)+e_F(p_i,S)=1,

where the one unit is already used by the common vertex z because H[D_i]=K3. Hence p_i is target-anticomplete to the two petals of every distinct support D_j.

Thus petals belonging to distinct supports are pairwise target-anticomplete. Three distinct supports would yield an independent triple by choosing one petal from each. Hence there are at most two distinct supports.

If one support has multiplicity m, its three vertices have global decoration at least

- m-1 on z;
- m on each x-adjacent petal.

The q35 repivot retains the other three decorated shell vertices, so its decoration total is at least

  3+(m-1)+m+m=3m+2.

A q35 shell has decoration total at most13, so m<=3.

At most two distinct supports, each of multiplicity at most3, can serve at most6 owners, contradicting the seven rows.

Therefore

  nu!=1.                                                     (8)

## 6. nu=0: x has exactly two or three non-neighbours in R

Now X is a target K4 and g_x=3. Equation (5) gives e(x,R)>=8, so x has at most three non-neighbours in R.

If x had no non-neighbour in R, (7) is impossible.

If x had exactly one non-neighbour, the proof of section5 applies verbatim: every support contains that same vertex, has exactly two x-neighbours, becomes a q35 pure K3, and at most six owners can be served.

Hence the only surviving c=7 allowance-three terminal has

> nu=0,
> X=K4,
> g_x=3,
> |R\N_H(x)| in {2,3}.                                      (9)

## 7. New exact frontier

The formerly arbitrary seven-row allowance-three problem has been reduced to two finite support geometries distinguished only by whether x has two or three non-neighbours in the 11-point alpha-two remainder R.

All higher shell data are fixed:

- all seven low rows share S=F union {x};
- X is a target K4;
- decorations on X are `(3,1,1,1)`;
- x has a 12-point core row;
- every low support meets the 2/3-point set `R\N_H(x)`.

The next task is the finite support-capacity closure for these two residual cases.