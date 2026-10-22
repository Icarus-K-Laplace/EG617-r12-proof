# E406 q30 -> q31 final-rise normal forms for d=3 and d=10

Status: `PROVED` for the stated final-rise classes. This does **not** close E406.

Assume the explicit T61 E406 parent contract and an adjacent legal repivot from a degree-13 pivot with `q=30`, core `C` of 285 edges, to a new degree-13 pivot with `q'=31`, core `C'` of 284 edges.

Let `y` be the shell vertex used for the repivot, with

- `d=d_M(y)`;
- `S=N_M(y)`;
- `D=N_C(y)`;
- `|S|=|D|=d`;
- `X=t(S)-e_M(S)`;
- `r=e_F(S,D)`;
- `eps_C(U)=sum_{u in U}(d_C(u)-12)`.

The exact identities are

`1 = 12d + eps_C(D) - e_C(D) - C(d,2) - X + r`,

and

`eps_C(D)-eps_C'(S) = 1 + e_C(D)-e_F(S)`.

Also `X<=q=30`.

## 1. Exact d=3 classification

For `d=3`,

`X = 32 + eps_C(D)-e_C(D)+r <=30`.

Hence

`e_C(D) >= 2 + eps_C(D)+r`.

Since `e_C(D)<=3`, only two cases survive after the exchange identity is imposed:

### D3-A

- `C[D] = P3` (`e_C(D)=2`);
- `eps_C(D)=0`;
- `r=0`;
- `F[S]=K3`;
- `eps_C'(S)=0`;
- `X=30`.

### D3-B

- `C[D]=K3`;
- `eps_C(D)=1`;
- `r=0`;
- `F[S]=K3`;
- `eps_C'(S)=0`;
- `X=30`.

In both cases `e_M(S)=0`. Since `q-X=0`, the exact subset identity gives

`e_M(A\S)=0`, `G_{A\S}=0`.

Thus the old q30 shell is bipartite across `S | (A\S)`, all decoration is on S, and `A\S` is an undecorated 10-clique in F.

## 2. The resulting q31 d=3 platforms

Write `T=A\(S union {y})`, so `|T|=9`. In the new shell

`A'={p} union T union D`.

The 10-set `B={p} union T` is independent in the new missing graph `M'`.

Let `c=e_F(T,D)`.

### From D3-B

Here `M'[D]` is empty and the three shell weights on D are fixed at

`(11,10,10)`.

Any undecorated `b in T` has new missing degree `3-a_b`, where `a_b` is its number of F-neighbours in D. q31 maximality excludes missing degree1 or2 because

- degree1 would require a singleton weight at least12, but the maximum is11;
- degree2 would require `t_i+t_j-e_M(ij)>=22`, but every pair has value at most21.

Therefore every T-vertex has new missing degree either3 or0. Hence each T-vertex is either anticomplete or complete to D in F.

If `r0` is the number of T-vertices complete to D, then `c=3r0`. Since the new decoration is `G'=1+c<=9`,

`r0 in {0,1,2}`.

Up to permutation of D, the exact q31 shell is

`M' = K_{3,10-r0} + r0 K1`,

with decoration on the 3-side

`g=(r0+1,r0,r0)`.

### From D3-A

Here `M'[D]` is one edge and the D-weights are fixed at

`(11,11,10)`,

where the M'-edge joins the two weight-11 vertices.

Again every undecorated T-vertex has new missing degree only3 or0: every possible 2-subset has charge exactly21 and every singleton has weight at most11.

Thus `c=3r0`, now with `G'=c<=9`, so

`r0 in {0,1,2,3}`.

The exact q31 shell is

`M' = (K_{3,10-r0} + r0 K1) + e_D`,

where `e_D` is the unique edge inside the 3-side, and

`g=(r0,r0,r0)`.

Hence **all d=3 final rises are reduced to seven explicit q31 platform families**.

## 3. Exact d=10 classification

For `d=10`,

`X = 74 + eps_C(D)-e_C(D)+r <=30`.

Hence

`e_C(D) >= 44 + eps_C(D)+r`.

Using the exchange identity, exactly two cases survive:

### D10-A

- `C[D]=K10`;
- `eps_C(D)=1`;
- `r=0`;
- `F[S]=K10`;
- `eps_C'(S)=0`;
- `X=30`.

### D10-B

- `C[D]=K10-e`;
- `eps_C(D)=0`;
- `r=0`;
- `F[S]=K10`;
- `eps_C'(S)=0`;
- `X=30`.

Again `e_M(S)=0`, and `q-X=0` gives

`e_M(A\S)=0`, `G_{A\S}=0`.

Thus the three vertices in `A\S` are an undecorated F-clique.

## 4. The resulting q31 d=10 platforms

Write `T=A\(S union {y})`, so `|T|=2`. In the new shell

`A'={p} union T union D`.

The 3-set `B={p} union T` is M'-independent. The shell weights on the 10-side D are fixed:

- D10-A: one weight4 and nine weight3;
- D10-B: the endpoints of the unique M'[D]-edge have weight4 and the other eight have weight3.

For `t in T`, let its new missing degree be `rho`. q31 maximality gives:

- `rho=1` impossible because its missing singleton has weight at most4 <12;
- `rho=2` impossible because any pair has charge at most8 <22;
- `rho=3` impossible because any triple has charge at most12 <30;
- `rho=4,...,9` were already excluded by the general q31 extreme-degree theorem.

Hence `rho` is0 or10.

If a T-vertex had `rho=0`, then it is F-complete to all ten D-vertices and contributes ten units to the imported-shell decoration. This gives `G'>=10`, contradicting the universal q31 ceiling `G'<=31-22=9`.

Therefore both T-vertices have `rho=10`.

So the only two d=10 q31 platforms are:

- `M'=K_{3,10}`, with `G'=1` on one vertex of the 10-side;
- `M'=K_{3,10}+e_D`, where `e_D` is one edge inside the 10-side and `G'=0`.

## 5. Consequence

Any q30 -> q31 final rise with distance3 or10 is no longer a general shell transition. It lands in one of exactly nine explicit q31 platform families:

- seven d=3 families;
- two d=10 families.

The unresolved E406 work is therefore a multi-support compatibility problem on these q31 platforms, together with any final-rise transitions of distances1,2,11,12 not yet eliminated.