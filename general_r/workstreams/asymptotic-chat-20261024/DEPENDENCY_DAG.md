# Dependency DAG — Asymptotic Synthesis

## Current headline DAG

```text
Problem 617 counterexample at r>=68
        |
        v
 H_A^ext: extract legal 4r+1 residual OR 5r+1 design terminal  [OPEN]
        |
        +-----------------------------+
        |                             |
        v                             v
  4r+1 induced residual          5r+1 design terminal
        |                             |
        v                             v
 residual-contract theorem       H_D robust nonextension [OPEN]
      r>=17 [PROVED]
        |
        v
 core H: |H|=3r-1, alpha<=3, omega<=r-1, delta>=r
        |
        +--> direct near-anchor triple
                  |
                  | if K<=7, parity => K<=6
                  v
           near-anchor reduction
                  |
                  v
           exact degree-r triple
                  |
                  v
     three-anchor AES theorem r>=68 [PROVED_ANALYTIC]
                  |
                  v
               K>=8
                  |
                  v
     q+epsilon = 3r+3-K/2
                  |
                  v
           q<=3r-1-epsilon
                  |
                  v
        medium d=4,...,r-3 impossible
                  |
        +---------+-----------------------+
        |             |          |        |
      d0/d1          d2         d3     high d>=r-2
        |             |          |        |
        |             |          v        v
        |             |      closed    <=3 owners,
        |             |                 <=9 shell kernel,
        |             |                 <=8 signatures
        +-------------+--------------------+
                      |
                      v
          H_C* remaining endpoint closure [OPEN]
                      |
                      v
             residual contradiction
```

Full theorem needs both H_A^ext branches to die.

## Newly closed front dependency

The following node is no longer open above r=17:

> from an extracted `4r+1` residual satisfying `alpha<=4`, `omega<=r-1`, and the inherited cap, derive `delta(F)=r+1`, an exact degree-(r+1) pivot, and core `delta(H)>=r`.

This is `PROVED_ANALYTIC` in the residual-extraction sibling. Consequently the asymptotic front blocker is strictly upstream: **extract 4r+1, or land in a controlled 5r+1 terminal**.

## Proven imported nodes

- hereditary cap and exact `4r+1` / `5r+1` order algebra;
- extracted-residual contract for r>=17;
- backend conservation and repivot identities;
- near-anchor reductions;
- exact three-anchor contradiction for r>=68;
- medium support exclusion;
- d3 common-S closure;
- high endpoint bounded kernel;
- exact affine-plane nonextension model.

## Open nodes blocking unconditional all-large-r

1. **A_ext:** upstream extraction / stopping classification;
2. **C-d2:** scalable d2 plateau/equality/positive-loss closure;
3. **C-d0/d1:** freeze/close the shallow endpoint sectors;
4. **C-high:** contradiction/improvement for remaining bounded high skeletons;
5. **D-stability:** classify the 5r+1 terminal into a nonextendable rigid design class.

## Non-blockers above 68

- residual core minimum-degree certification: proved from extracted residual for r>=17;
- Exact Three-Anchor H_B: derived analytically for r>=68.
