# q36 f=2 far-target-K2 — c=8, one d2 row, A=4 repeated two-edge multiplicity-two full closure

Status: `PROVED` under `Q36_F2_FAR_K2_C8_D2_A4_MULT2_TWOEDGE_SHARP_REDUCTION.md`, the pure-d2 support contract, and `alpha(F)<=4`.

The sharp reduction leaves exactly one repeated two-edge terminal:

- D={a,b,c} has target edges ac,bc and unique target nonedge ab;
- `(w_a,w_b,w_c)=(0,0,2)`;
- `O_D=6`, `e_F(F,D)=0`;
- the external owner architecture is 2+2+1.

This terminal is in fact immediately impossible.

Because `w_a=w_b=0`, both a and b are target-anticomplete to the common missing set

`S=F union {x}`.

Let D0 be the unique pure d2 support and choose `v0 in D0`. The pure-d2 contract makes v0 target-anticomplete to the d3-support union U and to S.

Choose any far point `f in F`. Since `a_F=0`, xf is a target nonedge.

Now

`{a,b,v0,x,f}`

is an independent5-set:

- ab is the unique internal target nonedge of D;
- a,b are target-nonadjacent to x and f because their weights are zero;
- v0 is target-anticomplete to D, x and f;
- xf is a target nonedge.

This contradicts `alpha(F)<=4`.

Therefore the final repeated two-edge multiplicity-two terminal is EMPTY.

Combined with

- `Q36_F2_FAR_K2_C8_D2_A4_MULT2_ONEEDGE_FULL_CLOSURE.md`,
- `Q36_F2_FAR_K2_C8_D2_A4_MULT2_K3_LOWWEIGHT_CLOSURE.md`, and
- `Q36_F2_FAR_K2_C8_D2_A4_MULT2_K3_FULL_CLOSURE.md`,

we obtain:

> no support of multiplicity2 survives in the far-K2 c8 one-d2 A4 layer.

Since multiplicity at least3 was already eliminated, every surviving A4 d3 support is now a distinct singleton support.