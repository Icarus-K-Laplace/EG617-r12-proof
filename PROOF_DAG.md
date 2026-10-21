# Canonical proof DAG

## Target

`Original EG617 r=12 counterexample -> contradiction`.

## Front-end DAG — current state

```text
Hypothetical balanced K145 / least-edge colour G
        |
        v
minimum-degree anchor + maximal genuine-K12 packing
        |
        v
contextual recurrence under temporary
"this fixed G has no induced R(4,49)" hypothesis
        |
        v
1752-node / 144-stop certificate
        |
        v
T61 unique stop: d=11, six genuine K12 blocks, 61 residual vertices
        |
        +--> z=0: anchor N[v] is a genuine K12 [PROVED]
        |
        +--> alpha(R)=5 [PROVED]
        |
        +--> delta(R)=12 branch [CLOSED]
        |       |
        |       +--> generic R(4,48) floor 310 [PROVED]
        |       +--> q20 leaf-rotation contradiction [PROVED]
        |
        +--> delta(R)=13
                |
                +--> E397 [CLOSED: q22 / zero-decoration support contradiction]
                |
                +--> E398 [CLOSED: exact q23 shell]
                |
                +--> E399 [CLOSED: exact q24 cells]
                |
                +--> E400 [CLOSED: uniform q25 shell theorem]
                |
                +--> E401..E408 [ACTIVE LINE A]
                        |
                        +--> E401: s=4, total excess9
                        +--> q25 extension (21,4) [OPEN]
                        +--> q26 cells G=1..4 [OPEN]
```

Therefore the front-end residual statement is now

`T61 survivor => delta=13 and 401<=E<=408`.

The master dichotomy remains

`K145 counterexample -> induced R(4,49) OR T61`.

## Front-end reusable ladder

```text
matching-transversal rigidity
        |
        +--> seven/eight genuine-block independence bounds
        +--> anchor defect z=0

q20 equality classification
        |
        +--> R(4,48) floor 310
        +--> T61 h12 closure

E=397+s, degree13 pivot
        |
        +--> neighbour degree-excess <= s
        +--> q23 shell theorem -> E398 closed
        +--> q24 shell theorem -> E399 closed
        +--> q25 shell theorem -> E400 closed
        +--> q26 / parameterized q=22+r stability [ACTIVE]
```

## Backend DAG

For every legitimate `F in R(4,49)`:

```text
degree-13 pivot
   |
   +--> e(F)=91+q+e(H)
   +--> CORE211: e(H)>=211
   +--> q28 profitable repivot
   +--> q29 generic good-repivot
   +--> uniform q27 contradiction
   |
   v
E329,E330,E331 excluded
   |
   v
E332 survivor => q30 + 211-core [ACTIVE LINE C]
```

High backend:

`E333..E340 -> uniform stability problem [ACTIVE LINE B]`.

## Final certification condition

EG617 r=12 may be declared proved only after BOTH:

1. the remaining T61 h13 window E401..E408 is excluded or always yields an induced R(4,49);
2. every legitimate R(4,49) backend layer is eliminated.
