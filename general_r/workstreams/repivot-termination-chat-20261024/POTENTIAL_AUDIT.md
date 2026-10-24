# Potential Audit — Round 2

Status: **No new strict potential certified.** The existing Q2 universal-monotonicity proposal remains DISPROVED_AS_STATED.

## 1. Frozen potential

The canonical potential is

Phi4=(q,tau,zeta,eta).

It is a bounded lexicographic tuple and can be maximized over legal pivots. This establishes a maximal representative, not a theorem that every nontrivial flat repivot increases a further scalar.

The fifth-coordinate candidate

Q2=sum_{v in H} kappa_v^2

has exact increment

Delta Q2 =
sum_{z in H\D_y}(2 kappa_z delta_z+delta_z^2)
+sum_{s in S_y}(sigma_s-e_F(s,D_y))^2
-sum_{u in D_y}kappa_u^2,

where delta_z=e_F(z,S_y)-e_H(z,D_y).

A legal repivot is reversible. If it is Phi4-flat, the reverse is also Phi4-flat and has the opposite Q2 increment. Therefore universal strict increase of Q2 on every nontrivial Phi4-flat move is impossible.

## 2. Round-2 structural coordinates are not potentials

The high-density clean-pair analysis introduces:

- the AES part deficits s_A,s_B,s_C, with sum h-2;
- six type classes A0,A1,B0,B1,C0,C1;
- witness slacks u_T, which sum to four in each witness triple;
- the exceptional outside count X, with X(3lambda-4-r)<=2r-2-K_U;
- part-assignment slacks u_i, which sum to 4+X;
- the optional edge count e_opt and foreign incidence E_foreign, satisfying
  2e_opt+E_foreign=K_U+sum_i n_i(u_i-1).

These are useful *state descriptors*, but they are not yet a well-defined potential on the full legal-repivot state graph:

1. the AES partition of G=overline(H[U]) may not be unique;
2. witness classes and the assignment of outside vertices may not be unique;
3. X and the slack vectors depend on those choices;
4. a reverse repivot can exchange the distinguished pair and change the chosen representation.

Taking a lexicographic maximum of an arbitrarily chosen representation would not establish a monotone theorem. No such claim is made.

## 3. A safe canonical-representative alternative

A valid weaker use of Q2 is to select, within each finite connected component of the Phi4-flat repivot graph, a representative minimizing (or maximizing) Q2, with a fixed deterministic tie-break on a canonical encoding of the entire state. This always exists for a finite component, but it proves no terminal contradiction by itself. To make it useful, one must prove that every such extremal representative has an impossible clean-pair or d1 structure.

The present Round-2 theorem does not establish that final implication. Thus the safe conclusion is:

- Phi4: **PROVED_SYMBOLIC** as a bounded lexicographic potential.
- Universal strict Q2 increase: **DISPROVED_AS_STATED**.
- Structural slack descriptors: **PROVED_CONDITIONAL** identities, not a potential.
- Any fifth-coordinate terminal elimination: **OPEN**.
