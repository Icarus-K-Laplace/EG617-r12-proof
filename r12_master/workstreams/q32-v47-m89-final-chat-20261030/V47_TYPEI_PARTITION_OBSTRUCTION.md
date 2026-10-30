# E408 Q32 v47 — Type-I source partition obstruction

Date: 2026-10-30

Status: **PROVED_CONDITIONAL AS A LEMMA; NOT AN EG617 CLOSURE.** The previous promotion is retracted: EG617 supplies neither omega(H)<=5 nor omega(C)<=5, and does not currently imply the Type-I factorization for every exact-129 color. See AUDIT_RETRACTION_BALANCED_PREMISES.md.

## 1. Core and coloring contract

The target graph H satisfies
\[
|V(H)|=47,\quad e(H)=285,\quad \delta(H)\ge12,\quad
\alpha(H)\le4,\quad \omega(H)\le11.
\]
The frozen Q32 core supplies \(\alpha(H)\le4\), \(e(H)=285\), and \(\delta(H)\ge12\). The actual EG617 balanced-coloring hypothesis only implies \(\omega(H)\le12\) on the 61-point color graph; the registered residual class \(R(4,49)\) supplies \(\omega(H)\le11\) for this 47-core. Neither gives \(\omega(H)\le5\).

For every color C in the 61-point residual, balancedness gives \(\alpha(C)\le12\) and \(\omega(C)\le12\), not \(\omega(C)\le5\). The Kang--Pikhurko Type-I factorization additionally requires the complement to be non-12-partite and uses the clique cap to eliminate the size-six equality profiles. Neither gate has been proved for every exact color in the registered Q32 contract. Thus the following argument is conditional on a separately certified Type-I source factorization; it is not currently available for every exact-129 color.

For an exact-129 non-target color C, the source-verified Type-I factorization supplies a point x and twelve disjoint monochromatic K5 factors
\[
B_1,\ldots,B_{12}
\]
partitioning \(V(K_{61})\setminus\{x\}\). Every \(B_i\) meets the 14-point outside set O: otherwise \(B_i\subseteq H\) would be an independent 5-set in H.

Let \(b_i=|B_i\cap O|\). Thus \(b_i\ge1\).

- If \(x\in O\), then \(\sum b_i=13\), so the profile is \((2,1^{11})\).
- If \(x\in H\), then \(\sum b_i=14\), so the profile is either \((2,2,1^{10})\) or \((3,1^{11})\).

Because every \(B_i\) is a C-monochromatic K5, its H-interior \(B_i\cap H\) is an independent set in H. These intersections are disjoint and, together with \(\{x\}\) when \(x\in H\), partition H.

Therefore every exact-129 Type-I color induces exactly one of these three forbidden partition shapes:

| Position/profile | Independent-part partition of H |
|---|---|
| \(x\in O\), \((2,1^{11})\) | \(11\cdot4+1\cdot3\) |
| \(x\in H\), \((2,2,1^{10})\) | \(10\cdot4+2\cdot3+1\cdot1\) |
| \(x\in H\), \((3,1^{11})\) | \(11\cdot4+1\cdot2+1\cdot1\) |

The next lemma excludes all three shapes without using the low-layer edge count \(e_C(H)\).

## 2. Unified tight-part obstruction

### Lemma

Let H satisfy the core contract above. Suppose H is partitioned into r independent 4-sets
\[
P_1,\ldots,P_r
\]
and some smaller independent parts, in one of the following cases:

1. \(r=11\), with one 3-set;
2. \(r=10\), with two 3-sets and one singleton;
3. \(r=11\), with one 2-set and one singleton.

Then H contains an independent 5-set or a clique of size at least six. In particular, none of these partitions exists under \(\alpha(H)\le4\) and \(\omega(H)\le5\).

### Proof

For any two independent 4-sets P,Q, the bipartite graph H[P,Q] has a perfect matching. Otherwise Hall gives S subset P with \(|N_Q(S)|<|S|\), and
\[
S\cup(Q\setminus N_Q(S))
\]
is an independent set of size at least five.

