# Q33 support-promotion — canonical state

Updated: 2026-10-30  
Branch: \`workstream/r12-q33-support-promotion-20261030\`.

## Headline
**E408 Q33 support promotion: OPEN / NOT_CERTIFIED.**

## Current source-correct necessary-profile result

The fixed ten-four-core component assumption was audited and not promoted as source-universal. The current model instead allows every one of the ten exact-color K5 components to have c_i in {0,1,2,3,4} core vertices; c_i=5 is impossible by alpha(H)<=4. The gadget core has size7,...,11.

With the variable-core U/W gadget-reserve DP:
- m=8: v=31,32,33,34 excluded; first profile-feasible v=35,h=6,7,8.
- m=9: v=32,33,34 excluded; first profile-feasible v=35,h=9.
- m=10: v=34,35,36,37 excluded; first profile-feasible v=38,h=10.

The product enumerator and independent recursive option generator agree for every per-color option set; the global DP checks all47 (m,v) cells.

## Status
- Sharp gadget overlap cap4: **PROVED_CONDITIONAL** under Q⊂G_C and alpha(C[G_C])<=2.
- Variable-core reserve inequalities: **PROVED_CONDITIONAL** under exact-129 factor and seven-witness interface.
- Variable-core finite screen: **COMPUTATION_CERTIFIED**.
- Remaining graph-level cases: **OPEN**.
- Global E408 Q33: **OPEN / NOT_CERTIFIED**.
- EG617(r=12): **OPEN / NOT_CERTIFIED**.

The earlier fixed c_i=4 screen is retained only as a conditional special case; it is not used for the current source-correct frontier.


## 2026-10-30 correction — canonical component-only witness choice

The seven-witness source lemma supplies seven isolated-K5 component four-sets in every exact-129 color (six B-labelled components and, if needed, the pivot component's H-part). We may choose these seven component witnesses for every one of the m exact-129 colors. For this support family h=0 by construction; no gadget-witness existence is assumed.

The component-only variable-core screen is strictly stronger than the previous all-h diagnostic:
- m=8: v=31,...,38 excluded; first aggregate survivor v=39.
- m=9: v=32,...,39 excluded; first aggregate survivor v=40.
- m=10: v=34,...,40 excluded; first aggregate survivor v=41.

The exact component-only verifier is Q33_INDEPENDENT_VERIFIER.py. It compares Cartesian-product and recursive per-color option generation and checks all 47 registered (m,v) cells. The previous gadget-inclusive verifier is archived as Q33_VARIABLE_CORE_ALL_H_VERIFIER.py.

Status remains: reserve theorem PROVED_CONDITIONAL under the registered Q33 parent contract; finite profile screen COMPUTATION_CERTIFIED; graph-level cases and global Q33 OPEN / NOT_CERTIFIED.
