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
        +--> z=0, alpha(R)=5
        |
        +--> delta=12 branch [CLOSED]
        |
        +--> delta=13
                |
                +--> E397 [CLOSED]
                +--> E398 [CLOSED]
                +--> E399 [CLOSED]
                +--> E400 [CLOSED]
                +--> E401..E404 [SOURCE-REPORTED PROVED: V6]
                +--> E405 [SOURCE-REPORTED PROVED: V7]
                |
                v
             E406..E408 [ACTIVE LINE A]
                |
                +--> E406 assistant-owned coexistence line
                |       +--> d=2 [CLOSED]
                |       +--> d=3 [CLOSED IN FULL]
                |       |       +--> Type-B [CLOSED]
                |       |       +--> Type-A O5 [CLOSED]
                |       |       +--> Type-A O4 four doubles [CLOSED]
                |       |       +--> Type-A O4 one triple + two doubles [CLOSED, eta0/eta1]
                |       |       +--> Type-A O4 two triples [CLOSED]
                |       |       +--> Type-A O4 four-full + double [CLOSED]
                |       +--> d=10 [CLOSED]
                |       +--> d=11 [CLOSED]
                |       +--> d=1 [OPEN]
                |       +--> d=12 [OPEN]
                |
                +--> E407,E408 Astra-A line
                        +--> V8 rho<=k-1 theorem [SOURCE-REPORTED]
                        +--> E407 low-Q maximum Q=27 [OPEN]
                        +--> E408 low-Q maximum Q in {27,28} [OPEN]
                        +--> correction-cycle compatibility [OPEN]
```

Latest package-level T61 window:

`E406..E408, delta=13`.

Within E406, the mathematical frontier is now exactly `d=1` and `d=12`.

## Backend DAG

For every legal `F in R(4,49)`:

```text
degree13 pivot
   |
   +--> e(F)=91+q+e(H)
   +--> CORE211
   +--> q28 profitable repivot
   +--> q29 generic good-repivot
   +--> uniform q27 contradiction
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

The only remaining legal R(4,49) backend interval is

`E333..E340 [ACTIVE LINE B]`.

Line-B V4 reports the support-repetition reduction to necessary families

`D2-A,D2-B,D2-C,D2-D,R9`

with repetition lower bounds `8,8,5,7,9`. These are necessary shell structures only, not realized graphs.

## Final certification condition

EG617 r=12 may be declared proved only after BOTH:

1. T61 `E406..E408` is closed, with E406 now reduced to `d1/d12`;
2. every legal R(4,49) layer `E333..E340` is eliminated.

There is no remaining E332 obligation.