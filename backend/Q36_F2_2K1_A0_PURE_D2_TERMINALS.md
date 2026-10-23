# q36 f=2, 2K1 far, a_F=0 — exact pure-d2 low-c terminals

Status: `PROVED REDUCTION` under `Q36_F2_2K1_A0_REDUCTION.md`, inherited D14, CORE211, and lexicographic q36 maximality.

By `Q36_F2_2K1_A0_LOW_C_D3_ELIMINATION.md`, every surviving state in this branch has only d2 low rows and therefore `c<=4`.

This note records the exact c=3,4 terminals.

## 1. Common setup

All low rows have missing set F, so `delta=0`. Let

- `X` be the decorated shell set, `|X|=11-c`;
- `nu=e_M(X)`;
- `G=sum_X g_x`.

The exact shell ledger becomes

`G=13-nu`.                                                   (1)

For c>=3, all d2 rows share one repeated support D of size2. By d2 rigidity,

- `H[D]=K2`;
- `kappa(D)=0`;
- D is target-anticomplete to F;
- the repivot has q=35.

Let

`k=e_F(D,X)`.

The 12-point set `{p} union C union X` has

- 11 edges from p to its shell vertices;
- `55-nu` target edges inside `C union X`, because C is a target clique, C is target-complete to X, and the only shell target nonedges there are the nu edges of M[X].

Hence it spans exactly

`66-nu`

target edges.

Adding the support D gives a 14-point set. It contributes

- one internal edge of D;
- `2c` low-owner/support edges from C to D;
- k edges from D to X;
- no edge from p to D.

Thus D14 gives

`66-nu + 1 + 2c + k <=69`,

or

> `k<=nu+2-2c`.                                             (2)

## 2. c=4 exact terminal

Here `|X|=7`. Since every X-vertex is decorated, (1) gives

`13-nu=G>=7`,

so `nu<=6`.

Equation (2) gives `k<=nu-6`, hence `nu>=6`.

Therefore

> `nu=6`, `G=7`, `k=0`.                                    (3)

Because seven decorated vertices have total decoration7, every x in X has

> `g_x=1`.                                                  (4)

Thus the c=4 terminal is completely normalized:

- X has seven vertices and exactly six missing edges;
- every X-vertex has decoration1;
- the four low owners share one pure K2 support D;
- D is target-anticomplete to X and F;
- every D14 inequality above is saturated.

In particular the q35 repivot through D has retained old decoration7 and inserts two support vertices of decoration at least3 each, so the new decoration total is exactly13 and the new shell missing-edge count is exactly22.

## 3. c=3 exact terminal

Here `|X|=8`, and the decoration floor gives

`13-nu=G>=8`,

so `nu<=5`.

Equation (2) gives

`k<=nu-4`,

hence `nu>=4`.

Therefore

> `nu in {4,5}` and `k<=nu-4`.                              (5)

More explicitly:

- if `nu=4`, then `G=9` and `k=0`;
- if `nu=5`, then `G=8` and `k<=1`.

The repeated support D is again a pure K2 of zero core excess and repivots to q35.

## 4. Remaining pure-d2 frontier

The entire `2K1,a_F=0` branch is now reduced to `c in {1,2,3,4}` with only d2 rows.

The c=3,4 sectors have the exact normal forms above. The c=1,2 sectors remain less rigid because a repeated support is not forced when c<=2.

No d3 row remains anywhere in this branch.