# Q33 support-promotion progress log

## 2026-10-30 — all-color U/W reserve coupling

Read the live root branch at HEAD \`b0459807acd4b7e386148056ddf77d7998918893\`, Q33 global-compat at \`0cb2ff3968f005c9cb255958df7c02b220678701\`, and the root dependency/receipt and named Q33 reserve/support sources. Created this isolated branch from the live global root HEAD.

New derivation:
1. Select seven witnesses from every exact-129 color, so there are 7m blocks and 42m pair-edges.
2. Use support floors v>=31,32,34 for m=8,9,10.
3. Derive the U-side reserve with gadget-overlap coefficient rho_m=min(6,4(11-m)), including sharper rho_10=4.
4. Add nonexact-color p12(w) floors to the W-side f0/f1 reserve.
5. Exhaust all h and every allowed support size.

Result:
- m=8: v=31,32 excluded; v=33 first survives at h=5.
- m=9: v=32,33 excluded; v=34 first survives at h=4,5,6.
- m=10: v=34 excluded; v=35 first survives at h=2,...,8.

Verification:
- Cartesian-product enumeration for f0/f1 and all h/v/m cells: PASS.
- Independent dynamic-programming implementation: PASS on all47 cells.
- Exact integer arithmetic only; no external solver.

Scope:
- Conditional necessary-capacity theorem, not a graph-level contradiction.
- No larger-support cell is claimed closed.
- Global root status remains unchanged.
