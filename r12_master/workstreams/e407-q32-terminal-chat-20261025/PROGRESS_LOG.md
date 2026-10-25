# E407 Q32 terminal — progress log

## 2026-10-25 — Round 1

### New mathematical result

**Proved conditionally:** the delta=16 minimum-support boundary is automatically four-partite and reduces to one labelled core kernel.

The proof uses the 49 linear K4 witnesses, the exact core ledger, Brouwer's second-Turan bound, equality in Turan on 18 vertices, and the total degree-excess budget. It excludes endpoint splits (4,1) and (3,2) for the five cross edges in H[U].

The sole surviving endpoint allocation is (5,0): all five distinct D-endpoints have the same K4 as their exact W-neighbourhood, and that K4 is complete to D. Each vertex in the other three W-components must be complete to a 7-part; labels may vary within a component, and no component-wide bijection is proved.

### Verification

Ran the local arithmetic/kernel audit script. Output: E407_DELTA16_STRUCTURAL_KERNEL_ARITHMETIC_OK.

The script checks exact edge ledgers, integer partition profiles, and finite excess inequalities. It does not verify graph realization, all graph-theoretic lemmas, or the original K145 theorem.

A reverse-saturation lemma was also proved: every vertex of W is complete to exactly one U-part. The proof handles the exceptional possibility of a 13-neighbour W-vertex and excludes it by the four-endpoint K4 degree contradiction.

### Global effect

- New closed contracts: 1 structural reduction (delta=16 boundary).
- Fully excluded E407 templates: 0.
- Remaining E407 minimum-support branches: delta<=15 (four-partite and non-four-partite), plus the surviving delta=16 kernel.
- E408 Q32/Q33: untouched.
- Original T61-to-K145 bridge: still OPEN / NOT_CERTIFIED.

### Next attack

Combine the forced vertex-level U-part neighbourhoods and common-K4 endpoint structure with the exact row/hub requirements of templates A-E. In parallel, use the near-Turan classification for delta=14,15 to bound the remaining cross edges in H[W]. Do not claim any template closed until an actual incompatibility proof is obtained.


## 2026-10-25 — Round 2 (corrected): audit of the \(\delta=16\) endpoint split

### Correction

An attempted closure of the \((5,0)\) endpoint split was invalid and is withdrawn. The error was assuming that the three non-endpoint vertices of \(D\), each having five neighbours in \(W\), must be complete to a \(K_5\). In the \((5,0)\) split, the endpoint \(K_4\) is complete to all of \(D\), so each non-endpoint \(D\)-vertex already has four neighbours in that \(K_4\) and has **exactly one** additional \(W\)-neighbour. That extra neighbour need not make it complete to a \(K_5\). The proposed pigeonhole/excess contradiction therefore does not follow.

### Results that remain valid

- The \(\delta=16\) boundary is forced four-partite, with \(U\)-parts \(7,7,7,8\) and \(H[W]=K_5\cup K_5\cup K_4\cup K_4\).
- The five cross edges in \(H[U]\) form a matching.
- Every \(W\)-vertex is complete to exactly one \(U\)-part.
- The \((4,1)\) and \((3,2)\) endpoint splits are excluded by degree-excess contradictions.
- In the remaining \((5,0)\) split, the endpoint \(K_4\) is complete to \(D\); each vertex in the other \(K_4,K_5,K_5\) components is complete to a small part; each of the three non-endpoint \(D\)-vertices has exactly one additional \(W\)-neighbour outside the endpoint \(K_4\).

### Current status and next attack

- E407 Q32: **OPEN / NOT_CERTIFIED**.
- \(\delta=16\): OPEN, narrowed to the labelled \((5,0)\) kernel.
- \(\delta\le15\): four-partite near-extremal and non-four-partite cases remain open.
- E408 Q32/Q33 and the original \(K_{145}\)-to-T61 bridge: untouched.

Next, characterize the three extra \(D\)-to-\(W\) edges and the full-part labels of the 14 vertices outside the endpoint \(K_4\), then intersect this incidence system with the five V12 shell templates. Do not claim \(\delta=16\) closed until the \((5,0)\) kernel is excluded or realized.


## 2026-10-25 — Round 3: exact witness-array multiplicities

### New proved identity

Under the \(\delta=16\) four-partite boundary, the 49 witness blocks and seven exact-129 color classes induce a resolvable Latin-square incidence system:

- every \(A\)-\(B\), \(A\)-\(C\), and \(B\)-\(C\) pair occurs in exactly one block;
- each color class is a transversal of the resulting order-7 Latin square;
- each color class uses seven distinct \(D\)-vertices and omits exactly one of the eight;
- for every \(d\in D\), the number \(r_d\) of colors omitting \(d\) equals the number of missing witness partners of \(d\) in each of \(A,B,C\).

Thus \(\sum_{d\in D}r_d=7\). The five actual \(H[U]\) cross edges are five matching pairs among these missing pairs, so each of the five endpoint labels has \(r_d\ge1\). Therefore endpoint labels use at least five omission units, leaving at most two for the three non-endpoint labels. At least three endpoint labels have \(r_d=1\), and at least one non-endpoint \(D\)-vertex has \(r_d=0\) and appears in every color class.

