# q36 f=2, 2K1 far, a_F=0 — low-allowance d3 capacity

Status: `PROVED REDUCTION` under `Q36_F2_2K1_A0_REDUCTION.md`, CORE211, row closure, and lexicographic q36 maximality.

This gives sharp capacity statements for d3 common-missing classes of allowance0 or1 and closes the all-d3/two-class sector for c>=7.

## 1. Setup

Use the a_F=0 notation. The two far supports leave an 11-point remainder R with

  alpha(H[R])<=2.

For a decorated vertex x missed by a d3 class, put

- n_x = number of low owners missing x;
- nu_x=d_(M[X])(x);
- L_x=n_x+nu_x+g_x;
- allowance A_x=L_x-7.

A support D in this class has size3 and satisfies

  delta(D):=kappa(D)+m(D)+e_F(x,D)<=A_x.

Its repivot charge is

  q_D=36-A_x+delta(D).

For v in R write

  w_v^(x)=kappa_v+e_F(v,x).

Row closure for every support in the x-class is controlled by this same w-weight.

## 2. Allowance zero class has at most two owners

Assume A_x=0.

Then every support has delta=0, hence

- H[D]=K3;
- kappa(D)=0;
- e_F(x,D)=0;
- the repivot stays at q36.

A repeated support is impossible: if one K3 served two owners, all three support vertices would be globally decorated. The repivot removes the one decorated missing vertex x and retains every other old decorated shell vertex, so inserting three decorated vertices strictly increases tau.

Proper overlap of distinct supports is also impossible because h(3-h)=2>0. Thus distinct supports are disjoint; the common-S theorem gives zero target edges between them.

Three such supports would yield an independent triple in R by choosing one vertex from each. Hence

> A_x=0 => n_x<=2.                                         (1)

## 3. Allowance one: at most two distinct support classes

Assume A_x=1.

Proper overlap remains impossible because h(3-h)=2>1. Thus distinct supports are disjoint and any two distinct supports have at most one target cross-edge.

Three distinct supports are impossible: choosing one vertex uniformly from each gives expected target-edge count at most3/9<1, hence some independent triple in R.

Therefore there are at most two distinct support classes.               (2)

If a support D repeats, it cannot have delta(D)=1, since then its repivot would remain at q36 and the repeated support vertices would increase tau. Hence every repeated support has delta=0 and is a pure K3 of core-degree12 vertices, target-anticomplete to x; its repivot has q35.          (3)

## 4. A repeated allowance-one K3 cannot coexist with a second class

Let D be a repeated pure K3 and suppose E is another distinct support in the same class.

The common-S theorem gives e_H(D,E)=0 because D has zero row allowance.

If H[E] contained a target nonedge, that nonedge together with any vertex of D would form an independent triple in R. Hence E must also be a target K3.

Put

  L=R\(D union E),

so |L|=5.

For v in L, to avoid an independent triple with one vertex from D and one from E, its neighbourhood in D union E must cover all target-nonedges of K3,3 between the two anticomplete K3 blocks. A vertex cover of K3,3 has size at least3. Hence

  e_H(v,D)+e_H(v,E)>=3.                                    (4)

Row closure gives

  e_H(v,D)<=w_v^(x),
  e_H(v,E)<=w_v^(x).

Therefore w_v^(x)>=3 for every v in L, so

  sum_L w_v^(x)>=15.                                       (5)

But CORE211 gives kappa(R)<=2. Since A_x=1 implies

  L_x=n_x+nu_x+g_x=8,

the core row of x has size

  |N_H(x)|=d_M(x)+g_x=n_x+2+nu_x+g_x=10.

Thus

  sum_R w_v^(x)=kappa(R)+e_F(x,R)<=2+10=12,

contradicting (5).

Hence:

> in an allowance-one d3 class, if a support repeats then it is the unique distinct support class.                 (6)

Combined with (2), every allowance-one class is either

- at most two singleton supports; or
- one repeated pure K3 support used by all owners in the class.

## 5. All-d3 / two-class branch has c<=6

Now assume every low row is d3 (`n2=0`) and there are exactly two decorated missing vertices x,z.

From the shell ledger,

  G=13-c-nu,

and the decoration floor G>=r=11-c gives

  nu<=2.                                                    (7)

The general class-sum bound from `Q36_F2_2K1_A0_REDUCTION.md` gives

  A_x+A_z<=nu-1<=1.                                        (8)

If both allowances are zero, (1) gives c<=4. Thus for c>=5 the allowances are {1,0}.

The allowance-zero class has at most two owners. Let n be the size of the allowance-one class, so

  n>=c-2.                                                   (9)

For c>=5, n>=3, so by (6) all n owners share one repeated pure K3 support D and the repivot has q35.

The repivot removes x and retains old decoration G-g_x. Every vertex of D has at least n shell owners, hence global decoration at least n-1. The q35 shell has decoration total at most13, so

  G-g_x+3(n-1)<=13.                                        (10)

Because A_x=1,

  n+nu_x+g_x=8,

hence `g_x=8-n-nu_x`. Substituting G=13-c-nu into (10) gives

  4n<=11+c+nu-nu_x<=13+c.                                 (11)

Using n>=c-2,

  4(c-2)<=c+13,

so c<=7.                                                    (12)

It remains to exclude c=7. Then (9)--(11) force

- n=5;
- the allowance-zero class has size2;
- nu=2;
- nu_x=0;
- g_x=3.

But c=7 gives r=4 decorated shell vertices and

  G=13-7-2=4.

If one decorated vertex already has g_x=3, the other three decorated vertices contribute at least one each, forcing G>=6, contradiction.

Therefore

> all-d3 with two missing classes => c<=6.                  (13)

Equivalently, for c>=7 in the a_F=0 branch, if all low rows are d3 then they must all miss the same decorated vertex.

## 6. New interface

The a_F=0 branch now has:

- at most one repeated pure-K2 d2 family;
- at most two d3 missing classes;
- allowance-zero d3 class size at most2;
- allowance-one d3 class either size at most2 or one repeated pure K3;
- the all-d3/two-class sector is empty for c>=7.

The next unresolved high-c sector is therefore a single d3 missing class (possibly together with one repeated d2 K2 family).