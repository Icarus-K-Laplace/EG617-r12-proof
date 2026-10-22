# Integration 1 CORE211 audit

Status: `PARTIAL_STANDALONE_RECOVERY`.

Integration 1 contains the clean 210-edge contradiction that upgrades the 35-point core floor to 211 once the minimum-degree input `delta(H)>=12` has been licensed.

## Recovered proof body

Assume `H in R(3,35)` and `delta(H)>=12`.

If `e(H)=210`, the degree sum is 420, hence H is 12-regular.

Let `L=bar(H)`. Then

- |L|=35;
- L is 22-regular;
- L is K4-free;
- alpha(L)<=11.

The Andrasfai--Erdos--Sos theorem for K4-free graphs says that if

`delta(L) > (5/8)|L|`,

then L is 3-partite. Here

`22 > (5/8)35 =21.875`.

Thus L is 3-partite. One part has at least `ceil(35/3)=12` vertices, giving an independent set of size12 in L, contradicting `alpha(L)<=11`.

Therefore `e(H)!=210`; with the previously licensed lower regime this gives `e(H)>=211`.

At equality e(H)=211, total degree excess over 12 is2, so the only degree multisets are

- `14,12^34`;
- `13^2,12^33`.

## Remaining self-containment issue

The Integration 1 proof of `delta(H)>=12` calls a previously audited 23-neighbourhood / cap-two exclusion. The current repository still needs that lower-order lemma either as:

- a standalone proof/certificate; or
- an exact bibliographic/certificate dependency.

Therefore this audit does **not** claim that CORE211 is bibliographically/proof-body self-contained from this one file alone. It does certify that the 210-edge AES contradiction and equality-degree consequences are fully recovered.

## Provenance

Integration 1 `385-448`, local pages 5--7 and 22--24.
