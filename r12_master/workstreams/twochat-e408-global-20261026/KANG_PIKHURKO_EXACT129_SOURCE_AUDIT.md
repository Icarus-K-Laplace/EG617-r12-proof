# Kang–Pikhurko exact-129 source audit

Updated: 2026-10-27
Status: **SOURCE VERIFIED / PARAMETER MAP VERIFIED / DEGREE-SEQUENCE CORRECTED**
Purpose: freeze the published exact-129 equality classification and prevent overstrengthening it.

## 1. Primary source

M. Kang and O. Pikhurko, **Maximum K_{r+1}-free graphs which are not r-partite**, Matematychni Studii 24 (2005), 12–20.

Primary PDF:

`https://opikhurko.warwick.ac.uk/E/KangPikhurko05ms.pdf`

Relevant source statements:

- Theorem 1: in the applicable range, `p_r(n)=t_r(n)-floor(n/r)+1`;
- Theorem 4: all extremal graphs arise from the explicit `G(n_1,...,n_r)` construction;
- Lemma 5: characterizes the optimal part-size sequences.

The construction starts from a complete r-partite graph, chooses two special parts `N_s,N_t`, chooses `y in N_t` and a **nonempty proper** subset `A subset N_s`, adds `x`, connects `x` to `A union {y}` and the ordinary parts, and deletes the edges between `y` and `A`.

## 2. Exact-129 complement translation

Let C be one non-target color restricted to a genuine 61-point T61 residual and assume

- `e(C)=129`;
- `alpha(C)<=12`;
- `omega(C)<=5`.

Let `G=complement(C)`. Then

`e(G)=C(61,2)-129=1830-129=1701`,

and `omega(G)=alpha(C)<=12`, so G is K13-free.

G is not 12-partite: otherwise the twelve parts would become twelve cliques in C, each of size at most5, covering at most60 vertices.

Thus G belongs to the Kang--Pikhurko non-12-partite K13-free class.

## 3. Equality arithmetic

The balanced Turan graph T12(61) has part sizes `6,5^11`, so

`t_12(61)=1830-[C(6,2)+11*C(5,2)]=1830-125=1705`.

Since `12<=(61-1)/2`, Theorem 1 gives

`p_12(61)=1705-floor(61/12)+1=1701`.

Therefore G is an equality graph.

## 4. Equality part-size sequences

Applying Lemma 5 to twelve nondecreasing positive integers summing60 gives exactly

1. `(5^12)`;
2. `(4,5^10,6)`;
3. `(4,4,5^8,6,6)`.

`verify_kp_exact129_instance.py` independently enumerates the integer sequences and reproduces exactly these three.

Types II and III contain a part of size6, hence C contains K6, contradicting `omega(C)<=5`. Therefore only `(5^12)` survives.

## 5. Valid Type-I factorization

Let the two special 5-parts be `N_s,N_t`, and let x be the added vertex.

For each of the other ten 5-parts:

- the part is independent in G, hence a K5 in C;
- G is complete from it to every other old part;
- x is adjacent in G to all of it.

Hence those ten parts are **isolated K5 components in C**.

All remaining nontrivial color edges lie on

`N_s union N_t union {x}`,

an 11-vertex gadget. Thus the source-verified factorization is

`C = 10 isolated K5 dot-union G_11`.

The gadget contains the two special 5-cliques and x, and has independence number at most2.

This factorization is a valid published-theorem instance and remains usable in E407/E408 component-witness arguments.

## 6. Correct Type-I degree sequence

This is the critical correction found by primary-source audit.

Put `a=|A|`. Because A is nonempty and proper in a 5-part,

`a in {1,2,3,4}`.

Take the complement of the published construction back to C.

- The 50 vertices in the ten isolated K5s have degree4.
- Every vertex of `N_s` has degree5 in the 11-vertex gadget:
  - vertices of A have four internal N_s neighbors plus y;
  - vertices of `N_s\A` have four internal neighbors plus x.
- Each of the four vertices of `N_t\{y}` has four internal neighbors plus x, hence degree5.
- `deg_C(y)=4+a`.
- `deg_C(x)=9-a`.

Therefore the variable degree pairs are exactly

- a=1: `(5,8)`;
- a=2: `(6,7)`;
- a=3: `(7,6)`;
- a=4: `(8,5)`.

There is **no degree9 vertex**.

Degree-sum check:

- a=1 or4: `50*4 + 10*5 + 8 = 258`;
- a=2 or3: `50*4 + 9*5 + 6 + 7 = 258`.

Both equal `2*129` as required.

## 7. Retraction consequence

The factor theorem is source-verified, but the following stronger project inference is false:

> every exact-129 Type-I color has a distinguished vertex of color-degree9.

Accordingly, any theorem whose contradiction requires degree9 exceptional-vertex injectivity must be re-audited or retracted. The branch-local retraction is recorded in

`KP_DEGREE9_RETRACTION_AND_E408_Q32_REOPEN.md`.

Affected E408-Q32 closure routes include:

- `Q32_GLOBAL_EXCEPTIONAL_INJECTIVITY.md`;
- `Q32_EXACT_COLOR_COUNT_COLLAPSE.md`;
- `Q32_NONFULL_SUPPORT_SHELL_CAPACITY.md` at the injectivity step;
- `E408_WHOLE_LAYER_EXACT_COUNT_CLOSURE.md`.

## 8. Promotion consequence

The exact-129 **factorization provenance gate passes**:

> exact-129 + alpha<=12 + omega<=5 on 61 vertices implies `10 isolated K5 + G11`.

The exact-129 **degree9 gate fails**.

This distinction is now canonical. Source verification must not be used to resurrect degree9 or exceptional-vertex injectivity.

## 9. Firewall

This audit claims neither an end-to-end formal proof nor closure of E408-Q32. It only fixes the exact published equality interface and its correct degree sequence.
