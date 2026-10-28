# E408 Q32 — all-color U-edge reserve from ten disjoint witness K4s

Date: 2026-10-28  
Status: **PROVED_CONDITIONAL necessary-structure theorem; Q32 remains OPEN.**

## 1. Contract

Work only in the registered E408-Q32 285-edge contract. Thus

- `|H|=47`, `e(H)=285`, `alpha(H)<=4`, `delta(H)>=12`;
- `sum_H(d_H-12)=6`;
- `m in {8,9,10}` non-target colors are exact-129;
- each exact-129 color supplies at least ten pairwise-disjoint independent core four-set witnesses;
- witnesses are monochromatic K4s in that exact non-target color;
- `U` is the union of all such witnesses and `v=|U|>=44`.

No 284-edge/Q33 statement and no retracted degree-9 exceptional-vertex claim is used.

For any non-target color `C`, a `C`-clique of order five inside `H` would be a target-independent five-set. Hence

`omega(C[U])<=4`.

The original coloring contract also gives

`alpha(C[U])<=12`.

Write `p_12(v)` for the ordinary minimum number of edges in a `v`-vertex graph with independence number at most 12.

## 2. Ten-K4 reserve lemma

### Lemma 2.1

Let `C` be a graph with `alpha(C)<=12`, `omega(C)<=4`, containing ten vertex-disjoint K4s. Then, for `v=|C|` in `{44,45,46,47}`,

| v | ordinary `p_12(v)` | forced floor with ten disjoint K4s |
|---:|---:|---:|
| 44 | 60 | **62** |
| 45 | 63 | **64** |
| 46 | 66 | 66 |
| 47 | 69 | 69 |

#### Proof for v=46,47

The ordinary Turan-complement lower bounds already give 66 and 69, respectively.

#### Proof for v=45

If `e(C)=p_12(45)=63`, equality in Turan's theorem forces

`C = 9 K4 dot-union 3 K3`.

Such a graph contains at most nine vertex-disjoint K4s. Therefore a graph containing ten disjoint K4s has `e(C)>=64`.

#### Proof for v=44

The ordinary floor is `p_12(44)=60`.

Equality `e(C)=60` forces

`C = 8 K4 dot-union 4 K3`,

which has only eight disjoint K4s.

It remains to exclude `e(C)=61`.

Put `J=bar C`. If `J` is not 12-partite, the registered Brouwer second-Turan bound gives

`e(C) >= p_12(44)+floor(44/12)-1 = 60+3-1 = 62`,

contradiction.

Suppose instead that `J` is 12-partite. Choose a 12-partition of `J`; its parts are cliques of `C`. Since `omega(C)<=4`, every part has size at most four. Let `I` be the number of `C`-edges internal to the parts and `X=61-I` the number of `C`-edges crossing the parts.

Convexity of `binom(s,2)` gives `I>=60`. There are only two possibilities with `I<=61`:

- `I=60`: part sizes are `4^8,3^4`, so there are eight size-four parts and `X=1`;
- `I=61`: part sizes are `4^9,3^2,2`, so there are nine size-four parts and `X=0`.

Any K4 not contained in one partition part uses vertices from at least two parts. The cheapest split is `3+1`, which requires at least three crossing `C`-edges. Because the ten K4s are vertex-disjoint, crossing edges required by distinct cross-part K4s are distinct.

Thus in the `I=60,X=1` case no cross-part K4 can occur and there are at most eight disjoint K4s. In the `I=61,X=0` case there are at most nine. Both contradict the assumed ten disjoint K4s.

Hence `e(C)>=62`. QED.

## 3. Eleven-witness strengthening

If an exact color supplies at least eleven disjoint witness K4s, then those K4s alone contribute

`11*C(4,2)=66`

edges inside U. Therefore at `v=44` or `45` such a color has `e_C(U)>=66`.

Let `h` be the number of exact colors supplying at least eleven witnesses.

## 4. All-color reserve inequalities

All eleven non-target colors partition the complement edges of `H[U]`. Nonexact colors still satisfy the ordinary `p_12(v)` floor. Hence:

### v=44

`p_12(44)=60`, exact ten-witness colors use at least62, and eleven-witness exact colors use at least66. Therefore

`e(bar(H[U])) >= 60(11-m)+62(m-h)+66h`

and so

> `e(bar(H[U])) >= 660+2m+4h`.

The exact 285-edge core identity gives

`e(bar(H[U])) = 703-E_U-e(H[W])`, `|W|=3`,

where `E_U=sum_{u in U}(d_H(u)-12)`. Consequently every v=44 completion must satisfy

> **`E_U + e(H[W]) + 2m + 4h <= 43`.**

For the already-derived `m=9` double/triple normal form:

- all-double (`t=0`) has `h=0`, hence `e(bar(H[U]))>=678`;
- one triple (`t=1`) has `h>=1`, hence `e(bar(H[U]))>=682`.

These bounds are independent of the separate shell-edge floors `e(M)>=25` and `e(M)>=28`.

### v=45

`p_12(45)=63`. Thus

`e(bar(H[U])) >= 63(11-m)+64(m-h)+66h`

and therefore

> `e(bar(H[U])) >= 693+m+2h`.

The exact core identity is

`e(bar(H[U]))=735-E_U-e(H[W])`, `|W|=2`,

so every v=45 completion satisfies

> **`E_U+e(H[W])+m+2h <=42`.**

### v=46,47

The witness-K4 condition does not improve the ordinary all-color floors by itself:

- v=46: `e(bar(H[U]))>=11*66=726`;
- v=47: `e(bar H)>=11*69=759`.

Further progress at these supports must use the Type-I placement/equality structure, not only the existence of ten K4s.

## 5. What this proves and what remains

This theorem is a genuine multicolor reserve statement: exact-color witness blocks and the nonexact-color Turan floors consume the **same** finite complement-edge pool of `H[U]`.

It does **not** close v=44 or v=45 by itself. In particular, the numerical reserve still leaves feasible slack after the six-unit core excess is inserted.

The next load-bearing step must therefore use the equality/near-equality structure forced when an exact color approaches the 62/64 floors, together with the corrected Type-I gadget and the shell/outer-block labels. Treating the displayed inequalities as an UNSAT certificate would be invalid.
