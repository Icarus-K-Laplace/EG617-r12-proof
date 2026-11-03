# Root verifier execution-scope audit

Date: 2026-11-03  
Source: `r12_master/workstreams/astra-global-root-integration-chat-20261031/INDEPENDENT_VERIFIER.py`, blob `b3b304789dfe08a0bf3b54478f9c3cbfdc5c5e26`.

## Function-by-function scope

| Function | What it actually checks | What it does not establish |
|---|---|---|
| `verify_sources` | Recomputes Git blob identities for files listed in `SOURCE_MANIFEST.json`. | It does not prove the mathematical statements in those files. |
| `verify_frontend` | Runs the third recurrence transcription and compares it with the two frozen implementations at all 1,752 nodes; checks all144 outer stops and the unique survivor; writes `FRONTEND_REPLAY.json`. | It does not re-prove the analytic recurrence inequalities; those are in the Markdown proof. |
| `verify_cover_retained` | Checks the source hash of the retained COVER verifier, its 2/8 canonical states, direct checks of those retained states, 81,920 subset identities, 104 repivot identities, and arithmetic. | It explicitly reports `shell_search_rerun=False`; it does not rerun the full COVER row-count enumeration or call the bipartite reconstruction routine. |
| `verify_new_arithmetic` | Checks contextual49 arithmetic, the 310/407/408 energy sums, Q20 family arithmetic, support-orbit counts, and shared-excess scalar inequalities. | It does not execute the E286 verifier or independently prove the support-to-graph reductions. |
| `verify_lower_order_families` | Imports the frozen low verifier and calls its type classification, 23-point neighborhood-cost checks, and minimum-degree arithmetic. | It does not replace the analytic M1–M6 derivation; the separate M2b extension replay is not invoked by this root function. |
| `verify_dag` | DFS-checks that every node's declared parents exist and that the declared graph is acyclic. | It does not check that the DAG contains every load-bearing theorem or every source dependency. Thus an acyclic 25-node DAG can still be incomplete. |

## Reproducibility conclusion

The root verifier is a finite arithmetic/provenance verifier, not a formal proof checker. Its saved `VERIFICATION_RESULT.json` is a prior run output. In this audit session the root script has been inspected, but it has **not** been executed from a fresh checkout. Component-level recurrence, lower-order, COVER, and E286 replays recorded elsewhere in this audit branch do not change that exact execution boundary.

For a clean-room run, the package should be freshly checked out at the frozen integration commit, all Python sources executed with the documented interpreter, outputs regenerated, and the regenerated hashes/results compared. The report must preserve the table above rather than summarize the result as “the verifier re-proves the complete theorem.”
