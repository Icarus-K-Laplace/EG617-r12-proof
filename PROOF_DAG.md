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
T61: d=11, six K12 in U, residual order61
     397 <= E <= 408
     delta in {12,13}
        |
        +--> alpha(R)=5 exactly [PROVED]
        |
        +--> anchor defect z=0 [PROVED]
        |       |
        |       v
        |    N[v] is a genuine K12
        |    seven genuine K12 blocks total
        |
        +--> h12 branch
        |       |
        |       +--> R(4,48) floor309 [PROVED]
        |       +--> E>=407 [PROVED]
        |       +--> E407 => outer (q,C48)=(20,309)
        |       +--> E408 => (20,310) or (21,309)
        |       |
        |       +--> C48=309 => inner q20 + H35=211
        |               |
        |               +--> shell M = K_{2,r}+isolates, 6<=r<=10
        |               +--> two 10-rows overlap >=7
        |               +--> finish contradiction [OPEN]
        |
        +--> h13 branch, E397..408 [OPEN]
                |
                +--> low-edge degree-excess / multi-pivot attack [ACTIVE]
                +--> if E406 and delta13, S31 q<=30 [PROVED interface]
                +--> T61->S30 coverage [OPEN]
```

Thus the proved front-end dichotomy remains:

`K145 counterexample -> legitimate induced R(4,49) OR tightened embedded T61`.

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

The new `z=0` theorem creates seven genuine blocks total but does NOT reverse the eight-block implication and does NOT itself produce a 49-point residual.

### S30 scope

```text
specified row-labelled (5,7,8,8)
   |
   +--> k2 singleton triangle closed [PROVED]
   +--> k0/k1 saturation lemmas
   +--> 14 + 13 scalar cases remain [OPEN]
```

No theorem currently maps all T61 states into this macro contract.

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
    applies CORE211 separately
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
uniform repivot / core-excess stability [ACTIVE LINE B]
```

## Final certification condition

EG617 r=12 may be declared proved only after BOTH are complete:

1. tightened embedded T61 is excluded or always yields a legitimate induced R(4,49);
2. every legitimate R(4,49) backend layer is eliminated.
