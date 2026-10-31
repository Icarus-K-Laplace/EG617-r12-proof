# Canonical proof DAG

## Target

`Original EG617 r=12 counterexample -> contradiction`.

The full theorem is **NOT_CERTIFIED**.

## Front-end DAG

```text
Hypothetical balanced K145 / least-edge colour G
        |
        v
contextual recurrence under temporary no-R(4,49) extraction
        |
        v
1752-node / 144-stop certificate
        |
        v
T61 unique stop
        |
        +--> delta=12 branch [CLOSED]
        |
        +--> delta=13
                |
                +--> E397 [CLOSED]
                +--> E398 [CLOSED]
                +--> E399 [CLOSED]
                +--> E400 [CLOSED]
                +--> E401..E404 [CLOSED, CANONICAL REPLAY]
                |       +--> <=288 core interface
                |       +--> EDGE13
                |       +--> uniform q<=29,G<=7 promotion to q>=30
                |       +--> pure q23/q24 shell lemmas
                |       +--> high-low excess support/cut
                +--> E405 [CLOSED, CANONICAL REPLAY]
                |       +--> no embedded R(3,36)
                |       +--> every actual47-core delta>=11
                |       +--> q25/q26 promotion
                |       +--> high-low cut -> Q>=27
                |       +--> Q27..29 promoted, Q30 -> q>=31
                +--> E406 [CLOSED, CANONICAL]
                |       +--> S31: exists q<=30 pivot
                |       +--> low-to-q30 bridge [PROVED]
                |       +--> q30 hereditary promotion [PROVED]
                |       +--> actual q30 -> q31 final edge
                |               +--> d=1 [CLOSED]
                |               +--> d=2 [CLOSED]
                |               +--> d=3 [CLOSED]
                |               +--> d=10 [CLOSED]
                |               +--> d=11 [CLOSED]
                |               +--> d=12 [CLOSED]
                |
                v
             E407,E408 [ACTIVE LINE A]
                |
                +--> V8 rho<=k-1 theorem [SOURCE-REPORTED]
                +--> E407 low-Q maximum Q=27 [OPEN]
                +--> E408 low-Q maximum Q in {27,28} [OPEN]
                +--> correction-cycle compatibility [OPEN]
```

Thus the continuous repository-canonical h13 closure is

`E397..E406`.

The active T61 edge window is exactly

`E407,E408`.

## Backend DAG

For every legal `F in R(4,49)`:

```text
degree13 pivot
   |
   +--> e(F)=91+q+e(H)
   +--> CORE211
   +--> q27/q28/q29 repivot machinery
   |
   v
E329,E330,E331 excluded
   |
   v
E332 q30+211 equality frontier
   |
   +--> d=4..9 profitable
   +--> d10 equality closed
   +--> d3 equality closed
   +--> extreme-degree shell reduced to G=4..8
   +--> G4,G5,G6,G7 closed
   +--> G8 h1 -> h0
   +--> G8 h0 unified closure
   |
   v
E332 = EMPTY [CLOSED AND FROZEN]
```

The only remaining legal `R(4,49)` backend interval is

`E333..E340 [ACTIVE LINE B]`.

Line-B V4 reports necessary families

`D2-A,D2-B,D2-C,D2-D,R9`

with repetition lower bounds `8,8,5,7,9`; these are not graph realizations.

## Final certification condition

EG617 r=12 may be declared proved only after BOTH:

1. T61 `E407,E408` is closed;
2. every legal `R(4,49)` layer `E333..E340` is eliminated.

There is no remaining E332 or E397--E406 obligation.
