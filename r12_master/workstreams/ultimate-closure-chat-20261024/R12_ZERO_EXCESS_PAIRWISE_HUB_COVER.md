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

## 6. Exact-129 witness-count audit — corrected

Every exact-129 color has at least seven K5 components avoiding S. At most one can contain pivot p, so the universally valid labelled count is at least six B-labelled components per exact-129 color. A pair of S vertices allowed to coexist in one K5 need not actually occupy the same component; therefore no beta-dependent increase from six to seven/eight is asserted.

At most four core vertices have positive excess, and the six B-labelled Q sets are disjoint within a color. Thus every exact-129 color supplies at least two zero-excess B-labelled witnesses. Global floors are 14 for E407 and 16 for E408 Q33.

If a full B row exists, any B-labelled witness that misses a hub must hit the full row's three-element core support. At most three disjoint witnesses per color can do so, leaving at least three hub-complete B-labelled witnesses per exact-129 color. Therefore E407 templates A-D and E with a full row have a safe global floor of 21. In E with no full row, all B rows miss both P3 endpoints; each of the six B-labelled witnesses per color hits both endpoints, yielding at least 42 endpoint-complete witnesses globally.

The separate shell-incidence lemma proves the union of full-row supports has size at least 11 in template A and at least 10 in C. See R12_FULL_ROW_SUPPORT_UNION.md.

The seven-neighbour transversal floor remains valid, but the E407 delta<=15 conclusion is conditional on L being non-four-partite. Unconditionally, the E407 window permits delta=16, in which case L must be four-partite but non-complete. For E408 Q33, a non-complete four-partite branch also remains arithmetically compatible.