More generally, for a 4-set P and an independent k-set T with \(k\in\{2,3\}\), H[P,T] has a matching saturating T by the same Hall argument. For a 4-set P and a singleton \(\{x\}\), at least one H-edge joins x to P, since otherwise \(P\cup\{x\}\) is an independent 5-set.

Choose these matchings independently and let M be their union. Edges chosen for different unordered pairs of parts are distinct.

The resulting edge and degree ledger is:

| Partition | \(e(M)\) | M-degree sum on each 4-part | Lower bound on F-degree sum per 4-part | Lower bounds on smaller parts |
|---|---:|---:|---:|---:|
| \(11\cdot4+3\) | 253 | \(4\cdot10+3=43\) | \(48-43=5\) | 3-part: \(3\cdot(12-11)=3\) |
| \(10\cdot4+3+3+1\) | 250 | \(4\cdot9+3+3+1=43\) | \(48-43=5\) | each 3-part: \(3\cdot(12-10)=6\); singleton: \(12-10=2\) |
| \(11\cdot4+2+1\) | 253 | \(4\cdot10+2+1=43\) | \(48-43=5\) | 2-part: \(2\cdot(12-11)=2\); singleton: \(12-11=1\) |

Put \(F=H\setminus M\). Since \(e(H)=285\), the total F-degree sum \(2e(F)\) is respectively 64, 70, and 64. The sum of the displayed lower bounds is 58, 64, and 58. In every case the total excess over all part lower bounds is exactly six.

Consequently at least \(r-6\) of the r four-parts are tight, meaning
\[
\sum_{v\in P}d_F(v)=5.
\]
There are therefore at least four tight 4-parts in case 2 and at least five in cases 1 and 3.

Fix a tight part P. Its four nonnegative F-degrees sum to five. The three vertices \(u_1,u_2,u_3\) with smallest F-degrees therefore satisfy
\[
d_F(u_1)+d_F(u_2)+d_F(u_3)\le3.
\]
They are independent because P is independent in H.

There are \(r-1\) other 4-parts. At most three of them contain an F-neighbor of one of the selected vertices. Hence at least
\[
(r-1)-3=r-4\ge6
\]
other 4-parts Q are clean: no F-edge joins any \(u_i\) to Q.

For each clean Q, the chosen perfect matching M[P,Q] sends \(u_1,u_2,u_3\) to three distinct vertices of Q. Since Q is clean, those are their only H-neighbors in Q. Let \(w_Q\) be the fourth vertex of Q. Then \(w_Q\) is nonadjacent to all three selected vertices.

