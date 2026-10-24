# High-Slack Alternative: Exact Arithmetic and Open Gap

Status: **The scalar slack identities are PROVED; the high-slack contradiction is OPEN**.

## Definitions

For a hypothetical counterexample to P(q), let N=q^2+1 and

\[
m_q=\frac{q^2(q-1)}2.
\]

For each color i, write

\[
e_i=m_q+q+a_i,\qquad a_i\ge0.
\]

For each vertex x, define the slack on W=V\{x} by

\[
s_i(x)=e_i-d_i(x)-m_q=q+a_i-d_i(x).
\]

The previously established identities are

\[
\sum_i a_i=m_q,\qquad
\sum_i s_i(x)=m_q,\qquad
\sum_x s_i(x)=q(q-1)+(q^2-1)a_i.
\]

The strengthened near-line lemma proves s_i(x)>=1 for every i,x: equality zero would force a monochromatic K_(q+1).

A color is called low-slack at x if s_i(x)<=q-2. Brouwer's theorem then gives its q-block partition.

## Theorem K.H1 — Necessary bound if at most one color is low-slack

If at a fixed vertex x at most one color has s_i(x)<=q-2, then at least q-1 colors satisfy s_i(x)>=q-1. Hence

\[
\sum_i s_i(x)\ge(q-1)^2.
\]

This does not contradict the exact total

\[
\sum_i s_i(x)=m_q,
\]

because

\[
m_q-(q-1)^2=\frac{(q-1)((q-1)^2+1)}2>0.
\]

Thus the obvious local-sum argument does not close the high-slack branch.

## Formal scalar profile showing the gap

The assignments

\[
a_i=\frac{q(q-1)}2,\qquad d_i(x)=q,\qquad
s_i(x)=\frac{q(q-1)}2
\]

for every color i and vertex x satisfy all the scalar identities above and have every color high-slack for q>=3. The corresponding edge count would be e_i=Nq/2, consistent with the degree-sum identities.

This is only a **formal arithmetic profile**, not a construction of a coloring or a claim that the required graphs exist. Its purpose is to certify that the currently proved scalar identities alone cannot force two low-slack colors.

## Exact remaining theorem

One needs a genuinely multicolor graph-compatibility inequality that uses more than edge totals and degree sums, for example:

- a restriction on how many colors can have d_i(x) <= a_i+1 simultaneously;
- a degree/excess inequality using alpha(G_i)<=q and omega(G_i)<=q together;
- or a direct proof that a high-slack configuration creates a forbidden independent transversal or a design terminal.

Until such a result is proved, the high-slack alternative remains OPEN and must not be reported as a contradiction.
