# Q33 seven-block / labelled-witness global contradiction

Updated: 2026-10-27  
Status: **PROVED_CONDITIONAL** for the registered 31-point / 56-witness Q33 terminal.

## 1. Frozen contract

Q33 uses a 47-vertex core \(H\) with
\[
e(H)=284,\quad \alpha(H)\le4,\quad \delta(H)\ge12,
\quad\sum_H(d_H-12)=4.
\]
At the registered minimum-support boundary, \(|U|=31\), \(|W|=16\),
\[
L=\overline{H[U]},\qquad e(L)=336+\delta,\qquad \delta\le17,
\]
and there are 56 selected labelled independent four-set witnesses, seven from each of eight selected exact-129 colors.

## 2. Exact-color-count reduction

The theorem `Q33_M10_EXACT_COLOR_CAPACITY_EXCLUSION.md` excludes \(m=10\), where \(m\) is the number of exact-129 non-target colors. Hence
\[
\boxed{m\in\{8,9\}.}
\]
Its preliminary W-capacity argument gives \(h\le4\), where \(h\) counts selected gadget witnesses. The later OA argument strengthens this to \(h\le3\), but \(h\le4\) is enough below.

## 3. Nonexact-color reserve on U

Fix any non-target color \(D\). Since the full coloring has no independent 13-set in color \(D\),
\[
\alpha(D[U])\le12.
\]
Thus by Turan's theorem
\[
e_D(U)\ge p_{12}(31)=26.
\]

Of the 56 selected witnesses, \(56-h\) are component witnesses. Each is the four-core-vertex part of an isolated monochromatic exact-color \(K_5\), so its six edges are owned by that exact color. These component-witness edge sets are pairwise disjoint. Therefore they occupy exactly
\[
6(56-h)=336-6h
\]
edges of \(L\).

Since \(e(L)=336+\delta\), all nonexact colors combined can use at most
\[
\boxed{\delta+6h}
\]
U-edges. With \(11-m\) nonexact colors, unique edge ownership gives the necessary inequality
\[
\boxed{26(11-m)\le\delta+6h.}\tag{1}
\]
No edge is charged twice: selected component edges are unavailable to nonexact colors, while all gadget-witness edges are deliberately left available in the upper bound.

Now \(\delta\le17\) and \(h\le4\), so
\[
\delta+6h\le41.
\]
But:
\[
m=9\implies26(11-m)=52>41,
\]
\[
m=8\implies26(11-m)=78>41.
\]
Both remaining exact-color counts are impossible.

Therefore the registered Q33 minimum-support terminal has no realization.

## 4. Consequence for the local P_C=49 frontier

The local all-component-edge-present branches of \((4,4,1^5)\) and \((4,3,2,1^4)\) remain locally unclassified. They are no longer required for the global Q33 closure: equation (1) rules out the simultaneous full-color system before those local profiles matter.

Thus the project should not spend further Q33 time proving a colorwise cap \(P_C\le48\) unless needed elsewhere.

## 5. Proof dependencies and scope

Used:
- Q33 284-edge / 31-point / 56-witness terminal;
- exact-129 Type-I factor theorem;
- shell-label distinction between component and gadget witnesses;
- exact-color count theorem excluding \(m=10\);
- Turan's theorem for \(p_{12}(31)=26\);
- unique edge ownership in the 12-edge-coloring.

Not used:
- Q32 285-edge identities;
- support-41 theorem;
- historical false monochromatic-K12 isolation claim;
- a proof of either remaining local P49 all-component profile.

This is a **conditional terminal closure**, not yet the full original \(K_{145}\) theorem. The upstream reduction must certify that every E408 Q33 branch enters this registered terminal contract.

Proof: `Q33_NONEXACT_U_RESERVE_CLOSURE.md`.  
Verifier: `verify_q33_nonexact_u_reserve.py`.