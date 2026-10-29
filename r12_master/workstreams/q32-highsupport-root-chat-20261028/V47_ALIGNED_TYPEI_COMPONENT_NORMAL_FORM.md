# E408 Q32 — corrected Type-I placement audit in the aligned low-z 3+7 cell

Date: 2026-10-29  
Status: **PROVED_CONDITIONAL restrictions only; triple placement is NOT excluded in general.**

> **Correction to the previous revision:** the twelve K5 factors in the KP placement profile comprise ten isolated K5 components plus the two special K5 cliques inside G11. It is incorrect to treat all twelve as isolated components or to fix G11's H/O counts from the placement profile alone. This version replaces those claims.

## 1. Balanced-coloring degree floor

Assume the aligned z=0,1 profile (2,2,2,1), so H is partitioned into three target-color K12 cliques X_1,X_2,X_3 and one target-color K11 clique X_0.

For every non-target color C:
- if v lies in a K12 part X_i, then C has at least one edge from v to each of the other two K12 parts, because X_j union {v} is a 13-set containing the target color internally and must contain every non-target color. Thus d_C(v,H)>=2;
- if v lies in X_0, the same argument applies to all three K12 parts, so d_C(v,H)>=3.

## 2. What this does prove about the twelve K5 factors

The exact Type-I color has twelve K5 factors: ten are isolated components, while the other two are the special cliques N_s,N_t inside G11. Each K5 factor has at least one O vertex, since a K5 entirely in H would be an independent five-set in the target graph H.

Every single-outside K5 (one O vertex, four H vertices) has its four H vertices in four distinct target clique parts, hence exactly one from each of X_0,X_1,X_2,X_3.

For a double-outside K5 (two O vertices, three H vertices), if it is one of the ten isolated components, each H vertex has C-degree exactly two in H. Therefore its three H vertices must lie one each in X_1,X_2,X_3 and none in X_0. **This conclusion is not asserted for a special K5 inside G11**, because the nine additional gadget edges may increase its H-vertex color degrees.

For a triple-outside K5 (three O vertices, two H vertices), if it is an isolated component, each H vertex has C-degree exactly one in H, contradicting the degree floor in Section 1. Therefore:

> **If the registered triple placement occurs, its unique triple-outside K5 must be one of the two special cliques N_s,N_t inside G11.**

In the triple placement the other special K5 has one O vertex. Thus, writing b_s=|N_s intersect O| and b_t=|N_t intersect O|,

`b_s+b_t=3+1=4`.

Since x_C is in H for the triple placement, G11 has four O vertices and seven H vertices. This is a necessary condition, **not** a contradiction.

## 3. Source-correct placement/gap ledger

Let `g_C=e_C(H)-69`. The registered KP placement audit gives:

| Placement | Twelve K5-factor profile | K5 interiors' H-H edges | Source-correct gap range |
|---|---|---:|---:|
| x_C in O | (2,1^11) | 69 | 0<=g_C<=4 |
| x_C in H, two-double | (2,2,1^10) | 66 | 0<=g_C<=5 |
| x_C in H, triple | (3,1^11) | 67 | 0<=g_C<=6 |

Let G_H be the number of the nine additional, non-K5 gadget edges whose two endpoints both lie in H. These are the only C-edges in H not already counted inside the twelve K5 factors.

- x_C in O: all gadget edges incident with x_C leave H, so `G_H=g_C`.
- x_C in H, two-double: `66+G_H=69+g_C`, hence `G_H=3+g_C`.
- x_C in H, triple: `67+G_H=69+g_C`, hence `G_H=2+g_C`.

The source-correct special-gadget audit further gives `G_H>=10-a-b_s-b_t` when x_C is in H, where a is the KP parameter. Consequently:
- two-double: `g_C>=max(0,3-a)`;
- triple: `g_C>=4-a`.

For triple placement, the necessary special-clique condition b_s+b_t=4 therefore combines with `G_H>=6-a`. This can be used in a later multicolor packing argument, but it does not by itself exclude the placement.

## 4. Corrected boundary

The prior revision's fixed claims `G11 has 2/3 O vertices`, `e_C(H intersect G11)=12+g_C` for x_C in O, `15+g_C` for two-double, and “triple placement is impossible” are withdrawn. They incorrectly counted the two special K5 cliques as isolated components.

The valid remaining direction is to couple the corrected `(b_s,b_t,a,G_H,g_C)` constraints with the six track-pair color-repeat ledger and the global `sum_C g_C=37` budget. Full-support Q32 and EG617(r=12) remain **OPEN / NOT_CERTIFIED**.


## 5. Sharpened triple-special geometry in the aligned cell

