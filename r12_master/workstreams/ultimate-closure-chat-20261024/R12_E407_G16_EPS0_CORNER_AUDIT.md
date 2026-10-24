# E407 g=16, epsilon_U=0 corner: incidence audit

Date: 2026-10-25  
Status: **AUDIT CORRECTION**. The boundary equations are valid; the claimed “one unused eighth point” and subsequent full-group hitting-set inference are not established.

## 1. Valid boundary equations

In the E407 witness-transversal boundary, let U be the 29-point witness support and W=H\U, with |W|=18. Write
\[
e(L)=294+\delta,\quad e(H[U])=112-\delta,\quad
e(U,W)=124+2\delta+\epsilon_U,\quad
e(H[W])=48-\delta-\epsilon_U.
\]
The budget gives \(\delta+\epsilon_U\le16\) and \(\epsilon_U+2\delta\ge2\). At the corner \(\delta=16,\epsilon_U=0\), these identities give
\[
e(L)=310,\quad e(H[U])=96,\quad e(U,W)=156,\quad e(H[W])=32.
\]
Since \(\alpha(H[W])\le4\) and \(p_4(18)=32\), equality forces
\[
H[W]\cong K_5\cup K_5\cup K_4\cup K_4.
\]
Also e(L)=310 exceeds the non-four-partite K4-free bound 309, so L is four-partite. The 49 edge-disjoint K4 witnesses force its part sizes to be (7,7,7,8).

## 2. What the 49 witnesses force — and what they do not

The three seven-point parts have 49 possible pairs for each pair of parts. Since there are 49 witnesses and no pair can be reused, every pair between any two of these three parts occurs exactly once. For each pair involving the eight-point part, only 49 of 56 possible pairs occur. There are therefore 21 unused pair-slots across the three seven-by-eight part pairs.

The five edges missing from L (equivalently, the five cross-part edges of H[U]) must lie among those 21 unused pair-slots; they cannot be between two seven-point parts, because every such pair already belongs to a witness. But the five missing edges need not share a common endpoint in the eight-point part. Nor is the eighth point forced to be unused by all witnesses.

## 3. Explicit local incidence counterexample

Let the four parts be A,B,C,D, with A,B,C each indexed by \(\mathbb F_7\) and D initially indexed by \(\mathbb F_7\). The 49 blocks
\[
Q_{a,b}=\{A_a,B_b,C_{a+b},D_{a+2b}\},\qquad a,b\in\mathbb F_7,
\]
form a transversal design: any pair of coordinates from different parts occurs at most once.

Add an eighth point z to D and replace the D-coordinate of the single block Q_{0,0} by z. All 49 blocks remain pairwise linear. The three seven-by-seven pair systems remain complete, and z is now used in one witness. For each seven-by-eight pair of parts, 49 distinct pairs are used and seven are unused.

Delete any five of the 21 unused pairs between D and A∪B∪C from L. The remaining graph is four-partite with 310 edges, all 49 witness blocks remain K4s, and the five deleted edges can be distributed among multiple D vertices. This is a local counterexample to the inference that z must be unused and that all five missing edges must be incident to z. It is not claimed to extend to a full 47-core satisfying all degree and shell constraints.

## 4. The size-8 hitting-set claim also fails at this incidence level

In the modified design, the set
\[
T=(D\setminus\{z\})\cup\{A_0\}
\]
has size eight and hits every one of the 49 blocks: 48 blocks use a D point in D\\{z}, and the modified block contains A_0. Yet T contains no entire part (seven of eight D points and only one A point).

Therefore the inference “every size-8 or size-9 hitting set contains a whole seven-point group” is not a consequence of pairwise linearity alone. The downstream claim that zero-excess W-neighborhoods can be assigned a unique whole-part label is not certified by the present incidence contract.

## 5. What remains usable

The following survive:
- the edge identities in Section 1;
- the conclusion that L is four-partite with parts (7,7,7,8) at this corner;
- the 49 blocks cover every pair between the three seven-point parts exactly once;
- all five H-cross edges lie among the 21 unused pairs involving the eight-point part;
- H[W]=K5∪K5∪K4∪K4.

The following are **not** used as proved:
- an eighth point unused by all Q blocks;
- all five H-cross edges incident to that point;
- a whole-part label for every size-8/9 hitting set;
- any contradiction derived solely from those unsupported consequences.

The g=16, epsilon_U=0 corner remains OPEN. It must be attacked with additional global core-degree, shell-support, and color-label constraints.
