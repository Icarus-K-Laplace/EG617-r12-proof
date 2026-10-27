# E407 crosscut — seven exact-129 colors are impossible

Updated: 2026-10-27
Status: **PROVED_CONDITIONAL** under the genuine h13 T61 full-color contract, exact-129 Type-I classification, the registered nonexact pointwise degree floors, and the Brouwer--Kang--Pikhurko second-Turan theorem.

This file is an auxiliary crosscut produced after the E408 closure. It does not modify the E407 sibling workstream and does not claim E407 Q32 closed.

## 1. Residual full-color ledger at E407

Let R be a genuine 61-vertex E407 h13 T61 residual. The eleven non-target colors satisfy

\[
e_C(R)=129+s_C,\qquad s_C\ge0,
\]

and the full residual edge partition gives

\[
\sum_C s_C=411-407=4.
\]

Let m be the number of exact colors, i.e. colors with s_C=0. Since the four units of excess are positive integers on the nonexact colors,

\[
7\le m\le10.
\]

We prove m!=7.

If m=7, then there are exactly four nonexact colors and their positive excesses sum to four. Hence every one has

\[
s_C=1,\qquad e_C(R)=130.
\]

## 2. Exact exceptional vertices are distinct in the m=7 branch

For an exact Type-I color, every residual vertex has color-degree at least four and the unique exceptional vertex has degree nine. Let n_v be the number of exact colors for which a residual vertex v is exceptional.

In the m=7 branch:

- target degree is at least13;
- the seven exact colors contribute at least 7*4+5n_v;
- each of the four 130-edge nonexact colors has minimum degree at least3.

Therefore

\[
60\ge13+28+5n_v+12=53+5n_v.
\]

Thus n_v<=1. Consequently the seven exact colors have seven distinct exceptional vertices. Let their set be

\[
X=\{x_1,\ldots,x_7\}.
\]

## 3. A 130-edge color has either zero or exactly four degree-three vertices

We record the low-degree lemma independently of Q32.

Let D be any non-target color on the 61-point residual with

\[
e(D)=130,\qquad \alpha(D)\le12,\qquad \omega(D)\le5,
\]

and the registered pointwise floor delta(D)>=3.

Suppose d_D(v)=3. Let S=N_D(v), |S|=3, and let N be the 57 non-neighbours of v other than v. Since v is anticomplete to N,

\[
\alpha(D[N])\le11,
\]

while omega(D[N])<=5. Since 57>55, the complement form of the Brouwer--Kang--Pikhurko second-Turan theorem gives

\[
e(D[N])\ge p_{11}(57)+\lfloor57/11\rfloor-1=120+5-1=124.
\]

After these 124 edges and the three v--S edges, at most three edges remain. Every point of S has degree at least three, so after its edge to v the three S-points require at least six further degree incidences. Three remaining edges can supply at most six incidences, with equality only if all three lie inside S. Hence S is a triangle, there are no S--N edges, and

\[
D[\{v\}\cup S]=K_4
\]

is an isolated component. All four vertices of that K4 have degree exactly three.

Two isolated K4 components are impossible. If two existed, deleting their eight vertices would leave a graph D' with

\[
|V(D')|=53,\qquad e(D')=118.
\]

Every independent set of D' can be enlarged by one vertex from each deleted K4, so alpha(D')<=10; also omega(D')<=5. Since 53>50,

\[
e(D')\ge p_{10}(53)+\lfloor53/10\rfloor-1=115+5-1=119,
\]

contradicting e(D')=118.

Therefore for every 130-edge color D, its degree-three set is either empty or exactly the four vertices of one isolated K4. In particular

\[
|L_D|\in\{0,4\},
\]

where L_D={v:d_D(v)=3}.

## 4. Every exact exceptional vertex lies in at least two low-degree K4s

Fix x in X. Its own exact color contributes degree9, while the other six exact colors contribute at least4 each. Therefore all seven exact colors contribute at least

\[
9+6\cdot4=33
\]

at x. The target contributes at least13, so the four nonexact 130-edge colors together have degree sum at most

\[
60-33-13=14.
\]

Each has degree at least3. If at most one of the four degrees were equal to3, their sum would be at least

\[
3+4+4+4=15,
\]

a contradiction. Hence at least two of the four nonexact colors have degree exactly3 at x.

Equivalently, if the four degree-three K4 sets are L_1,...,L_4 (allowing an empty set when a color has no degree-three vertices), then every x in X satisfies

\[
r_x:=|\{i:x\in L_i\}|\ge2.
\]

## 5. Pairwise intersection capacity gives the contradiction

For two different nonexact colors i!=j,

\[
|L_i\cap L_j|\le1.
\]

Indeed, if two vertices u,v belonged to both L_i and L_j, then each L-set is an isolated monochromatic K4, so the edge uv would simultaneously have both colors, impossible in an edge-coloring.

Therefore the total pairwise block intersection count satisfies

\[
\sum_v \binom{r_v}{2}
=\sum_{1\le i<j\le4}|L_i\cap L_j|
\le\binom42=6.
\]

But the seven distinct exact exceptional vertices all have r_x>=2, so already on X

\[
\sum_{x\in X}\binom{r_x}{2}\ge7.
\]

Contradiction.

Hence

\[
\boxed{m\ne7.}
\]

Since the E407 excess ledger gives 7<=m<=10, every genuine E407 h13 T61 residual must satisfy

\[
\boxed{m\in\{8,9,10\}.}
\]

## 6. Consequence for the live E407 Q32 V12 terminal

The active V12 common-core workstream currently selects seven exact-129 color classes and builds 49 labelled support blocks from them. The theorem above proves that, in any genuine E407 parent realizing that terminal, those seven selected colors cannot be all the exact colors.

Therefore every surviving V12 terminal must contain at least one additional exact-129 color outside the seven selected classes:

\[
\boxed{\text{selected exact classes}=7,\qquad \text{global exact count }m\ge8.}
\]

This is a new interface for the common-core attack. Any eventual realization must simultaneously accommodate the existing seven selected support systems and at least one extra exact Type-I factor on the same 61-point residual.

No claim is made here that the eighth exact color supplies one of the previously selected support classes, or that the present theorem by itself excludes a V12 shell template.

## 7. Firewall

Used:

- E407 h13 residual full-color excess identity sum s_C=4;
- target minimum degree13;
- exact-129 Type-I exceptional degree9 / ordinary degree at least4;
- s=1 nonexact minimum degree at least3;
- alpha(C)<=12 and omega(C)<=5 for every non-target residual color;
- Brouwer--Kang--Pikhurko second-Turan bound in complement form;
- unique edge ownership.

Not used:

- the E408 seven-block equality system;
- Q32 285-edge core identities;
- Q33 284-edge support-31 identities;
- the E407 five-template shell classification;
- the Didin-dependent delta=14 branch.

Thus this crosscut is independent of the E407 shell-template casework and can be imported into that workstream only if its named full-color/extremal inputs are accepted.
