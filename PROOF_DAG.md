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
        +--> delta=12 branch [CLOSED via R448>=310 + q20 rotation]
        |
        +--> delta=13
                |
                +--> E397 [CLOSED]
                +--> E398 [CLOSED: q23]
                +--> E399 [CLOSED: q24]
                +--> E400 [CLOSED: q25]
                +--> E401..E404 [SOURCE-REPORTED PROVED in V6; replay status tracked separately]
                +--> E405 [SOURCE-REPORTED PROVED in V7; replay status tracked separately]
                |
                v
             E406..E408 [ACTIVE LINE A]
                |
                +--> E406 assistant-owned coexistence line
                |       +--> final-rise d=2,10,11 [CLOSED]
                |       +--> d=3 Type-B [CLOSED]
                |       +--> d=3 Type-A: O5 [CLOSED]
                |       +--> d=3 Type-A O4 simple-four-double eta=0 [CLOSED]
                |       +--> d=3 Type-A O4 simple-four-double eta=1 [CLOSED]
                |       +--> active d=3 Type-A O4 multiplicities:
                |       |       one triple + two doubles;
                |       |       two triples
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

The evidence status of V6/V7/V8 remains explicitly tracked in the result ledgers; source-reported package results are not silently promoted beyond their audited scope.

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

Therefore the **only remaining legal R(4,49) backend interval** is

`E333..E340 [ACTIVE LINE B]`.

Latest Line-B source package V4 reports:

- support-repetition theorem for a maximal `(q,tau)` pivot;
- relevant distance class has size 9 or 10;
- at least five legal neighbours share one nonempty two-point missing set;
- D1 and the zero-defect two-hub family are excluded;
- remaining necessary shell families are `D2-A,D2-B,D2-C,D2-D,R9`, with repetition lower bounds `8,8,5,7,9`.

These are necessary shell structures, not realized graphs. No layer E333..E340 is closed yet.

## Final certification condition

EG617 r=12 may be declared proved only after BOTH:

1. the remaining T61 front-end window `E406..E408` is closed (or every survivor is forced into an already-eliminated legal R(4,49) branch under a certified interface);
2. every legal R(4,49) layer `E333..E340` is eliminated.

There is no remaining E332 obligation.