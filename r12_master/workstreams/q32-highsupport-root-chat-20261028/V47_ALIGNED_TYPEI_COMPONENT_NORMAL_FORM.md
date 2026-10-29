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
