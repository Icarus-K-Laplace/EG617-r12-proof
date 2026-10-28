# E408 Q32 high support — source-correct near-Turan normal form

Date: 2026-10-28
Status: **PROVED_CONDITIONAL structural reduction; not a Q32 closure.**

## 1. Scope and firewall

Work only in the live E408-Q32 contract

- `|H|=47`, `e(H)=285`, `alpha(H)<=4`, `delta(H)>=12`;
- `O={p} union A`, `|O|=14`, `R=H dot-union O`;
- for an exact-129 non-target color `C`, the source-verified Kang--Pikhurko Type-I factorization is
  `C = 10 isolated K5 dot-union G11`;
- excluding the KP special point `x`, the other 60 residual vertices partition into twelve color-C K5s;
- every one of these twelve K5s meets `O`, because a C-K5 contained in H would be a target-independent five-set;
- the only gadget edges outside the twelve K5 internal edge sets are
  `y--A0`, `x--(Ns\A0)`, `x--(Nt\{y})`,
  where `A0` is a nonempty proper subset of the special five-part `Ns`, so there are exactly nine such gadget edges.

No degree-nine exceptional vertex and no exceptional-vertex injectivity are used.

## 2. Exact-129 placement theorem on the full 47-core

Let `b_1,...,b_12` be the numbers of outside-H vertices in the twelve K5 factors. Each `b_i>=1`.

### 2.1 `x in O`

The twelve K5s contain the other thirteen O-points. Hence

`sum b_i = 13`,

so necessarily

> `b = (2,1^11)` up to order.

Thus the K5 interiors contribute

`C(3,2)+11*C(4,2)=3+66=69`

C-edges in H. All gadget edges incident with x leave H, so the only possible additional H-edges are the `y--A0` edges. Therefore

> `69 <= e_C(H) <= 73`.

This placement has exactly eleven single-outside K5s and therefore exactly eleven core K4 witnesses.

### 2.2 `x in H`

Now all fourteen O-points lie in the twelve K5s. Therefore

`sum b_i=14`,

and exactly one of the following holds:

- two-double type: `b=(2,2,1^10)`;
- triple type: `b=(3,1^11)`.

The K5 interiors contribute respectively

- two-double: `2*C(3,2)+10*C(4,2)=66`;
- triple: `C(2,2)+11*C(4,2)=67`.

There are only nine gadget edges. Moreover each special K5 meets O; hence at least one gadget edge has an O endpoint and cannot be an H-H edge. Consequently

- two-double: `69 <= e_C(H) <= 74`;
- triple: `69 <= e_C(H) <= 75`.

The witness counts are respectively ten and eleven.

### 2.3 Uniform consequence

For every exact-129 color in the full-support v=47 branch,

> **`69 <= e_C(H) <= 75`.**

Writing `g_C=e_C(H)-69`, every exact color satisfies

> **`0 <= g_C <= 6`.**

The upper bound is source-correct and uses only the Type-I factorization plus the fact that all twelve K5s meet O.

## 3. The 69-edge layer is genuinely feasible locally

A strict per-color improvement `e_C(H)>=70` is false at the level of the valid source interface.

A source-correct placement can be made as follows. Choose KP parameter `a=1`; put the exceptional point `x` in the shell `A`; put `y` in `A`; put the unique vertex of `A0` in `A`; put `p` as the unique outside point of an ordinary isolated K5; put one further ordinary isolated K5 through two shell points; and distribute the remaining shell points one per remaining K5 so that the twelve K5 outside-counts are `(2,1^11)`. Arrange `x,y,A0` in their prescribed special positions. Then no non-target K5 contains both `p` and a shell point, every gadget edge has an outside endpoint, and no forbidden non-target `p--A` edge is created. Hence

> `e_C(H)=69`.

Therefore v=47 cannot be closed by claiming that every exact color individually pays a strict `+1` over the ordinary 69-floor.

## 4. Rigidity of the 69 and 70 layers

Let D be any non-target color on H. Then `alpha(D)<=12`, so `bar D` is K13-free.

The ordinary Turan floor is

`e_D(H)>=69`,

with equality iff

