# Balanced Two-Chamber Correction Theorem

Assumptions: A+B, `r>=12`, the standard low-owner clique cap, and a pivot p maximal in

`Phi_3=(q,tau,zeta)`.

Fix a d2 exact class

`Y=Y_{S,D}(p)`

of multiplicity m, and suppose repivot through its owners is `Phi_3`-flat.

By the exact class-neutral involution,

`zeta(new)=m-1`.

Phi3-flatness therefore gives

> **`m=zeta(p)+1`.**                                         (0.1)

Let `Z=Z_0(p)`, so `|Z|=m-1`, and define

`C_0={p} union Z`,

`C_1=Y`.

Then `|C_0|=|C_1|=m`.

---

## 1. The correction block is a target K_(2m)

Every vertex of C1 is a regular d2 owner; every vertex of Z is a regular d0 owner; p is the pivot. All regular low-endpoint owners are pairwise target-adjacent, and p is target-adjacent to every shell vertex. Therefore

> **`F[C_0 union C_1]=K_(2m)`.**                              (1.1)

Hence

> **`2m<=r-1`.**                                             (1.2)

---

## 2. C0 is one neutral chamber

For every `z in Z`, repivot `p -> z` is d0-neutral:

- the core remains H;
- q,tau,zeta are unchanged;
- the other vertices of C0 remain the d0 population after swapping p and z;
- the exact `(S,D)` class C1 is unchanged.

Thus every pivot in C0 represents the same quotient state:

> **Chamber 0:** core H, d0 population `C_0\{pivot}`, exact d2 class C1 with pair `(S,D)`.

---

## 3. C1 is exactly the reverse neutral chamber

Take `y in C_1` and repivot through y. The exact class-neutral involution gives simultaneously

> `zeta(y)=m-1=|C_1\{y}|`,
>
> `m_y(D,S)=zeta(p)+1=m`.

But `C_1\{y}` are already d0 in the y-view, so the first equality shows that they are **all** d0 vertices: no extra d0 vertex exists.

Likewise `C_0` are already reverse `(D,S)` owners in the y-view, and `|C_0|=m`; the second equality shows that they are the **entire** reverse class: no extra reverse owner exists.

The new core is

> **`H'=(H\D) union S`.**                                    (3.1)

Hence every pivot in C1 represents the same quotient state:

> **Chamber 1:** core H', d0 population `C_1\{pivot}`, exact reverse class C0 with pair `(D,S)`.

No maximality argument beyond the initial Phi3-flat equality is needed; exactness follows from the involution theorem.

---

## 4. Correction cycles have only two quotient states

Inside the 2m-vertex correction block:

- moves within C0 are d0-neutral relabellings and stay in Chamber 0;
- moves within C1 are d0-neutral relabellings and stay in Chamber 1;
- every move from C0 to C1 is the same core exchange `H -> H'` swapping S out and D in;
- every move from C1 to C0 is the reverse exchange `H' -> H`.

Therefore, after quotienting d0 relabellings,

> **the complete balanced correction graph is the two-state involution**
>
> **`H <--> H'`.**                                          (4.1)

There is no genuine long correction cycle in this branch.

**Status:** `PROVED_CONDITIONAL`.

---

## 5. Allowance is invariant under the flat swap

Let the old shell pair S have `b=e_M(S)` and class allowance a. For `s in S`, after the forward repivot,

`kappa'_s=sigma_s-e_F(s,D)`.

In the reverse view the shell missing pair is D, so the reverse charge weight of s is

`w'_s=kappa'_s+e_F(s,D)=sigma_s`.

Hence

`w'(S)=sigma_u+sigma_v=a-b`.

The internal missing count of S as a core support in the reverse view is exactly b. Therefore the reverse support defect is

`w'(S)+mu'(S)=(a-b)+b=a`.

Since the reverse row is q-flat, its class allowance equals this defect:

> **`a_reverse=a_forward=a`.**                               (5.1)

---

## 6. The pair missing-statuses exchange

Let

`mu=1-e_H(D)`

be the old internal missing count of D. In the reverse chamber D is a shell pair, so

> `b_reverse=mu`.                                            (6.1)

Conversely S is a core support in H', with

> `mu_reverse=b`.                                            (6.2)

Thus the chambers exchange

> **`(S,b) <-> (D,mu)`**                                     (6.3)

while preserving allowance a.

The old q-flat equality is

`a=kappa_H(D)+e_F(S,D)+mu`.

The new-core excess on S is

`kappa_(H')(S)=a-b-e_F(S,D)`.

Therefore

> **`kappa_H(D)-kappa_(H')(S)=b-mu`.**                        (6.4)

---

## 7. Consequence for the termination program

The balanced repeated-support branch is one symbolic terminal family described by

- a target clique `K_(2m)` split into equal chambers C0,C1;
- two fully decorated pairs S,D;
- two legal cores H and `H-D+S`;
- invariant allowance a;
- exchanged missing indicators `b <-> mu`;
- exact excess relation (6.4);
- multiplicity `m<=floor((r-1)/2)`.

The repeated-support problem is therefore no longer cycle termination; it is elimination or further rigidity of this **Balanced Two-Chamber Correction Block**.

The only remaining source of new scalable combinatorial structure is the distinct-support fully-decorated d2 branch.