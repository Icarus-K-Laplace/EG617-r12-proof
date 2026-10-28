# E408 Q32 Case-II — v=44,m=8 normal form

Date: 2026-10-28
Status: **PROVED_CONDITIONAL reduction; m=8 remains OPEN after this file.**

## 1. Frozen inputs

Work under the registered E408-Q32 contract with `|U|=44`, hence `W=H\U` has three vertices, and `m=8` exact-129 colors.

We use:

- target residual minimum degree at least 13;
- each exact color has pointwise degree at least 4;
- the three nonexact colors each have 130 edges and, by `Q32_130_MINDEG4_AND_CASEI_M8_CLOSURE.md`, minimum degree at least 4;
- for `w in W`, corrected multiplicity gives `n_w>=m-6=2`;
- each exact color has one source-correct Type-I special point `x_C`;
- for a special incidence `x_C=w`, the excess over exact baseline degree 4 is `5-a_C`, with `a_C in {1,2,3,4}`;
- the zero-shell lemma from `V44_M9_PARAMETER_SYSTEM.md`: if `x_C=w in H` and w has no C-neighbor in A, then edge `pw` has color C. Hence at a fixed w at most one special exact color can have zero shell degree;
- for every exact color with `x_C!=w`, corrected multiplicity places w in a multi-outside K5, so w has at least two distinct shell neighbors in that color.

No degree-9 exceptional point, exceptional injectivity, Case-I shell cover, Q33 identity, or E407 identity is used.

## 2. Pointwise slack is only three

At every residual vertex z,

`60 = sum over all 12 color-degrees at z`.

The floor contribution is

- target: at least 13;
- eight exact colors: at least `8*4=32`;
- three nonexact 130-edge colors: at least `3*4=12`.

Thus the total floor is 57, leaving at most three units of pointwise slack.

If z is special for exact colors `C_1,...,C_n`, their special excess alone is

`E_z=sum_i(5-a_i)`.

Each summand is at least one, so `n<=E_z<=3`.

For `w in W`, corrected multiplicity also gives `n_w>=2`; hence

> `n_w in {2,3}` for every W-point.

Since each of the eight exact colors has only one special point,

`sum_{w in W} n_w <=8`.

Therefore, up to permutation of the three W-points, the only multiplicity partitions are

> `(2,2,2)`, `(3,2,2)`, `(3,3,2)`.

The partition `(3,3,3)` is impossible because it would require nine special labels from only eight exact colors.

## 3. Source-parameter normal form

### 3.1 A W-point with n=3

Three special incidences already contribute at least three slack units. Since only three total slack units exist, equality holds throughout.

Thus all three source parameters are

> `(a_1,a_2,a_3)=(4,4,4)`.

Moreover at this point:

- target degree is exactly 13;
- every non-special exact color has degree exactly 4;
- every nonexact color has degree exactly 4.

Writing `epsilon_w=d_H(w)-12` and `r_A(w)=d_F(w,A)`, target degree 13 gives

> `epsilon_w+r_A(w)=1`.

Hence `(epsilon_w,r_A(w))` is either `(1,0)` or `(0,1)`.

### 3.2 A W-point with n=2

The two special excesses must total at most three. Up to order the only legal parameter pairs are

> `(4,4)` with special excess 2, or `(4,3)` with special excess 3.

No `(4,2)` or `(3,3)` profile is possible because either would already contribute four slack units.

## 4. Shell ownership at an n=2 W-point

Fix `w in W` with `n_w=2`. There are six non-special exact colors. Each uses at least two shell edges incident with w, and edge-color uniqueness makes these shell-neighbor sets disjoint. Thus the six non-special exact colors own at least twelve of the thirteen shell edges from w to A.

There are two special exact colors at w. By the zero-shell lemma, at most one of them can have zero shell degree, because every zero-shell special color would have to own the same edge `pw`. Therefore at least one special exact color must own a shell edge.

Consequently at least `12+1=13` shell edges are exact-colored. Since only thirteen exist, equality is forced:

1. every one of the six non-special exact colors owns exactly two shell edges at w;
2. exactly one of the two special exact colors owns exactly one shell edge at w;
3. the other special exact color has zero shell degree and therefore owns `pw`;
4. no target or nonexact color owns any edge from w to A.

Thus

> `r_A(w)=0`.

Since target degree is at least 13 and `d_F(w)=d_H(w)+r_A(w)` for w in H,

> `epsilon_w>=1`.

If the parameter pair is `(4,3)`, all three pointwise slack units are already consumed by the special exact colors. Hence target degree is exactly13 and therefore

> `(4,3) => epsilon_w=1`.

If the parameter pair is `(4,4)`, one slack unit remains outside the two special exact colors. Since `r_A(w)=0`, this gives

> `(4,4) => epsilon_w in {1,2}`.

## 5. Consequence for triple-outside colors

At an n=2 W-point w, a non-special exact color cannot place w in a triple-outside K5: that color would use three shell edges at w, while the other five non-special exact colors use at least two each, consuming all thirteen shell edges before either of the two special colors is considered. Both special colors would then have zero shell degree, contradicting the zero-shell lemma.

Therefore:

> at every n=2 W-point, every non-special exact color places w in a double-outside K5, never a triple-outside K5.

In particular, if an exact color has its special point in H and is of the m=9-style triple type (one triple-outside K5), then its special point must equal every n=2 W-point at which it would otherwise be non-special. Hence:

- under multiplicity `(2,2,2)`, no H-special triple-type exact color exists;
- under `(3,2,2)`, no H-special triple-type exact color exists;
- under `(3,3,2)`, any H-special triple-type exact color must be special at the unique n=2 W-point.

This statement does not classify colors whose special point lies outside H; those require a separate outside-special ledger and are not silently identified with the H-special double/triple dichotomy.

## 6. n=3 shell consequence

At an n=3 W-point there are five non-special exact colors, so they consume at least ten shell edges. At most one of the three special exact colors can have zero shell degree, hence at least two special exact colors own shell edges. Therefore at least twelve of the thirteen shell edges incident with w are exact-colored.

Together with `epsilon_w+r_A(w)=1`, this leaves only the two possibilities already recorded:

- `epsilon_w=1,r_A(w)=0`, or
- `epsilon_w=0,r_A(w)=1`.

## 7. Verified finite arithmetic scope

The multiplicity enumeration uses only

`n_w in {2,3}` and `sum_W n_w<=8`,

and yields exactly the three sorted partitions `(2,2,2),(3,2,2),(3,3,2)`.

No SAT/ILP nonexistence claim is made here. This file is a rigorous local normal form, not a closure of m=8.