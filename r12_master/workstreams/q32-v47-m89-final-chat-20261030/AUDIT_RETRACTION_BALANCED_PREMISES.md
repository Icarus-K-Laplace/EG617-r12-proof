# Critical audit correction — missing K6-free and Type-I source hypotheses

Date: 2026-10-30  
Status: **PROMOTION RETRACTED; Q32 m=8,9 REMAIN OPEN**

## 1. The actual EG617 hypothesis

Erdős Problem 617 asks whether every r-edge-coloring of K_(r^2+1) has an (r+1)-vertex set whose induced clique misses a color. A hypothetical counterexample is a **balanced coloring**: every 13-vertex set in the r=12 case contains all twelve colors.

For any color graph C on the 61-point residual, this gives
\[
\alpha(C)\le12,\qquad \omega(C)\le12.
\]
It does **not** give \(\omega(C)\le5\). In particular, a monochromatic K6 is allowed; the forbidden monochromatic clique size is K13.

For the target core H, the registered residual class is R(4,49), whose clique cap is \(\omega(H)\le11\), not \(\omega(H)\le5\). The frozen Q32 core contract explicitly supplies only
\[
|H|=47,\quad e(H)=285,\quad \alpha(H)\le4,\quad \delta(H)\ge12,
\]
and total degree excess six. There is no global no-monochromatic-K6 premise in EG617.

Primary problem statement and open status: https://erdosproblems.ai/wiki/problems/extremal_graph_theory/E0617.

## 2. The Kang–Pikhurko exact-129 gate does not automatically give Type I

The source audit's exact-129 argument assumes
\[
e(C)=129,\quad \alpha(C)\le12,\quad \omega(C)\le5.
\]
It then sets G=overline(C), obtains a K13-free graph, and uses \(\omega(C)\le5\) to show that G is not 12-partite: a 12-partition of G would be a cover of C by twelve cliques of size at most five, covering at most 60 vertices.

The balanced-coloring hypothesis only gives \(\omega(C)\le12\). It neither rules out a 12-partite complement nor eliminates the size-six equality parts in the non-12-partite Kang–Pikhurko equality classification. The latter two optimal part-size sequences contain size-six parts and are excluded in the source audit only by the unavailable \(\omega(C)\le5\) premise.

A concrete one-color local model demonstrates the gap:
\[
C_0=5K_6\ \dot\cup\ 3K_5\ \dot\cup\ 4K_4.
\]
It has
\[
|V(C_0)|=5\cdot6+3\cdot5+4\cdot4=61,
\]
\[
e(C_0)=5\binom62+3\binom52+4\binom42
=75+30+24=129,
\]
\[
\alpha(C_0)=5+3+4=12,\qquad \omega(C_0)=6.
\]
Its complement is 12-partite. Every 13-set contains a C0-edge by the pigeonhole principle, so it satisfies the balanced-coloring one-color necessary condition \(\alpha(C_0)\le12\). It is **not** asserted to extend to a full twelve-coloring; it proves that the local hypotheses used in the exact-129 source audit do not imply the Type-I interface.

Thus the twelve disjoint K5 factors partitioning K61 minus x are not currently established for every exact-129 color in the EG617 Q32 parent.

## 3. The tight-part lemma itself is valid, but its conclusion is not a contradiction here

The Hall/tight-part calculation in V47_TYPEI_PARTITION_OBSTRUCTION.md is a valid conditional lemma:

- under the stated independent-partition shape;
- with |H|=47, e(H)=285, delta(H)>=12, alpha(H)<=4;

it forces either an independent 5-set or a clique of size at least six in H.

Since alpha(H)<=4, the conclusion is omega(H)>=6. This contradicts an **additional** omega(H)<=5 hypothesis, but the actual Q32 parent allows omega(H)<=11. Therefore the lemma does not exclude any of the three partition shapes under the registered EG617 contract. In particular, the K6/K7 witnesses returned by the verifier are permitted objects, not invalid candidates.

