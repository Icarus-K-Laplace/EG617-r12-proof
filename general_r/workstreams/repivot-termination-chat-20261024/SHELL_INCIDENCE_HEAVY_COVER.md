# Shell-Incidence Heavy-Cover Theorem

Assumptions: hypotheses A+B, `r>=12`, and a legal pivot p with shell A.

This theorem compresses the shell missing sets of all low-endpoint regular owners without any common-S assumption.

## 1. Global shell-to-core incidence budget

For each shell vertex `s in A`, define

`t_s=d_M(s)+g_s`.

By the symbolic backend degree ledger, `t_s` is exactly the number of target neighbours of s in the core H:

` t_s=e_F(s,H) `.

Summing over A,

`sum_{s in A} t_s=2e(M)+G_A`.

Since

`q=e(M)+G_A`,

we obtain

`sum_A t_s=2q-G_A<=2q`.

Under hypothesis B,

> **`sum_A t_s<=6r-2`.**                                    (1.1)

Thus the entire shell has only O(r) core-incidence mass.

---

## 2. Exact singleton allowance identity

Let y be any regular shell owner. Put

`S=S_y=N_M(y)`, `|S|=d`,

and let

`b=e_M(S)`.

Use y alone as a singleton common-S family. Then

`L=A\(S union {y})`, `|L|=r-d`.

For `s in S`,

`d_M(s)=1+m_S(s)+m_L(s)`

because y is one missing neighbour of s. Hence

`sigma_s=m_L(s)+g_s-|L|`

`=t_s-1-m_S(s)-(r-d)`

`=t_s-(r+1-d)-m_S(s)`.

Summing over S and using

`sum_{s in S} m_S(s)=2b`,

we get

`sum_{s in S} sigma_s`
`=sum_{s in S}t_s-d(r+1-d)-2b`.

The exact allowance localization is

`a=b+sum_{s in S}sigma_s`.

Therefore:

> **Singleton incidence identity**
>
> **`sum_{s in S_y} t_s=d(r+1-d)+a_y+b_y`.**                (2.1)

In particular, because `a_y,b_y>=0`,

> **`sum_{s in S_y} t_s>=d(r+1-d)`.**                       (2.2)

This is exact and independent of owner multiplicity.

**Status:** `PROVED_SYMBOLIC`.

---

## 3. d1 support set has size at most five

For d=1, (2.2) gives, for the unique shell missing partner s,

`t_s>=r`.

Define

`C_1={s in A:t_s>=r}`.

By (1.1),

`|C_1| r<=6r-2`,

so for every r>=3,

> **`|C_1|<=5`.**                                            (3.1)

Therefore:

> **Every d1 regular owner has its unique shell missing partner in one fixed set of at most five shell vertices.**

Consequently all d1 owners split into at most five common-S classes.

**Status:** `PROVED_CONDITIONAL` (uses q ceiling from B).

---

## 4. d2 support graph has a six-vertex transversal

For d=2, every shell missing pair `S_y={s,t}` satisfies

`t_s+t_t>=2(r-1)`.                                           (4.1)

Hence at least one endpoint has

`t>=r-1`.

Define

`C_2={s in A:t_s>=r-1}`.

By (1.1), for r>=6,

`|C_2|<=floor((6r-2)/(r-1))<=6`.

Therefore:

> **Every d2 shell missing pair meets the fixed heavy set `C_2`, with `|C_2|<=6`.**   (4.2)

Equivalently, the graph whose edges are the distinct d2 shell missing pairs has vertex-cover number at most six.

This is a global statement across all d2 owners and all common-S classes.

**Status:** `PROVED_CONDITIONAL`.

---

## 5. d2 star-plus-bounded-core refinement

Define the superheavy set

`P={s in A: 2t_s>=3(r-1)}`

and the half-heavy set

`Q={s in A: 2t_s>=r-1}`.

From (1.1), for r>=12,

`|P|<=floor((12r-4)/(3r-3))<=4`,

and

`|Q|<=floor((12r-4)/(r-1))<=12`.                             (5.1)

Take a d2 support edge `{s,t}`.

If it meets P, it lies in one of at most four star families centered at P.

If it does not meet P, then both endpoints have

`t_s,t_t<3(r-1)/2`.

Together with (4.1), this forces

`t_s>(r-1)/2`, `t_t>(r-1)/2`,

so both endpoints lie in Q.

Therefore:

> **D2 Star-Core Reduction.** Every d2 shell missing pair is either
>
> 1. incident with one of at most four superheavy hubs in P; or
> 2. entirely contained in a bounded set Q of at most twelve shell vertices.   (5.2)

Thus every r-growing family of *distinct* d2 shell supports is confined to at most four stars. All non-star support diversity lives inside an r-independent twelve-vertex core.

**Status:** `PROVED_CONDITIONAL`.

---

## 6. d3 side remark

For d=3, (2.2) gives

`sum_{s in S_y}t_s>=3(r-2)`.

Hence each d3 support meets

`C_3={s:t_s>=r-2}`.

The global budget gives

- `|C_3|<=7` at r=12;
- `|C_3|<=6` for every r>=13.

The d3 endpoint is already eliminated by the stronger Bridge-B/B-floor argument, so this is recorded only as consistency evidence.

---

## 7. Main-theorem impact

Before this theorem, d1 and d2 shell supports could a priori range over O(r) shell vertices with no fixed transversal.

After it:

- d1 has at most five shell support classes;
- d2 has transversal number at most six;
- all unbounded d2 support diversity lies in at most four star systems;
- the remaining d2 support graph is contained in at most twelve shell vertices.

Therefore the only genuinely scalable low-endpoint geometry has the form of **at most four weighted d2 stars**. This is the correct object for the next multi-pivot compatibility theorem; there is no need to enumerate arbitrary pair-support graphs.