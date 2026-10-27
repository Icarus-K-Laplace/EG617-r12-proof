# E408 Q32: close the v=44 terminal by exceptional-degree capacity

Date: 2026-10-27  
Status: **PROVED_CONDITIONAL** under the registered Q32 285-edge / exact-129 Type-I / v=44 triple-pair normal form.  
Scope: excludes \(|U|=44\). It does not use the Q33 284-edge theorem and does not yet exclude \(|U|=45,46,47\).

## 1. Q32 v=44 normal form

Use the independent Q32 contract:
\[
|V(H)|=47,\quad e(H)=285,\quad \alpha(H)\le4,\quad \delta(H)\ge12,
\quad \sum_H(d_H-12)=6.
\]
Let \(U\) be the union of all exact-color four-point witnesses. The sibling capacity theorem proves \(|U|\ge44\). Assume \(|U|=44\), and put
\[
W=H\setminus U,\qquad |W|=3.
\]
Let \(m\in\{8,9,10\}\) be the number of exact-129 non-target colors.

The registered low-support triple-pair theorem proves that at most three exact colors can have their exceptional Type-I vertex outside \(W\) in the corresponding v=44 ten-witness normal form. Equivalently, at least
\[
\boxed{m-3}
\]
exact colors have their Type-I exceptional vertex \(x_C\in W\).

For \(w\in W\), write
\[
n_w=|\{C:\ C\text{ exact-129 and }x_C=w\}|.
\]
Then
\[
\boxed{\sum_{w\in W}n_w\ge m-3.}\tag{1}
\]

## 2. Degree floor for exact-129 colors

The contextual equality theorem says every exact-129 color on the 61-point residual is KP Type I: ten isolated \(K_5\) components plus an 11-point gadget consisting of two \(K_5\)'s and an exceptional vertex of degree 9.

Therefore every residual vertex has exact-color degree at least 4. If the vertex is the exceptional vertex of that exact color, its degree is 9, i.e. five more than the baseline four.

Hence for any \(w\in W\), the sum of its degrees over all \(m\) exact colors is at least
\[
\boxed{4m+5n_w.}\tag{2}
\]

## 3. Degree floor for the nonexact colors

Let \(D\) be a non-target color with
\[
e_D(R)=129+s,\qquad s\in\{1,2,3\}.
\]
For a vertex \(v\in R\), put \(d=d_D(v)\). The set of nonneighbors of \(v\) in \(R\setminus\{v\}\) has size \(60-d\). If the induced D-graph on those nonneighbors contained an independent 12-set, adjoining \(v\) would give a D-independent 13-set. Thus that induced graph has independence number at most 11 and therefore at least
\[
p_{11}(60-d)
\]
edges.

Those edges are among the \(e_D(R)-d\) edges not incident with \(v\). Hence the necessary inequality
\[
\boxed{p_{11}(60-d)\le129+s-d.}\tag{3}
\]

The exact small values are
\[
p_{11}(60)=135,\qquad p_{11}(59)=130,\qquad p_{11}(58)=125.
\]
Therefore:
- if \(s=1\), then \(d\ge2\);
- if \(s=2\) or \(s=3\), then \(d\ge1\).

Since the nonexact positive excesses sum to three, their degree contribution at **every** residual vertex is at least
\[
B_m:=
\begin{cases}
6,&m=8 \quad(s=1,1,1),\\
3,&m=9 \quad(s=1,2),\\
1,&m=10\quad(s=3).
\end{cases}\tag{4}
\]

## 4. Total degree contradiction on each point of W

Every residual vertex has exactly 60 incident edges split among the target color and the eleven non-target colors. The Q32 residual minimum-degree contract gives
\[
d_F(w)\ge13.
\]
Combining target degree, (2), and (4),
\[
60\ge13+(4m+5n_w)+B_m.
\]
Thus
\[
5n_w\le47-4m-B_m.
\]
For the three possible values of m:
\[
\begin{array}{c|c|c}
m&B_m&47-4m-B_m\\ \hline
8&6&9\\
9&3&8\\
10&1&6
\end{array}
\]
so in every case
\[
\boxed{n_w\le1.}\tag{5}
\]
Since \(|W|=3\), (5) yields
\[
\sum_{w\in W}n_w\le3.
\]
But (1) gives
\[
\sum_{w\in W}n_w\ge m-3\ge5,
\]
a contradiction.

Therefore
\[
\boxed{|U|\ne44.}
\]

Combined with the sibling support floor \(|U|\ge44\), the surviving Q32 support sizes are now
\[
\boxed{|U|\in\{45,46,47\}.}
\]

## 5. Firewall

Used only:
- Q32 285-edge residual/core contract;
- exact-129 Type-I factor theorem;
- v=44 triple-pair normal form from `LOW_SUPPORT_TRIPLE_PAIR_CAPACITY.md`;
- the residual excess identity \(\sum s_C=3\);
- Turan floors for independence number 11 after deleting a vertex and its color-neighborhood.

Not used:
- Q33 284-edge/excess-four equations;
- Q33 31-point/56-witness closure;
- support-41 results;
- any unverified single-edge monochromatic-K12 inference.

The remaining Q32 task is to exclude v=45,46,47 or compress them to a smaller graph-level terminal.