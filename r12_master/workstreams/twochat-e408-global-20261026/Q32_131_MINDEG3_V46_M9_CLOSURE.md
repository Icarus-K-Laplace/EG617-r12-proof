# E408 Q32 — 131-edge minimum degree three and Case-I v=46,m=9 closure

Date: 2026-10-28  
Status: **PROVED_CONDITIONAL** under the registered E408 residual contract and the named Brouwer second-Turan input.

## 1. 131-edge minimum-degree theorem

### Theorem 1.1

Let C be a non-target color graph on the 61-point E408 residual R satisfying

`e(C)=131`, `alpha(C)<=12`, `omega(C)<=5`.

Then

> **`delta(C)>=3`.**

### Proof

Assume first that a vertex v has `d_C(v)=2`. Let N be the set of vertices different from v that are nonadjacent to v in color C. Then

`|N|=60-2=58`.

If `alpha(C[N])>=12`, an independent 12-set in N together with v is a C-independent 13-set, contradicting `alpha(C)<=12`. Hence

`alpha(C[N])<=11`.

Also `omega(C[N])<=5`.

Equivalently, `bar(C[N])` is K12-free. It cannot be 11-partite: an 11-partition of `bar(C[N])` would partition N into eleven C-cliques, each of size at most five, and hence could cover at most55 vertices, not58.

The registered Brouwer non-11-partite second-Turan bound therefore gives

`e(C[N]) >= p_11(58)+floor(58/11)-1`.

Now `58=11*5+3`, so

`p_11(58)=3*C(6,2)+8*C(5,2)=45+80=125`,

and therefore

`e(C[N])>=125+5-1=129`.

The two C-neighbors u,w of v are outside N. Since `e(C)=131`, the 129 edges inside N together with vu and vw already exhaust all131 edges. Equality is forced throughout. In particular there is no C-edge

- from u to N;
- from w to N;
- between u and w.

Thus `d_C(u)=d_C(w)=1`.

It remains only to note that degree one is itself impossible in a 131-edge color. If z had `d_C(z)=1`, its non-neighborhood N' would have59 vertices, with `alpha(C[N'])<=11`, `omega(C[N'])<=5`, and non-11-partite complement for the same 55-vertex covering reason. Hence

`e(C[N']) >= p_11(59)+floor(59/11)-1`.

Since `59=11*5+4`,

`p_11(59)=4*C(6,2)+7*C(5,2)=60+70=130`,

so `e(C[N'])>=130+5-1=134`. Adding the one edge incident with z gives at least135 edges, contradicting `e(C)=131`.

Therefore no degree-two vertex exists, and a fortiori no degree-one/zero vertex exists. Hence `delta(C)>=3`. QED.

## 2. Scope of the external theorem

The Brouwer input is used only after checking:

1. `bar(C[N])` is K12-free because `alpha(C[N])<=11`;
2. it is not 11-partite because eleven C-cliques of size at most5 cover at most55 vertices;
3. the relevant orders58 and59 are in the registered range.

No Kang--Pikhurko degree-nine statement is used.

## 3. Consequence for the Q32 nonexact degree floors

When E408 has exactly `m=9` exact-129 colors, the two nonexact residual colors have edge counts130 and131.

The already-audited 130-edge theorem gives minimum degree at least3. Theorem 1.1 now gives the same floor for the 131-edge color. Thus the correct pointwise nonexact floor sum is

> **`L_9=3+3=6`,**

not the older `3+2=5` used in the first v=46 rigidity pass.

For reference, the other two exact-color counts retain

- `m=8`: three 130-edge colors, `L_8=9`;
- `m=10`: one132-edge color, `L_10=2`.

## 4. Close Case I, v=46,m=9

Use the already-proved Case-I support theorem. At `v=46`, `W={w}`. The Case-I matching argument gives

`n_w>=m-3=6`,

where n_w is the number of exact colors whose Type-I special vertex is w.

Every exact color contributes degree at least4 at w, and a color for which w is special contributes at least one extra unit because the source-correct special degree is at least5. Therefore the nine exact colors contribute at least

`4m+n_w >=36+6=42`.

The target color contributes at least13. By the corrected nonexact floor, the 130- and 131-edge colors contribute at least

`3+3=6`.

Hence the 60 incident edges at w would satisfy

`60 >= 13+42+6 =61`,

impossible.

Therefore

> **Case I / v=46 / m=9 is empty.**

This closure is shorter and stronger than the former equality normal form: there is no need to continue into the six `(5,8)` special-gadget equality configurations.

## 5. Updated Case-I frontier

After this theorem, the source-correct Case-I Q32 frontier is:

- v=44: closed;
- v=45: closed;
- v=46,m=10: closed;
- **v=46,m=9: closed by this theorem**;
- v=46,m=8: open (`n_w in {5,6}` under the previous rigidity theorem);
- v=47: open.

The Case-II v=44,m=9 and m=8 terminals are unaffected except that every pointwise m=9 degree budget may now use the stronger nonexact sum `L_9=6`.

## 6. Firewall

This theorem uses the 61-point color contract and the Q32 Case-I support/matching theorem. It does not use:

- Q33's 284-edge core;
- the false degree-nine exceptional-vertex claim;
- support-41;
- SAT/ILP nonexistence;
- any assumption that an abstract scalar profile is graph-realizable.
