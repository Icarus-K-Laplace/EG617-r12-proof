# Global-to-Local Slack Dictionary

Status: **PROVED**.

Let `chi` be a hypothetical counterexample to `P(q)` on

`N=q^2+1`

vertices. Let `G_i` be color graph `i`, with ambient edge count `e_i` and degree `d_i(x)` at vertex `x`.

Put

`m_q := q*C(q,2)=q^2(q-1)/2`,

the Turan-complement minimum on every `q^2`-vertex restriction.

## Theorem K.6 — Ambient edge floor

Every color satisfies

`e_i >= m_q+q`.

### Proof

For every vertex `x`, the restriction `G_i-x` has `q^2` vertices and independence number at most `q`, so

`e_i-d_i(x) >= m_q`.

Sum over all `N=q^2+1` vertices. Since `sum_x d_i(x)=2e_i`,

`(N-2)e_i >= N m_q`,

that is

`(q^2-1)e_i >= (q^2+1)m_q`.

Hence

`e_i >= m_q * (q^2+1)/(q^2-1)`

`= m_q + q^2/(q+1)`.

Since `q^2/(q+1)=q-1+1/(q+1)`, integrality gives

`e_i >= m_q+q`.

## Definition — Ambient excess

Write

`e_i=m_q+q+a_i`,

where `a_i>=0` is an integer.

## Theorem K.7 — Exact total ambient excess

The ambient excesses satisfy

`sum_i a_i = m_q`.

### Proof

The color graphs partition all edges of `K_(q^2+1)`, so

`sum_i e_i=C(q^2+1,2)=q^2(q^2+1)/2`.

Subtract `q(m_q+q)` and simplify:

`sum_i a_i = q^2(q-1)/2 = m_q`.

## Theorem K.8 — Exact local slack identity

For vertex `x`, define the `q^2`-restriction slack

`s_i(x):=e(G_i-x)-m_q=e_i-d_i(x)-m_q`.

Then

> **`s_i(x)=q+a_i-d_i(x)`.**

In particular:

- `s_i(x)>=0` is equivalent to the restriction Turan floor;
- `d_i(x)<=q+a_i` for every `i,x`;
- the Brouwer low-slack window `s_i(x)<=q-2` is equivalent to

  `d_i(x)>=a_i+2`.

Thus low-slack coordinatization is exactly a **relative high-degree event** measured against the ambient excess `a_i`.

## Corollary K.9 — Local total slack is constant

For every vertex `x`,

`sum_i s_i(x)=m_q`.

Indeed

`sum_i (q+a_i-d_i(x))=q^2+m_q-q^2=m_q`.

## Corollary K.10 — Slack mass of one color across all deletions

For every color `i`,

`sum_x s_i(x)=q(q-1)+(q^2-1)a_i`.

This follows either by summing K.8 over vertices or from

`sum_x s_i(x)=(N-2)e_i-Nm_q`.

## Strategic implication

The local structural theorem is now completely translated into global graph statistics:

> to force a low-slack `q x q` coordinatization for color `i` at vertex `x`, it is enough and necessary (within the Brouwer window) to force `d_i(x)>=a_i+2`.

The remaining global problem is therefore a multicolor degree/excess forcing theorem. Simple averaging does not automatically give two such colors at one vertex because the average ambient excess is

`m_q/q=q(q-1)/2`,

much larger than a typical color degree. Any successful argument must exploit compatibility between colors, not one-color averages alone.