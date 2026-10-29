# Q33 high-support U-reserve audit

Updated: 2026-10-29  
Status: **Local inequalities PROVED_CONDITIONAL; global support promotion OPEN.**  
Scope: the 284-edge / excess-four E408 Q33 core only. This does not touch the 285-edge Q32 terminal.

## 1. The exact 31-point theorem remains valid only on its contract

For |U|=31, W=H\U, and 56 labelled independent four-set witnesses (seven from each of eight selected exact-129 colors), write

\[
L_U=\overline{H[U]},\qquad e(L_U)=336+\delta,\qquad \delta\le17.
\]

If h selected witnesses are gadget witnesses rather than isolated-component witnesses, the remaining 56-h component witnesses own exactly 336-6h distinct edges of L_U. Every nonexact color needs p12(31)=26 edges on U. Thus

\[
26(11-m)\le\delta+6h\le17+24=41.
\]

This excludes m=8,9; the separate m=10 component-capacity exclusion is also proved under the same 31-point contract.

The local arithmetic is sound. The missing issue is coverage: the parent reduction must prove that the support used by these 56 witnesses is exactly 31, or close every larger-support case.

## 2. General support v=|U| — necessary scalar inequality

Let 31<=v<=47, w=47-v, and let U be the union of 56 selected witnesses from a fixed set of eight exact-129 colors. Let h in {0,...,8} count selected gadget witnesses. Under the retained shell-label theorem, each selected color has at most one selected gadget witness.

Set epsilon_W=sum_{x in W}(d_H(x)-12)<=4 and e_W=e(H[W]). Since e(H)=284,

\[
e(L_U)=\binom v2-284+12w+\epsilon_W-e_W
\le \binom v2-280+12w-p_4(w)=:L_{\max}(v)
\]

for w>0; for w=0, epsilon_W=0 gives L_max(47)=binom(47,2)-284=797. Here p4(w) is the Turán minimum-edge count for a graph on w vertices with independence number at most four, and the complement of H[W] is K5-free.

A second capacity bound restricts h. If a selected color has no selected gadget witness, its seven selected component four-sets cover 28 vertices of U; its other three isolated K5 components can therefore use at most v-28 core vertices in U. Define

\[
f_0(v)=\min_{\substack{k_i\in\{0,1,2,3,4\}\\\sum_{i=1}^3 k_i\le v-28}}\sum_{i=1}^3\binom{4-k_i}{2}.
\]

If a selected color has one gadget witness, its six selected component witnesses and the gadget witness still cover 28 vertices of U, leaving at most v-28 U-incidences across its four unselected isolated components. Define

\[
f_1(v)=\min_{\substack{k_i\in\{0,1,2,3,4\}\\\sum_{i=1}^4 k_i\le v-28}}\sum_{i=1}^4\binom{4-k_i}{2}.
\]

The W-parts of these unselected component K4s contribute distinct edges to the complement of H[W]. Hence

\[
(8-h)f_0(v)+hf_1(v)\le t_4(w),
\]

where t4(w)=binom(w,2)-p4(w). This gives the upper bound h<=h_max(v) in the table.

Finally, each of the 11-m nonexact colors needs at least p12(v) U-edges. These edges are disjoint from the 336-6h edges already owned by selected component witnesses. Therefore every such parent must satisfy

\[
(11-m)p_{12}(v)\le e(L_U)-(336-6h)
\le L_{\max}(v)-336+6h_{\max}(v).
\tag{*}
\]

This derivation does not assume v=31.

## 3. Independently replayed exact arithmetic table

The standard-library verifier verify_q33_high_support_u_reserve.py enumerates the finite overlap profiles defining f0 and f1, computes the Turán floors, and checks (*) for every v=31,...,47.

| v | w | f0 | f1 | h_max | L_max | reserve cap L_max-336+6h_max | p12(v) | m=8 needs | m=9 needs | m=10 needs | Excluded by (*) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
|31|16|9|15|4|353|41|26|78|52|26|8, 9|
|32|15|7|12|5|375|69|28|84|56|28|8|
|33|14|5|10|6|398|98|30|90|60|30|—|
|34|13|3|8|7|422|128|32|96|64|32|—|
|35|12|2|6|8|447|159|34|102|68|34|—|
|36|11|1|4|8|472|184|36|108|72|36|—|
|37|10|0|3|8|498|210|39|117|78|39|—|
|38|9|0|2|8|525|237|42|126|84|42|—|
|39|8|0|1|8|553|265|45|135|90|45|—|
|40|7|0|0|8|581|293|48|144|96|48|—|
|41|6|0|0|8|610|322|51|153|102|51|—|
|42|5|0|0|8|640|352|54|162|108|54|—|
|43|4|0|0|8|671|383|57|171|114|57|—|
|44|3|0|0|8|702|414|60|180|120|60|—|
|45|2|0|0|8|734|446|63|189|126|63|—|
|46|1|0|0|8|767|479|66|198|132|66|—|
|47|0|0|0|8|797|509|69|207|138|69|—|

The table is a necessary scalar-capacity audit, not a graph-realization or UNSAT certificate. The m=10 theorem in Q33_M10_EXACT_COLOR_CAPACITY_EXCLUSION.md excludes m=10 only under its exact 31-point contract; it does not promote the larger-support rows to closure.

## 4. Parent-coverage conclusion

The upstream zero-excess witness theorem establishes lower support bounds, including |U|>=31 for the selected eight-color family. It does not show that the 56-witness union from a fixed eight-color subset has size exactly 31, nor does it eliminate v=32,...,47.

Therefore:
- exact v=31 Q33 terminal: **PROVED_CONDITIONAL impossible**;
- v=32,m=8: excluded by the audited scalar reserve (*);
- v=32,m=9,10: **OPEN** under this reserve;
- v>=33: **OPEN** for m=8,9,10 under this reserve alone;
- global E408 Q33 parent closure: **OPEN**.

## 5. Shortest repair

A valid promotion requires either:

1. prove a universal witness-selection lemma that every Q33 parent has eight exact-129 colors with 56 selected witnesses whose union has exactly 31 points; or
2. extend the core/witness incidence argument to rule out all remaining rows v=32,...,47, with separate use of the full-component support theorem only where its hypotheses actually match.

Until one route is proved, do not label Q33 globally closed.
