# h=5 pattern D resolution: {01,02,03,12,13}

**Status:** PROVED_CONDITIONAL (analytic, conditional only on the E286 support reduction, the stated scalar blocker inequalities, the shared-center and shared-leaf inequalities, and the T=8 common-neighbor bound).  
**Date:** 2026-11-01.

## Contract

The clique sizes are
\[
|K_0|=|K_1|=10,\qquad |K_2|=|K_3|=11.
\]
The support points are \(p_{01},p_{02},p_{03},p_{12},p_{13}\). The four mixed points \(p_{02},p_{03},p_{12},p_{13}\) each join a \(K_{10}\) center to a \(K_{11}\) leaf. The point \(p_{01}\) joins the two \(K_{10}\) centers.

## Per-center charge

Fix \(K_i\), \(i\in\{0,1\}\), and let \(x,y\) be its two incident mixed points. Each mixed point has a nonempty missing set in its \(K_{11}\) leaf, since it cannot complete a \(K_{11}\).

- **Both complete \(K_i\).** They are nonadjacent, since otherwise \(K_i\cup\{x,y\}\) is a \(K_{12}\). Their common neighborhood contains \(K_i\), so \(\epsilon(x)+\epsilon(y)\geq10-3=7\) by the common-neighborhood bound.
- **Exactly one completes \(K_i\).** Let \(y\) be the noncompleting point and let \(A=K_i\setminus N(y)\), \(B=L_y\setminus N(y)\), with \(a=|A|,b=|B|\). The other point \(x\) completes \(K_i\). The point \(y\) has degree at least \(21-a-b\); each vertex of \(A\) has its nine internal neighbors, \(x\), and all \(b\) vertices of \(B\); each vertex of \(B\) has its ten internal neighbors and all \(a\) vertices of \(A\). Hence the charge on \(y,A,B\) is at least
  \[
  f_{\rm diamond}(a,b)=
  \max(0,9-a-b)+a\max(0,b-2)+b\max(0,a-2)\geq5.
  \]
- **Neither completes \(K_i\).** Put \(A_x=K_i\setminus N(x)\), \(B_x=L_x\setminus N(x)\), and similarly \(A_y,B_y\), with sizes \(a_x,b_x,a_y,b_y\). Both \(B_x,B_y\) are nonempty and lie in distinct \(K_{11}\) leaves. The blocker property gives all edges \(A_x\times B_x\) and \(A_y\times B_y\). For \(v\in K_i\):
  - if \(v\in A_x\setminus A_y\), it is adjacent to \(y\) and all of \(B_x\), so \(\epsilon(v)\geq\max(0,b_x-2)\geq\max(0,b_x-3)\);
  - if \(v\in A_y\setminus A_x\), the symmetric bound holds;
  - if \(v\in A_x\cap A_y\), it is adjacent to the disjoint sets \(B_x,B_y\), so
    \[
    \epsilon(v)\geq\max(0,b_x+b_y-3)
    \geq\max(0,b_x-3)+\max(0,b_y-3).
    \]
  Summing pointwise over \(K_i\),
  \[
  \sum_{v\in K_i}\epsilon(v)\geq
  a_x\max(0,b_x-3)+a_y\max(0,b_y-3).
  \]
  The support-point and leaf-missing-set charges are disjoint from \(K_i\), and satisfy
  \[
  \epsilon(x)\geq\max(0,9-a_x-b_x),\quad
  \sum_{w\in B_x}\epsilon(w)\geq b_x\max(0,a_x-2),
  \]
  with the analogous bounds for \(y\). Thus the total charge on \(K_i,x,y,B_x,B_y\) is at least
  \[
  f_{10,11}(a_x,b_x)+f_{10,11}(a_y,b_y)\geq4+4=8.
  \]

In all three cases, the two mixed points incident to a fixed \(K_{10}\) force at least five excess units.

## Add the two centers

Apply the preceding argument to \(K_0\) and \(K_1\). Their mixed support points are disjoint. The only possible overlaps between the two center charges occur in the shared \(K_{11}\) leaves \(K_2,K_3\). In either such leaf, the opposite missing sets lie in the distinct cliques \(K_0,K_1\), so the shared-leaf inequality proves pointwise additivity: a vertex missing only one support point receives the other support-point adjacency, while a vertex missing both receives the two disjoint forced-neighbor sets. Thus the two center charges add without double-counting any excess. Therefore
\[
T\geq5+5=10>8,
\]
contradicting \(T=8\). Pattern \(D\) is impossible.

## Audit boundary

This note closes only pattern \(D\). It does not certify patterns \(P,B,C\), the other support orbits, the lower-order gate, or the full \(K_{145}\) proof.
