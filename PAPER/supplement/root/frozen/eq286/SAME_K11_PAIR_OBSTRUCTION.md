# Two support points on the same \(K_{11}\)--\(K_{11}\) pair

**Status:** PROVED_CONDITIONAL (analytic, conditional only on the \(f_{11}\) blocker bound, the small-side concentration inequality, and the \(T=8\) common-neighborhood capacity).  
**Date:** 2026-11-01.

## Contract

Let \(z,z'\) be distinct vertices with the same two-point support \(\{0,1\}\). Let \(K_0,K_1\) be their two private \(K_{11}\) cliques, and write
\[
A=K_0\setminus N(z),\quad B=K_1\setminus N(z),\qquad
A'=K_0\setminus N(z'),\quad B'=K_1\setminus N(z').
\]
Put \(a=|A|,b=|B|,a'=|A'|,b'=|B'|\). All four missing sets are nonempty. The blocker property gives
\[
A\times B\subseteq E(H),\qquad A'\times B'\subseteq E(H).
\]
Since the total excess is eight, each individual \(f_{11}\)-charge is at most eight. The scalar \(f_{11}\) bound therefore implies that each point has a missing side of size at most two, and a missing side of size two forces the opposite side to have size at most four.

## Case 1: the small sides are opposite

Suppose, after possibly swapping \(z,z'\) and the clique labels, that \(A\) and \(B'\) are small sides. The concentrated inequality
\[
\epsilon(z)+\sum_{x\in A}\epsilon(x)\geq6,\qquad
\epsilon(z')+\sum_{y\in B'}\epsilon(y)\geq6
\]
uses disjoint vertex sets: the support points are distinct, \(A\subseteq K_0\), and \(B'\subseteq K_1\). Thus \(T\geq12\), impossible.

## Case 2: the small sides are in the same clique

Relabel so that \(a\leq a'\leq2\), with both \(A,A'\subseteq K_0\).

### \(a=a'=2\)

The \(f_{11}\leq8\) condition gives \(b'\leq4\), hence
\[
\epsilon(z')\geq10-a'-b'\geq4.
\]
The concentrated small-side inequality gives
\[
\epsilon(z)+\sum_{x\in A}\epsilon(x)\geq6.
\]
These charges are disjoint, so \(T\geq10\).

### \(a=1,\ a'=2\), and \(A\cap A'=\varnothing\)

Write \(A=\{x\}\). The vertex \(x\) is adjacent to \(z'\) and to every vertex of \(B\), so
\[
\epsilon(x)\geq b-1.
\]
Also \(\epsilon(z)\geq9-b\). Thus \(\epsilon(z)+\epsilon(x)\geq8\). Since \(b'\leq4\),
\[
\epsilon(z')\geq8-b'\geq4.
\]
The three charged vertices are distinct, so \(T\geq12\).

### \(a=1,\ a'=2\), and \(A\subset A'\)

Write \(A=\{x\}\), \(A'=\{x,y\}\), and \(B_0=|B\cup B'|\). The vertex \(x\) is adjacent to all of \(B\cup B'\), giving
\[
\epsilon(x)\geq(B_0-2)_+.
\]
Since \(\epsilon(z)\geq(9-b)_+\) and \(B_0\geq b\),
\[
\epsilon(z)+\epsilon(x)\geq(9-b)_++(b-2)_+\geq7.
\]
The vertex \(y\) is adjacent to \(z\) and all of \(B'\), so \(\epsilon(y)\geq b'-1\). Moreover \(\epsilon(z')\geq8-b'\), as \(a'=2,b'\leq4\). Hence
\[
\epsilon(y)+\epsilon(z')\geq(b'-1)+(8-b')=7.
\]
The two pairs of charged vertices are disjoint, so \(T\geq14\).

### \(a=a'=1\), and \(A,A'\) are distinct

Write \(A=\{x\}\), \(A'=\{y\}\). As above,
\[
\epsilon(z)+\epsilon(x)\geq(9-b)_++(b-1)_+\geq8,
\]
and symmetrically \(\epsilon(z')+\epsilon(y)\geq8\). These charges are disjoint, so \(T\geq16\).

### \(a=a'=1\), and \(A=A'=\{x\}\)

The vertices \(z,z'\) are nonadjacent: they share the ten vertices of \(K_0\setminus\{x\}\), and an edge \(zz'\) would create a \(K_{12}\). Put \(B_0=|B\cup B'|\). Their common neighborhood contains \(K_0\setminus\{x\}\) and \(K_1\setminus(B\cup B')\), so
\[
c(z,z')\geq21-B_0.
\]
The common-neighborhood bound yields
\[
\epsilon(z)+\epsilon(z')\geq18-B_0.
\]
The blocker edges make \(x\) adjacent to every vertex of \(B\cup B'\), so
\[
\epsilon(x)\geq(B_0-2)_+.
\]
Therefore
\[
\epsilon(z)+\epsilon(z')+\epsilon(x)
\geq18-B_0+(B_0-2)_+\geq16.
\]

All possible same-side small-set intersections have been covered. Every case forces \(T>8\), so two support points on the same \(K_{11}\)--\(K_{11}\) pair cannot exist.