The full statement and proof are in DELTA16_WITNESS_ARRAY.md.

### Why this matters

This converts the 49-witness count into a precise incidence/omission identity. It does not by itself exclude the surviving \((5,0)\) \(W\)-kernel or any of templates A–E. The next step is to combine the omission multiplicities with the template-specific shell-row/hub-hit requirements rather than use only scalar incidence totals.

### Current status

- \(\delta=16\): OPEN, narrowed to the labelled \((5,0)\) kernel plus the exact witness-array constraints.
- \(\delta\le15\): OPEN.
- E407 Q32 overall: OPEN / NOT_CERTIFIED.


## 2026-10-25 — Round 4: \(\delta=15\) non-four-partite branch reduced

### New proved result

At \(\delta=15\), a non-four-partite \(K_5\)-free graph \(L\) on 29 vertices has 309 edges, exactly the Brouwer second-Turán maximum. Applying the Kang–Pikhurko equality classification, \(L\) has a 28-vertex complete four-partite base plus an exceptional vertex \(x\), with base part profile one of
\[
(7,7,7,7),\quad(6,7,7,8),\quad(6,6,8,8).
\]

Using the 49 pairwise edge-disjoint witness \(K_4\)'s:
- Let \(A\) be the proper nonempty subset in the Kang–Pikhurko construction, \(a=|A|\), and \(t\) the number of witness blocks containing \(x\).
- \(P_1P_2\)-edge capacity gives \(t\ge49-n_1n_2+a\).
- The exceptional vertex has degree \(n_3+n_4+a+1\), and each \(x\)-block uses three distinct \(x\)-edges, so \(3t\le n_3+n_4+a+1\).

These two inequalities eliminate the base profiles \((6,7,7,8)\) and \((6,6,8,8)\). Thus only the balanced base profile \((7,7,7,7)\) can survive.

For that profile:
- \(a\le t\le\lfloor(15+a)/3\rfloor\);
- \(t_A,t_y\) (the two possible types of \(x\)-block) must be \((a,0)\), \((a-1,1)\), or \((a,1)\);
- every one of the 49 \(P_3P_4\) pairs is used by exactly one witness block;
- the 15-edge leave has exact pair-type counts, and every vertex in \(P_3\cup P_4\) has leave-degree exactly one.

The full proof and exact leave ledger are in DELTA15_SECOND_TURAN_PACKING.md. The equality classification is cited there to Kang–Pikhurko (2005).

### Effect and limits

This is a genuine reduction of the \(\delta=15\) non-four-partite branch, not its elimination. The balanced equality construction and its exact 15-edge leave remain compatible at the current counting level; the shell-row/hub constraints must still be applied.

Current status:
- \(\delta=16\): OPEN, narrowed to the \((5,0)\) endpoint kernel.
- \(\delta=15\) non-four-partite: only the balanced Kang–Pikhurko base profile remains; OPEN.
- \(\delta=15\) four-partite, \(\delta=14\), and \(\delta\le13\): OPEN.
- E407 Q32 overall: OPEN / NOT_CERTIFIED.


### Round 4 addendum — core-degree restriction on the KP exceptional vertex

Using \(d_{H[U]}(x)=13-a\), the core minimum degree, and the already classified \(H[W]\) profiles, the exceptional vertex has
\[
d_H(x,W)=a-1+\epsilon_x.
\]
The independence-number constraint forces it to be complete to a whole \(W\)-clique component. In the one-cross-edge \(K_4,K_4,K_5,K_5\) profile, degree at most five still forces a whole component because avoiding an independent transversal without completing a component would require at least six neighbours.

This reduces the Kang–Pikhurko subset size from \(a=1,\ldots,6\) to **\(a\in\{4,5,6\}\)**:
- with \(\epsilon_U=0\), the \(K_3\cup K_5^3\) profile permits \(a\ge4\), while the profiles with minimum clique size four require \(a\ge5\);
- with \(\epsilon_U=1\), \(H[W]=K_4\cup K_4\cup K_5\cup K_5\), so \(a\ge4\), and \(a=4\) forces \(\epsilon_x=1\).

This is another necessary-condition reduction; the balanced \((7,7,7,7)\) equality profile remains OPEN.


## 2026-10-25 — Round 5: \(\delta=15\) non-four-partite branch excluded

### New terminal contradiction

The balanced Kang–Pikhurko profile left after Round 4 is now excluded by combining the exceptional vertices \(x,y\) with the independent-set constraint on \(H\).

For the balanced \((7,7,7,7)\) base and \(a=|A|\):
\[
d_{H[U]}(x)=13-a,\qquad d_{H[U]}(y)=6+a,
\]
so
\[
d_H(x,W)=a-1+\epsilon_x,\qquad d_H(y,W)=6-a+\epsilon_y,
\qquad \epsilon_x+\epsilon_y\le\epsilon_U\le1.
\]

