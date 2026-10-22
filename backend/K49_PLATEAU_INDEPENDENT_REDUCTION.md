# K4,9 plateau — independent reduction to one residual

Status: `PROVED REDUCTION` under the top-channel CORE211 / lexicographic maximal-pivot contract.

This independently reconstructs most of the earlier source-reported K4,9 plateau theorem without using the package verifier.

## Setup

Let p be a degree-13 pivot with missing shell

`M=K_{4,9}`

with sides X (size4) and Y (size9). Assume all shell decoration lies on X and total decoration `G in {0,1,2}`. Thus

`q=36+G`.

Assume the pivot is lexicographically maximal for `(q,tau)`, where tau counts shell vertices of global degree greater than13.

In the top E338--E340 channels, the 35-core H has211 edges, minimum degree12, and total internal degree excess2.

## 1. Every regular X-vertex is a nondecreasing d=9 repivot

Take a regular x in X. Then its missing neighbourhood is S=Y, |S|=9, and Y is M-independent. Its core row D=N_H(x) has size9.

The exact repivot identity gives

`q_x-q = I_H(D)-36-36+e_F(Y,D)`.

Writing `epsilon_H(D)=sum_{u in D}(d_H(u)-12)` and `h=e_H(D)`,

`I_H(D)=108+epsilon_H(D)-h`,

hence

`q_x-q = 36 + epsilon_H(D)-h + e_F(Y,D) >=0`,

because `h<=36`.

Therefore either q strictly rises, or equality holds everywhere.

## 2. Plateau equality is a pure K9 support

If `q_x=q`, then necessarily

- `H[D]=K9`;
- every vertex of D has H-degree12;
- `e_F(Y,D)=0`.

So every plateau support is a pure K9 of core-degree12 vertices, target-anticomplete to the nine-side Y.

## 3. Lexicographic maximality forces plateau supports to be globally regular

The repivot at x removes the nine regular Y-vertices from the shell and inserts D. All other shell vertices retained by the exchange keep their global degrees.

Hence if any vertex of D has global degree greater than13, tau strictly increases while q stays fixed, contradicting lexicographic maximality.

Therefore every vertex in every plateau support D is globally degree13.

Since each such vertex already has internal H-degree12 and is adjacent to x in the old shell, it has no target shell neighbour other than x.

Consequently plateau supports belonging to two distinct regular vertices x,x' in X are disjoint: a common support vertex would be adjacent to both x and x', making its global degree at least14.

Moreover every other shell row is disjoint from each plateau support.

## 4. Decoration layers G=0 and G=1 are impossible

### G=0

All four X-vertices are regular. If none raises q, four pairwise-disjoint K9 supports are required, needing36 core vertices. The core has35. Contradiction.

### G=1

Exactly one X-vertex has decoration1 and the other three are regular. Three disjoint plateau supports consume27 core vertices, leaving only8.

The decorated X-vertex has core-row size

`d_M(x)+g_x=9+1=10`.

But lexicographic maximality forces this row to avoid all27 plateau-support vertices. It would have to fit10 vertices inside an 8-point remainder. Contradiction.

## 5. G=2 concentrated decoration is impossible

If the two decoration units lie on one X-vertex, the other three X-vertices are regular and again require three disjoint K9 supports occupying27 core vertices.

The decorated vertex now has row size11 and must avoid those27 vertices, impossible inside the remaining8.

## 6. Unique residual

The only K4,9 plateau state not eliminated by the preceding argument is therefore

- `G=2` split as `1+1` on two X-vertices;
- exactly two regular X-vertices x1,x2;
- their plateau supports D1,D2 are disjoint pure K9s of globally degree13 vertices;
- `|D1 union D2|=18`;
- letting `L=H\(D1 union D2)`, `|L|=17`;
- the two decorated X-rows (each of size10) and all nine Y-rows (each of size4) lie entirely inside L.

The shell-core incidence count checks exactly:

`9+9+10+10+9*4 = 74 = 2q-G` for q=38,G=2.

Thus the entire source-reported K4,9 theorem is reduced independently to one 17-point residual incidence system.

This file does not yet eliminate that final split-decoration residual.
