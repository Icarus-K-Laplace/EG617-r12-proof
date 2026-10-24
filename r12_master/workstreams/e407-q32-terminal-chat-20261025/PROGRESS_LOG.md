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
