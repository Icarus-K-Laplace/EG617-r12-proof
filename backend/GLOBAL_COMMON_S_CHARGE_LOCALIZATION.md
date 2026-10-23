# Global Common-S Charge Localization Theorem

Status: `PROVED_ANALYTIC`.

Dependencies:

- pivot shell/core decomposition;
- common-S owner definition;
- global degree-decoration notation;
- exact identity `q=e(M)+G_A`.

Purpose: control the total common-S core charge directly from the pivot q-budget and the internal missing-edge imbalance of the shell. This supplies the scalar bridge needed by the global charge-barrier theorems.

## 1. Setup

Let p be a regular pivot with shell A of size h and core H.

Let Y be a common-S family of N regular shell owners with

`S_y=S`, `|S|=d`

for every owner.

Put

`T=A\(Y union S)`.

Then

`|T|=h-d-N`.

Because Y is common-S:

- every Y--S pair is a shell missing edge;
- every Y--Y pair is a target edge;
- every Y--T pair is a target edge.

Hence every shell missing edge not in `Y x S` lies entirely inside

`S union T`.

Write

`m_SS=e_M(S)`,
`m_ST=e_M(S,T)`,
`m_TT=e_M(T)`.                                               (L1)

Let

`G_S=sum_(s in S) g_s`,
`G_A=sum_(a in A) g_a`.                                     (L2)

For core vertices use the common-S charge

`w_v=kappa_v+e_F(v,S)`,

and total charge

`W=sum_(v in H) w_v`.                                       (L3)

Let

`K=sum_(v in H) kappa_v`.                                   (L4)

## 2. Exact shell missing-edge ledger

The owner--missing-set block contributes exactly

`dN`

missing edges.

All other missing edges lie inside `S union T`. Therefore

> `e(M)=dN+m_SS+m_ST+m_TT`.                                 (L5)

Since

`q=e(M)+G_A`,

we have

> `G_A=q-dN-m_SS-m_ST-m_TT`.                               (L6)

## 3. Exact S--core incidence count

Fix `s in S`.

Its total target degree is

`h+g_s`.

Inside the pivot/shell part:

- s is adjacent to p;
- s has no target neighbours in Y;
- among `(S union T)\{s}`, it has
  `h-N-1-d_M(s,S union T)` target neighbours.

Therefore its core degree is

`e_F(s,H)`
` =h+g_s-1-[h-N-1-d_M(s,S union T)]`
` =N+g_s+d_M(s,S union T)`.                                 (L7)

Summing over `s in S` gives

> `e_F(S,H)=dN+G_S+2m_SS+m_ST`.                             (L8)

Hence

> `W=K+dN+G_S+2m_SS+m_ST`.                                 (L9)

This is exact.

## 4. Charge localization inequality

Because `G_S<=G_A`, combine (L6) and (L9):

`W`
` <=K+dN+[q-dN-m_SS-m_ST-m_TT]+2m_SS+m_ST`
` =K+q+m_SS-m_TT`.

Therefore:

> **Common-S charge localization theorem**
>
> `W<=K+q+e_M(S)-e_M(T)`.                                  (L10)

In particular, since `e_M(T)>=0`,

> `W<=K+q+e_M(S)`                                           (L11)
>
> ` <=K+q+C(d,2)`.                                          (L12)

This bound is independent of owner multiplicity distribution and support geometry.

## 5. Refined owner-count form

Equation (L5) and nonnegativity of `G_A` imply

`m_SS+m_ST+m_TT<=q-dN`.                                     (L13)

Thus

`m_SS<=min(C(d,2),q-dN)`.                                   (L14)

Substituting into (L10) gives

> `W<=K+q+min(C(d,2),q-dN)-m_TT`.                           (L15)

Hence large owner count automatically tightens the total charge budget.

## 6. E334 q32/core211 consequences

Under the source-reported surviving E334 channel,

`q=32`,
`e(H)=211`,

so

`K=2e(H)-420=2`.                                            (L16)

### d=3

Equation (L12) gives

> `W<=2+32+3=37`.                                           (L17)

More precisely,

`W<=34+min(3,32-3N)-m_TT`.                                  (L18)

For N=10:

> `W<=36`.                                                   (L19)

For N=9:

> `W<=37`.                                                   (L20)

### d=2

Equation (L12) gives

> `W<=2+32+1=35`.                                           (L21)

Thus every common-S d2 subsystem in this q32/core211 channel automatically lies in a genuinely low-charge regime.

## 7. Immediate interaction with global pattern barriers

`GLOBAL_D3_PATTERN_CHARGE_BARRIERS.md` proves that a three-class Type-H d3 one-loss pattern in a 35-core requires

`W>=62`.

But (L17) gives `W<=37` in E334 q32/core211.

Therefore:

> **no three-class Type-H equality geometry can occur in an E334 q32/core211 common-S subsystem.**   (L22)

This eliminates an entire equality family by one scalar comparison.

The Type-P three-class barrier is `W>=33`, so in E334 it is confined to the narrow charge window

`33<=W<=37`,                                                  (L23)

rather than an arbitrary configuration.

## 8. Structural meaning

The theorem explains why high-backend common-S systems cannot freely spend charge in the core:

- every owner already consumes d shell missing edges;
- q fixes the combined missing-edge plus shell-decoration budget;
- any decoration moved onto S increases S--core incidence;
- internal missing edges of T reduce the available core charge.

Thus shell topology and core charge are two views of the same conserved budget.

## 9. Generalization

The exact identities (L5), (L8), (L9) and inequality (L10) are symbolic in

- shell size h;
- support/missing size d;
- owner count N;
- core excess K;
- pivot q.

No numerical r=12 constant is used in their derivation. The only r-specific values appear in Section6.

Therefore the charge localization theorem transfers directly to higher-r pivot systems with the same shell/core bookkeeping.