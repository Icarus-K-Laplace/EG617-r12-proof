# h=5 pattern D resolution: {01,02,03,12,13}

**Status:** PROVED (analytic, conditional only on the stated E286 support reduction, scalar blocker inequalities, pointwise shared-incidence inequality, shared-leaf inequality, and the T=8 common-neighbor bound).  
**Date:** 2026-10-31.

## Contract

The clique sizes are
\[
|K_0|=|K_1|=10,\qquad |K_2|=|K_3|=11.
\]
The support points are \(p_{01},p_{02},p_{03},p_{12},p_{13}\). The four mixed points \(p_{02},p_{03},p_{12},p_{13}\) each join a \(K_{10}\) center to a \(K_{11}\) leaf. The point \(p_{01}\) joins the two \(K_{10}\) centers.

## Per-center charge

Fix \(K_i\), \(i\in\{0,1\}\), and let \(x,y\) be its two incident mixed points. A mixed point cannot complete its \(K_{11}\) leaf, so its missing set there is nonempty.

- If both \(x,y\) complete \(K_i\), they are nonadjacent (otherwise \(K_i\cup\{x,y\}\) is a \(K_{12}\)). They have at least ten common neighbors in \(K_i\), so the T=8 common-neighbor bound gives \(\epsilon(x)+\epsilon(y)\geq7\).
- If exactly one of \(x,y\) completes \(K_i\), the other point is noncompleting but has an additional \(K_i\)-completer. The mixed-diamond inequality \(f_{10,11}^{\rm diamond}\geq5\) charges at least five units on that point and its two missing sets.
- If neither completes \(K_i\), both have positive missing sets in \(K_i\) and in their \(K_{11}\) leaves. Each \(f_{10,11}\) blocker costs at least four. The two charges add at \(K_i\) by the pointwise shared-incidence inequality: its three incident support points are the two mixed points and \(p_{01}\), and only \(p_{01}\) can create a negative increment because the mixed points cannot complete a \(K_{11}\). The two charges also add at the relevant \(K_{11}\) leaf by the shared-leaf inequality, since their opposite missing sets lie in distinct \(K_{10}\) cliques. Thus the combined charge is at least eight.

In every case, the two mixed points incident to \(K_i\) force at least five excess units, with all charges assigned to their support vertices and missing-set vertices.

## Add the two centers

Apply the preceding argument to \(K_0\) and \(K_1\). The four mixed support points are distinct. The only cliques shared between the two center charges are \(K_2,K_3\); in each such \(K_{11}\), the two opposite missing sets lie in the distinct cliques \(K_0,K_1\), so the shared-leaf inequality makes the charges additive. Therefore
\[
T\geq5+5=10>8,
\]
contradicting \(T=8\). Pattern \(D\) is impossible.

## Audit boundary

This note closes only pattern \(D\). It does not certify patterns \(P,B,C\), the other support orbits, the lower-order gate, or the full \(K_{145}\) proof.
