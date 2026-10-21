# E-version q27 analytic classification audit

Status: `RECOVERY_AUDIT`.

## Main finding

The E-version materially improves the provenance of the q=27 shell classification. It does not merely list the two finite survivors. It gives an analytic reduction, conditional on the inherited shell floor/axioms, from q=27 to exactly

- `K_{3,8} + 2K_1`,
- `K_{3,9} + K_1`.

This means the remaining q27 proof-completeness gap is smaller than previously recorded: the whole topology classification need not remain a black-box computation, but the lower inherited input `z=e(M)>=22` and the precise standard shell axioms must still be independently licensed/recovered.

## Recovered argument skeleton

Assume the corrected 13-vertex degree-13 shell semantics

`q = z + sum g_v`,  `t_v=d_M(v)+g_v`,  `g_v>=0`,

with missing-edge inequality

`t_u+t_v>=12` for `uv in E(M)`,

and inherited constraints including `z>=22`, `alpha(M)<=10`, no `K5`, triangle charge `t(T)>=24`, and K4 charge `t(Q)>=35`.

### K4 branch

If `Q=K4 subset M`, then writing `e0` for outside-outside missing edges gives the lower bound `q>=29+e0`, hence q=27 is impossible.

### Triangle but no K4

Write a missing triangle `T`, let `e0` be the number of outside-outside missing edges and `e1` the triangle-to-outside missing edges, so `z=3+e1+e0`.
Triangle charge yields a triangle-excess lower bound. The E-version combines this with missing-edge inequalities on the outside graph to obtain q>=28 whenever `1<=e0<=7`, q>=29 when `e0>=8`, and a separate attachment-boundary check for `e0=0`. Hence q=27 has no triangle survivor.

The `e0=0` boundary still deserves a clean standalone rewrite because the historical text invokes a finite attachment enumeration.

### Triangle-free branch

The E-version shows:

1. matching number cannot be <=2 (bipartite/Konig would force an independent 11-set; the non-bipartite odd-cycle alternative is too sparse for the inherited edge floor);
2. four disjoint missing edges are impossible: for their 8 endpoints `X`, edge tightness gives `t(X)>=48`, hence `e(M[X])>=48-q=21`, contradicting Mantel on 8 triangle-free vertices (`e<=16`);
3. therefore `nu(M)=3`;
4. in the bipartite case, Konig gives a 3-vertex cover `C`; combining the cover/matching-partner degree sum with three matching-edge inequalities forces q>=27 with equality only in the two complete bipartite equality shapes `K3,8+2K1` and `K3,9+K1`.

The non-bipartite triangle-free subcase is stated to collapse to a short odd-cycle sparse family; this step should be rewritten explicitly before promotion to standalone `PROVED`.

## Relationship to A/B recovery

- B pp.581-583 supplies analytic decoration uniqueness for the two equality topologies.
- A supplies the analytic Type-I/Type-II repivot contradictions.
- E supplies most of the topology-classification proof body.

Thus q27 is now close to fully self-contained. The remaining obligations are:

1. recover/prove the inherited `z>=22` shell floor in the exact q27 regime;
2. rewrite the triangle `e0=0` attachment boundary without relying on opaque historical enumeration, or store a replayable certificate;
3. write the non-bipartite triangle-free `nu=3` exclusion explicitly;
4. verify the repivot licensing condition used by the A-version closure.

Until those are discharged, keep the complete q27 theorem as `PROVED_ANALYTIC_WITH_DEPENDENCIES`, not unconditional standalone `PROVED`.
