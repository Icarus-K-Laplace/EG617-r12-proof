# E406 d=3 Type-A: exact O=5 exceptional reduction

Status: `PROVED` for the reduction below. The Type-A d3 branch and E406 remain `OPEN`.

Dependencies:

- `E406_D3_FOUR_TRIANGLE_COMPRESSION.md`;
- `E406_D3_REMAINDER_SATURATION.md`;
- `E406_D3_O5_COMPRESSION.md`.

We work in Type A with `eta=1` and `O=5`. Then

- `R=1`;
- `e(H)=151`;
- total H-core excess is exactly3;
- the unique partial incidence enters the unique internally-defective support triangle;
- every H vertex satisfies `epsilon_x+s_D(x)=1`, so `epsilon_x` is 0 or1;
- the surviving O5 branch has a singleton partial carrier, so every multi-full vertex has `r_x=0`.

Each of the four support rows has ten full H-carriers. Let `m` be the number of multi-full H vertices. Since `O=sum(k_x-1)=5` and four-full vertices are already impossible, the multi-full membership increments are only1 (double) or2 (triple).

## 1. Exact three-family enumeration

### m=3

The increment partition is necessarily `2+2+1`: two triple-full vertices and one double. The pure classes contain31 vertices. Since each pure class has size at most8, the sorted pure profile is forced to be

`(7,8,8,8)`.

Every triple among these four rows has pure-size pattern `(8,8,8)` or `(7,8,8)`, both already excluded by the triple-full transversal lemma. Thus `m=3` is impossible.

### m=4

The increment partition is `2+1+1+1`: one triple and three doubles. The pure classes contain30 vertices, hence the only sorted profiles are

`(6,8,8,8)` or `(7,7,8,8)`.

For `(6,8,8,8)`, the triple must contain the 6-class; otherwise it is `(8,8,8)`. Therefore its type is exactly `(6,8,8)`.

For `(7,7,8,8)`, the triple must contain both 7-classes; otherwise it is `(7,8,8)`. Therefore its type is exactly `(7,7,8)`.

### m=5

All five multi-full vertices are doubles. The pure classes contain29 vertices. The only sorted profiles are

`(5,8,8,8)`, `(6,7,8,8)`, `(7,7,7,8)`.

The first and third profiles are already eliminated by `E406_D3_O5_COMPRESSION.md`. Hence only `(6,7,8,8)` remains.

Therefore every surviving Type-A eta=1,O=5 state belongs to exactly one of:

- **Family A:** pure profile `(6,8,8,8)`, one `(6,8,8)` triple and three doubles;
- **Family B:** pure profile `(7,7,8,8)`, one `(7,7,8)` triple and three doubles;
- **Family C:** pure profile `(6,7,8,8)`, five doubles.

## 2. Every surviving triple must have epsilon=1

Let x be a triple-full vertex. Since the unique partial carrier is a singleton, `r_x=0`.

### Triple type (6,8,8)

Assume `epsilon_x=0`. Then x has H-degree3. Let `a,b,c` be its missing-set sizes in the three pure classes. Since the class sizes sum22,

`a+b+c>=19`,

with `a<=6`, `b,c<=8`.

The triple-transversal lemma requires at least

`min(ab,ac,bc)`

cross edges among the three missing sets. The minimum under these constraints is24, attained at `(a,b,c)=(3,8,8)` up to order.

Pure vertices in a 6-class have at most4 external H-neighbours plus excess; pure vertices in an 8-class have at most2 plus excess. Since the global H-excess is only3, the total degree capacity available to cross edges is at most

`floor((4a+2b+2c+3)/2)`.

At `(3,8,8)` this is23, and every other feasible missing-set distribution only strengthens the gap. Contradiction.

Thus a `(6,8,8)` triple has `epsilon_x=1`.

### Triple type (7,7,8)

Assume `epsilon_x=0`. Again x has H-degree3 and its missing-set sizes satisfy

`a+b+c>=19`,

with `a,b<=7`, `c<=8`.

The smallest transversal requirement is at least28, for example at `(4,7,8)`, whereas the total external-degree capacity, even after allowing all three H-excess units to lie in the missing sets, is at most

`floor((3a+3b+2c+3)/2)<=26`

at the extremal boundary; all other feasible distributions are stronger. Contradiction.

Hence a `(7,7,8)` triple also has `epsilon_x=1`.

By the saturated identity `epsilon_x+s_D(x)=1`, every surviving triple is therefore anticomplete to the shell-side D.

## 3. Family B is impossible

In Family B the triple already consumes one of the three H-excess units.

The remaining three multi-full vertices are doubles among row sizes `7,7,8,8`.

- an `8-8` double costs at least6 excess units and is impossible;
- every `7-8` or `7-7` double must itself have positive excess under the global budget3, by the pair-overlap lemma in `E406_D3_O5_COMPRESSION.md`.

Thus all three doubles each consume at least one excess unit, in addition to the triple's one unit. Total H-excess is at least4, contradicting the exact budget3.

Therefore Family B is empty.

## 4. Exact incidence orientation of Family A

Label the 6-class A and the three 8-classes B,C,D. The `(6,8,8)` triple may be labelled ABC.

The special full-row deficits are `(4,2,2,2)`. After the triple contributes `(1,1,1,0)`, the residual deficit is `(3,1,1,2)`.

An `8-8` double is impossible. Therefore all three doubles must be incident with A. Their A-degree is exactly3. The singleton partial carrier cannot lie in A (else only two A-incidences would remain for three doubles), and cannot lie in an 8-class of residual deficit1 if that would force an 8-8 double. The unique solution up to symmetry is:

- doubles `AB, AC, AD`;
- singleton partial carrier full to row D.

Thus Family A has a unique row-labelled orientation up to the symmetry swapping B and C.

The triple ABC has epsilon1 and is D-anticomplete. Only two H-excess units remain for all three `(6,8)` doubles and the pure classes.

## 5. Exact incidence count of Family C

Label the classes by sizes `A=6`, `B=7`, `C=D=8`.

The special full-row deficits are `(4,3,2,2)`. The singleton partial carrier cannot use an 8-class (the usual singleton-full-row K12 restriction), so it is full to A or B.

There are five doubles and no `C-D` double, since an `8-8` double alone exceeds the total excess budget.

Hence:

- if the singleton is full to A, the double multigraph has degree sequence `(3,3,2,2)`, so exactly two doubles avoid A; both are `B-8` doubles and hence both have epsilon1;
- if the singleton is full to B, the double multigraph has degree sequence `(4,2,2,2)`, so exactly one double avoids A; it is a `B-8` double and has epsilon1.

Thus Family C has either exactly two or exactly one forced positive-excess `B-8` double(s). The remaining doubles are of types `(6,7)` or `(6,8)` and must fit the residual excess budget.

## 6. Current Type-A O5 frontier

The entire eta=1,O=5 branch is now reduced to only two exact mechanisms:

1. **Family A:** unique labelled pattern `(6,8,8,8)` with triple ABC, doubles AB/AC/AD, one singleton partial carrier on D, and only two H-excess units left after the triple;
2. **Family C:** `(6,7,8,8)` with five doubles, one or two forced positive `7-8` doubles depending on the singleton row.

No other Type-A O5 state survives.