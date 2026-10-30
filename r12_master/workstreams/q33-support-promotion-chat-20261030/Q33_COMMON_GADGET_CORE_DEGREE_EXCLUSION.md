# Q33 common gadget-core degree exclusion

Date: 2026-10-30
Status: PROVED_CONDITIONAL under the registered E408 Q33 exact-129, residual-degree, and color-count contracts.

## 1. Exact-129 gadget minimum degree

For every exact-129 color C, the source-verified KP Type-I factorization is C[R]=10 isolated K5 components plus an 11-vertex exceptional gadget G_C. The primary-source degree audit gives nine ordinary gadget vertices degree5 and two special vertices of degrees 4+a and 9-a, where a is 1,2,3,4. Thus every gadget vertex has C-degree at least5. Since the gadget is a component of the C-color graph, this is also its total C-degree in R.

## 2. Nonexact-color minimum degree

Let D be a nonexact non-target color with alpha(D[R])<=12 and q=e(D[R]) in {130,131,132}. For z in R put d=d_D(z). The 60-d vertices nonadjacent to z induce a graph with independence number at most11, else an independent 12-set together with z gives an independent13-set in D[R]. Therefore
\[
q\ge d+p_{11}(60-d).
\]
The exact values are p11(60)=135, p11(59)=130, p11(58)=125. Hence delta(D)>=2 for q=130, and delta(D)>=1 for q=131 or132.

## 3. Common gadget-core intersection

Let W_* be the common core intersection of all m exact-129 gadgets. For z in W_*, every exact color contributes at least5 to its non-target degree.

The E408 residual count vector is:
- m=8: three nonexact colors of130 edges;
- m=9: nonexact colors of130 and131 edges;
- m=10: one nonexact color of132 edges.

The T61 crosscut contract gives 60-d_F(z)<=47 for every core vertex z. Thus the total non-target degree forced at a common gadget-core point is at least:
- m=8: 8*5 +3*2 =46;
- m=9: 9*5 +2+1 =48;
- m=10: 10*5 +1 =51.

Consequently W_* is empty for m=9,10. For m=8, every z in W_* is degree-saturated at46 or47. At degree46, all exact-color degrees are exactly5 and all nonexact-color degrees exactly2. At degree47, the total excess above these minima is one. Also d_F(z) is13 or14, so since d_H(z)>=12, z has at most two target neighbours in the 13-point shell. The pairwise gadget-intersection theorem gives |W_*|<=2.

## 4. Full-component support consequence

Let A=union_C(H minus G_C)=H minus W_* be the union of all core vertices in isolated K5 components across exact colors. This differs from the smaller union of the selected seven witness four-sets.

For m=9,10, W_*=empty and A=H, so |A|=47. For m=8, |A|>=45.

## 5. Scope

This uses the source-audited KP gadget degree sequence, alpha(D[R])<=12 for non-target colors, the E408 excess-three color-count vector, and the T61 bound 60-d_F(z)<=47. It does not use degree-nine exceptional-vertex injectivity or the fixed-four-core assumption. It does not close the labelled incidence problem. Q33 remains OPEN / NOT_CERTIFIED.
