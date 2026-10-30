# Cross-root parent contract audit

Date: 2026-10-30. Status: **PROVED_CONDITIONAL** on the explicit genuine h13 T61 parent contract. The mapping from that contract is proved here.

## Read-only sources

Global head b0459807acd4b7e386148056ddf77d7998918893:

- front_end/FRONTEND_BRIDGE_THEOREM.md, F0/F7/F8: definition of R(a,n), induced caps,61-point residual, alpha<=5, omega<=11, actual minimum degree12 or13, h13 pivot identity.
- front_end/T61_H13_FULL_COLOR_DEGREE_AND_ANTINEIGHBORHOOD.md, Section1: genuine h13 F with E407/E408, alpha<=5, omega<=11, delta(F)=13.
- front_end/E408_Q33_CORE_ALMOST_REGULAR_NORMAL_FORM.md: explicit E408/q33 identity; its old retained minimum-degree gate is replaced here.
- front_end/T61_H13_V11_SOURCE_AUDIT.md: Q31/Q32/Q33 labels refer to maximum regular-pivot charge; its retained-seed closures are not imported.
- global ROOT_DEPENDENCY_DAG.md: read for scope only, not proof of any parent property.

E407 V12 head0b48d1f768e3d3c1d3137e0c3ec12f1ff618bb91:
E407_PARENT_PROMOTION_THEOREM.md specifies a61-point E407 residual, delta>=13, alpha<=5, omega<=11, all hereditary caps and maximum regular-pivot charge32. Since 2*407/61<14, delta>=13 here implies actual minimum degree13. A regular pivot exists. Its extra V12/MS-29 hypotheses are not needed by the new transfer.

Q32 head f56cc9eba646e71d63c4b55f468a2340bcdd64c2 and Q33 head bdc2046ea08f12455a37fd412fe2e19514118ada were read for their actual parent mappings and minimum-degree audit. Exact source blob IDs are in SOURCE_MANIFEST.json.

## P0. Actual parent assumptions

Let F be an induced genuine T61 target residual on61 vertices with

    e(F)=E in {407,408}, delta(F)=13,
    alpha(F)<=5, omega(F)<=11,
    e(F[U])<=D(|U|) for every U subset V(F).

The density condition comes from the original balanced12-coloring on the SAME vertices: every other color has independence number at most12 on every subset, hence at least p12(|U|) edges. Unique edge ownership gives e_F(U)<=binom(|U|,2)-11p12(|U|). This is why the minimum-degree gate is legal; edge count alone would not suffice.

Choose a degree13 pivot p. Put A=N_F(p), H=F[V(F) minus (A union {p})]. Thus |A|=13 and |H|=47, independently of any selected witness-support size.

## P1. Charge and the91 baseline

Let M be the missing-edge graph of F[A], z=e(M). For a in A define

    g_a=d_F(a)-13>=0, t_a=|N_F(a) intersect H|.

The actual degree identity is

    13+g_a=1+(12-d_M(a))+t_a,
    t_a=d_M(a)+g_a.

Hence sum_A t_a=2z+sum_A g_a and q_p:=z+sum_A g_a. Partitioning edges into the pivot star, shell interior, shell-core crosscut and core gives

    E=13+(78-z)+(2z+sum_A g_a)+e(H)
     =91+q_p+e(H).

The91 is 13+binom(13,2), not an assumed actual number of removed clique edges. The shell need not be a clique. The formula holds for every regular pivot, not only a maximum-charge pivot.

## P2. Each forbidden-core hypothesis

| Item | E407/q31 | E407/q32 | E408/q32 | E408/q33 |
|---|---|---|---|---|
|pivot degree|13 by selected regular pivot|13|13|13|
|order H|61-14=47|47|47|47|
|edge count E-91-q|285|284|285|284|
|alpha(H)<=4|p is anticomplete to H; an independent5 would extend to6 in F|same argument|same argument|same argument|
|omega(H)<=11|H is induced in F|same|same|same|
|every hereditary cap|H[U]=F[U] for U subset H|same|same|same|
|delta(H)>=12|H in R(4,47), e(H)=285<=286; apply reconstructed Theorem M|284<=286; same theorem|285<=286; same theorem|284<=286; same theorem|
|contradiction|universal low-edge theorem|same|same|same|

Thus every row is fully mapped under P0. There is no support-size or source-profile condition. The minimum-degree proof M is independent of the choice of E or q, and all of its hereditary hypotheses are supplied in each column.

## P3. Maximum charge and all regular pivots

If Q_max is defined as max q_p over degree13 pivots, the set is nonempty because delta(F)=13 and the graph is finite. A parent with Q_max equal to a table charge has a pivot realizing it, so the same contradiction applies. No extra pivot-existence theorem is used for those layers.

More strongly, Theorem M and the low-edge obstruction give e(J)>=286 for every J in R(4,47). Therefore EVERY regular pivot of P0 obeys

    q_p=E-91-e(H)<=E-377.

E407 yields q_p<=30; E408 yields q_p<=31. This excludes all larger charges, including the four requested rows. It does not itself prove that a hypothetical parent must have a larger charge. Any reduction establishing such a lower bound must be audited separately before declaring an entire energy layer empty.

## P4. What remains conditional

P0 is a contextual parent obtained from the original K145 reduction. We have audited its exact interface, not re-certified the whole recurrence, contextual R(4,49) alternative, all low-energy closures or every root coverage edge. The four parent contradictions are PROVED_CONDITIONAL on P0. They do not constitute unconditional EG617(r=12) closure.
