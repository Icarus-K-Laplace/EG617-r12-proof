# Dependency audit — E408 global incidence sprint

Updated: 2026-10-27

## 1. Source branch heads checked

| Source | HEAD | Role |
|---|---|---|
| workstream/r12-e408-q33-global-compat-20261025 | 0cb2ff3968f005c9cb255958df7c02b220678701 | Q33 seven-block ledger and 31-point/56-witness terminal |
| workstream/r12-e408-q32-excess6-20261025 | a0ba6db26c7e8b00a4217dcbcbf298895dff93ce | Q32 285-edge capacity and support-44 terminal |
| workstream/r12-unified-witness-capacity-20261025 | faa8183c150dd78b000d0957fa8a63cebd52e146 | labelled witness capacity |
| workstream/r12-witness-packing-chat-20261025 | f5d3daa07403877ede9885e1bd5c2f46b16d81da | witness packing |
| workstream/r12-zero-excess-witness-20261025 | c8c4833c7830370a703d228ee23e3b88484d6baa | zero-excess witness constraints |
| workstream/r12-ultimate-closure-20261024 | 1aa47d10edd5ece2b73a0891af7ac2ce37ecbb40 | root proof DAG and retained contracts |

Sibling workstreams remain read-only.

## 2. Local Q33 profile results retained

- \((6,2,1^5)\): PROVED_CONDITIONAL excluded by the sibling double-star theorem; finite replay 571,394 configurations, zero failures.
- \((7,1^6)\): PROVED_CONDITIONAL excluded in this branch; exact gadget verifier 27,380 high-pair checks plus 48 low-pair/D checks, zero failures.
- \((4,4,1^5)\), \((4,3,2,1^4)\): still locally OPEN in all-component-edge-present branches.

These last two are no longer proof blockers for Q33 because the full-color U-edge capacity contradiction bypasses them.

## 3. Historical inference firewall

The statement that a monochromatic \(K_{12}\) has no external edge of its own color is false. The correct theorem is \(d_C(z,K_{12})\le1\). None of the new global Q33 closure steps use the false stronger claim.

## 4. Q33 exact-color count theorem

`Q33_M10_EXACT_COLOR_CAPACITY_EXCLUSION.md` proves, under the registered Q33 minimum-support contract,
\[
m\ne10.
\]
The same proof's preliminary W-capacity gives \(h\le4\), later sharpened to \(h\le3\). The proof is Q33-only and does not import Q32.

## 5. New load-bearing Q33 closure theorem

`Q33_NONEXACT_U_RESERVE_CLOSURE.md` proves:

1. every non-target color on the 31-point support satisfies \(e_C(U)\ge p_{12}(31)=26\);
2. the \(56-h\) selected component witnesses own \(336-6h\) distinct exact-color edges of \(L=\overline{H[U]}\);
3. hence all nonexact colors combined have at most \(\delta+6h\) U-edge slots;
4. therefore \(26(11-m)\le\delta+6h\);
5. after \(m=10\) is excluded and with \(\delta\le17,h\le4\), the remaining \(m=8,9\) cases require 78 or 52 slots versus at most 41.

Status: **PROVED_CONDITIONAL** for the registered 31-point/56-witness Q33 terminal.

Arithmetic verifier: `verify_q33_nonexact_u_reserve.py`.

No sharing/double-counting issue exists: each graph edge has one color; selected component K4 edges are already exact-colored and unavailable to nonexact colors; gadget-witness edges are all left available in the generous upper bound.

## 6. Q33 promotion scope

The source Q33 canonical state identifies the remaining terminal as the 31-point/56-witness boundary, split into four-partite and non-four-partite L branches. The new theorem does not distinguish those branches and contradicts both simultaneously.

Therefore this branch may promote the **registered Q33 terminal** from OPEN to PROVED_CONDITIONAL impossible.

It must not promote the original EG617(r=12) theorem unless the upstream K145-to-T61/Q33 reduction and all sibling Q32/backend branches are also closed.

## 7. Q32 remains independent and OPEN

Source: `CORE285_CAPACITY_THEOREM.md` and `LOW_SUPPORT_TRIPLE_PAIR_CAPACITY.md` on `workstream/r12-e408-q32-excess6-20261025`.

The Q32 contract is 47 vertices, 285 edges, total degree excess six, q=32. The retained theorem proves \(|U|\ge44\). At \(|U|=44\), the three-point complement and pair-uniqueness normal form remain OPEN.

No 284-edge Q33 edge-count identity or U=31 argument may be imported.

## 8. Remaining blockers after this update

- Q33 registered terminal: **PROVED_CONDITIONAL impossible**.
- Q32 285-edge \(v=44\) terminal: **OPEN**.
- Q32 \(v=45,46,47\) if reached: **OPEN unless covered by sibling theorem**.
- Original K145-to-T61/front-end bridge and other backend branches: retain their sibling statuses; not promoted here.
- EG617(r=12): **OPEN / NOT_CERTIFIED**.