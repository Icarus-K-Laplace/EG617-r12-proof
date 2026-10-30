# Q33 assumption-gap audit: variable component core sizes

Date: 2026-10-30  
Status: **AUDIT FINDING — fixed ten-four-core profile is not promoted as source-universal.**

## 1. Source facts actually certified

1. The Kang–Pikhurko exact-129 source audit certifies a factorization into ten isolated K5 components plus an 11-vertex exceptional gadget, under the stated 61-point, alpha<=12, omega<=5 hypotheses.
2. The Q33 cross-color gadget theorem explicitly warns that the full component support includes core vertices from components with more than one shell vertex, and that not every core point belongs to a four-point witness.
3. The R12 witness-packing boundary kernel supplies seven selected four-set witnesses per exact color (including the possible pivot-component H-part), with at least six B-labelled component Q-sets. It does not state that all ten K5 components have four core vertices.
4. The root dependency DAG registers the seven-witness Q33 interface, not a universal one-shell-per-component theorem.
5. The Q33 M10 exact-color-capacity note invokes a retained shell-label theorem for the stronger assertion that every K5 component has exactly one shell vertex. That stronger premise is not separately identified as a certified root dependency in the audited root DAG.

Therefore the earlier fixed profile with exactly three/four unselected component K4s per color is **conditional on the stronger one-shell-per-component premise**. It must not be used as a universal Q33 source reduction without separately promoting that premise.

## 2. Source-correct replacement

Let c_i be the number of core vertices in the i-th isolated K5 component of an exact-129 color C. Since a component with five core vertices would be an independent 5-set in H and alpha(H)<=4,
\[
0\le c_i\le4.
\]
Let g_C be the number of core vertices in the 11-vertex gadget. The ten components and gadget partition the 47-point core, so
\[
g_C=47-\sum_{i=1}^{10}c_i.
\]
Since each c_i<=4, g_C>=7; since the gadget has 11 vertices, g_C<=11. Thus
\[
7\le g_C\le11,\qquad 36\le\sum_i c_i\le40.
\]

If the selected seven witnesses for C are all component witnesses, seven component K4s contribute28 core vertices and the remaining three components have total core size
\[
8\le C_{\rm rest}\le12.
\]
If six component witnesses and one gadget witness are selected, the six component K4s contribute24 core vertices and the remaining four components have total core size
\[
12\le C_{\rm rest}\le16.
\]

The variable-core profile model below enumerates every remaining component size c_i in {0,1,2,3,4} and every U-split k_i in {0,...,c_i}. It does not assume every remaining component is a four-core K4.
