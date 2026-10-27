# Kang–Pikhurko exact-129 source audit

Updated: 2026-10-27
Status: **SOURCE VERIFIED / PARAMETER MAP VERIFIED**
Purpose: discharge the provenance uncertainty behind the retained exact-129 Type-I factor theorem used by the E407/E408 root chain.

## 1. Primary source

M. Kang and O. Pikhurko, **Maximum K_{r+1}-free graphs which are not r-partite**, Matematychni Studii 24 (2005), 12–20.

Primary PDF:

`https://opikhurko.warwick.ac.uk/E/KangPikhurko05ms.pdf`

Relevant source statements:

- **Theorem 1:** for `n >= r+3`, `r>=2`, and `r <= (n-1)/2`,
  `p_r(n)=t_r(n)-floor(n/r)+1`, and the extremal graphs are characterized by Theorem 4 and Lemma 5.
- **Theorem 4:** `p_r(n)` is the maximum of the explicit construction `G(n_1,...,n_r)` over the allowed integer sequences, and **all** extremal graphs arise from that construction.
- **Lemma 5:** in the regime `r <= (n-1)/2`, the optimal nondecreasing sequences `n_1,...,n_r`, summing to `n-1`, are exactly those satisfying
  `n_1>=2`,
  `n_2<=n_1+1`,
  `n_r<=n_1+2`,
  `n_r<=n_3+1`.

The construction starts from a complete r-partite graph on parts `N_i`, adds one new vertex `x`, modifies only the two smallest nontrivial parts `N_s,N_t`, and otherwise keeps the complete cross-part structure. Its exact definition is in Section 2 immediately before equation (4).

## 2. Translate an exact-129 color to the KP problem

Let `C` be one non-target color restricted to a genuine 61-point T61 residual `R` and assume

- `e(C[R])=129`;
- `alpha(C[R])<=12`;
- `omega(C[R])<=5`.

Put

`G = complement(C[R])`.

Then

`e(G)=C(61,2)-129 = 1830-129 = 1701`.

Also

`omega(G)=alpha(C[R])<=12`,

so `G` is `K_13`-free.

It is not 12-partite. Indeed, if it were 12-partite, then the twelve color classes would be cliques of `C[R]`. Since `omega(C[R])<=5`, they could cover at most `12*5=60` vertices, not61. Thus

`G in mathcal G_{61,12}`

in Kang–Pikhurko's notation.

## 3. Equality arithmetic

For `T_12(61)`, the balanced 12 parts have sizes

`6,5,5,5,5,5,5,5,5,5,5,5`.

Hence the number of missing within-part pairs is

`C(6,2)+11*C(5,2)=15+110=125`,

so

`t_12(61)=C(61,2)-125=1830-125=1705`.

Here

`12 <= (61-1)/2 = 30`,

and Kang–Pikhurko Theorem 1 gives

`p_12(61)=1705-floor(61/12)+1=1705-5+1=1701`.

Therefore `G` is not merely admissible: it is an **equality graph** for the Kang–Pikhurko theorem.

## 4. Enumerate the equality part-size sequences

Apply Lemma 5 with 12 nondecreasing positive integers summing to60. The four optimality inequalities leave exactly three sequences:

1. `(5^12)`;
2. `(4,5^10,6)`;
3. `(4,4,5^8,6,6)`.

The companion verifier `verify_kp_exact129_instance.py` enumerates the integer sequences independently and reproduces exactly these three.

These are precisely the three historical project labels Type I, Type II, Type III.

## 5. Eliminate Types II and III using the contextual clique cap

Each construction part `N_i` is independent in the KP graph `G`, hence a clique of size `n_i` in the original color graph `C[R]`.

Both Type II and Type III contain a part of size6. Therefore they contain a `K_6` in `C[R]`, contradicting

`omega(C[R])<=5`.

Thus only Type I survives:

`(n_1,...,n_12)=(5,5,...,5)`.

## 6. Recover the exact Type-I color factor

In the KP construction, choose the two special 5-parts `N_s,N_t` and the added vertex `x`.

For each of the other ten 5-parts `N_i`:

- `G[N_i]` has no edges, so `C[N_i]=K_5`;
- `G` is complete from `N_i` to every other old part;
- `x` is adjacent in `G` to all of `N_i`.

Therefore in `C[R]`, each such `N_i` is an **isolated K_5 component**.

All nontrivial interactions outside these ten components are contained in

`U = N_s union N_t union {x}`,

which has size11.

Hence every exact-129 non-target color in the genuine T61 context has exactly

`10 K_5 dot-union U_11`,

where the ten `K_5` are isolated components and `U_11` is the KP exceptional gadget.

The gadget has

- clique number exactly5, because each special part is a K5 in `C`;
- independence number exactly2.

For the latter, each independent set can contain at most one vertex from each special K5; adding `x` cannot create an independent triple because the KP construction connects `x` in the complement to all but the designated proper-subset/one-vertex pattern, while the remaining cross-pair is exactly the deleted-edge pattern. Direct inspection of the construction gives maximum two.

This is exactly the retained project factor theorem used in the E408 exact-count argument and the E407 selected-component/support bridge.

## 7. Promotion consequence

The statement

> every 61-point exact-129 non-target color with `alpha<=12` and `omega<=5` is Type I, hence `10 isolated K5 + 11-point exceptional gadget`

is **not an OPEN project assumption**.

It is a direct parameter instance of the published Kang–Pikhurko equality classification, plus the elementary complement translation and the contextual clique cap.

Accordingly, the exact-129 factor theorem's **source provenance gate is discharged**.

This does not by itself promote the whole fixed-r=12 proof to unqualified `PROVED`: other external theorem instances and the computation-certified V9/V10/V11/V12/front-end packages still require their own final source/replay freeze.

## 8. Audit firewall

This audit does not claim:

- that every other external theorem used by the root chain has been frozen;
- that the finite recurrence/state certificates have been formally verified;
- that the proof is machine-checked end-to-end.

It only closes the previously explicit uncertainty about the exact-129 Type-I equality/factor theorem.
