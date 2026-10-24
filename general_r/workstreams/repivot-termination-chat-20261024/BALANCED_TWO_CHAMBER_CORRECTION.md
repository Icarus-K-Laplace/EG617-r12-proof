# Balanced Two-Chamber Correction Theorem

Assumptions: A+B, `r>=12`, the standard low-owner clique cap, and a pivot p maximal in

`Phi_3=(q,tau,zeta)`.

Fix a d2 exact repeated class

`Y=Y_{S,D}`

with multiplicity m, and suppose repivot through one/every owner of this exact class is `Phi_3`-flat.

By the zeta exchange theorem,

`m=zeta(p)+1`.

Let

`Z=Z_0(p)`

be the d0 population, so `|Z|=m-1`, and define

> `C_0={p} union Z`,
>
> `C_1=Y`.

Then

`|C_0|=|C_1|=m`.

---

## 1. The correction block is a target K_(2m)

Every vertex of `C_1` is a regular d2 owner; every vertex of Z is a regular d0 owner; p is the pivot.

All regular low-endpoint owners are pairwise target-adjacent, and p is target-adjacent to every shell vertex. Therefore

> **`F[C_0 union C_1]=K_(2m)`.**                              (1.1)

Hence

> **`2m<=r-1`.**                                             (1.2)

This recovers the balanced multiplicity cap.

---

## 2. C0 is one neutral chamber

For every `z in Z`, repivot p -> z is d0 neutral:

- the core remains H;
- q,tau,zeta are unchanged;
- the other vertices of `C_0` remain the d0 population after swapping p and z;
- the exact `(S,D)` class C1 is unchanged, because a neutral pivot swap changes neither H nor the missing/core-neighbour relation of the C1 owners.

Thus every pivot in C0 represents the same quotient state:

> **Chamber 0:** core H, d0 population `C_0\{pivot}`, exact d2 class C1 with pair `(S,D)`.

All C0 pivots have the same `Phi_3` value.

---

## 3. C1 is the reverse neutral chamber

Take any `y in C_1` and repivot through y.

The exchange theorem gives:

- every vertex of `C_1\{y}` becomes d0;
- every vertex of Z and p becomes a reverse d2 owner with shell missing set D and core support S.

Because the exchange is zeta-flat and `|C_1\{y}|=m-1=zeta`, there are no additional d0 vertices.

Because p is globally `Phi_3`-maximal and y has the same `Phi_3` value, y is also maximal. The reverse class already has m vertices (`C_0`). If it were larger, a q/tau-flat reverse row would violate the zeta multiplicity bound. Hence the reverse class is exactly C0.

The new core is

> **`H'=(H\D) union S`.**                                    (3.1)

Therefore every pivot in C1 represents the same quotient state:

> **Chamber 1:** core H', d0 population `C_1\{pivot}`, exact reverse d2 class C0 with pair `(D,S)`.

All C1 pivots have the same `Phi_3` value.

---

## 4. Correction cycles have only two quotient states

Inside the 2m-vertex correction block:

- moves within C0 are d0-neutral relabellings and stay in Chamber 0;
- moves within C1 are d0-neutral relabellings and stay in Chamber 1;
- every move from C0 to C1 is the same core exchange `H -> H'` swapping S out and D in;
- every move from C1 to C0 is the reverse exchange `H' -> H`.

Therefore, after quotienting d0 relabellings,

> **the complete balanced repeated-support correction graph is the two-state involution**
>
> **`H  <-->  H'`.**                                        (4.1)

There is no longer a genuine long correction cycle to classify in this branch.

**Status:** `PROVED_CONDITIONAL`.

---

## 5. Allowance is invariant under the flat swap

Let the old shell pair S have

`b=e_M(S)`

and class allowance a. For `s in S`, after the forward repivot,

`kappa'_s=sigma_s-e_F(s,D)`.

In the reverse view the shell missing pair is D, so the reverse charge weight of s is

`w'_s=kappa'_s+e_F(s,D)=sigma_s`.

Hence

`w'(S)=sigma_u+sigma_v=a-b`.

The internal missing count of S as a core support in the reverse view is exactly b. Therefore the reverse support defect is

`w'(S)+mu'(S)=(a-b)+b=a`.

Since the reverse row is q-flat, its class allowance is exactly this defect. Thus

> **`a_reverse=a_forward=a`.**                               (5.1)

So allowance is an invariant of the two-chamber correction block.

---

## 6. The pair missing-statuses exchange

Let

`mu=1-e_H(D)`

be the old internal missing count of D. In the reverse chamber D is a shell pair, so its shell missing indicator is

> `b_reverse=mu`.                                            (6.1)

Conversely S is a core support in H', with internal missing indicator

> `mu_reverse=b`.                                            (6.2)

Thus the two chambers swap

> **`(S,b) <-> (D,mu)`**                                     (6.3)

while preserving allowance a.

The old q-flat equality is

`a=kappa_H(D)+e_F(S,D)+mu`.

The new-core excess on S is

`kappa_(H')(S)=a-b-e_F(S,D)`.

Therefore

> **`kappa_H(D)-kappa_(H')(S)=b-mu`.**                        (6.4)

So the only possible change in the total excess carried by the exchanged pair is the one-bit difference between their missing statuses.

---

## 7. Consequence for the termination program

The zeta-balanced repeated-support branch is no longer an arbitrary correction-cycle family. It is one symbolic terminal family described by:

- a target clique `K_(2m)` split into two equal chambers C0,C1;
- two fully decorated pairs S,D;
- two legal cores H and `H-D+S`;
- invariant allowance a;
- exchanged missing indicators `b <-> mu`;
- the exact excess relation (6.4);
- multiplicity `m<=floor((r-1)/2)`.

Hence the remaining repeated-support task is not cycle termination. It is the elimination (or further rigidity) of this **Balanced Two-Chamber Correction Block**.

The other remaining fully-decorated d2 branch is the genuinely distinct-support system.

**Main impact:** the repeated correction-cycle part of the unique scalable d2 plateau has collapsed to a single two-state symbolic family independent of cycle length.