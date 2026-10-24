# Robust exact core: current theorem boundary

## Status

- **PROVED_ANALYTIC:** the existing stability theorem gives (r^2-O(r)) clean transversal blocks.
- **PROVED_ANALYTIC:** HP-LI forces a linear edit charge for low-incidence off-hub repeated pairs.
- **OPEN:** deletion of (O(1)) vertices yielding two exact orthogonal partitions.
- **OPEN:** an (O(r))-repair theorem whose every repair conflicts with the coloring constraints.
- **OPEN:** direct nonextension from the near-design without exactifying it.

No affine-plane or prime-power existence assumption is made.

## 1. What the clean-block count actually gives

The frozen theorem retains at least
[
r^2-93r-54
]
size-5 exact transversals, pairwise linear, in partial parallel classes. This is (r^2-O(r)) blocks, not a complete resolvable (TD(5,r)).

The complement of this family may still contain (O(r)) bad ideal blocks and (O(r)) pair-multiplicity defects. The local high-incidence pattern in `HUB_PROPAGATION_THEOREM.md` has eight nonclean blocks in one color and obeys the current per-color scalar budgets. Thus the present theorem does not imply that the exceptional blocks meet (X), nor that deleting (O(1)) vertices repairs them.

## 2. Conditional exact-core statement

The following is valid but presently only a conditional interface:

> If one can exhibit a common (5r)-point subset (W'\subseteq W) and (r) pairwise edge-disjoint parallel classes, each consisting of (r) exact size-5 transversals of the five (r)-point groups, with every cross-group pair covered exactly once, then (W') is an exact (TD(5,r)) (equivalently, four mutually orthogonal Latin-square structure).

This condition is much stronger than the existing partial-TD result. It is not currently derived from the (O(r)) defect budget. Also, a (TD(5,r)) is not automatically an affine plane of order (r); no affine-plane theorem may be invoked without checking the exact design parameters.

The upstream exact affine/net nonextension theorem applies only after its own exact partition hypotheses are established. It does not apply to the current (5r+1)-vertex terminal merely because the terminal is close to a transversal design.

## 3. Why the obvious repair argument is invalid

An argument of the form “there are only (O(r)) defects, so delete (O(1)) vertices and obtain an exact core” is false as a counting inference: (O(r)) defects can touch (\Theta(r)) distinct vertices. The target-side hub theorem rules this out only for **target internal deletions**. It says nothing yet about non-target block-incidence defects or repeated/missing cross-pairs.

Similarly, a repair operation on one non-target partition may reassign a cross-group pair that is already owned by another color. Such a repair is not local in the multicolor edge partition unless its pair ownership is explicitly tracked.

## 4. Minimum missing theorem

A sufficient next result would be either:

1. **Hub propagation:** every high-incidence (d_i\ge6) trap away from (X) forces enough cross-color pair conflicts that only (O(1)) colors can contain one; or
2. **Global completion inequality:** if (q) colors contain the explicit (d_i=6) local trap, then their cross-pair demand plus the target cross-cover demand exceeds the cross-pair universe or the available non-target slack.

The current aggregate inequalities allow (q=\Theta(r)) at the scalar level. The unresolved step is to prove that such local traps cannot be made globally pair-disjoint. Until that is done, neither exact-core route nor robust nonextension is closed.