If the triple placement survives, its special K5 must be N_s and the other special K5 N_t is single-outside, so N_s has three O vertices and two H vertices while N_t has one O vertex and four H vertices.

Let y be the distinguished point in N_t. It must lie in H: if y were in O, then x together with the four H vertices N_t minus {y} would form a C-colored K5 wholly inside H, contradicting alpha(H)<=4. Thus N_t minus {y} contains three H vertices and one O vertex.

The four H vertices of N_t form a C-colored K4, hence an independent four-set in H. They must occupy one vertex from each of X_0,X_1,X_2,X_3. Since x is C-adjacent to every vertex of N_t minus {y}, x must lie in the same target part as y; otherwise one of those C-edges would lie inside a target clique.

The two H vertices u,v of the triple special clique N_s are C-adjacent. Neither can lie in X_0: each has only its partner in N_s and one gadget neighbor (x or y) as C-neighbors in H, giving degree at most two, below the X_0 floor of three. Neither can lie in the part containing x,y, because its unique gadget edge to x or y would then be a C-edge inside a target clique. Therefore u,v lie in the other two K12 parts, one in each.

This fixes the part geometry:
- x,y lie in one K12 part X_k;
- the two H vertices of N_s lie in the other two K12 parts;
- the four H vertices of N_t occupy one vertex in each of X_0,X_1,X_2,X_3.

Finally, the five extra gadget edges with both endpoints in H are forced in count: the two N_s H vertices each receive one H-neighbor through either y--A_0 or x--(N_s\\A_0), and x has C-edges to the three H vertices in N_t\\{y}. Thus `G_H=2+3=5`, and
[
e_C(H)=67+5=72,qquad \boxed{g_C=3}.
]
So triple placement is not eliminated, but in this aligned cell it is confined to a specific special-gadget geometry and spends exactly three units of the 37-unit color-gap budget.


## 6. All aligned exact colors have gap at most three

The previous local normal form can be pushed one step further.

### x_C in O

All extra gadget edges incident with x_C leave H. Hence `g_C` counts only the H-H edges among `y--A_0`, so `g_C=|A_0 intersect H|` if y is in H and `g_C=0` if y is in O. Every H vertex in N_s lies in a distinct target part; if y is in H, A_0 cannot contain the N_s H vertex in y's part. Thus
[
oxed{g_C\le 3.}
]

### x_C in H, two-double placement

If y is in H, every H vertex of N_s contributes exactly one H-H gadget edge, and the H vertices of N_t other than y contribute `4-b_t` edges. Therefore
[
G_H=(5-b_s)+(4-b_t)=9-(b_s+b_t),quad
g_C=G_H-3=6-(b_s+b_t).
]

The case `b_s+b_t=2` (both special K5s single-outside) is impossible:
- if y is in O, x_C plus the four H vertices of N_t would be a C-colored K5 wholly in H;
- if y is in H, x_C and y must lie in the same target part, but N_s has an H vertex in every target part, and its unique extra edge to either x_C or y would then lie inside a target clique.

Hence `b_s+b_t>=3`, and `g_C<=3`.

If y is in O, N_t must be double-outside, since otherwise x_C plus the four H vertices of N_t would again form a C-colored K5 in H. Thus b_t=2. The nine-edge gadget count gives
`G_H=|N_s\\setminus A_0 intersect H|+3`.
At most three H vertices of N_s can lie outside x_C's target part, so `G_H<=6` and `g_C=G_H-3<=3).

### x_C in H, triple placement

Section 5 gives `g_C=3`.

Consequently, **every exact color in the aligned z=0,1 cell satisfies `0<=g_C<=3`**.

## 7. Forced gap in the unique nonexact color

The registered total gap identity is `sum_{C non-target} g_C=37`. There are ten exact colors, each with gap at most three, so the unique nonexact color D must satisfy
[
oxed{7\le g_D\le21},qquad
oxed{76\le e_D(H)=69+g_D\le90}.
]

For the upper bound, every O vertex lies outside each K12 clique. Applying the balanced-coloring condition to each 13-set X_i union {v} shows that D has at least one D-edge from v to each of X_1,X_2,X_3. Thus `e_D(H,O)>=14*3=42`. Since `e(D)=132`,
`69+g_D+42<=132`, so `g_D<=21`. Also `mu_D<=21-g_D<=14`, where `mu_D=e_D(O)`.

It follows that the ten exact colors contribute between 16 and 30 units of the 37-unit gap, so at least six exact colors have positive gap. This is a global budget reduction, not a contradiction; the remaining nonexact-color interval and aligned cells stay OPEN.
