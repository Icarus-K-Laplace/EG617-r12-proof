# T61 generalization map

| r=12 object | candidate r-form | classification | status / reason |
|---|---|---|---|
| `145` | `r^2+1` | exact symbolic | `PROVED_SYMBOLIC` original problem order |
| least-color `870` | `r(r^2+1)/2` | exact symbolic | `PROVED_SYMBOLIC` averaging |
| anchor degree `11` | `r-1` | structural stop parameter | `PROVED_SYMBOLIC` once this stop is reached; forcing is `OPEN` |
| genuine `K12` | genuine `K_r` | exact symbolic | `PROVED_SYMBOLIC` |
| six anchored blocks | `r-6` blocks | exact symbolic | produces `5r+1`; forcing is `OPEN` |
| `61` | `5r+1` | exact symbolic | `PROVED_SYMBOLIC`, not numerology |
| seven unanchored blocks | `r-5` blocks | conditional equality artifact | at r=12 follows after `z=0`; general `z=0` is not forced |
| `49` | `4r+1` | exact symbolic | next packing level `j=r-5` |
| `alpha_61<=5` | `alpha(R)<=5` | exact symbolic | greedy representatives |
| `alpha_61=5` | `alpha(R)=5` | contextual symbolic | under no `(4r+1)` residual |
| `omega_61<=11` | `omega(R)<=r-1` | exact symbolic | maximal `K_r` packing |
| `delta_61>=12` | `delta(R)>=r` | contextual symbolic | nonneighbourhood extraction argument |
| `delta in {12,13}` | `delta in {r,r+1}` | small-r budget artifact | **DISPROVED_AS_GENERAL_PATTERN** from same ledger for `r>=16` |
| outer base `408` | `3r^2-2r` | exact symbolic | anchor ledger |
| lower edge `397=408-11` | no linear analogue from present ledger | fixed-r small-slack artifact | general outer charge is `Theta(r^2)` for `r>=20` |
| `z=0`, anchor `K12` | `z=0`, anchor `K_r` | fixed-r equality artifact | **DISPROVED_AS_GENERAL_PATTERN as forced by the r12 argument** |
| h13 shell `13` | shell size tied to local min degree, not terminal definition | backend/local | do not promote |
| q22--q31 windows | symbolic only after additional core floors | local equality layers | not part of `T_r` |
| q30/q31 promotion | repivot backend phenomenon | sibling-workstream object | excluded from this line |
| common `K11` | possible `K_(r-1)` equality shadow | finite-equality hint only | `OPEN`; no general classification claimed |
| five-template coexistence | possibly reflects `alpha=5` / five target groups | finite-geometry hint | `CONJECTURE` only until derived symbolically |
| correction allowances | defect variables in an `O(r)` edit system | robust analogue exists | replace fixed templates by multicolor edit/overlap budget |
| shell structure | local pivot equality structure | not terminal-defining | r=12 source only |

## Main interpretation

The quantities `61`, `49`, `11`, `12`, and the block counts have clean symbolic ancestors. The detailed E397--E408 q-windows and coexistence templates do not.

The appropriate general replacement for fixed template casework is the exact local multicolor slack identity plus the `O(r)` simultaneous stability theorem: the terminal is forced near a partial resolvable `TD(5,r)`, rather than forced into the literal r=12 shell templates.
