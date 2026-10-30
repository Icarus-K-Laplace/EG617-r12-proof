# E408/Q32 parent-to-core contract mapping

Date: 2026-10-30  
Status: **FOUR CORE ITEMS SOURCE-MAPPED; MINIMUM-DEGREE ITEM NOT INDEPENDENTLY CERTIFIED. PARENT PROMOTION BLOCKED.**

## 1. Parent construction

Let F be the genuine 61-point T61 target residual and p a target-degree-13 pivot. Put A=N_F(p) and

    H = F - N_F[p].

Then |H|=61-1-13=47. The front-end edge identity is

    e(F)=91+q+e(H).

For the E408/Q32 charge q=32 and e(F)=408, this gives

    e(H)=408-91-32=285.

The point p is anticomplete to H. Since alpha(F)<=5, alpha(H)<=4. Since H is induced in F and omega(F)<=11, omega(H)<=11.

These four mappings are direct and do not use any sibling support theorem.

## 2. Five-item contract table

| U6 hypothesis | Parent derivation | Audit status |
|---|---|---|
| |H|=47 | 61-point T61 residual minus pivot and its 13-neighborhood | VERIFIED |
| e(H)=285 | e(F)=408, q=32, identity e(F)=91+q+e(H) | VERIFIED |
| alpha(H)<=4 | p is anticomplete to H and alpha(F)<=5 | VERIFIED |
| omega(H)<=11 | H is induced in F and omega(F)<=11 | VERIFIED |
| delta(H)>=12 | Imported through the E406 47-core minimum-degree theorem and the lower-order R(3,35) seed | **NOT INDEPENDENTLY CERTIFIED** |

The total excess six is then an identity, not another parent premise:

    2e(H)-12|H| = 570-564 = 6.

## 3. Exact dependency chain for the unresolved minimum degree

The current root proof chain is:

1. E406_CORE_MINDEG_288.md assumes a 47-core C in R(4,47), e(C)<=288, and proves delta(C)>=12.
2. In its degree-11 contradiction, it deletes the degree-11 pivot and its 11 neighbors, obtaining a 35-point graph J in R(3,35).
3. It invokes CORE211.md to obtain e(J)>=211.
4. CORE211.md states e(J)>=211 for every J in R(3,35). Its clean 210-edge AES contradiction is fully recovered in INTEGRATED1_CORE211_AUDIT.md, but that audit explicitly says the lower-order input delta(J)>=12 has not been recovered self-containedly.
5. The same audit says the proof of delta(J)>=12 calls a previously audited “23-neighbourhood / cap-two exclusion”. The repository still needs that lemma as a standalone proof/certificate or an exact bibliographic/certificate dependency.

This is a proof-body gap, not a counterexample to the minimum-degree theorem. The current ASSUMPTION_LEDGER.md labels the L2 seed PROVED, while INTEGRATED1_CORE211_AUDIT.md labels the recovery PARTIAL_STANDALONE_RECOVERY and explicitly records the missing A4 dependency. V9 also lists the minimum-degree seed as retained input, not as a theorem newly proved by V9. The conflict must be resolved by recovering the A4 proof/certificate or supplying its exact external source and checking the hypotheses.

## 4. Fail-closed conclusion

The Q32 terminal's frozen contract states delta(H)>=12, but a frozen contract is not by itself a proof that the genuine T61 parent always satisfies it. Until the lower-order 23-neighbourhood / cap-two exclusion is recovered and checked, the parent implication

    genuine E408/Q32 parent => all five U6 hypotheses

remains conditional.

Do not replace this gap by:
- treating the status label PROVED in ASSUMPTION_LEDGER.md as a replay;
- assuming the 47-core minimum degree follows from e(H)=285 alone;
- importing a sibling branch's local closure;
- promoting U6 to a root theorem.

The shortest next task is to recover the exact A4 artifact named by the Integration 1 audit, prove its hypotheses match R(3,35), and independently replay any finite certificate it uses. If it cannot be recovered, re-prove delta(J)>=12 directly from the R(3,35) definition and hereditary D(n) caps.
