# E407/E408 global compatibility: exact constraints and remaining kernel

Status: **PARTIAL COMPATIBILITY SYNTHESIS; E407 and E408 REMAIN OPEN**.  
This file combines the latest fixed-r12 proof assets without treating necessary conditions as contradictions.

## 1. E407: what is actually closed

### Certified local exclusion

`front_end/E407_CELL_B_FULL_CLOSURE.md` proves that the sharp `|W|=23) Cell-B completion is empty, relative to its stated Brouwer/Kang--Pikhurko inputs and the Cell-B color-certificate lemma. Its proof uses independent-4 saturation, exact 3-neighbourhood partitions, and the color-degree normal form.

This is not a full E407 closure.

### Remaining Q32 bridge

The current source-reported V12 reduction says E407 Q32 has five `rho=0` templates sharing a common regular K11. The source audit explicitly says the V12 package has not been independently replayed in this session, and no actual completion is reported.

The required theorem remains:

> None of the five explicit common-K11 shell templates can coexist with one and the same 47-point core `C` satisfying `|C|=47`, `e(C)=284`, `delta(C)>=12`, `alpha(C)<=4`, `omega(C)<=11`, together with all labelled shell-core row equations and inherited caps.

The actual five template data and their replayable certificate must be available as canonical inputs before an independent compatibility proof can be completed. The Cell-B exclusion cannot be substituted for this theorem.

## 2. E408 outer equality: exact seven-block system

For E408, the outer equality ledger forces

`G = B_0 dot_union ... dot_union B_6 dot_union R`,

where each `B_i=K12`, `|R|=61`, `e_G(R)=408), and there are no target edges between distinct pieces. Every color has exactly870 edges globally.

For each non-target color C define

- `P_C=sum_{i<j} d_ij(C)`: block--block duplicate count;
- `R_C=sum_i r_i(C)`: block--R duplicate count;
- `s_C=e_C(R)-129>=0): residual excess.

The exact identities are

> `P_C+R_C+s_C=62` for every non-target color C,

and

> `sum_C P_C=252`, `sum_C R_C=427`, `sum_C s_C=3`.

The last equality implies that the number m of exact-129 colors is one of `8,9,10`.

## 3. Exact-129 blocker theorem: cross-block consequences

For each exact-129 color, the contextual Kang--Pikhurko equality classification and `omega(C[R])<=5` force Type I:

- ten isolated K5 components;
- one 11-point exceptional gadget U.

For each outer target block `B_i), each of its 12 vertices has a blocker neighbourhood in R. At most ten such neighbourhoods have size5, and those size-5 blockers must be distinct isolated K5 components. The other at least two blockers have size at least6. Therefore `r_i(C)>=1) for every i and

> `R_C>=7`, hence `P_C<=55`.

A useful aggregate consequence is

> `sum_{C exact129} R_C >= 62m-252`.

Indeed `P_C=62-R_C) for exact colors, while the sum of their P_C is at most the global total252. Thus the lower bound is 244, 306, or 368 when m is 8, 9, or 10, respectively. This is a necessary global load on the block--R incidences, not a contradiction by itself.

## 4. New Q33 local/global interface

Assume the E408 Q33 d3 shell interface. Let A be the 13-point shell, S a candidate missing triple, B=A\S with |B|=10, M the shell missing graph, and H the 47-point core. Use the exact variables in `front_end/E408_Q33_D3_EXACT_BUDGET.md`:

- `beta=e_M(S)`;
- `X=sum_{a in S} X_a`;
- `G_B=sum_{b in B} g_b);
- `c_S=e_M(S,B));
- `k_b=d_M(b,S)).

The exact allowance identity is

> **`beta+X+G_B=3`.**

The D(14) hereditary cap and `e(M)=c_S+beta) give `c_S>=22-beta). Further,

- at least `7+beta+X` of the ten B-rows are regular;
- at least 3, 4, 4, or 5 regular B-rows have `k_b>=2` for `beta=0,1,2,3), respectively;
- the 47-core has total degree excess four above12, so at least43 core vertices have degree12;
- every such degree-12 core vertex must receive a target incidence from A;
- total shell--core incidence is `sum_{a in A} t_a=e(M)+33>=55).

These are exact necessary constraints, not an exclusion of any beta case.

## 5. Exact-129 colors also constrain the inner B=K10

For every exact-129 color C, its restriction to R has ten K5 components plus U, with `alpha(C[U])=2). The Q33 set B is a target K10, hence an independent set of size10 in every non-target color C[R].

Therefore:

> **`|B intersect U_C|<=2`** for every exact-129 color C.

Reason: B contains at most one vertex from each isolated K5 component and at most two vertices from U. Thus at least eight B-vertices lie in distinct K5 components of C[R]. If `u_C=|B intersect U_C|`, exactly `10-u_C` distinct K5 components are occupied by B, and `u_C` K5 components contain no B-vertex.

This is a genuine compatibility constraint between the local Q33 shell and each exact-129 color structure. It does not yet determine which shell missing edges are colored by each component and does not by itself contradict the seven-block duplicate budget.

## 6. Why the current inequalities do not yet close E408 Q33

The exact-129 blocker theorem constrains neighborhoods from the **outer** target blocks `B_i) into R. The local shell B is a ten-point target clique *inside* R. The two sets must not be conflated.

The following remain simultaneous obligations for a legal Q33 completion:

1. `beta+X+G_B=3), `c_S>=22-beta), the row-union constraints and the labelled 284-edge core;
2. for every exact-129 color, `|B intersect U_C|<=2) and the ten K5-component incidences;
3. for every outer block and every exact-129 color, the blocker-neighbourhood constraints and `r_i(C)>=1);
4. the global budgets `P_C+R_C+s_C=62), `sum P=252), `sum R=427), `sum s=3);
5. all eleven non-target colors partitioning the 1830 pairs of R consistently.

No inspected proof currently derives an incompatibility among all five simultaneously. The right next target is an incidence-compatibility lemma or a finite kernel whose states are proved equivalent to these exact contracts and independently checked. The present document does not claim that such a kernel has been eliminated.

## 7. E408 Q32 and E407 Q32 status

- E408 Q32 has no complete global compatibility proof in the inspected assets.
- E407 Q32 still requires the common-K11-template / same-core compatibility theorem and independent V12 replay.
- E408 Q33 d3 has the exact local budget and almost-regular core normal form, but the full family of Q33 shells and global color assignments remains open.

Accordingly the fixed-r12 theorem remains `OPEN / NOT_CERTIFIED`.
