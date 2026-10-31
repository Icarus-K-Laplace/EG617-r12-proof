# Final integrated theorem: no balanced12-coloring of K145

Date: 2026-10-31. Mathematical status: PROVED by the analytic proofs and finite certificates identified here. This is an independently audited integration proposal; the existing global root has not been modified. The finite checks are executable ordinary Python, not a proof-assistant formalization.

**Theorem.** There is no edge-coloring of K145 with12 colors such that every13-vertex set contains an edge of every color. Equivalently, every12-coloring of K145 has a13-set missing a color. This is the original K145 obstruction requested for EG617(r=12).

## Proof

Assume such a coloring exists, and choose a least-edge color graph G. Then e(G)<=870, alpha(G)<=12, omega(G)<=12, and every induced target graph obeys D(n)=binom(n,2)-11p12(n). By Brooks, a minimum-degree vertex has degree d<=11. The full derivation, with the exact hypotheses of each external theorem, is K145_TO_T61_FRONTEND_AUDIT.md Sections1--3.

There is no induced contextual R(4,49) in G. Indeed the cap/lower-order chain forces minimum degree13 and hence at least319 target edges. Each other color has independence<=12 and clique number<=4, so its complement is K13-free but not12-partite. The second Turan theorem forces at least79 edges of each other color, leaving at most307 target edges. This contradiction applies to the induced objects of this original coloring.

Remove the closed neighborhood of the chosen vertex and a maximal packing of j disjoint target K12s. The13-point cap limits every exterior vertex to one neighbor in each K12. The independent-transversal argument gives j<=11 and a residual R in the contextual class R(11-j,144-d-12j). Exact edge partition gives

    e(R)<=870-binom(d+1,2)-66j,

with all omitted charges explicitly nonnegative, including the defect of the initial neighborhood. Thus all144 pairs0<=d,j<=11 exhaust the possibilities.

The fully proved recurrence in K145_TO_T61_FRONTEND_AUDIT.md Section4 bounds every such residual class. Its seeds are consequences of the independent lower-order,47-point and48-point theorems below; the contextual49 input was proved above without those terminal conclusions. Three implementations agree on all1,752 nodes. The retained144-stop table has a unique survivor d=11,j=6, giving a61-point induced graph F with alpha<=5, omega<=11, all caps and397<=E=e(F)<=408.

A minimum degree below12 would leave a contextual49 object in a vertex's nonneighborhood. A minimum degree at least14 forces E>=427. Hence delta(F) is12 or13.

If delta(F)=12, every degree12 pivot has an actual48-core C in R(4,48). The dedicated proof H12_AND_EXCEPTIONAL_PARENT_AUDIT.md establishes delta(C)>=12 and e(C)>=310 without transporting a47-point bound. Its12-shell has charge q>=20. Thus E=78+q+e(C)>=408. Equality would require q20. The complete q20 classification is a missing K_(2,r),6<=r<=10, plus isolates, with hub weights10 and regular lows. Repivot at a leaf: the two inserted hubs each have new-core degree at most11, contrary to the independently proved minimum degree12 of every48-core. Therefore all E<=408,h12 are impossible.

If delta(F)=13, for every regular pivot p let C_p=F-N[p]. It has47 points, alpha<=4, omega<=11 and all caps. The self-contained minimum-degree gate plus the abstract low-edge and286 obstructions give e(C_p)>=287. For q_p=e(complement F[N(p)])+sum_(a in N(p))(d_F(a)-13),

    E=91+q_p+e(C_p).

The regular set is nonempty; let Q be its maximum charge. The energy-independent part of the audited COVER proof, Sections1--7, gives Q>=29. Therefore E>=91+29+287=407 and all lower h13 energies are excluded. At E407 the full COVER theorem gives Q>=30 while the core bound gives Q<=29. At E408 it gives Q>=31 while the core bound gives Q<=30. Both contradict.

All alternatives for F have failed, while the exhaustive frontend forces F to exist. The assumed original coloring cannot exist. QED.

## How to inspect and reproduce this proof

Read the frontend audit, the h12 proof, the low/286 audit and the full frozen COVER theorem. The exact prior proofs are vendored with commit and Git blob identity in SOURCE_MANIFEST.json; this package can be read without unpublished sibling hypotheses. GLOBAL_THEOREM_LEDGER.md states every theorem domain. PROOF_DAG.json is a25-node acyclic dependency graph checked by the verifier.

Run `python -B INDEPENDENT_VERIFIER.py` from any working directory. It authenticates frozen bytes, recomputes the full contextual recurrence independently, rechecks retained COVER identities and lower-order family certificates, and emits VERIFICATION_RESULT.json and FRONTEND_REPLAY.json. It does not rerun the prohibited284/285/286 graph searches or COVER shell enumeration. The latter's completeness is supported by the inspected finite loop bounds, the frozen prior output and the proved graph-to-state reduction.

The mathematical conclusion concerns the stated K145 theorem. Abstract uncolored R(4,49) high-energy questions are not declared solved by the contextual contradiction. Publication or promotion into another branch is a separate operation recorded in ROOT_PROMOTION_RECEIPT.md.
