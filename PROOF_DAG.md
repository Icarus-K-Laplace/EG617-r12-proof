# Canonical proof DAG

## Target

`Original EG617 r=12 counterexample -> contradiction`.

## Front-end DAG

```text
Hypothetical K_145 counterexample
        |
        v
outer forcing / block construction
        |
        v
seven genuine K_12 blocks
        |
        v
61-point residual (O61-type parent contract)
        |
        +--> S27  -- closed under certified contract
        |
        +--> S31  -- strict descent to q <= 30 under explicit parent contract
        |
        +--> S30  -- ACTIVE
        |
        v
force eighth genuine K_12 block OR contradiction
        |
        v
49-point residual F
        |
        +--> alpha(F) <= 4 under the genuine eight-block theorem
        +--> prove inherited target-clique cap / omega(F) <= 11
        |
        v
F in R(4,49)
```

Current front-end status: **OPEN**. The key missing implication is the clean-room forcing from the original counterexample through O61/S30 to a legitimate 49-point residual.

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
   +--> e(F) = 91 + q + e(H)
   +--> CORE211: e(H) >= 211
   +--> q=28 profitable repivot
   +--> q=29 + delta(H)>=12 => degree-13 good repivot y with q_y>=30
   +--> uniform q=27 contradiction (dependency must remain audited)
   |
   v
E329, E330, E331 excluded
```

Important scope separation for q29:

```text
q29 good-repivot existence theorem
    DOES NOT require e(H)=211

E331 fixed-edge corollary
    uses CORE211 separately to force q_y<=29
    and hence contradicts the q29 theorem
```

Then:

```text
E332 survivor => (q,e(H)) = (30,211)
   |
   v
q30 equality system over almost-12-regular 211-core  [ACTIVE LINE C]
```

High layers:

```text
E333 ... E340
   |
   v
seek uniform repivot / core-excess stability theorem  [ACTIVE LINE B]
```

## Final certification condition

EG617 `r=12` can be declared proved only after BOTH are complete:

1. `K_145 -> legitimate F in R(4,49)`;
2. `R(4,49) = empty` under the inherited residual contracts actually established by the front-end.
