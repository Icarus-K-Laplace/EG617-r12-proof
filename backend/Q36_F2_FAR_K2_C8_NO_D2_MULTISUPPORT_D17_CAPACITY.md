# q36 f=2 far-target-K2 — c=8 no-d2 corrected D17 multi-support capacity

Status: `PROVED` under `Q36_F2_FAR_K2_D14_CONTRACT_CORRECTION.md`, the inherited D(n) caps from `front_end/FRONTEND_BRIDGE_THEOREM.md`, and the c=8 no-d2 shell geometry.

This theorem replaces the invalid use of `{p} union C union F` as a target K11 by a genuine hereditary-cap argument on the correct dense base.

## 1. Correct 11-point base

Let all eight low owners form the target clique C and let x be the active decorated missing vertex. Put `Y=X\{x}` and

`rho=e_M(Y) in {0,1}`.

The correct 11-point shell base is

`B={p} union C union Y`.

Every C--Y pair is a target edge, p is adjacent to all ten shell vertices, and the only possible missing edge in B is the Y-edge. Hence

`e(B)=55-rho`.                                               (1)

## 2. The inherited D17 constant

From the bridge contract

`D(n)=C(n,2)-11*p_12(n)`.

For n=17, write `17=1*12+5`. Thus

`p_12(17)=5`

and

`D(17)=C(17,2)-55=136-55=81`.                              (2)

## 3. Two disjoint support classes

Let D,E be two disjoint three-point core support classes, with owner multiplicities r,s among the eight low owners C.

Inside the induced 17-set `B union D union E`, the following target edges are forced:

- `55-rho` edges inside B;
- `3r` C--D incidences from the r owners of D;
- `3s` C--E incidences from the s owners of E;
- `e_H(D)` and `e_H(E)` internal support edges;
- `e_H(D,E)` cross edges;
- `e_F(Y,D union E)` inactive-shell incidences.

There may be further target incidences from other C-owners into D or E; ignoring them only weakens the lower bound. Therefore the inherited D17 cap gives

`55-rho + 3(r+s) + e_H(D)+e_H(E)+e_H(D,E)+e_F(Y,D union E) <=81`.

Equivalently

> `3(r+s)+e_H(D)+e_H(E)+e_H(D,E)+e_F(Y,D union E) <=26+rho`.   (3)

This is the corrected two-support capacity theorem.

## 4. K3--K3 consequence

If both D and E are target K3 supports, then

`e_H(D)+e_H(E)=6`.

Dropping the remaining nonnegative terms in (3) gives

`3(r+s)+6<=26+rho`.

Hence

- if rho=0, `r+s<=6`;
- if rho=1, `r+s<=7`.

Thus:

> two disjoint target-K3 support classes can never carry all eight low owners.  (4)

In particular a `4+4` pair of disjoint K3 classes is impossible even in the corrected rho=1 channel.

## 5. One-edge / two-edge variants

The same formula gives immediately:

- K3 + two-edge support:
  `3(r+s)<=21+rho`;
- K3 + one-edge support:
  `3(r+s)<=22+rho`;
- two two-edge supports:
  `3(r+s)<=22+rho`;
- one-edge + two-edge:
  `3(r+s)<=23+rho`;
- two one-edge supports:
  `3(r+s)<=24+rho`.

Any positive D--E cross edge or Y-incidence sharpens these bounds by the corresponding amount.

## 6. Scope

This theorem applies to c=8 far-target-K2 no-d2 support classes under the corrected D14/clique contract. It does not assume target-K4-freeness, does not use the false `{p} union C union F` K11 base, and does not require a fixed-size core remainder.

Its immediate use is in the A=3 and A=4 multiplicity classifications.