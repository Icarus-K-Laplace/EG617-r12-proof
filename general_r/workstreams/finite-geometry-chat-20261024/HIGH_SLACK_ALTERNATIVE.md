# High-Slack Alternative: Exact Arithmetic and Open Gap

Status: **The scalar slack identities and the universal excess floor are PROVED; the high-slack contradiction is OPEN**.

## Definitions

For a hypothetical counterexample to P(q), let N=q^2+1 and

\[
m_q=\frac{q^2(q-1)}2.
\]

For each color i, write

\[
e_i=m_q+q+a_i.
\]

For each vertex x, define the slack on W=V minus {x} by

\[
s_i(x)=e_i-d_i(x)-m_q=q+a_i-d_i(x).
\]

The exact identities are

\[
\sum_i a_i=m_q,\qquad
\sum_i s_i(x)=m_q,\qquad
\sum_x s_i(x)=q(q-1)+(q^2-1)a_i.
\]

## Theorem K.H1 — Universal global excess floor

The low-slack weighted blocker argument proves

\[
\boxed{a_i\ge q-1\quad\text{for every color }i.}
\]

Reason: if a_i<=q-2, the identity for sum_x s_i(x) makes the average slack strictly below q-1, so some vertex has s_i(x)<=q-2. The low-slack clique partition then yields d_i(x)>=2q-s_i(x)-1 and hence a_i>=q-1, contradiction.

Therefore

\[
\sum_i(a_i-(q-1))=\frac{q(q-1)(q-2)}2.
\]

This is a genuine global strengthening over merely ruling out exact Turan equality.

## Theorem K.H2 — Necessary bound if at most one color is low-slack at a fixed vertex

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

Thus the obvious local-sum argument still does not close the high-slack branch.

## Formal scalar profile showing the gap

The assignments

\[
a_i=\frac{q(q-1)}2,\qquad d_i(x)=q,\qquad
s_i(x)=\frac{q(q-1)}2
\]

for every color i and vertex x satisfy all the scalar identities, the universal floor a_i>=q-1, and the local-slack lower bound s_i(x)>=1 for q>=3. They make every color high-slack for q>=3. This is only a **formal arithmetic profile**, not a construction of a coloring or a claim that the required graphs exist.

Its purpose is to certify that the currently proved scalar identities alone cannot force two low-slack colors.

## Exact remaining theorem

One needs a genuinely multicolor graph-compatibility inequality that uses more than edge totals and degree sums, for example:

- a restriction on how many colors can have d_i(x) <= a_i+1 simultaneously;
- a degree/excess inequality using alpha(G_i)<=q and omega(G_i)<=q together;
- or a direct proof that a high-slack configuration creates a forbidden independent transversal or a design terminal.

Until such a result is proved, the high-slack alternative remains OPEN and must not be reported as a contradiction.
