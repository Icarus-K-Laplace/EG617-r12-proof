# Q33 support-promotion — canonical state

Updated: 2026-10-30
Branch: workstream/r12-q33-support-promotion-20261030

## Headline

E408 Q33: OPEN / NOT_CERTIFIED. This workstream has strengthened necessary structure and finite profile screens; it has not produced a labelled graph-level contradiction or root promotion.

## Current certified child results

1. Exact-129 factor: every exact-129 color has ten isolated K5 components and an 11-vertex KP Type-I gadget, under the source-audited equality classification.
2. Seven component witnesses: every exact-129 color supplies seven pairwise-disjoint component K4 witnesses in H; across colors the witnesses are pairwise linear. Selecting these seven in every exact color fixes h=0.
3. KP gadget core profile: the gadget is two special K5 parts plus one exceptional vertex. Since each K5 has at most four core vertices and the exceptional vertex contributes at most one, 7<=g_C<=9. For the three unselected components this gives 10<=sum(c_i)<=12.
4. KP gadget minimum degree: every vertex of the 11-point gadget has C-degree at least5.
5. Nonexact minimum degree: for nonexact colors with 130,131,132 edges on R and alpha<=12, the minimum degree is respectively at least2,1,1.
6. Common gadget-core degree theorem: W_* = intersection_C(G_C intersection H) is empty for m=9,10. For m=8, |W_*|<=2 and every point in it has total non-target degree46 or47.
7. KP-refined U/W screen:
   - m=8 excludes v=31..38;
   - m=9 excludes v=32..39;
   - m=10 excludes v=34..40.
   First aggregate survivors are (8,39),(9,40),(10,41).
8. First-survivor W equality: at (8,39), H[W]=4K2 and each exact-color W-edge set is a 3-edge matching; at (9,40), H[W]=3K2 union K1 and each is a 2-edge matching; at (10,41), W slack is at most3.

## Promotion consequence

Let A=union_C(H minus G_C)=H minus W_* be the union of all core vertices in isolated components across exact colors. This is distinct from the union of the selected seven-witness four-sets.

- For m=9,10, W_* is empty, so A=H and |A|=47.
- For m=8, |A|>=45, with at most two degree-saturated common-gadget points omitted.

## Next structural target

Use the all-core component incidence system for m=9,10, and the saturated one/two-point exception for m=8, together with the two special KP K5s, exceptional-vertex location, full KP degree sequence, four units of core degree excess, seven-block near-Latin duplicate ledger, shell labels, and pairwise gadget intersections.

Do not replace this by scalar capacity alone. No solver UNSAT or graph-level closure is claimed.

## Status ledger

- KP exact-129 factor and degree sequence: SOURCE_VERIFIED.
- KP-refined component-core interval: PROVED_CONDITIONAL.
- U/W finite profile screen: COMPUTATION_CERTIFIED.
- Common gadget-core degree exclusion: PROVED_CONDITIONAL.
- Remaining labelled incidence completion: OPEN.
- Q33 / E408 / EG617(r=12): OPEN / NOT_CERTIFIED.
