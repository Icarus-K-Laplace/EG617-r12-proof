# Audit of the witness-union capacity refinement

Date: 2026-10-25  
Source: sibling artifact R12_WITNESS_UNION_CAPACITY_REFINEMENT.md, emergency-sprint branch.  
Verdict: **core-capacity theorem and table valid; beta-dependent component-count applications require correction.**

## 1. Valid core-capacity theorem

For a 47-vertex core H with e(H)=284, minimum degree at least 12, and alpha(H)<=4, let U be the union of N independent four-sets Q_i with pairwise intersections at most one. Put v=|U| and E_U=sum_{x in U}(d_H(x)-12). Then
\[
6N\le e(\overline{H[U]})
\le {v\choose2}-p_4(47-v)-12v+284-E_U.
\]
The proof is sound: each Q_i is a K4 in the complement and the K4 edge sets are disjoint; summing degrees over U and using e(H[W])>=p_4(47-v) gives the upper bound.

The numeric capacities are correct:
\[
C_{28}=290,\ C_{29}=310,\ C_{30}=331,\ C_{31}=353,\ C_{32}=375,\ C_{33}=398.
\]
Consequences that use only the universal witness count are:
- E407: seven exact-129 colors, each giving at least seven S-avoiding Q sets, yields N>=49 and v>=29; eight or more exact-129 colors yields N>=56 and v>=31.
- E408 Q33: at least eight exact-129 colors yields N>=56 and v>=31, regardless of beta.
- E408 Q32 remains outside this contract.

## 2. Invalid beta-dependent applications

The sibling artifact claims that for E407 templates C/D/E, or E408 Q33 with beta>=1, at most two K5 components can meet S, yielding eight S-avoiding components per exact-129 color. This is not established. If M[S] contains an edge, its endpoints are *allowed* to lie in the same non-target K5, but they may instead lie in separate K5 components. The condition omega(M[S])<=2 limits the number of S vertices in any one component; it does not limit the number of distinct components meeting S to two.

Therefore the stronger counts N>=56 for E407 C/D/E from seven colors, N>=64 from eight colors, and the beta>=1 implication v>=33 in E408 Q33 must not be used unless a separate color-specific co-location lemma is proved.

The safe count is seven S-avoiding components per exact-129 color (at least six B-labelled after allowing one pivot component), independent of beta. Thus the core-capacity application alone leaves:
- E407 with exactly seven exact-129 colors: v>=29 for every template;
- E407 with at least eight exact-129 colors: v>=31 for every template;
- E408 Q33: v>=31 for every beta.

The direct disjointness bound still applies whenever an independent argument proves eight disjoint Q sets in one color: then v>=32. What is withdrawn is the claim that beta>=1 alone supplies those eight sets.

## 3. E408 Q33 four-partite subcase remains useful

The sibling's later four-partite analysis is separate from the invalid beta count. If E408 Q33 has v=31 and L is four-partite, the 56 witnesses force part sizes (8,8,8,7). The incidence argument gives
\[
\epsilon_U+2\delta\ge8,\qquad \delta+\epsilon_U\le17,
\]
where \(0\le\epsilon_U\le4\). Thus \(\delta\ge2\). This is a valid conditional reduction of the four-partite subcase, not a proof that L must be four-partite and not a terminal contradiction.

## 4. Status

The core-capacity lemma is retained. The beta-dependent witness-count strengthening is not imported. E407 union boundaries and E408 Q33 remain OPEN / NOT_CERTIFIED.
