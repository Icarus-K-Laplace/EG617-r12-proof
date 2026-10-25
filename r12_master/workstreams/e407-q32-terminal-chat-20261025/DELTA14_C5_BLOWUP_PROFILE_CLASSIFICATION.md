# E407 Q32: the explicit local model is the only admissible \(C_5\)-blow-up profile

Date: 2026-10-25  
Status: **FINITE CLASSIFICATION CERTIFIED** within the \(C_5\)-blow-up subclass.

## Statement

Suppose \(J\) is a blow-up of \(C_5\) with five nonempty consecutive parts of sizes
\[
(a,b,c,d,e)\in\mathbb Z_{>0}^5,
\]
such that
\[
a+b+c+d+e=15,\qquad
ab+bc+cd+de+ea=49,
\]
and \(\Delta(J)\le7\). Then, up to rotation and reflection of the five-cycle,
\[
\boxed{(a,b,c,d,e)=(1,2,5,5,2),}
\]
equivalently \((5,5,2,1,2)\).

## Proof

A vertex in each blow-up part has degree equal to the sum of the sizes of its two neighbouring parts. Thus the maximum-degree condition is exactly
\[
b+e\le7,\quad a+c\le7,\quad b+d\le7,\quad c+e\le7,\quad d+a\le7.
\]
Enumerate the positive integer compositions of 15 into five ordered parts. For each tuple, compute the five-cycle edge count and the five part-degrees, then identify tuples under the ten rotations/reflections of \(C_5\). The exact exhaustive enumeration is reproduced by the verifier named verify_c5_blowup_profile.py: there are seven dihedral classes with edge count 49 before the degree cap, and exactly one after imposing \(\Delta(J)\le7\), namely \((1,2,5,5,2)\).

This is a finite arithmetic classification of the blow-up subclass; it does **not** prove that every triangle-free saturated graph \(J\) in the E407 terminal is a \(C_5\)-blow-up.

## Consequence for the E407 local candidate

The 49-witness matching structure gives \(\Delta(J)\le7\), and the saturated-kernel ledger gives \(|V(J)|=15,e(J)=49\). Therefore, **if** the remaining saturated kernel can be shown to be a \(C_5\)-blow-up, it must be the explicit local model already excluded from every full-core extension in DELTA14_SATURATED_CANDIDATE_EXTENSION_EXCLUSION.md.

The outstanding general gap is now sharply stated: exclude or classify non-\(C_5\)-blow-up triangle-free, non-bipartite, triangle-saturated 15-vertex graphs with 49 edges and the two witness-induced orthogonal near-perfect matching decompositions.
