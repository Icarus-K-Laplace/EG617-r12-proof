# Proof completeness audit

Updated: 2026-10-22

## Executive conclusion

The repository is a **complete canonical research-state repository**, but it is still **not yet a fully self-contained proof manuscript** from which an external mathematician can verify every accepted theorem without consulting any lower-order source/certificate.

Two notions remain separate:

- **state completeness**: current research progress and open/closed status are synchronized — YES;
- **proof-body completeness**: every theorem needed by the current DAG has a standalone proof or replayable certificate — NOT YET.

## Fully represented current research assets

Standalone proof bodies or replayable certificates now include:

- front-end dichotomy `K145 -> induced R(4,49) OR T61`;
- contextual recurrence certificate;
- `R(4,48)>=310` and complete T61 h12 closure;
- T61 E397--E400 closures, including q23/q24/q25 shell arguments;
- generic q29 good-repivot theorem with its three structural branches;
- standalone E329/E330/E331 closure chain and E332 reduction to q30+211;
- E332 d10 and d3 branch closures;
- E332 extreme-degree reduction;
- current human- and machine-readable state registries.

## Remaining foundational gaps

### 1. CORE211 lower-order minimum-degree dependency

Integration 1 recovers the clean 210-edge contradiction completely: once `delta(H)>=12`, a hypothetical 210-edge core is 12-regular; its complement is 22-regular, K4-free, and AES forces a 3-partition with an independent set of size at least12, contradiction.

The remaining self-containment gap is narrower: the repository still needs the full standalone proof/certificate for the inherited 23-neighbourhood / cap-two argument that yields `delta(H)>=12` for every `H in R(3,35)`.

See `consolidation/INTEGRATED1_CORE211_AUDIT.md`.

### 2. q27 equality closure

The analytic body is recovered:

- E-version analytic topology reduction;
- B-version decoration uniqueness;
- A-version Type-I/II repivot contradiction.

The remaining dependency is the exact lower-order/topology certificate or complete analytic derivation licensing the two equality topologies

- `K3,8+2K1`;
- `K3,9+K1`.

### 3. Front-end inherited lower-order lemmas

The modern bridge and T61 proof files expose their assumptions, but several lower-order Ramsey/density facts are still inherited audited inputs. Publication-level self containment requires each such input to have either a proof/certificate or an exact citation.

### 4. External theorem provenance

Results such as Andrasfai--Erdos--Sos still need publication-grade bibliographic metadata and precise scope in a dedicated references/dependencies file.

## Gaps resolved by Integration 1 recovery

The following former proof-body gaps are no longer listed as missing:

- **generic q29 good-repivot**: reconstructed as `backend/Q29_GOOD_REPIVOT_FULL_PROOF.md`;
- **E329/E330/E331 low-backend chain**: reconstructed as `backend/E329_E332_CLOSURE.md`.

Integration 1 also independently matches the modern T61 E397--E400/q23--q25 ladder, but current front-end files remain the canonical proofs because they are cleaner and use the final notation/contracts.

## Raw source bundles

The large Integration 1/2 PDFs and A--J archive are not mirrored wholesale into GitHub. Accepted content is reconstructed into canonical/consolidation files. Source mapping is recorded under `history/`.

## Certification target

The repository may be called **self-contained-proof complete** only when:

1. every `PROVED` theorem in `machine/THEOREM_REGISTRY.json` points to a standalone proof source;
2. every `COMPUTATION_CERTIFIED` theorem has replayable verifier/data;
3. every external theorem has exact citation/scope;
4. the main DAG can be followed without historical PDFs/chat;
5. all notation and dependencies are reconstructible from repository files alone.

Current verdict: `STATE_COMPLETE / PROOF_BODY_INCOMPLETE`, with the remaining foundational gap set substantially narrower than before Integration 1 recovery.
