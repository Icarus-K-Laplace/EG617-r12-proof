# Canonical proof dependency chain — fixed r=12

**Target:** prove that no 12-edge-coloring of (K_{145}) makes every 13-vertex set contain all 12 colors.

Frozen source: integrated proof commit `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`. Independent certification: `09a88cc4fe1e2cf1f3a87475d6484f681910b23e`.

## Dependency overview

```text
Hypothetical 12-coloring of K145
        |
        v
Induced color caps + least-edge color graph
        |
        +--> contextual R(4,49) is impossible in the original full-color setting
        |
        v
Exact extraction / packing / charge ledger
        |
        v
Finite recurrence: 1,752 nodes, 144 outer stops
        |
        v
Unique residual T61, 397 <= E <= 408
        |
        +--> delta=12: R(4,48) floor 310 + q20 inserted-hub contradiction
        |
        +--> delta=13:
                |
                +--> every 47-core has at least 287 edges
                |
                +--> energy-independent COVER gives Q >= 29
                |
                +--> E=407: COVER gives Q >= 30, core gives Q <= 29
                |
                +--> E=408: COVER gives Q >= 31, core gives Q <= 30
        |
        v
All T61 alternatives excluded
        |
        v
Contradiction to the original K145 coloring
```

## Load-bearing theorem interfaces

- **Contextual (R(4,49)) exclusion:** applies only inside the original balanced full-coloring context. It is not promoted to the generic uncolored Ramsey–Turán problem.
- **47-point low-edge theorem:** exact hypotheses and proof are in the frozen low-edge package; the resulting (R(4,47)) floor is 287.
- **286-edge equality:** separate equality classification with shared-excess and support-intersection accounting.
- **48-point floor:** the h12 argument uses its own 48-point minimum-degree gate and 310-edge lower bound; it is not inferred from the 47-point result.
- **COVER:** the Q29 general bound and E407/E408 promotions apply under the stated 61-point hereditary contract.
- **Recurrence:** the finite table is accompanied by analytic rule/completeness derivations; its replay is computational evidence, not a substitute for those derivations.

## Machine-readable dependency objects

- `r12_master/workstreams/astra-global-root-integration-chat-20261031/PROOF_DAG.json`
- `r12_master/workstreams/astra-global-root-integration-chat-20261031/GLOBAL_PROOF_DEPENDENCY_DAG.md`
- `r12_master/workstreams/r12-final-certification-chat-20261031/CANONICAL_PROOF_DAG.json`

The independent certification report records 58 obligations and checks both the source 25-node DAG and its independently reconstructed dependency graph.

## Scope boundary

The abstract uncolored high-energy (R(4,49)) layers E333–E340 and the general-(r) problem are not proved by this dependency chain and are not required by it. Lean formalization and external human peer review remain future work.
