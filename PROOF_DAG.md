# Canonical proof DAG

## Target

`Original EG617 r=12 counterexample -> contradiction`.

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
                +--> E401..E408 [ACTIVE LINE A]
                        |
                        +--> q25 (21,4) extension [OPEN]
                        +--> q26 G=1..4 cells [OPEN]
                        +--> parameterized q=22+r stability [TARGET]
```

Current front-end terminal:

`T61 survivor => delta=13 and 401<=E<=408`.

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
E332 survivor => q30 + 211-core
   |
   +--> undecorated d=4..9 [PROFITABLE -> CLOSED]
   |
   +--> d10 equality
   |       |
   |       +--> pure K3,10
   |       +--> K10/K3 row geometry
   |       +--> overlap/coverage contradiction
   |       v
   |     [CLOSED]
   |
   +--> d3 equality
   |       |
   |       +--> Type A/B only
   |       +--> row classes 3+3+3 or 3+3+2
   |       +--> four simultaneous pivot views
   |       +--> 156 required vs 120 available incidences
   |       v
   |     [CLOSED]
   |
   v
extreme-degree q30 shell [ACTIVE LINE C]
   |
   +--> every undecorated degree in {0,1,2,11,12}
   +--> at most two high regular vertices
   +--> G>=4
   +--> G=4 => exact (h,k,l)=(2,4,7)
   |
   v
eliminate G=4..8 [OPEN]
```

High backend:

`E333..E340 -> uniform stability problem [ACTIVE LINE B]`.

## Final certification condition

EG617 r=12 may be declared proved only after BOTH:

1. the remaining T61 h13 window E401..E408 is excluded or always yields an induced legal R(4,49);
2. E332 and E333..E340 are eliminated for every legal R(4,49).