> `D = 11 K4 dot-union K3`.

For the 70-edge layer, the registered Brouwer/Kang--Pikhurko second-Turan bound gives that a K13-free 47-vertex graph which is not 12-partite has at most

`t_12(47)-floor(47/12)+1 = 1010`

edges. Since `e_D(H)=70` means `e(bar D)=1081-70=1011`, `bar D` must be 12-partite.

Because `omega(D)<=4`, every part has size at most four. Twelve parts cover 47 vertices, so their sizes are forced to be

> `4^11,3`.

They already account for 69 D-edges. Hence a 70-edge D consists of this unique base layer plus exactly one D-edge crossing the twelve parts.

A K4 crossing two or more parts requires at least three cross-part D-edges (the cheapest split is 3+1). Therefore:

> in both the 69- and 70-edge layers, every D-colored K4 lies wholly in one of the eleven four-parts.

In particular an exact color with ten witnesses occupies ten distinct four-parts, and an exact color with eleven witnesses occupies all eleven four-parts.

## 5. Exact low-layer Type-I arithmetic

Combining Sections 2 and 4 gives the following source-correct normal forms.

For `e_C(H)=69`:

- `x in O`: `(2,1^11)` K5 outside profile and zero H-H gadget edges;
- `x in H`, two-double: `(2,2,1^10)` and exactly three H-H gadget edges;
- `x in H`, triple: `(3,1^11)` and exactly two H-H gadget edges.

For `e_C(H)=70`:

- `x in O`: `(2,1^11)` and exactly one H-H gadget edge;
- `x in H`, two-double: `(2,2,1^10)` and exactly four H-H gadget edges;
- `x in H`, triple: `(3,1^11)` and exactly three H-H gadget edges.

Thus the 69/70 layers are not merely scalar edge counts: they have a finite placement normal form tied to the true KP gadget.

## 6. Source parameter forces core gap when x lies in H

Assume now `x in H`. Let

`b_s=|Ns cap O|`, `b_t=|Nt cap O|`.

Both are positive because every one of the twelve K5 factors meets O.

Let `G_H` be the number of the nine non-clique gadget edges with both endpoints in H.

If `y in O`, then the y--A0 edges contribute no H-H edge, while among the x--(Ns\A0) and x--(Nt\{y}) edges at most `b_s-a` and `b_t-1` respectively can leave H. Hence

`G_H >= (5-a)-(b_s-a) + 4-(b_t-1) = 10-a-b_s-b_t`.

If `y in H`, the y--A0 family contributes at least `a-(b_s-1)` H-H edges, the x--(Ns\A0) family at least `(5-a)-(b_s-a)`, and the x--(Nt\{y}) family at least `4-b_t`; the sum is `9-b_s-b_t`, which is at least `10-a-b_s-b_t` because `a>=1`.

Thus uniformly

> **`G_H >= 10-a-b_s-b_t`.**

### 6.1 Two-double placement

The total outside multiplicity of the two special K5s satisfies `b_s+b_t<=4`. The twelve K5 interiors contribute 66 H-edges. Hence

`e_C(H)>=66+(6-a)=72-a`,

so

> **two-double: `g_C>=max(0,3-a)`.**

### 6.2 Triple placement

Again `b_s+b_t<=4`, while the clique interiors contribute67 H-edges. Therefore

`e_C(H)>=67+(6-a)=73-a`,

and

> **triple: `g_C>=4-a`.**

These are source-correct parameter-to-gap bounds. They use neither degree-nine nor exceptional-point injectivity.

In particular, low source parameter cannot coexist with a zero-gap exact color when x lies in H:

- two-double a=1 forces `g>=2`, a=2 forces `g>=1`;
- triple a=1,2,3 force `g>=3,2,1` respectively.

## 7. Consequence for the next attack

The missing v=47 contradiction, if true, must be multicolor. The single-color strict-reserve route is blocked by the explicit 69-edge source-correct placement above.

The correct next object is the simultaneous packing of the eleven color layers in the common 796-edge pool `bar H`, with exact colors constrained by the placement normal forms and parameter-to-gap bounds above and all colors constrained by edge uniqueness.
