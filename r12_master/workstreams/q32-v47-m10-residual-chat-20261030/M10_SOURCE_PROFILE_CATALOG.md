# M10 source-correct Type-I profile catalog

Status: PROVED at the aggregate outside-count level; endpoint-labelled source completions remain OPEN.

## 1. Source contract

For each exact-129 non-target color C, the audited Kang–Pikhurko equality graph has twelve disjoint color-K5 factors:
- ten isolated K5 components;
- two special K5 factors N_s and N_t inside the 11-vertex gadget G_11;
- one distinguished gadget point x_C.

The source gadget also has y in N_t and a nonempty proper subset A_0 of N_s. Put a=|A_0|, so a is one of 1,2,3,4. Its source cross-edge families are y-A_0, x_C-(N_s\\A_0), and x_C-(N_t\\{y}).

Every one of the twelve K5 factors meets O. If b_i is the number of its vertices in O, then b_i>=1. The source equality classification gives:
- x_C in O: sum b_i=13 and the multiset is (2,1^11);
- x_C in H: sum b_i=14 and the multiset is either (2,2,1^10) or (3,1^11).

There are no other aggregate outside-count profiles.

## 2. Exhaustive occupancy families

Let k be the number of double-outside factors among the ten isolated factors. For the two-double mode, the remaining 2-k double factors lie among N_s,N_t. For the triple mode, the triple factor must be special: an isolated triple-outside K5 would leave an H-vertex with only one same-color H-neighbor, violating the source degree floor.

| Family | x_C | Aggregate profile | Isolated doubles | Special occupancy | |H intersect G_11| | Aligned four-track residual profile |
|---|---|---|---:|---|---:|---|
| O-I | O | (2,1^11) | 1 | N_s,N_t single | 8 | (2,2,2,2) |
| O-S | O | (2,1^11) | 0 | one of N_s,N_t double | 7 | (2,2,2,1) |
| H-SS | H, two-double | (2,2,1^10) | 0 | both N_s,N_t double | 7 | (2,2,2,1) |
| H-IS | H, two-double | (2,2,1^10) | 1 | one special double, one special single | 8 | (2,2,2,2) |
| H-II | H, two-double | (2,2,1^10) | 2 | N_s,N_t single | 9 | (2,2,2,3) |
| H-T | H, triple | (3,1^11) | 0 | one special triple, the other special single | 7 | (2,2,2,1) |

The last column is only asserted when the aligned target partition T_0,T_1,T_2,T_3 exists: a single-outside K5 contributes a transversal H-K4; a double-outside K5 contributes a transversal H-K3 and cannot use T_0; a triple-outside factor is special. The nine-vertex H-II profile follows by counting eight transversal K4s, two transversal K3s, and the remaining G_11 vertices in the aligned four-track cell. It is not a general partition claim outside that cell.

N_s and N_t are labelled separately. The source gadget is asymmetric, so swapping their occupancy is not silently identified. The table lists occupancy families, not a claim that every endpoint-labelled realization in each family is feasible.

## 3. Special-factor outside totals

The aggregate outside count in the two special factors is:

| Family | b_s+b_t |
|---|---:|
| O-I | 2 |
| O-S | 3 |
| H-SS | 4 |
| H-IS | 3 |
| H-II | 2 |
| H-T | 4 |

This table is useful because the source lower bounds on gadget H-edges depend on a, b_s+b_t, and the location of y. For x_C in H, the source audit gives the two-double and triple gap bounds g_C<=5 and g_C<=6, respectively; for x_C in O, g_C<=4. These are upper bounds, not a closure.

## 4. What is already audited and what is not

- O-I: the aligned isolated-double audit proves the eight-vertex residual accounting, its two-K4 base, and the T_0-centered exclusion. Its large-track-centered exceptional subcase remains OPEN.
- H-IS: the aligned audit covers the one-isolated/one-special double placement. Its exceptional y-in-H large-track-centered branch remains OPEN.
- H-SS: the aligned two-special-double source-pattern audit gives its four-row (y,a) table. This is conditional on the aligned four-track contract.
- H-II: the two-isolated-double, nine-vertex G_11 residual mode is present in the source-count space but has no dedicated endpoint-labelled residual audit. OPEN.
- O-S: the two possible special positions N_s and N_t must be kept distinct until the gadget edge families and target-part restrictions are checked.
- H-T: the triple must be special; the aligned normal form places it in N_s. The generic source placement and the N_s/N_t-labelled endpoint cases must not be conflated.

The complete vertex-labelled source model in Q32_FULLSUPPORT_VERTEX_LABELLED_CSP.md explicitly allows surplus outside vertices to lie in isolated factors. It is a formulation, not a solved m=10 UNSAT certificate.

## 5. Source completeness boundary

The six rows above exhaust the aggregate K5 outside-count distributions:
- x_C in O: one double factor, which is isolated or special;
- x_C in H, two-double: zero, one, or two isolated double factors;
- x_C in H, triple: the triple factor is special.

This is source-complete as an occupancy catalog. It is not yet a complete classification of all labelled choices of x_C,y,A_0,N_s,N_t, target-track placements, gadget edges, and cross-color edge ownership. Those are retained as explicit open dimensions rather than suppressed by an all-isolated-single assumption.
