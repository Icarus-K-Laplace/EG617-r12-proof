# h=4 orbit resolution: {01,01,023,23}

**Status:** PROVED (analytic, conditional only on the already stated E286 support reduction and T=8 common-neighbor bound).  
**Date:** 2026-10-31.

## Contract

The support multiset is
\[
\{01,01,023,23\}.
\]
For seed \(s_i\), let \(d_i\) be its number of incidences with support points and let \(K_i\) be its private clique. The reduction gives
\[
|K_i|=13-d_i.
\]
Counting incidences in the displayed multiset,
\[
(d_0,d_1,d_2,d_3)=(3,2,2,2),
\qquad
(|K_0|,|K_1|,|K_2|,|K_3|)=(10,11,11,11).
\]
The two points with support \(01\) are denoted \(x,y\); the point with support \(23\) is \(w\).

## Lemma

At least one of the following disjoint excess charges occurs:

1. One of \(x,y\) misses both \(K_0,K_1\), contributing at least four excess units on that point and its two missing sets; or
2. Both \(x,y\) are complete to \(K_0\), contributing at least seven excess units on \(\{x,y\}\).

**Proof.** A support-\(01\) point is adjacent to the seed \(s_1\in K_1\). It cannot be adjacent to every vertex of \(K_1\), because \(K_1\) is a \(K_{11}\) and adding the support point would create a \(K_{12}\). Thus its missing set in \(K_1\) is nonempty. If it does not also miss a vertex of \(K_0\), it is complete to \(K_0\). This proves the dichotomy for each of \(x,y\).

If one point misses both cliques, the \(K_{10}\)-\(K_{11}\) mixed blocker inequality \(f_{10,11}\ge4\) charges at least four units on that support point and its missing vertices. These vertices lie in \(K_0\cup K_1\cup\{x,y\}\), disjoint from the \(23\) blocker, which is supported on \(K_2,K_3,w\).

Otherwise both \(x,y\) are complete to \(K_0\). They cannot be adjacent, since \(K_0\cup\{x,y\}\) would be a \(K_{12}\). Hence they are a nonedge with at least ten common neighbors, namely all of \(K_0\). The total-excess-eight common-neighbor bound
\[
c(x,y)\le3+\epsilon(x)+\epsilon(y)
\]
therefore gives
\[
\epsilon(x)+\epsilon(y)\ge7.
\]
Again this charge is disjoint from the \(23\) blocker. \(\square\)

## Conclusion for the orbit

The \(23\) support point \(w\) has support on \(K_{11},K_{11}\), so the \(f_{11}\) blocker inequality contributes at least six excess units on \(w\) and its missing vertices in \(K_2,K_3\). Combining with the lemma gives either
\[
T\ge6+4=10
\quad\text{or}\quad
T\ge6+7=13,
\]
contrary to \(T=8\).

In particular, the alleged opposite-completion subcase (one of \(x,y\) complete to \(K_0\), the other complete to \(K_1\)) is not a legal case: no vertex can complete the \(K_{11}\) clique \(K_1\) under \(\omega(H)\le11\).

## Audit boundary

This note closes only this h=4 support orbit. It does not by itself certify the other nine support orbits, the scalar/shared-incidence arguments elsewhere in the E286 proof, the lower-order gate, or the full K145 manuscript.
