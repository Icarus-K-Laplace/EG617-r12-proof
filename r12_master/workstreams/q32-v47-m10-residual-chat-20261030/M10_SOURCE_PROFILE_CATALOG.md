# M10 source-correct Type-I aggregate occupancy catalog

Date: 2026-10-30  
Status: SOURCE-COMPLETE at aggregate factor-occupancy level; endpoint-labelled source completions remain OPEN.

## 1. Source contract

For an exact-129 non-target color C on the 61-point source, the source-verified Kang–Pikhurko equality graph gives

    C = I_1 dot-union ... dot-union I_10 dot-union G_11,

where I_1,...,I_10 are the ten isolated K5 components and G_11 contains the two special K5 factors N_s,N_t and the distinguished point x_C. The gadget has the nine non-K5 edges

    y--A_0,   x_C--(N_s minus A_0),   x_C--(N_t minus {y}),

with y in N_t and A_0 a nonempty proper subset of N_s. Write a=|A_0| in {1,2,3,4}.

The twelve K5 factors are I_1,...,I_10,N_s,N_t. Every factor meets O: otherwise its five vertices would be an independent five-set in the target graph H.

Let b_F=|F intersect O| for each factor F. Thus b_F>=1.

## 2. Exact aggregate outside-count theorem

If x_C lies in O, the twelve K5 factors contain the other thirteen O-points:

    sum_F b_F=13.

Consequently the unique aggregate profile is (2,1^11).

If x_C lies in H, the twelve factors contain all fourteen O-points:

    sum_F b_F=14.

There are exactly two aggregate profiles: (2,2,1^10) (two-double) and (3,1^11) (triple). There are no other aggregate outside-count profiles. These equations do not say that all isolated K5 factors are single-outside.

## 3. Complete labelled factor-occupancy enumeration

Keep the ten isolated factors labelled and keep N_s,N_t distinct. The aggregate occupancy choices are exactly 90:

| x_C location | Profile | Isolated-factor occupancy | Special-factor occupancy | Number |
|---|---|---|---|---:|
| O | one double | one of I_1,...,I_10 is double | N_s,N_t single | 10 |
| O | one double | all isolated factors single | N_s double or N_t double | 2 |
| H | two-double | all isolated factors single | both N_s,N_t double | 1 |
| H | two-double | one isolated double | N_s double, N_t single | 10 |
| H | two-double | one isolated double | N_s single, N_t double | 10 |
| H | two-double | two distinct isolated doubles | N_s,N_t single | 45 |
| H | triple | one isolated triple | N_s,N_t single | 10 |
| H | triple | all isolated factors single | N_s triple, N_t single | 1 |
| H | triple | all isolated factors single | N_s single, N_t triple | 1 |
| Total | | | | 90 |

The companion verifier enumerates these 90 labelled factor assignments directly and checks the totals and all derived arithmetic. M10_SOURCE_OCCUPANCY_90.csv is the row-level catalog.

### Crucial correction

The isolated-triple row is not excluded by the aggregate Type-I source theorem. The claim that an isolated triple-outside K5 always violates a universal same-color degree floor is unsupported in the general full-support Q32 contract. A degree floor of two or three is available in certain already-aligned target-part cells, but it cannot be imported into arbitrary m=10 source placements.

Therefore H-TI (one isolated triple) is an OPEN source mode and must remain in the complete catalog.

## 4. Derived G_11 H-vertex and K5-interior counts

Let b_s,b_t be the outside counts of N_s,N_t. Since G_11 has eleven vertices, including x_C,

    |G_11 intersect H| = 11 - b_s - b_t - 1_{x_C in O}.

The twelve K5 interiors contribute the following number of H-H edges:
- x_C in O, profile (2,1^11): 3+11*6=69;
- x_C in H, two-double profile: 2*3+10*6=66;
- x_C in H, triple profile: 1+11*6=67.

| Mode | b_s+b_t | G_11 H vertices | K5-interior H edges |
|---|---:|---:|---:|
| O-I: isolated double | 2 | 8 | 69 |
| O-N_s: N_s double | 3 | 7 | 69 |
| O-N_t: N_t double | 3 | 7 | 69 |
| H-SS: both specials double | 4 | 7 | 66 |
| H-I/N_s: isolated + N_s double | 3 | 8 | 66 |
| H-I/N_t: isolated + N_t double | 3 | 8 | 66 |
| H-II: two isolated doubles | 2 | 9 | 66 |
| H-TI: isolated triple | 2 | 9 | 67 |
| H-T/N_s: N_s triple | 4 | 7 | 67 |
| H-T/N_t: N_t triple | 4 | 7 | 67 |

If g_C=e_C(H)-69 and G_H is the number of non-K5 gadget edges with both endpoints in H, then exactly

    G_H = g_C                 when x_C in O,
    G_H = 3+g_C               in the two-double case,
    G_H = 2+g_C               in the triple case.

The source-correct global upper bounds are g_C<=4 for x_C in O, g_C<=5 for x_C in H two-double, and g_C<=6 for x_C in H triple.

## 5. Parameter-to-gap lower bounds

The source audit gives, for x_C in H,

    G_H >= 10 - a - b_s - b_t.

Substituting the exact K5-interior contribution gives:

| Mode | Lower bound on g_C |
|---|---|
| H-SS (b_s+b_t=4) | max(0,3-a) |
| H-I/N_s or H-I/N_t (sum=3) | max(0,4-a) |
| H-II (sum=2) | max(0,5-a) |
| H-TI (sum=2) | max(0,6-a) |
| H-T/N_s or H-T/N_t (sum=4) | max(0,4-a) |

These bounds are source-derived and retain the labelled special factors. In particular the isolated-triple mode is not a free extra mode: it pays g_C>=6-a, so for a=1,2,3,4 it needs at least 5,4,3,2 gap units respectively.

For x_C in O, the nine gadget edges incident with x_C leave H, so only y--A_0 can contribute H-H edges; hence 0<=g_C<=4.

## 6. Placement restrictions conditional on the target graph

The aggregate 90-row catalog is not a claim that all 90 modes extend to a full 61-point coloring. The following extra restrictions are valid when the indicated source/target placements occur:

- If x_C is in H and N_t is single-outside, y must lie in H. If y were outside, x_C together with the four H-vertices of N_t minus {y} would form a C-colored K5 inside H.
- If x_C is in H and N_s is single-outside, A_0 must contain at least one H-vertex; otherwise x_C together with the four H-vertices of N_s minus A_0 would form a C-colored K5 inside H.
- If N_s is single-outside and y lies in H, A_0 cannot be exactly the four H-vertices of N_s (the case a=4 with the outside vertex omitted); otherwise y together with those four H-vertices would form a C-colored K5 inside H.
- In the aligned z=0,1 target-part cell, stronger pointwise degree floors give additional restrictions, including the exclusion of an isolated triple there. Those aligned-cell restrictions are not universal source restrictions.

All remaining y/A_0 endpoint placements must be retained until checked against the actual target-part assignment, pointwise color-degree constraints, and global color-edge ownership.

## 7. Source-completeness boundary

This catalog is complete for the aggregate choice of which of the twelve labelled K5 factors receive the two outside points or the three outside points. It is not yet a complete endpoint-labelled enumeration of:
- the identities of the outside vertices inside each factor;
- the location of y in N_t;
- the subset A_0 in N_s;
- the source gadget edge endpoints after the target-part assignment;
- compatibility with the ten-block pivot graph and other colors.

No source occupancy row is promoted to a globally feasible Q32 candidate without those checks.
