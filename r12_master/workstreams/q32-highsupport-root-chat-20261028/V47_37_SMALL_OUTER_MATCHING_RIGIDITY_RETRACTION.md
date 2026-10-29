# Audit correction: small-to-outer matching rigidity is RETRACTED

Date: 2026-10-29. Status: **RETRACTED / INVALID PROOF**.

The invalid step was charging both endpoints of a cut in the matching-coordinate partition to one small-side label s. The registered 4,5,5 switch theorem says the opposite: in a transposition switch, the two extra edges hit the two distinct moved labels, one each.

Exact local witness from `verify_three_block_switch_lemma.py`: `sigma=(0 1)`, `extra_ac=(0,1)`, `extra_bc=(0,0)`. With the two outer blocks as the theorem's A,B and the small block as C, the extra edges are `D_0 A_1` and `E_0 A_0`. This is a valid alpha<=4 configuration, so the two small endpoints are different.

Withdrawn conclusions:
- `p_D(s)` is constant across all outer blocks;
- all small-to-outer matching permutations are globally fixed by the cut argument;
- the derived global aligned/single-transposition dichotomy and its fiber-profile exclusions.

The seven-vertex minimum-degree-four cut-endpoint lemma remains correct, but its verifier checks only that graph-theoretic cut bound, not the invalid endpoint-charge premise.

The small-block degree ledger remains valid: `epsilon_s=e_A(s)+n_s-3>=0`, `sum epsilon_s=2`, `e_A(s)=3-n_s+epsilon_s`, and `sum e_A(s)=7`. The 4,5,5 local switch theorem and verifier remain valid. The independent z=0,1 track-partition alignment theorem is not withdrawn by this audit; its separate proof must stand on its own.

No global Q32 closure is claimed. EG617(r=12) remains **OPEN / NOT_CERTIFIED**.
