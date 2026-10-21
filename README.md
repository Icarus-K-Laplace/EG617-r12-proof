# EG617 r=12 proof reconstruction

> **STATUS: NOT_CERTIFIED**
>
> This repository tracks the clean-room reconstruction of the `r = 12` case of Erdős Problem 617. The full theorem has **not** been proved yet.

## Current three-line program

- **Line A — Astra A:** eliminate the unique embedded T61 obstruction or extract a legal induced `R(4,49)`.
- **Line B — Astra B:** eliminate `333 <= e(F) <= 340` for legal `R(4,49)` residuals.
- **Line C — central line:** eliminate `E332`, reduced to `q=30` over a 211-edge 35-core.

## Front-end breakthrough and current T61

The broad bridge is already reduced to one outer stop.

**PROVED dichotomy:**

`least-edge colour G -> legitimate induced R(4,49) OR embedded T61`.

The V1 contextual recurrence is **COMPUTATION_CERTIFIED** with 1752 nodes and 144 outer comparisons, replayed by two independent integer implementations.

T61 starts from the exact stop `(d,j,a,n)=(11,6,5,61)` with `397<=E<=408` and `delta in {12,13}`.

New analytic tightening now gives:

- `alpha(R)=5` exactly under contextual no extraction;
- anchor defect `z=0`;
- the anchor closed neighbourhood is a genuine target K12, so seven genuine K12 blocks exist in total;
- simplified outer ledger `E+sigma+g+x6+y6=408`;
- modern generic `R(4,48)` edge floor `>=309`;
- the T61 h12 branch starts at E407;
- a 309-edge 48-core has exact inner `q=20, H35=211` and missing shell `K_{2,r}+isolates`, `6<=r<=10`;
- its two 10-vertex centre rows overlap in at least seven vertices of the 211-core.

These results are in `front_end/T61_NEW_LEMMAS.md`.

## Backend assets

- Exact degree-13 pivot bookkeeping and shell charge identities.
- `CORE211`: `H in R(3,35) => e(H)>=211`.
- q28 profitable repivot.
- Generic q29 good-repivot: q29 + inherited `delta(H)>=12` gives a degree-13 pivot with `q_y>=30`; this does **not** require `e(H)=211`.
- E329, E330, E331 closed in the reconstructed DAG.
- E332 reduces to `(q,e(H))=(30,211)`.
- Equality CORE211 degree multisets: `14,12^34` or `13^2,12^33`.

## Local front-end assets

- Matching-transversal rigidity and equality rotation.
- Eight genuine K12 blocks imply a legal R449.
- S31 strict descent only under its explicit E406/delta13 parent contract.
- S30 `(5,7,8,8)` singleton-triangle labelled branch closed; additional scalar saturation lemmas leave 14 k0 and 13 k1 necessary scalar cases.

## Main blockers

1. **Line A:** finish tightened T61, preferably h12 first and then h13 low-excess layers.
2. **Line C:** eliminate E332 q30+211.
3. **Line B:** eliminate E333–E340 with a uniform stability theorem.

Historical CLOSED/UNSAT labels are never accepted without exact assumptions and proof provenance.

Start with `RESEARCH_INDEX.md`, then `CANONICAL_STATE.md`, `PROOF_DAG.md`, `ASSET_LEDGER.md`, and `OPEN_FRONTIERS.md`.
