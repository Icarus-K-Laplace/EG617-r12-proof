# E408 Q32 — double-track vertices force alpha(H[R]) <= 3 in the 3+7 cell

Date: 2026-10-28  
Status: **PROVED local theorem; exact residual-type pruning.**

## 1. Immediate obstruction

In the 3+7 cell, a double-track outer vertex q has two common labels across the three small blocks. It must receive all three extra small-to-outer edges, so `k(q)=3). Since each outer vertex has degree 12 and already has nine mandatory base Q-neighbors, `e_Q(q)+d_R(q)=3); hence `e_Q(q)>=3) and
[
d_R(q)=0.
]

Therefore, if `alpha(H[R])=4), an independent 4-set in R together with q is an independent 5-set in H. Thus
[
oxed{\text{double-track vertex exists }\Longrightarrow\alpha(H[R])\le3.}
]

This is stronger than the previous fiber-size cap alone.

## 2. Exact residual-type pruning

In the disconnected 3+7 cell, `e(H[R])=3+z), `z in {0,1,2,3,4}`, `Delta(H[R])<=2`, and the registered 18-type list is in `verify_v47_m10_residual_path_cycle_types.py`. Its independence numbers yield:

| z | e(H[R]) | Residual graph types with alpha=3 (double-track still possible) |
|---:|---:|---|
| 0 | 3 | none |
| 1 | 4 | none |
| 2 | 5 | `C3 dot-union 2P2` |
| 3 | 6 | `2C3 dot-union K1`, `C3 dot-union P4`, `C5 dot-union P2` |
| 4 | 7 | `C7`, `C3 dot-union C4` |

All other listed residual types have independence number four and therefore forbid any double-track vertex.

Consequences:
- z=0,1: every outer vertex is singleton-track.
- z=2: a double-track can occur only when `H[R]=C3 dot-union 2P2`.
- z=3: only the three listed residual types can support a double-track.
- z=4: only `C7` and `C3 dot-union C4` can support a double-track.

Combine this with the already-proved double-track edge floor `n_h+n_j<=3` and the switch duplicate-fiber budget `n_s<=y_D). No global Q32 closure is claimed.
