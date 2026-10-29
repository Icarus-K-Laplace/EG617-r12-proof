# E408 Q32 full-support vertex-labelled CSP

Date: 2026-10-29  
Status: **FORMULATION ADDED; NOT SOLVED.** No SAT, UNSAT, or Q32 closure claim is made.

## Scope

This workstream models the actual 61-vertex, 12-color source contract for the live E408/Q32 full-support terminal. It covers m=8,9,10 and every source placement admitted by the registered Type-I factorization. The separate command-line option --aligned-z01 adds the six common-P track-pair factorizations and partial projection packing for the proved aligned m=10, z in {0,1} subcase.

Files:

- q32_fullsupport_vertex_labelled_csp.py: Z3 exact model plus lazy, valid independence-set cuts.
- verify_q32_fullsupport_candidate.py: independent source/edge/degree/alpha verifier.
- Candidate JSON, SMT-LIB model, and solver proof output are written only to a caller-selected run directory; they are not checked into the proof archive unless inspected first.

## Exact model

Vertices are labelled 0,...,60; H={0,...,46}, O={47,...,60}, pivot p=47, and A={48,...,60}. Color 0 is the target color; exact-129 colors are relabelled 1,...,m.

For every unordered pair uv, integer c_uv in {0,...,11} assigns its unique color. For every exact color C, variables label its special point x_C, distinguished point y_C, the twelve disjoint K5 factors F_C,0,...,F_C,11, and the nonempty proper subset A_0,C contained in F_C,10. Factors 0–9 are the ten isolated factors; 10 and 11 are N_s,N_t. The source edge predicate is exactly

E_C = union_k binom(F_C,k,2)
      union {y_C a : a in A_0,C}
      union {x_C a : a in N_s minus A_0,C}
      union {x_C b : b in N_t minus {y_C}}.

The model enforces E_C = {uv : c_uv=C}, not just the number of edges in each factor. Thus different exact colors cannot share an edge, and the actual endpoint labels are global across all colors.

## Source-mode coverage correction

A previous draft overconstrained the source by forcing all four surplus outside vertices of G_11 into the two special K5s. That is not valid: excess outside vertices can belong to isolated factors, including an isolated-double mode that leaves an 8-vertex H-intersection with G_11. The model now uses the source-correct conditions:

- each of the twelve K5 factors meets O;
- the twelve factors contain 13 vertices of O when x_C is in O, and all 14 when x_C is in H;
- the implied profiles are (2,1^11) for x_C in O, and either (2,2,1^10) or (3,1^11) for x_C in H;
- no extra condition forces the surplus outside vertices to lie in N_s,N_t.

The full-support check is also source-corrected: each h in H must occur in at least one exact-color K5 factor with exactly one O-vertex, including a special N_s or N_t factor if that is the witness. It does not incorrectly restrict coverage to factor indices 0–9.

## Global constraints

1. Every edge has exactly one color and the registered per-color edge counts are imposed: e_0=398+m, e_C=129 for exact colors, e_C=130 for colors m+1,...,10, and e_11=132.
2. All 13 edges pA have color 0.
3. The target core satisfies e(H)=285, delta(H)>=12, and sum over h in H of (d_H(h)-12)=6.
4. The eleven non-target colors satisfy the exact 37-unit identity sum_C(e_C(H)-69)=37; each has at least 69 core edges and each exact color has at most 75.
5. Full support: every vertex of H belongs to some source K5 factor with exactly one O-vertex, giving a core K4 witness.
6. The original balanced-coloring premise is encoded exactly by alpha(H)<=4 and alpha(G_C)<=12 for all twelve colors. Since these are exponential set constraints, the solver uses lazy separation: any found independent 5-set in H, or independent 13-set in a color graph, adds the valid clause that at least one pair in that set has the corresponding color. Every accepted SAT candidate is checked again by the independent verifier.

The all-color pointwise reserve quota is not hard-coded as a premise. The current reserve note's 13+4m+q_z+L_m count is not independently re-derived inside this solver's trusted core; using the complete coloring constraints is safer than silently importing an unverified strengthening. This does not retract the reserve note; it marks that dependency for independent proof audit.

## Aligned m=10, z=0,1 common-P submodel

With --aligned-z01, the model additionally fixes T_0 as a target K_11 and T_1,T_2,T_3 as target K_12 tracks, with residual counts (1,2,2,2) and z<=1 target edges between residual vertices in distinct tracks. It explicitly labels the six pair factors P_ij and the eleven selected color matchings M_C,ij on each pair:

