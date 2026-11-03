# E286 Section 11: independent double-K11 intersection attack

Date: 2026-11-03  
Frozen source: `frozen/eq286/286_EDGE_EQUALITY_CLASSIFICATION.md`, Section 11, at integration commit `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`.

## Verdict

**NO GAP FOUND.** An independent intersection-parameter enumeration verifies a stronger local charge lower bound: two distinct mixed points supported on the same K11/K11 pair force total excess at least14, under the Section 11 hypotheses. The theorem only needs to exclude total excess8.

## 1. Independent degree accounting

Let X,Y be the two K11s. For the two mixed points z,z', write their missing sets as
`A subset X, B subset Y` and `A' subset X, B' subset Y`, with sizes a,b,a',b'>=1. Put
`r=|A intersect A'|, s=|B intersect B'|`.

The blocker lemma gives complete bipartite adjacency A--B and A'--B'. Internal degree in each K11 is10.

Partition X into A\A', A'\A, A intersect A', and the complement. A vertex in A\A' is adjacent to z' and all b vertices of B, hence has excess at least (b-1)_+. A vertex in A'\A has excess at least (b'-1)_+. A vertex in A intersect A' is adjacent to B union B', of size b+b'-s, hence has excess at least (b+b'-s-2)_+. Therefore the total excess on X is at least
[
L_X=(a-r)(b-1)_+ +(a'-r)(b'-1)_+ +r(b+b'-s-2)_+.
]
Symmetrically,
[
L_Y=(b-s)(a-1)_+ +(b'-s)(a'-1)_+ +s(a+a'-r-2)_+.
]
(The three terms correspond respectively to B\\B', B'\\B, and B intersect B'; the executable checker implements this partition explicitly.)

Each mixed point has degree at least 22-a-b (respectively 22-a'-b'), with one extra if z,z' are adjacent. Thus its individual excess lower bound is (10-a-b+adj)_+.

If z,z' are nonadjacent, their common neighborhood contains at least
[
c_X+c_Y=(11-a-a'+r)+(11-b-b'+s)
]
vertices. The T=8 common-neighbor inequality from Section 1 gives
[
epsilon(z)+epsilon(z')ge c_X+c_Y-3.
]
If they are adjacent, then c_X,c_Y are each at most9, since ten common vertices in either K11 would form a K12 together with z,z'.

Finally, total excess T=8 implies each individual f11 blocker charge is at most8. This reduces the full integer parameter domain to 3,387 intersection states.

## 2. Independent exhaustive result

The separately written `RECHECK_E286_DOUBLE_K11_PAIR.py` enumerates every allowed a,a',b,b',r,s and both possible z-z' relations, with adjacency rejected whenever it creates a K12.

- Intersection states: 3,387.
- States where z,z' may be adjacent: 2,748.
- States where K12 forces them nonadjacent: 639.
- Minimum forced charge if nonadjacent: 15.
- Minimum forced charge if adjacent: 14.
- Minimum over all allowed states/relations: **14**.
- Exactly five parameter states attain the lower bound:
  - (a,a',b,b',r,s)=(2,2,2,2,2,2)
  - (2,2,3,3,2,3)
  - (2,2,4,4,2,4)
  - (3,3,2,2,3,2)
  - (4,4,2,2,4,2)

These are equality states of the derived *lower-bound expression*, not claims that a full 47-vertex graph realizes them. The script output is stored in `RECHECK_E286_DOUBLE_K11_PAIR.json`.

## 3. Relation to the analytic proof

The frozen Section 11 already has an analytic case split:
- opposite small missing sides: two disjoint six-unit charges;
- same-side (2,2): a six-unit charge plus at least four on the other point;
- (1,2) disjoint or nested: separate vertex/point charges;
- (1,1) distinct: two eight-unit charges;
- (1,1) equal: the common-neighbor inequality plus the shared missing vertex.

The new enumeration does not replace that proof. It independently checks the entire intersection geometry, including overlap sizes and the possible edge z z', and shows the analytic case split is conservative: the raw local charge constraints already force at least14.

## 4. Scope

This is a focused audit of Section 11's local accounting. It does not certify the other support eliminations or the full E286 theorem. No frozen theorem source is modified.
