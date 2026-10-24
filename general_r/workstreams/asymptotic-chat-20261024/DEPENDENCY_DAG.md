# Dependency DAG — Asymptotic Synthesis

## Headline DAG

```text
Problem 617 counterexample at r
        |
        v
 H_A front extraction/dichotomy  [OPEN]
        |
        +-----------------------------+
        |                             |
        v                             v
  4r+1 legal residual            5r+1 design terminal
        |                             |
        |                             v
        |                        H_D robust nonextension [OPEN]
        |
        v
 core H: |H|=3r-1, alpha<=3, omega<=r-1, delta>=r
        |
        +--> inherited cap: K<=2r-2
        |
        +--> direct near-anchor triple
                  |
                  | if K<=7, parity => K<=6
                  v
           near-anchor reduction (r>=13)
                  |
                  v
           exact degree-r triple
                  |
                  v
     three-anchor AES theorem (r>=68) [PROVED_ANALYTIC]
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
        +---------+----------+
        |         |          |
      d0/d1      d2         d3             high d>=r-2
        |         |          |                    |
        |         |          v                    v
        |         |     common-S closed     <=3 owners,
        |         |     [PROVED cond.]      <=9 shell kernel,
        |         |                          <=8 signatures
        |         |                          [PROVED cond.]
        +---------+-------------------------------+
                  |
                  v
        H_C* remaining endpoint closure [OPEN]
                  |
                  v
          residual branch contradiction
```

Full theorem requires both branches of H_A to die:

```text
(residual contradiction) AND (H_D design contradiction)
                    |
                    v
                  P(r)
```

for every `r>=68`.

## Proven imported nodes

### Front algebra

- hereditary cap `D_r(n)`;
- exact orders `4r+1`, `5r+1` once the corresponding block count is reached;
- shell/core order `r+1` / `3r-1`;
- `alpha(H)<=3`, `omega(H)<=r-1`.

### Backend identities

- `e(F)=C(r+2,2)+q+e(H)`;
- `K=6r+6-2epsilon-2q`;
- regular repivot base `q_y>=d(r+1-d)`;
- common-S allowance and row closure;
- exact d2 one-loss charge identity.

### Anchor

- direct near-anchor forcing under the core contract;
- near-anchor to exact-anchor reduction for r>=13 under `K<=6`;
- exact three-anchor contradiction for r>=68.

### Endpoint

- medium d exclusion;
- d3 common-S closure under A+B;
- high endpoint at most three owners and finite kernel;
- d2 concentrated `K=8,a=3,b=1` state impossible for r>=13.

### Design exact model

- standard affine-plane `K_(r^2)` construction cannot be extended by one vertex.

## Open nodes that block unconditional all-large-r

1. **A-front:** symbolic recurrence/extraction and `delta(H)>=r` certification.
2. **C-d2:** scalable d2 plateau/equality/positive-loss closure.
3. **C-d0/d1:** freeze/close the shallow endpoint sectors.
4. **C-high:** contradiction/improvement for every finite high skeleton (unless absorbed into a broader C theorem).
5. **D-stability:** classify the 5r+1 terminal into an exact/robust nonextendable design family.

## Non-blocker above 68

Exact Three-Anchor H_B is no longer a separate blocker for the asymptotic theorem. It remains important only for lowering r0 below 68 and for finite-r completion.
