# Repeated-Class Exchange Duality and the zeta Coordinate

Assumptions: legal regular repivots in one residual graph F. This lemma is symbolic in the support size d; the d2 application is the main use here.

## 1. View notation

At pivot p let

- shell A;
- core H;
- y a regular shell owner;
- `S=S_y subset A`, `D=D_y subset H`, `|S|=|D|=d`;
- `T=A\(S union {y})`.

After repivoting through y,

> `A_y={p} union T union D`,
>
> `H_y=(H\D) union S`.                                      (1.1)

Define an **exact `(S,D)` owner class** at p by

`Y_{S,D}={x in A : x regular, S_x=S, D_x=D}`.

Let

`m=|Y_{S,D}|`,

and assume `y in Y_{S,D}`.

Also let

`Z_0(p)={z in A:z regular and d_z=0}`,

`zeta(p)=|Z_0(p)|`.

---

# 2. Exact class-to-zero transport

### Lemma 2.1

Every other owner

`x in Y_{S,D}\{y}`

becomes a d=0 regular owner in the y-view.

### Proof

Such an x has, in the p-view,

- shell missing set exactly S;
- core target-neighbour set exactly D.

In the new shell `A_y={p} union T union D`:

- x is target-adjacent to p;
- x is target-adjacent to every vertex of T other than itself because its old shell missing set is S;
- x is target-adjacent to every vertex of D because its old core support is D.

So x has no shell missing neighbour in the y-view.

In the new core `H_y=(H\D) union S`:

- x has no target neighbour in `H\D`, because its old core neighbours were exactly D;
- x has no target neighbour in S, because S was exactly its old shell missing set.

So x has no new-core target neighbour either. Since x remains regular in F, it is a d=0 owner.

Therefore

> **`zeta(y)>=m-1`.**                                        (2.1)

QED.

---

# 3. Exact zero-to-reverse-class transport

### Lemma 3.1

Every old d=0 owner

`z in Z_0(p)`

becomes, in the y-view, a regular owner with

> shell missing set D,
>
> core support S.

The old pivot p itself has the same reverse pair `(D,S)`.

### Proof

An old d0 owner z is target-adjacent to every other vertex of A and has no target neighbour in H.

In the new shell `A_y={p} union T union D`:

- z is target-adjacent to p and to T;
- z is target-nonadjacent to every vertex of D, because D lies in the old core H.

Hence its new shell missing set is exactly D.

In the new core `H_y=(H\D) union S`:

- z is target-nonadjacent to `H\D`;
- z is target-adjacent to S, because S lay in the old shell A.

Hence its new core support is exactly S.

For the old pivot p, the same statement holds: p is target-nonadjacent to old-core D and target-adjacent to old-shell S. Thus p is also a reverse `(D,S)` owner in the y-view.

Therefore the reverse class at y has multiplicity at least

> **`zeta(p)+1`.**                                           (3.1)

QED.

---

# 4. d0 repivots preserve zeta

If y itself is a d0 owner, then `S=D=empty`. The new core is H and the new shell is obtained by swapping y and p.

Every old d0 owner other than y remains d0, and p becomes d0. Hence

> **`zeta(y)=zeta(p)` for every d0 neutral repivot.**         (4.1)

Thus zeta is well-defined on the quotient by d0 pivot relabellings.

---

# 5. The third lexicographic coordinate

Define

> **`Phi_3(p)=(q_p,tau_p,zeta(p))`.**                         (5.1)

Each coordinate is an integer and bounded on the finite residual graph:

- q is bounded by the backend ceiling;
- tau is at most `r+1`;
- zeta is at most `r+1`.

Therefore `Phi_3` is a genuine well-founded lexicographic potential.

Now suppose `p -> y` is q-flat and tau-flat, and y lies in an exact repeated `(S,D)` class of multiplicity m. By (2.1),

`zeta(y)>=m-1`.

Hence:

> **Repeated-class zeta improvement criterion**
>
> if `m>=zeta(p)+2`, then
> `Phi_3(y)>_lex Phi_3(p)`.                                  (5.2)

Consequently, at a `Phi_3`-maximal pivot,

> **every exact repeated class that admits a q/tau-flat repivot has**
>
> **`m<=zeta(p)+1`.**                                        (5.3)

This is a genuine new plateau restriction unavailable from `(q,tau)` alone.

---

# 6. Equality rigidity

Assume p is `Phi_3`-maximal and a q/tau-flat repeated-class repivot y has

`m=zeta(p)+1`.

Then (2.1) gives

`zeta(y)>=zeta(p)`.

Maximality gives the reverse inequality, so

> **`zeta(y)=zeta(p)=m-1`.**                                 (6.1)

Thus the `m-1` owners in `Y_{S,D}\{y}` account for **all** d0 owners in the y-view: no additional shell vertex may become d0.

At the same time, Lemma 3.1 gives a reverse `(D,S)` class of multiplicity at least

`zeta(p)+1=m`.

Therefore a zeta-flat repeated-class exchange has the rigid form

> an m-owner `(S,D)` class is exchanged for
> an m-owner-or-larger reverse `(D,S)` class,
> while the other `m-1` original owners become exactly the full d0 population of the new view.   (6.2)

If the reverse class were larger than m and one of its rows were q/tau-flat, the same zeta criterion would force a strict improvement on the next step. Hence any closed `Phi_3`-flat correction cycle must have exact multiplicity balance at every repeated-class exchange.

**Status:** exchange duality and zeta criterion `PROVED_SYMBOLIC`; complete classification of balanced cycles `OPEN`.

---

# 7. d2 fully-decorated consequence

For a repeated d2 support D, both vertices of D have support multiplicity at least two and hence are globally decorated.

If the repivot is tau-flat, then

`|D intersect X|=|S intersect X|`.

Since `|D intersect X|=2`, necessarily

> **`S subset X`.**                                         (7.1)

Thus every q/tau-flat repeated d2 class automatically lies in the fully-decorated shell-pair regime isolated by `D2_FIXED_CLASS_PLATEAU.md`.

Combining with (5.3):

> At a `Phi_3=(q,tau,zeta)`-maximal pivot, every q/tau-flat repeated d2 class in the unique scalable shell regime has multiplicity at most `zeta+1`; equality is a rigid support/neutral-population exchange.

This transfers any unbounded repeated-support multiplicity into an equally large d0 neutral population and converts the remaining obstruction into a balanced correction-cycle problem.

---

# 8. Main-theorem impact

The previous candidate `Q2=sum kappa^2` is exact and bounded but has no proved universal monotonicity.

The coordinate zeta is different: it has a proved monotonicity criterion on the exact repeated-support plateau, the main multiplicity obstruction left by the fixed-class d2 theorem.

The current preferred potential is therefore

> **`Phi=(q,tau,zeta, ... )`**

with a fourth coordinate needed only for

1. distinct-support fully-decorated d2 plateau systems; and
2. zeta-balanced repeated-class correction cycles.

This is a strict reduction of the potential-design problem.