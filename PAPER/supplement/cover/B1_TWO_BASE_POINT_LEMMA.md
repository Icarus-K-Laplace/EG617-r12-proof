# Exceptional Q28 B1 states: two base points in every row triple

**Status:** analytic correction incorporated in \`PAPER/sections/08-cover.tex\` on 1 November 2026.  
**Scope:** the two exceptional q=28 B1 states with hub weights \`(9,9,10)\` and all low rows regular.

## Contract and row classes

Fix a maximum-charge pivot \(p\) in a 61-vertex parent \(F\) with
\[
|V(F)|=61,\quad \delta(F)=13,\quad \alpha(F)\le5,\quad
\omega(F)\le11,\quad E=408,\quad Q=28.
\]
In either B1 state the missing graph at \(p\) is \(K_{3,k}\) together with
\(10-k\) isolates, where \(k\in\{8,9\}\). Its three hubs have weights
\((9,9,10)\), and all ten low vertices are regular. Put
\(K=\{p\}\cup Y\), where \(Y\) is the ten low vertices. Then \(K\) is a
target \(K_{11}\). For each \(v\in K\), let \(T_v\) be its three neighbors
outside \(K\). The shell-state all-or-none rule says that every other
\(w\in K\) is adjacent to either all or none of \(T_v\). Hence the triples
are equal or disjoint. Their multiplicities \(c_i\) are 2 or 3 and sum
to 11, so there are at least four distinct row classes.

## At least two base points per triple

For the class \(T_p\), its multiplicity is \(c=11-k\). Each hub has missing
degree \(k\), and its weight is \(9,9,\) or \(10\). Since
\(d_F(x)=13+g_x\) and \(g_x=t_x-k\), the two weight-9 hubs have degree
\[
13+(9-k)=22-k=c+11,
\]
while the weight-10 hub has degree \(c+12\). Thus \(T_p\) has two base
points of degree \(c+11\).

An inactive low is a true twin of \(p\), so its outside triple is \(T_p\). For an active low \(v\), the ten other shell vertices are exactly \(K\setminus\{v\}\) and are all regular. Thus its repivot shell is either one of the two q27 states, or (if its charge is 28) one of the two B1 states: the six q28 states with a decorated low row are excluded by regularity. Both allowed types have only full or empty low rows, proving the all-or-none rule for every active triple.

Now take an active low vertex \(v\in K\), and let \(D_v=T_v\) be its
three-point row in the old 47-core \(C\). In the B1 state, the other ten
shell vertices outside \(N_M(v)\) are regular and undecorated, so
\(\rho=0\). The exact repivot identity at \(\beta=11\) gives
\[
q_v=27+h_{11}+\kappa+b\le Q=28,
\]
where
\[
h_{11}=\sum_{x\in D_v}(d_C(x)-11),\quad
\kappa=3-e_C(D_v),\quad
b=e_F(S,D_v),
\]
and \(S=T_p\) is the old three-hub set.

If \(\kappa=1\), then \(h_{11}=b=0\). All three vertices of \(D_v\)
would have degree 11 in \(C\), so the deficient-clique lemma says they
form a clique, contrary to \(e_C(D_v)=2\). Values \(\kappa\ge2\) are
impossible from the charge inequality. Therefore \(\kappa=0\), and
\[
h_{11}+b\le1.
\]
Thus \(D_v\) is a triangle, and at most one of its vertices can either
have degree 12 in \(C\) or be adjacent to \(S\). At least two vertices
\(x\in D_v\) satisfy both \(d_C(x)=11\) and \(N_F(x)\cap S=\varnothing\).
Each such \(x\) has exactly \(c_i\) neighbors in \(K\), by the all-or-none
rule, where \(c_i\) is the multiplicity of its row class. Since \(F\) is
the disjoint union of \(K\), \(S\), and \(C\), these two points have
\[
d_F(x)=d_C(x)+c_i=c_i+11.
\]
Every row class therefore contains at least two base points of degree
\(c_i+11\); at most one point in the triple may have degree \(c_i+12\).

## Cross-row contradiction using base points only

Choose a base point \(x\in T_i\) and a pivot \(p_j\in K\) from a
different row class \(j\). The triples are disjoint, and the only
neighbors of \(p_j\) outside \(K\) are \(T_j\), so \(x\) is nonadjacent
to \(p_j\) and lies in its actual core \(C_{p_j}\). Exactly \(c_i\) of
\(x\)'s neighbors in \(K\) are removed with \(N[p_j]\). Hence
\[
d_{C_{p_j}}(x)
=d_F(x)-c_i-e_F(x,T_j)
=11-e_F(x,T_j).
\]
Every actual 47-core has minimum degree at least 11. Therefore
\(e_F(x,T_j)=0\): base points of \(T_i\) are anticomplete to \(T_j\).

Choose three distinct row classes \(i,j,k\), which exist because there
are at least four. Take base points \(x\in T_i\), \(y\in T_j\), and a
pivot \(p_k\in K\) from class \(k\). Both \(x,y\) lie in \(C_{p_k}\);
the preceding argument shows each has degree exactly 11 there, and
they are nonadjacent. This contradicts the deficient-clique lemma,
which says that the degree-11 vertices of any actual 47-core form a
clique.

The correction does not assert that all three points of a row triple
have degree \(c_i+11\). It uses only the two guaranteed base points,
which are sufficient for the three-class contradiction.
