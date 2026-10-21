# Proof completeness audit

Updated: 2026-10-22

## Executive conclusion

The repository is currently a **complete canonical research-state repository**, but it is **not yet a fully self-contained proof manuscript** from which an external mathematician can verify every accepted theorem without consulting prior source bundles.

Current canonical frontier, statuses, recent proofs, open obligations, and machine-readable theorem registry are synchronized. However, several older foundational assets are still represented only by theorem statements or proof sketches rather than full clean-room proofs.

Therefore two different notions of completeness must be kept separate:

- **state completeness**: current research progress and open/closed status are synchronized in this repository — YES;
- **proof-body completeness**: every theorem needed by the current DAG has a standalone, line-by-line proof or replayable certificate in this repository — NOT YET.

## Fully represented current research assets

The following recent assets have standalone proof bodies or replayable certificates in the repository:

- front-end dichotomy `K145 -> induced R(4,49) OR T61` and its assumption/dependency ledgers;
- contextual front-end recurrence certificate (1752 nodes / 144 outer comparisons);
- generic `R(4,48) >= 310` proof;
- complete T61 minimum-degree-12 closure;
- T61 E397–E400 closures, including q23/q24/q25 shell arguments;
- E332 reduction to q30 + 211-core;
- E332 d10 equality branch closure;
- E332 d3 equality branch closure;
- E332 extreme-degree shell reduction and current G=4..8 frontier;
- current human-readable and machine-readable state/open-frontier registries.

## Foundational proof bodies that remain incomplete inside GitHub

### 1. CORE211

`backend/CORE211.md` currently records the theorem and equality degree sequences, but not the full clean proof.

A self-contained version still needs to include:

- the derivation of `delta(H)>=12` for `H in R(3,35)`;
- the contradiction for `e(H)=210`;
- the complement formulation;
- the exact use and citation of the Andrasfai-Erdos-Sos theorem;
- the equality-degree conclusion for `e(H)=211`.

Until this is expanded, an external reader cannot verify CORE211 from this repository alone.

### 2. q28 / q29 repivot theorem

`backend/Q28_Q29_REPIVOT.md` contains the identities and theorem statement, but the full structural case analysis proving existence of a good q29 repivot is summarized rather than written out.

A complete proof needs the three branches:

- missing graph contains K4;
- triangle-free missing graph;
- triangle but no K4;

with all shell inequalities and equality exclusions explicit.

### 3. uniform q27 contradiction

The canonical state currently treats the q27 Type-I/Type-II contradiction as an audited dependency, but there is no standalone complete proof file reconstructing both equality families and the repivot row-class contradiction.

This is a major proof-completeness gap because the low backend closures depend on it.

### 4. E329/E330/E331 low-backend closure chain

The status is synchronized, but there is no single standalone manuscript-quality file that derives every allowed `(q,e(H))` pair and closes all three layers from q27/q28/q29 plus CORE211.

### 5. Some front-end inherited lower-order lemmas

The modern front-end bridge files contain exact assumptions and the certified recurrence, but several lower-order Ramsey/density facts are currently treated as inherited audited inputs rather than re-proved in GitHub.

For publication-level self containment, each such input must either:

- have a complete proof/certificate in this repository; or
- have an explicit bibliographic citation and a statement showing exactly how it is used.

### 6. External theorem provenance

External results such as Andrasfai-Erdos-Sos need bibliographic metadata in a dedicated references/dependencies file. At present the mathematical role is known but the repository is not yet publication-grade bibliographically self-contained.

## Raw source bundles not mirrored

The large Integration 1/2 PDFs, A-J archive, and historical ZIP bundles are not mirrored wholesale into GitHub. Their accepted current mathematical content has been reconstructed into canonical files, but they remain necessary provenance for some older proof bodies until the gaps above are rewritten fully.

## Machine readability

`machine/CANONICAL_STATE.json`, `machine/THEOREM_REGISTRY.json`, and `machine/OPEN_FRONTIERS.json` make the current theorem state machine-readable. This is sufficient for a model to identify the active frontier and theorem statuses, but not by itself sufficient to verify every proof.

The theorem registry should point every PROVED theorem to a standalone proof file rather than to a state summary wherever possible.

## Certification target for repository completeness

The repository may be called **self-contained-proof complete** only when all of the following hold:

1. every `PROVED` theorem in `machine/THEOREM_REGISTRY.json` has a standalone proof source;
2. every `COMPUTATION_CERTIFIED` theorem has a replayable verifier and immutable certificate data;
3. every external result has exact citation and scope;
4. the complete main DAG can be followed from the original K145 hypothesis to the current open leaves without consulting Integration PDFs or chat history;
5. a fresh reader can reconstruct all notation and every theorem dependency from repository files alone.

Current verdict: `STATE_COMPLETE / PROOF_BODY_INCOMPLETE`.
