# High backend right edge: atomic-defect theorem for q36--q38

Status: `PROVED` under the standard legal R(4,49) shell/core contract.

This subline is deliberately disjoint from the Astra-B E333 repeated-pair/core-support assignment. It targets the right edge E338--E340.

## 1. Ceiling states and tiny core excess

For a legal residual F in R(4,49), every degree-13 pivot satisfies

`e(F)=91+q+e(H)`,

where H in R(3,35), `e(H)>=211`, `delta(H)>=12`.

Hence the charge ceilings are

- E338: q<=36;
- E339: q<=37;
- E340: q<=38.

Equality with the ceiling is equivalent to `e(H)=211`. Therefore the ceiling-core total excess above degree12 is always

`sum_{v in H}(d_H(v)-12)=2`.

The only 211-core degree multisets are `14,12^34` and `13^2,12^33`.

## 2. Exact repivot notation

At a ceiling pivot p, let A be the 13-shell, M its missing graph, and y an undecorated shell vertex. Put

- `d=d_M(y)`;
- `S=N_M(y)`;
- `D=N_H(y)`, |D|=d;
- `rho=e_M(A\S)+G_{A\S}`;
- `h=sum_{v in D}(d_H(v)-12)`;
- `kappa=C(d,2)-e_H(D)`;
- `b=e_F(S,D)`.

The exact repivot identity is

`q_y-q = d(13-d)+rho+h+kappa+b-(q)`,

equivalently

`q_y-q = d(13-d)+rho+h+kappa+b-q`.

All four correction terms are nonnegative integers.

## 3. No regular missing degree5--8 at a ceiling pivot

At a q-maximal ceiling pivot, q_y<=q for every legal regular repivot. Hence

`d(13-d)<=q`.

For q in {36,37,38},

`d(13-d)>q`

for d=5,6,7,8. Therefore every regular shell missing degree lies in

`{0,1,2,3,4,9,10,11,12}`.

## 4. Atomic defect budget for d=4 or9

For d=4 or9,

`d(13-d)=36`.

Write

`q=36+s`, `s in {0,1,2}`.

Then

`q_y-q = rho+h+kappa+b-s`.

Maximality q_y<=q gives the exact inequality

> `rho+h+kappa+b <= s`.  (AD)

Thus:

### q=36

`s=0`, so

`rho=h=kappa=b=0`.

Every d4/d9 repivot is a zero-defect plateau exchange:

- all shell charge outside S vanishes;
- D induces a clique in H;
- every D-vertex has H-degree12;
- S is target-anticomplete to D.

### q=37

`s=1`. At most one unit can occur among the four defect coordinates

`(rho,h,kappa,b)`.

### q=38

`s=2`. The total atomic defect across the same four coordinates is at most2.

This is an analytic replacement for the q36--q38 scalar defect-table statement: every actual d4/d9 ceiling exchange lies in the integer simplex

`rho+h+kappa+b<=q-36`.

## 5. Consequence for the right-edge program

The high backend right edge can now be attacked by classifying only:

1. zero-defect d4/d9 plateau systems at q36;
2. one-defect perturbations at q37;
3. at-most-two-defect perturbations at q38.

The already reported K4,9 theorem is one zero-/low-defect subfamily, but this theorem does not assume the shell is complete bipartite and does not treat necessary scalar states as realized graphs.

No edge layer E338--E340 is declared closed here.
