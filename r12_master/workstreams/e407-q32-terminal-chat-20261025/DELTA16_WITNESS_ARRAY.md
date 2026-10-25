# E407 Q32 \(\delta=16\): exact witness-array constraints

Date: 2026-10-25  
Status: **PROVED under the frozen \(\delta=16\) core/witness contract; compatibility with the shell templates remains OPEN.**

## 1. Contract

Use the notation of `FOUR_PARTITE_TERMINAL.md`. The four parts of \(L=\overline{H[U]}\) are \(A,B,C,D\), with sizes \(7,7,7,8\). The 49 selected independent 4-sets \(Q\) are \(K_4\)'s in \(L\), one point per part. They are partitioned into seven color classes \(\mathcal Q_1,\ldots,\mathcal Q_7\), each of size seven; sets in one class are disjoint, and any two witnesses share at most one point.

## 2. Each color class is a transversal of the \(A,B,C\) Latin square

There are 49 possible \(A\)-\(B\) pairs and 49 witness blocks. No pair repeats, so every \(A\)-\(B\) pair occurs exactly once. The same holds for \(A\)-\(C\) and \(B\)-\(C\). Thus the \(C\)-coordinate is a Latin square \(c=L(a,b)\) on \(A\times B\).

For a fixed color \(i\), the seven witness blocks are disjoint and use one vertex from each of \(A,B,C\). They therefore use each point of each of these three parts exactly once: their triples form a transversal of this Latin square. The seven color classes partition all 49 cells into seven transversals.

Within each color class, the seven \(D\)-coordinates are distinct, so the class omits exactly one of the eight \(D\)-vertices.

## 3. Missing-partner multiplicity identity

For \(d\in D\), define:
- \(m_d\): the number of witness blocks containing \(d\);
- \(r_d\): the number of colors whose seven-block class omits \(d\).

Since every color class contains \(d\) exactly once unless it omits \(d\),
\[
m_d=7-r_d.
\]

The \(D\)-pairs in the witness blocks never repeat. Therefore \(d\) is paired with \(m_d\) distinct vertices in each of \(A,B,C\), and is the missing witness partner of exactly
\[
7-m_d=r_d
\]
vertices in each small part. In particular,
\[
\sum_{d\in D}r_d=7.
\]
Equivalently, each of the seven colors omits exactly one \(D\)-vertex, and the omission multiplicities across colors are exactly \((r_d)_{d\in D}\).

Every small-part vertex has exactly one missing \(D\)-partner among the 49 witness blocks: it occurs once in each of the seven colors and its seven \(D\)-partners are distinct.

## 4. Consequences of the five \(H[U]\) cross edges

The five \(H[U]\) cross edges form a matching \(M\subseteq D\times(A\cup B\cup C)\). Every edge of \(M\) is a missing witness pair, because each witness \(Q\) is independent in \(H\). Thus each of the five endpoint labels \(d\in D_{\rm end}\) satisfies \(r_d\ge1\), and its unique \(H[U]\) edge is one of the \(r_d\) missing pairs in the corresponding small part.

Consequently,
\[
\sum_{d\in D_{\rm end}}r_d\ge5,\qquad
\sum_{d\notin D_{\rm end}}r_d\le2.
\]
This gives three exact restrictions:

1. At least three of the five endpoint labels have \(r_d=1\), because only two excess omission units remain beyond the baseline one per endpoint.
2. At most two of the three non-endpoint labels have \(r_d>0\); in particular, at least one non-endpoint \(d\) has \(r_d=0\).
3. The endpoint \(D\)-labels are omitted by at least five of the seven color classes in total, while non-endpoint labels account for at most two color omissions.

If \(r_d=0\), then \(d\) appears in all seven color classes and is paired with every vertex of each of \(A,B,C\) exactly once. Thus at least one non-endpoint \(D\)-vertex defines a full transversal across the seven classes.

## 5. What this does and does not close

This identity is stronger than the scalar block count: it fixes the multiplicity of every missing \(D\)-partner and ties that multiplicity to the exact-129 color omitted from each class. It is an exact incidence constraint, not a contradiction.

The next useful compatibility test is to combine:
- the five prescribed missing pairs that are actual \(H[U]\) edges;
- the at-most-two extra omission units beyond one per endpoint label;
- the shell-template-specific hub-hit requirements for each color class;
- the \(W\)-side \((5,0)\) labelled kernel in `FOUR_PARTITE_TERMINAL.md`.

No claim is made that the Latin-square/transversal incidence system is unrealizable in isolation. Its compatibility with the complete E407 core is moot at \\(\delta=16\\), because the W-side endpoint argument already excludes that core. E407 Q32 remains OPEN / NOT_CERTIFIED for other \\(\delta\\)-values.
