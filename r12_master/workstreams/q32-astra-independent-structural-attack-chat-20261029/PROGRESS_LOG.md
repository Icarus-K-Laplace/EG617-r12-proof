# Progress log

## 2026-10-29 — source freeze

Read the three requested branch heads:
high-support433a5b39a98325f00e99650b0270d79f7753a47d,
low-support9afd7c1a59056052974f9dc78933010d10e88bba,
global-root6e61d995a257bc854c3df2fb47d9da7bc6c6e160.

Created the requested branch from the high-support head. No A/B directory was modified. Recursive source tree has513 entries and no AGENTS.md. The recent c6500b24..433a5b39 comparison contains seven commits, ten modified files and two additions; no removals or renames. Changes include corrected count vectors, weakened unconditional reserve quotas, conditional m8 variable-point restrictions, and the new nonexact-gap saturation.

Re-read the source Type-I construction in the primary Kang–Pikhurko PDF:
https://opikhurko.warwick.ac.uk/E/KangPikhurko05ms.pdf
The new reserve theorem itself needs no published extremal theorem.

## First mathematical commit

c650e9cf49b8f58bc5bb261b41ae56560b1c1348:
complete57-edge outside-reserve theorem, simultaneous627>626 packing contradiction, and parent/CSP clique-cap audit. Verified the GitHub commit diff contains only the three intended files in this directory, then fast-forwarded the dedicated branch.

The scope is conditional exclusion of the aligned cells, not whole Q32.

## Independent verification and extension

Both verification scripts passed in Python3.12.14.
Constructed two56-edge-outside countermodels with K6, and one sharp57-edge-outside legal Type-I single-color example.
Exhaustively checked32768 shell-neighborhood subsets across the two equality shapes.
Independently enumerated18 residual path/cycle types.

Proved the four-nonempty-fiber obstruction for the3+7 cell. It excludes14 of those18 types under the registered local normal form and genuine parent clique cap. Four empty-fiber types remain. Full edge lists, verification output, source hashes and file hashes accompany the second commit.

## Root status

## Concurrent source-head refresh

Before the second commit, the high-support branch advanced to541653af1a28187d9b05ddcbcb118c5460fe3f1c via b1e1044 (outside-component bijection), a3f3f8f (forced-K6 closure), and541653a (status reconciliation). The full comparison against our immutable433a5b39 base was read. It has three additions and twelve modifications, no deletions or renames. The sibling independently reaches the same m10,z0/1 component-bijection/K6 contradiction; therefore this is now overlapping evidence, not an exclusively new open-cell closure. Our uniform57-edge theorem for every color, explicit sharpness/countermodels, parent-cap audit, and broader14-of18 nonempty-fiber exclusion remain distinct contributions. The target-color K6 overconstraint is unchanged by this refresh. The low-support and global-root heads remain at the originally recorded SHAs. No moving branch is silently substituted for a frozen proof source.

OPEN / NOT_CERTIFIED. No claim of full Q32 closure, genuine multicolor counterexample, full-model UNSAT, or success criterion E.

## 2026-10-30: analytic closure of the z4 empty-fiber escape

Read the high-support541653af..1de8a375 comparison in full; the new results are z3 residual and heavy-graph catalogs, with no new closure. Low-support and global-root heads remained unchanged at the refresh. Dedicated own branch began at3394c7170851a620ac865f73953f21ecfa99393b.

Proved COLORED_PACKING_OBSTRUCTION.md Section4: every C3+C4,z4 cell in the registered m10 disconnected3+7 normal form is impossible under the genuine parent clique cap. Unequal empty/nonempty map statuses violate small-label degree demands; different empty partitions violate local blockers. For equal (0,3,2,2) partitions, avoiding a K12 forces at least two special outer blocks. Their light neighbors have only two exact forms. All blocks supplying labels2,3 must be heavy-adjacent to every special block. The two-incidence heavy budget forces exactly two of each type, leaving E0=6<9.

Independent local replay passed:3456 normalized4,5,5 triples,42336 local matching representations,44 ordered empty-class partition cases,782 raw accepted local representations,158 distinct summaries, and the complete special-block light-neighbor check. No solver or time-limit inference was used. All seven requested Markdown files remain in the original directory; the existing theorem/status files were updated, with one new verifier and its local summary data. Full replay log and SHA256 manifest accompany the commit.

New excluded contract: C3+C4 at z4, including all empty-fiber configurations, in the named3+7 cell. With the previous14-type theorem,15 of18 types are excluded. Remaining types: C3+2P2,z2; C3+P4,z3;2C3+P1,z3, each with at least one empty class. Other m10 splits and m8,m9 remain OPEN; the EG617 root remains NOT_CERTIFIED.