- K_12 x K_12 = P_ij disjoint-union over C of M_C,ij, with each M_C and P a perfect matching;
- K_11 x K_12 = P_0i disjoint-union over C of M_C,0i, where each M_C saturates T_0 and P_0i has degree one on T_0, without asserting a matching on the K_12 side;
- every isolated-factor color edge is selected into its color matching; selected matchings preserve the G_11/non-gadget split, and any color-C edge left in P must have both endpoints in G_11;
- each exact color has at most one color-C edge in the union of the three P_0i;
- pair-projection multiplicity is at most one when its K_2,2 block meets P_ij, at most two otherwise; two colors share at most one large-track pair projection.

The aligned submodel allows G_11 to have one or two vertices in T_0, while retaining two in each K_12 track. This preserves both the 7-vertex gadget-residual mode and the legitimate 8-vertex isolated-double mode rather than silently assuming only the former.

## Verification protocol and limitations

Run the independent verifier self-test, then a bounded solver smoke test. The bounded test is not a proof attempt.

    python verify_q32_fullsupport_candidate.py --self-test
    python q32_fullsupport_vertex_labelled_csp.py --m 10 --aligned-z01 --max-iterations 1 --out-dir /tmp/q32-smoke

For a real run, use separate output directories for m=8,9,10, retain the final SMT-LIB file, and independently replay any exported UNSAT proof with a pinned Z3 version. A solver result alone is not accepted:

- SAT requires a full candidate JSON that passes the independent verifier, including all 12 alpha constraints.
- UNSAT requires the exact model plus exported proof artifact and independent replay.
- timeout/unknown leaves the relevant branch OPEN.

No full solver run or UNSAT proof is claimed by this commit. E408/Q32 remains **OPEN / NOT_CERTIFIED**.


## Explicit pivot-packing strengthening

The generic model also encodes the exact K4-packing slack frontier. Let Q be the union of the m disjoint pivot blocks and R=H\\Q, n=47-4m. Define

- x = e_H(Q)-4 binom(m,2),
- y = e_H(Q,R)-mn,
- z = e_H(R)-p_4(n), with p_4(15)=21, p_4(11)=10, p_4(7)=3.

The model enforces x,y,z>=0, x+y+z=32, 2x+y>=5m, y+2z>=D_m for D_8=18, D_9=13, D_10=8, and the exact excess split
(2x+y-5m)+(y+2z-D_m)=6. It also explicitly enforces at least four H-edges between every pair of pivot K4 blocks and at least one H-neighbor from every residual vertex into every pivot block. These are necessary consequences of alpha(H)<=4 and the six-unit degree-excess contract; they strengthen the search but are not sufficient for closure.


## Execution-blocker and source-mode audit (2026-10-29)

A source-level audit found two real implementation issues before any full solver run:

1. The CSP attempted symbolic indexing of a Python dictionary with a Z3 integer. That is not a valid symbolic array lookup and would raise a Python KeyError during model construction. It is now encoded as a finite disjunction over vertex labels, enforcing that the selected y vertex has component label 11.
2. The candidate verifier incorrectly forced all ten isolated K5 factors to contain exactly one outside vertex. This contradicts the generic source-correct model, which permits the excess outside points to occur in isolated factors (including isolated-double modes, and triple placements in the x-in-H profile where otherwise allowed). The verifier now checks the full aggregate outside-count profile and the per-factor caps without that overconstraint.

These are formulation/verifier repairs, not a mathematical closure. The full model has not been executed because the current chat runtime lacks Z3 and cannot directly fetch the committed source into the local shell; no SAT/UNSAT result is claimed.


### Source-profile regression tests

The independent candidate verifier has explicit source-profile regression tests for isolated-double and isolated-triple occupancy patterns in the generic model, while retaining the aggregate outside-count and per-factor-cap checks. These tests protect against accidentally constraining the generic source mode to the aligned subcase.


### Independent verifier malformed-input guard (2026-10-29)

The verifier now returns immediately on a malformed K5 factor list instead of continuing into pivot-packing checks that require a populated component map. A self-test constructs a malformed source witness and checks for a normal validation error rather than an exception. This hardens the independent checker against corrupted candidate files; it does not change the mathematical model.
