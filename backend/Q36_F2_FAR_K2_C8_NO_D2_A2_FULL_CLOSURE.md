# q36 f=2 far-target-K2 — c=8 no-d2, allowance two closure (RETRACTED)

Status: `RETRACTED`.

Reason: `Q36_F2_FAR_K2_D14_CONTRACT_CORRECTION.md` invalidated the D14 multiplicity shortcut used in the original owner-counting step.

Under the corrected far-K2 D14 interface

`3m + O_D + e_F(Y,D) + e_H(D) <= 14 + nu_Y`,

an A=2 repeated target-K3 support can still have multiplicity four when `nu_Y=1`. The original proof bounded repeated K3 multiplicity by three and therefore did not cover this equality channel.

Many later row-closure / sunflower arguments in the old file may remain reusable, but the file as a full closure is not certified.

Current task: rebuild A=2 under the corrected contract, in particular the `nu_Y=1`, multiplicity-four repeated-K3 channel. Do not cite the previous `A=2 is EMPTY` conclusion.