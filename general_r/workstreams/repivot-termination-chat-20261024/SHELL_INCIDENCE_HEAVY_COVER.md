# Shell-Incidence Heavy-Cover Theorem

Assumptions: hypotheses A+B, `r>=12`, and a legal pivot p with shell A.

This theorem compresses the shell missing sets of all low-endpoint regular owners without any common-S assumption.

## 1. Global shell-to-core incidence budget

For each shell vertex `s in A`, define

`t_s=d_M(s)+g_s=e_F(s,H)`.

Summing over A,

`sum_A t_s=2e(M)+G_A=2q-G_A<=2q`.

Under hypothesis B,

> **`sum_A t_s<=6r-2`.**                                    (1.1)

---

## 2. Exact singleton transport identity

Let y be any regular shell owner. Put

`S=S_y=N_M(y)`, `|S|=d`, `b=e_M(S)`.

Use y alone as a singleton common-S family. Then

`L=A\(S union {y})`, `|L|=r-d`.

For `s in S`, because y is a missing neighbour of s,

`d_M(s)=1+m_S(s)+m_L(s)`.

Hence the exact transport slack is

> **`sigma_s=t_s-(r+1-d)-m_S(s)`.**                          (2.1)

Legal repivot-core minimum degree gives

> **`sigma_s>=0` for every s in S.**                         (2.2)

Summing (2.1) and using `sum m_S(s)=2b` gives

`sum_S sigma_s=sum_S t_s-d(r+1-d)-2b`.

Allowance localization `a=b+sum_S sigma_s` therefore yields

> **`sum_{s in S_y} t_s=d(r+1-d)+a_y+b_y`.**                (2.3)

The pointwise inequalities (2.1)–(2.2) are stronger than the summed bound and drive the endpoint collapse below.

**Status:** `PROVED_SYMBOLIC` conditional only on the legal repivot-core minimum-degree contract.

---

## 3. d1: at most five shell support classes

For d=1, `m_S(s)=0`, so (2.1) gives

`sigma_s=t_s-r>=0`.

Thus the unique missing partner of every d1 owner satisfies

`t_s>=r`.

Let

`C_1={s:t_s>=r}`.

By (1.1),

`|C_1|<=floor((6r-2)/r)=5`.

Therefore:

> **D1 Shell-Support Reduction. Every d1 regular owner has its unique shell missing partner in one fixed set of at most five vertices.**

Hence there are at most five d1 common-S classes, independent of r.

**Status:** `PROVED_CONDITIONAL` (A+B).

---

## 4. d2: all support endpoints lie in at most six shell vertices

Let `S={s,t}` and put

`b=e_M(S) in {0,1}`.

For each endpoint, `m_S=b`. Equation (2.1) becomes

> `sigma_s=t_s-r+1-b`,
>
> `sigma_t=t_t-r+1-b`.

By nonnegativity of transport slack,

> **`t_s,t_t>=r-1+b`.**                                     (4.1)

In particular every endpoint of every d2 shell missing pair satisfies

`t>=r-1`.

Define

`U_2={v in A : v occurs in S_y for some d2 regular owner y}`.

Then `U_2 subset {v:t_v>=r-1}`. By (1.1), for `r>=6`,

> **`|U_2|<=6`.**                                            (4.2)

Therefore:

> **D2 Six-Point Support-Universe Theorem. All shell missing pairs of all d2 regular owners are 2-subsets of one fixed set `U_2` of at most six shell vertices.**

Consequently the number of distinct d2 shell missing sets is at most

> **`C(6,2)=15`.**                                           (4.3)

If a d2 support pair is itself a shell missing edge (`b=1`), then both endpoints satisfy `t>=r`; hence every such pair lies inside the even smaller set `C_1`, of size at most five.

This is strictly stronger than the earlier six-vertex-transversal / four-star reduction: no r-growing shell-support family survives at all.

**Status:** `PROVED_CONDITIONAL`.

---

## 5. d2 weighted six-vertex encoding

For every active d2 endpoint `u in U_2`, define

`h_u=t_u-(r-1)>=0`.

For a support pair `S={u,v}` with `b_{uv}=e_M({u,v})`, equation (2.3) specializes to

> **`a_{uv}=h_u+h_v-b_{uv}`.**                               (5.1)

Thus the allowance of every one of the at most fifteen d2 shell classes is determined by

- a graph `M[U_2]` on at most six vertices; and
- at most six nonnegative integer weights `h_u`.

No additional r-dependent shell combinatorics remains.

The global incidence budget also yields

`sum_{u in U_2} [(r-1)+h_u] <=6r-2`,

hence if `m=|U_2|`,

> **`sum_{u in U_2} h_u <= (6-m)r+m-2`.**                    (5.2)

If `m=6`, this collapses further to

> **`sum h_u<=4`.**                                          (5.3)

So the maximal six-endpoint case has a completely bounded allowance profile independent of r.

---

## 6. Owner-count / endpoint-count tradeoff

Every regular d2 owner y itself has

`t_y=d_M(y)+g_y=2`.

No d2 owner can lie in `U_2`: two d2 owners are target-adjacent (otherwise zero-gap would require the union of two 2-sets to equal A), so one d2 owner cannot be a missing-set endpoint of another.

Let N be the total number of d2 regular owners and `m=|U_2|`. From (1.1),

`m(r-1)+2N<=6r-2`.

Therefore

> **`2N<=(6-m)r+m-2`.**                                     (6.1)

In particular:

- `m=6 => N<=2`;
- `m=5 => N<=floor((r+3)/2)`;
- if `N>(r+3)/2`, then necessarily `m<=4`, so there are at most six distinct d2 shell support classes.

This gives a useful multiplicity-versus-support-diversity tradeoff for the next multi-pivot theorem.

---

## 7. d3 consistency bound

For d=3, (2.1) gives

`sigma_s=t_s-r+2-m_S(s)>=0`,

so every d3 support endpoint satisfies

`t_s>=r-2`.

Thus all d3 shell support endpoints lie in at most seven vertices for r=12 and at most six for r>=13. The d3 endpoint is already eliminated by the stronger B-floor/low-charge argument.

---

## 8. Main-theorem impact

The low endpoint shell geometry is now fixed-width:

- d1: at most 5 shell support types;
- d2: at most 6 support vertices and at most 15 shell support types;
- d3: eliminated.

Hence **no low-endpoint shell-support case count grows with r**. Any remaining r-growth occurs only through owner multiplicities and the core-support / transported-excess systems *inside finitely many common-S classes*.

The next theorem should therefore be a finite-class multi-pivot transport theorem, not a shell-support classification theorem.