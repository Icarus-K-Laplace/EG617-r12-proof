# Pair-indexed zero-excess witnesses and hub-cover certificates

Date: 2026-10-25  
Status: **PROVED under the retained 284-edge core contract.** This is a necessary-structure theorem, not a terminal contradiction.

## 1. Contract and inherited lemma

Let H be the 47-vertex core in E407 Q32 or E408 Q33, with
\[
\alpha(H)\le4,\quad \delta(H)\ge12,\quad e(H)=284,\quad
\sum_{x\in H}(d_H(x)-12)=4.
\]
Let H_0 be the induced subgraph on vertices of core degree exactly 12. For a shell row b, let
\[
T_b=N_F(b)\cap H_0.
\]
For a regular B-row with t_b=|N_F(b)\cap H|\le3, we have |T_b|≤3.

The sibling workstream's robust zero-excess independent-four theorem states that for every T⊆H_0 with |T|≤6,
\[
\alpha(H_0-T)=4.
\]
Its finite arithmetic table was independently recomputed here: the ten endpoint gaps p_3(47-k-t)-U(E,k,t) are
\[
30,22,14,5\quad(E=4,t=6,k=1,\ldots,4)
\]
and
\[
44,38,31,23,15,6\quad(E=6,t=4,k=1,\ldots,6).
\]
All are strictly positive. The 284-edge case therefore supplies the required six-deletion guarantee.

## 2. Pairwise common-witness theorem

**Theorem 2.1.** For any two regular B-rows b,c with t_b,t_c≤3, there exists a four-set
\[
Q_{bc}\subseteq H_0\setminus(T_b\cup T_c)
\]
that is independent in H. In particular, Q_bc is target-anticomplete to both b and c, and all four of its vertices have core degree 12.

**Proof.** The union T_b∪T_c has at most six vertices. The inherited robust theorem gives alpha(H_0\(T_b∪T_c))=4, so choose an independent four-set there. By construction it avoids both target-neighborhood rows. ∎

This is a common-witness statement for each labelled pair. It does **not** assert that witnesses chosen for different pairs are distinct.

## 3. Hub-cover strengthening

Write
\[
S_b=N_M(b)\cap S
\]
for the set of hubs missed by b in the target shell graph.

**Theorem 3.1.** If S_b∪S_c=S, then every common witness Q_bc from Theorem 2.1 is hub-complete: it has a target neighbor in each of the three hub rows.

**Proof.** Suppose Q_bc missed a hub s. Since S_b∪S_c=S, at least one of b,c misses s in the target shell graph; say b. The set Q_bc is anticomplete to b by Theorem 2.1, and by supposition it is anticomplete to s. Thus Q_bc∪{b,s} is an independent six-set in F, contradicting alpha(F)≤5. ∎

This combines two previously separate constraints: the zero-excess core forces a common four-set for each row pair, and the shell missing-set union determines which of those common witnesses must hit all three hubs.

## 4. Pair-indexed coverage across the five E407 templates

Let n_3 be the number of full B-rows, meaning S_b=S and t_b=3. The registered V12 row-count contracts give:
- A: n_3≥6;
- B: n_3≥2;
- C: n_3≥6;
- D: n_3≥1;
- E: either n_3≥1 or n_3=0.

Whenever a pair contains a full row, its missing-set union is S. Therefore the number of **labelled row-pair certificates** that are forced to have a hub-complete zero-excess witness is at least
\[
\binom{10}{2}-\binom{10-n_3}{2}.
\]

| Template | Guaranteed n_3 | Pair certificates with hub-complete Q_bc |
|---|---:|---:|
| A | 6 | 39 |
| B | 2 | 17 |
| C | 6 | 39 |
| D | 1 | 9 |
| E, n_3≥1 | 1 | 9 |

These numbers count pairs, not distinct four-sets. A single Q may be anticomplete to more than two B-rows, so no injectivity or 39/17/9 distinct-witness conclusion is claimed.

### Exceptional template E branch

If n_3=0, the row constraints force every B-row to miss exactly the two endpoints of the P3 on S: n_0=n_1=0 and n_2=10. For each of the 45 B-row pairs, Theorem 2.1 supplies a common zero-excess witness anticomplete to both rows. Every such witness must hit both endpoints of the P3, since otherwise it and either missed endpoint together with a B-row give an independent six-set. Thus all 45 labelled pairs have endpoint-complete common-witness certificates; again, the certificates need not be distinct.

## 5. E408 Q33 transfer and the E408 Q32 firewall

In E408 Q33, the retained budget guarantees at least seven undecorated B-rows with t_b=k_b≤3. Every pair among those rows has a common zero-excess independent-four witness. Such a witness is hub-complete whenever the pair's two missing-hub sets cover S.

E408 Q32 has e(H)=285 and total core excess six. The retained robust theorem only guarantees alpha(H_0-T)=4 for |T|≤4 in that layer. Thus the pairwise conclusion transfers only to pairs with |T_b∪T_c|≤4; the six-deletion proof for the 284-edge core must not be reused there.

## 6. Exact-129 witness-count audit across sibling branches

The independently reviewed component count is:
- A/B: at least seven K5 components avoid S, but at most one can contain pivot p; hence at least six are B-labelled components {b}∪Q.
- C/D/E: at least eight K5 components avoid S, but at most one can contain p; hence at least seven are B-labelled components {b}∪Q.
- In every eligible template with n_3≥1, a B-labelled witness Q that misses any hub must hit a full B-row. That full row has exactly three core neighbors, and the component witnesses are disjoint within one color. Therefore at most three B-labelled witnesses per exact-129 color can fail to be hub-complete.

Consequently the safe hub-complete lower bounds are:
- A/B: at least 3 per exact-129 color, hence at least 21 globally in E407;
- C/D/E with n_3≥1: at least 4 per exact-129 color, hence at least 28 globally in E407;
- E with n_3=0: at least 7 endpoint-complete B-labelled witnesses per exact-129 color, hence at least 49 globally.

**Audit qualification.** Some newer sibling prose counts all no-S K5 components (including a possible component {p}∪Q) as if each Q had a B-label. The total independent-four packing count of seven/eight Q-sets per exact color is valid and supports the separate |V_*|≥29 / |V_*|≥31 support theorem. But a pivot-containing Q is not known to be anticomplete to a B-row, so it cannot be used in the argument that a non-hub-complete witness must hit every full B-row. We do not promote the stronger 28/35 A–E hub-complete counts unless that missing label condition is separately proved.

## 7. What remains open

The pair-indexed theorem gives a hub-complete zero-excess witness for every qualifying row pair, but witnesses may repeat. The exact-129 K5 packing gives linearity across distinct colors, but those color-component witnesses need not coincide with the zero-excess Q_bc witnesses. A valid closure must connect these two families or derive a contradiction from the actual 284-edge core.

E407 Q32 and E408 Q33 remain OPEN / NOT_CERTIFIED. E408 Q32 remains separately OPEN at the 285-edge / excess-six layer.
