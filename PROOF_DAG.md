# Canonical proof DAG

## Target

`Original EG617 r=12 counterexample -> contradiction`.

## Front-end DAG — current clean state

```text
Hypothetical balanced K145 / least-edge colour G
        |
        v
minimum-degree anchor + maximal genuine-K12 packing
        |
        v
contextual induced-subgraph recurrence under temporary
"this fixed G contains no induced R(4,49)" hypothesis
        |
        v
1752-node / 144-stop arithmetic certificate
        |
        v
all outer stops excluded except one
        |
        v
T61: (d,j,a,n)=(11,6,5,61)
     397 <= E <= 408
     delta in {12,13}
     alpha<=5, omega<=11, inherited caps
        |
        +--> extract legitimate induced R(4,49)  [OPEN]
        |
        +--> prove T61 empty                      [OPEN]
```

This yields the proved dichotomy:

`K145 counterexample -> legitimate induced R(4,49) OR embedded T61`.

### Genuine-block side assets

```text
matching-transversal rigidity
        |
        v
equality rotation saturates all 12 cross slots
        |
        +--> 8 genuine K12 blocks -> legitimate R(4,49) [PROVED]
        |
        +--> 7 genuine K12 blocks -> alpha61<=5 [PROVED]
```

Do not reverse these implications. The existence of seven/eight genuine blocks is not automatic from the block lemmas.

### T61 downstream filters

```text
T61
 |
 +--> if E=406 and delta=13: S31 gives degree-13 pivot q<=30 [PROVED conditional interface]
 |
 +--> q27 core closure S27 only with its extra min-degree11 premise [scope-limited]
 |
 +--> canonical S30 macro contract [OPEN coverage]
 |
 +--> anchored six blocks -> seventh genuine unanchored block [OPEN; z=0 would suffice]
```

For the specified row-labelled S30 `(5,7,8,8)` branch:

```text
k2: uv,uw,vw -> analytic contradiction [PROVED]
k0/k1: new saturation lemmas remove many scalar cases
remaining: 14 scalar cases for k0, 13 for k1 [OPEN]
```

## Backend DAG

For every legitimate `F in R(4,49)`:

```text
degree-13 pivot
   |
   v
49 = 1 + 13 + 35
   |
   v
shell/core bookkeeping
   |
   +--> e(F)=91+q+e(H)
   +--> CORE211: e(H)>=211
   +--> q=28 profitable repivot
   +--> q=29 + delta(H)>=12 => degree-13 repivot y with q_y>=30
   +--> uniform q=27 contradiction
   |
   v
E329, E330, E331 excluded
```

Scope separation:

```text
q29 good-repivot existence theorem
    does NOT require e(H)=211

E331 corollary
    applies CORE211 separately to force q_y<=29
```

Then:

```text
E332 survivor => (q,e(H))=(30,211)
   |
   v
q30 equality system over almost-12-regular 211-core [ACTIVE LINE C]
```

High layers:

```text
E333 ... E340
   |
   v
uniform repivot / core-excess stability problem [ACTIVE LINE B]
```

## Final certification condition

EG617 `r=12` may be declared proved only after BOTH are complete:

1. embedded T61 is excluded or always yields a legitimate induced `R(4,49)`;
2. every legitimate `R(4,49)` backend layer is eliminated.