The lemma can be retained as a conditional structural result, but it cannot be called an EG617 obstruction without a new argument that excludes the forced clique using only the actual omega(H)<=11 contract and the remaining parent structure.

## 4. The solver and verifier encode a stronger, different problem

The current local candidate verifier:
- reconstructs every exact color as twelve disjoint K5 factors partitioning all vertices except x (Type-I-only source model);
- when check_omega=True, explicitly rejects every monochromatic K6 in every color;
- invokes the Type-I partition helper and treats a target clique of size at least six as a verifier failure.

The current local solver:
- imposes core_edges[c] >= 71 using the tight-part/K7 contradiction;
- adds lazy monochromatic-K6 cuts for all twelve colors;
- keeps the Type-I exact-color source factorization.

All three are stronger than the actual balanced-coloring premise. The K6 separator and the 71-edge floor are not valid cuts for EG617. A solver run on this encoding, even if it were UNSAT, would not prove the original Q32 terminal.

No full SMT run was performed, so there is no computational result to preserve or reinterpret.

## 5. Retraction and corrected status

The following previous claims are withdrawn as EG617 conclusions:
- exact-129 Type-I factorization for every exact color;
- no exact-129 Type-I color on a valid Q32 core;
- analytic closure of full-support Q32 m=8,9;
- support- and m-independent closure of all Q32 v=44,45,46,47, m=8,9,10;
- the universal e_C(H)>=71 floor when its proof invokes omega(H)<=5;
- any verifier or solver status that treats a K6 in H or in a color graph as a violation of balancedness.

Correct status:
- the Hall/tight-part lemma is **PROVED_CONDITIONAL** under its augmented clique cap;
- the Kang–Pikhurko Type-I factorization is **PROVED_CONDITIONAL** under its source hypotheses, including the needed non-12-partiteness and size-six exclusion;
- the local full-support Q32 m=8,9 terminal is **OPEN / NOT_CERTIFIED** under the actual EG617 contract;
- the parent root remains unchanged and **OPEN / NOT_CERTIFIED**.

## 6. What would be needed to revive this route

A valid continuation must establish, from the full balanced-coloring and outer Q32 contract rather than assume:

1. for each exact-129 color, either a source classification covering the 12-partite complement case and both non-12-partite size-six profiles, or a theorem that rules those cases out;
2. a valid replacement for the omega(H)<=5 step, because omega(H)<=11 is the actual core cap;
3. if using the current Type-I-only verifier, a proof that every exact color in every surviving Q32 row is Type I.

Until these gates close, keep the source profiles general and do not promote the previous analytic closure.


## 7. Salvaged source-complete partition theorem

The missing Type-I source gate does **not** destroy the weaker H-partition conclusion. A new theorem, V47_EXACT129_UNIVERSAL_PARTITION.md, handles both cases:

- If the complement of C is 12-partite, its 12 independent parts are C-cliques; their intersections with H are independent in H and, since |H|=47 and alpha(H)<=4, have sizes 4^11,3.
- If the complement is not 12-partite, Kang–Pikhurko Theorem 1 applies. All three equality profiles (5^12), (4,5^10,6), and (4,4,5^8,6,6) are retained. Their 12 old parts are C-cliques and partition V minus x. Since each H-intersection has size at most four and the total outside-incidence excess is 1 when x is outside O and 2 when x is in H, the induced H-partition is respectively 11K4+K3, 10K4+2K3+K1, or 11K4+K2+K1.

Thus **every** exact-129 color, including the 12-partite complement case and both size-six Kang–Pikhurko profiles, induces one of the three H-partition shapes. This removes the need for a Type-I-only source factorization for the partition argument.

The tight-part lemma then gives a source-complete conclusion:
\[
\text{every exact-129 color}\Longrightarrow
\text{one of the three H-partitions}\Longrightarrow
\omega(H)\ge6,
\]
using alpha(H)<=4 and the frozen core contract. This is a genuine structural result, but it still does not contradict the actual omega(H)<=11 cap. The m=8/9 closure remains OPEN / NOT_CERTIFIED.