The exact core ledger gives \(e(H[W])=33-\epsilon_U\). Since \(\alpha(H[W])\le4\), the complement on 18 vertices has 120 or 121 edges, above the non-four-partite second-Turán threshold 118. Hence \(\overline{H[W]}\) is four-partite, and the allowed \(H[W]\) profiles are:
- \(\epsilon_U=0\): \(K_3\cup K_5^3\), \(K_4^3\cup K_6\), or \(K_4\cup K_4\cup K_5\cup K_5\) plus one cross edge;
- \(\epsilon_U=1\): \(K_4\cup K_4\cup K_5\cup K_5\).

Every \(u\in U\) must be complete to a whole \(W\)-clique part when the parts are anticomplete. In the one-cross-edge profile, the same conclusion holds for \(u\) with at most five \(W\)-neighbours: otherwise it needs at least six neighbours to block all independent transversals.

- If \(\epsilon_U=0\), \(x\) requires \(a-1\) to be at least the smallest part size, while \(y\) requires \(6-a\) to be at least that same minimum. The three profiles respectively force \(a\ge4,a\le3\); \(a\ge5,a\le2\); and \(a\ge5,a\le2\). Each is impossible.
- If \(\epsilon_U=1\), all parts have size at least four, forcing \(a-1+\epsilon_x\ge4\) and \(6-a+\epsilon_y\ge4\). Thus \(a\ge4\) but \(a\le3\), contradiction.

Therefore the whole \(\delta=15\), \(L\) non-four-partite branch is **EXCLUDED**, under the retained 49-witness/core contract and the Kang–Pikhurko equality classification.

### Current frontier

- \(\delta=16\): OPEN, reduced to the labelled \((5,0)\) endpoint kernel.
- \(\delta=15\), \(L\) non-four-partite: **EXCLUDED**.
- \(\delta=15\), \(L\) four-partite: OPEN.
- \(\delta=14\) and lower: OPEN.
- E407 Q32 overall: OPEN / NOT_CERTIFIED; no complete \(K_{145}\) proof is claimed.


## 2026-10-25 — Round 6: \(\delta=16\) four-partite branch excluded

### New terminal contradiction

The \(\delta=16\) support-boundary case is now excluded under the retained E407 core/witness contract.

The reduction forces:
- \(L=\overline{H[U]}\) four-partite with parts \(7,7,7,8\);
- \(H[U]\) has 91 within-part edges and five cross edges, which form a matching;
- \(\epsilon_U=0\), \(H[W]=K_5\cup K_5\cup K_4\cup K_4\);
- each of the five \(D\)-endpoints has exactly one \(K_4\) as its \(W\)-neighbourhood.

The \((4,1)\) and \((3,2)\) endpoint splits contradict the total four-unit excess budget. For the remaining \((5,0)\) split, all five endpoints share one \(K_4=C_0\). Every \(w\in C_0\) is adjacent to the five endpoint vertices. If \(w\) were not complete to the 8-part \(D\), reverse saturation forces it to be complete to a 7-part, giving at least \(7+5=12\) \(U\)-neighbours and hence \(\epsilon_w\ge3\). At most one \(w\in C_0\) can be such an exception. But then at least two non-endpoint vertices of \(D\) would have only three neighbours in \(C_0\) and two outside; neither set of neighbours contains a whole \(W\)-component (all components have size at least four), contradicting \(\alpha(H)\le4\). Hence all four vertices of \(C_0\) are complete to \(D\), yielding a \(K_8\cup K_4\) joined completely across, i.e. a forbidden \(K_{12}\) in \(H\).

This closes the last endpoint split. The proof is in FOUR_PARTITE_TERMINAL.md; the arithmetic consistency checks are in verify_e407_delta16_kernel.py.

### Independent audit of the \(\delta=15\) non-four-partite exclusion

The previous round's \(x,y\) degree contradiction was rechecked. Under the Kang–Pikhurko equality classification, the two unbalanced base profiles fail the 49-block edge-capacity inequalities. In the balanced \((7,7,7,7)\) profile,
\[
d_H(x,W)=a-1+\epsilon_x,\qquad d_H(y,W)=6-a+\epsilon_y,\qquad \epsilon_x+\epsilon_y\le\epsilon_U\le1.
\]
The \(W\)-side Brouwer bound forces the stated four-clique-part profiles. Independence-number saturation requires each of \(x,y\) to be complete to a whole \(W\)-part; for the one-cross-edge profile the same follows for vertices with at most five \(W\)-neighbours. Each allowed profile then forces incompatible lower and upper bounds on \(a\). The exclusion remains conditional on the retained core/witness contract and the cited Kang–Pikhurko equality classification.

### Updated frontier

- \(\delta=16\), four-partite: **EXCLUDED**.
- \(\delta=15\), non-four-partite: **EXCLUDED** under the retained contract.
- \(\delta=15\), four-partite: OPEN.
- \(\delta\le14\): OPEN (both four-partite and non-four-partite cases where allowed).
- E407 Q32 overall: **OPEN / NOT_CERTIFIED**.
- E408 Q32/Q33 and the original \(K_{145}\)-to-T61 bridge: untouched.