For two clean parts Q,Q', if \(w_Qw_{Q'}\notin E(H)\), then
\[
\{u_1,u_2,u_3,w_Q,w_{Q'}\}
\]
is an independent 5-set, impossible. Thus all the \(w_Q\) are pairwise adjacent. Since there are at least six clean parts, they form a clique of size at least six, also impossible.

This proves the lemma.

## 3. Exact-color contradiction

The Type-I source factorization forces one of the three partition shapes in Section 1. The lemma shows that each such partition forces \(\omega(H)\ge6\), once \(\alpha(H)\le4\) is used. It contradicts only the additional hypothesis \(\omega(H)\le5\). The actual Q32 parent permits \(\omega(H)\le11\), so this is **not** a contradiction under the registered EG617 contract.

Moreover, the parent has not proved that every exact-129 color is Type I. The balanced-coloring assumptions give only \(\alpha(C),\omega(C)\le12\); the exact-129 complement may be 12-partite, or may lie in a non-Type-I equality profile. Therefore no conclusion that all exact-129 colors are excluded follows.

The former statements that m=8 and m=9 are analytically closed are withdrawn. Both full-support Q32 branches remain **OPEN / NOT_CERTIFIED**.

This argument is stronger than the preceding \(e_C(H)\ge71\) result: it does not use the 69/70 near-Turán classification, the 37-unit edge-gap ledger, pivot matching composition, or any m-specific reserve bound.

## 4. Scope firewall and remaining global status

- **Valid conditional result:** each of the three stated partition shapes forces an independent 5-set or a clique of size at least six in H.
- **Not established:** that the extra clique cap omega(H)<=5 holds in EG617; that every exact-129 color is Type I; or that all exact colors induce one of the three partitions.
- **Correct project status:** E408/Q32 full-support v=47, m=8 and m=9 remain OPEN / NOT_CERTIFIED.
- The verifier's clique witness is not a failure under EG617: K6 and K7 are permitted by the actual omega(H)<=11 residual contract.


## 5. Primary-source provenance of the Type-I factorization

The imported exact-129 factorization is independently recorded in the parent root workstream's KANG_PIKHURKO_EXACT129_SOURCE_AUDIT.md and follows the published source:

M. Kang and O. Pikhurko, “Maximum \(K_{r+1}\)-free graphs which are not \(r\)-partite,” *Matematychni Studii* 24 (2005), 12–20. Primary PDF: https://opikhurko.warwick.ac.uk/E/KangPikhurko05ms.pdf.

The exact-129 translation is:
- C has 129 edges, \(\alpha(C)\le12\), and \(\omega(C)\le5\);
- its complement G has 1701 edges, is K13-free, and is not 12-partite (otherwise C would be a union of twelve cliques of size at most five and cover at most 60 vertices);
- \(t_{12}(61)=1705\), so Theorem 1 gives \(p_{12}(61)=1705-\lfloor61/12\rfloor+1=1701\);
- Theorem 4 and Lemma 5 classify the equality graphs. The three optimal part-size sequences are \((5^{12})\), \((4,5^{10},6)\), and \((4,4,5^8,6,6)\). The latter two contain a part of size six and would give a K6 in C, forbidden by \(\omega(C)\le5\).

Thus only \((5^{12})\) survives. Complementing the published construction gives ten isolated K5 components in C and two additional special K5 cliques \(N_s,N_t\) inside the 11-vertex gadget \(G_{11}\), together with the special point x. These twelve disjoint K5s partition exactly \(V(K_{61})\setminus\{x\}\). This is the precise source interface used in Sections 1–3.

No degree-nine exceptional vertex is assumed. The published gadget parameter has \(|A|\in\{1,2,3,4\}\), and its variable degrees are \((4+a,9-a)\); the present obstruction uses only the twelve K5 factors and their partition property.


## 6. Parent-level corollary: support- and m-independent

The earlier support- and m-independent parent promotion claim is **RETRACTED**. It used the unavailable hypotheses omega(H)<=5 and omega(C)<=5 and an unproved Type-I source gate. The actual parent contract permits omega(H)<=11 and omega(C)<=12. Consequently this lemma presently closes no Q32 support row and supplies no parent-promotion edge. E407 Q32/V12, E408 Q33 support promotion, and the original EG617 theorem remain unaffected.


## 7. Critical audit correction — actual EG617 hypotheses

The current EG617 problem is the balanced-coloring problem: every 13-set must contain all twelve colors. This implies \(\alpha(C)\le12\) and \(\omega(C)\le12\) for each color graph C; it does not prohibit monochromatic K6. On the 47-point Q32 core, the registered R(4,49) contract gives \(\omega(H)\le11\), not five.

The exact-129 source audit's Type-I conclusion used \(\omega(C)\le5\) to prove that \(\overline C\) is non-12-partite and to eliminate the two Kang–Pikhurko equality profiles containing a size-six part. Without that hypothesis, the complement may be 12-partite. For example, \(C_0=5K_6\dot\cup3K_5\dot\cup4K_4\) has 61 vertices, 129 edges, \(\alpha(C_0)=12\), and \(\omega(C_0)=6\), and its complement is 12-partite. This is a local one-color model, not a claimed full coloring.

The tight-part lemma remains a valid conditional theorem, but its conclusion under \(\alpha(H)\le4\) is only \(\omega(H)\ge6\), which is allowed by the actual \(\omega(H)\le11\) cap. It therefore cannot exclude the three partitions in EG617. The previous m=8/9 and all-support Q32 closure claims are withdrawn; see AUDIT_RETRACTION_BALANCED_PREMISES.md.
