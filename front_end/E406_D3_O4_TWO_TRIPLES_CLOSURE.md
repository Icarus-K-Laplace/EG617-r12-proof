# E406 d=3 Type-A O4: uniform two-triple closure

Status: `PROVED EMPTY` for both eta=0 and eta=1.

Assume a modern Type-A O4 state in which the entire overlap budget O=4 is realized by exactly two triple-full H-vertices.

Let:

- `p_i` be the pure-class size of support row i;
- `d_i=8-p_i`;
- `s_i` be the number of singleton-full carriers on row i;
- `m_i` be the number of the two triple vertices full to row i;
- `delta_i=1` for the unique 9-full row and `0` for the three 10-full rows.

The full-row count on row i is `10-delta_i`, so the number of non-pure full memberships required there is

`(10-delta_i)-p_i = 2+d_i-delta_i`.

Hence

`s_i = 2+d_i-delta_i-m_i`.

The vertices in `P_i`, the support triangle `T_i`, and all singleton-full carriers on row i form a clique. K12-freeness gives

`p_i+3+s_i<=11`,

therefore

`s_i<=8-p_i=d_i`.

Substituting into the row-demand equation yields

`m_i>=2-delta_i`.

Summing over the four rows gives

`sum_i m_i >= 1+2+2+2 = 7`.

But two triple-full vertices contribute exactly six row memberships in total:

`sum_i m_i=3+3=6`.

Contradiction.

Therefore no Type-A O4 state can realize the multiplicity type two triples, independently of eta and independently of the detailed H-edge structure.

Consequently, after the simple-four-double closures and the eta=1 one-triple/two-double closure, the only remaining Type-A O4 multiplicity family is eta=0 with one triple plus two doubles.