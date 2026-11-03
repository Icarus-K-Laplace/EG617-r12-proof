# Independent EG617(r=12) audit status

Date: 2026-11-02
Frozen Astra integration snapshot: `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`
Audit branch: `workstream/r12-astra-independent-audit-20261102`

## Findings this round

1. **Finite recurrence replay:** two independently transcribed integer implementations agree at 1,752 nodes, with zero mismatches. All 144 extraction stops were checked; the unique survivor is ((d,j,a,n)=(11,6,5,61)), with bound397 and budget408. See `RECHECK_FRONTEND.py/json`.
2. **Lower-order finite checks:** the M2 type quotient and M3 23-vertex blowup representatives were independently rechecked; 20 compatible type-set pairs, 10 missing-cross-edge cases, and 61 representatives (49 valid, 12 excluded) were obtained. See `RECHECK_LOWER_M2_M3.py/json`.
3. **E286 finite checks:** support orbit counts 2,3,5 and scalar minima were reproduced. See `RECHECK_E286_SUPPORTS.py/json`.
4. **E286 D support:** a previously implicit zero-completer case has been filled by a scalar-charge argument. The proof is recorded separately in `E286_D_SUPPORT_REPAIR.md`. Together with the original sections 3–12, this closes the ten listed support orbits at the analytic-reading level. No counterexample was found. This repair is not Lean-formalized.
5. **Shared-leaf accounting:** the original baseline sentence is imprecise for a vertex missing exactly one point, but the intended inequality is valid. A corrected pointwise derivation is in `AUDIT_NOTES.md`.
6. **COVER beta=12:** the possible circularity in Section9 is resolved. Formula (3) needs the parent core minimum degree12 only; formula (4) needs the repivoted core minimum degree12. The text licenses these at the relevant uses.
7. **h13 COVER q30:** a line-by-line reading of the q30 Family I/II reduction and eliminations found no additional concrete counterexample in this pass. The analytic arguments still require formal/independent peer verification.

## Root-package issues still open

- The 25-node `PROOF_DAG.json` is acyclic and its parent references resolve, but it omits explicit nodes for ledger entries `GATE47` and `D48`. A corrected proposal is in `PROOF_DAG_CORRECTED_PROPOSAL.json`; the frozen integration branch was not modified.
- The Q32 25-point common-neighborhood bound cites SECOND_TURAN in one source, while a self-contained shortest-odd-cycle/Mantel proof is also vendored. The integration source map must identify which route is actually invoked.
- External leaves BROOKS, TURAN, AES, and SECOND_TURAN need exact statement/hypothesis entries in the final theorem ledger.
- No Lean kernel certification of the original K145 theorem is established by this audit. No full clean-room CI run of the integration commit was reported.

## Certification posture

The finite arithmetic and the specific local repairs recorded here have passed this audit session. The K145 proof is **not certified by this report as a whole**: dependency-ledger closure, clean-room build, proof-assistant status, and further independent analytic review remain separate requirements. The global integration branch and all sibling workstreams were left unchanged.


## New h12 audit result (2026-11-02)

The dedicated h12 chain and the (R(4,48)) floor310 proof have now received a separate analytic audit. No counterexample or load-bearing gap was found. The q=20 equality structure was rechecked by enumerating 65,536 attachment patterns and 7,006,595 decoration allocations after the analytic C4/one-side-attachment reduction; 163 labeled configurations survive and all are (K_{2,r}\sqcup(10-r)K_1), (6\le r\le10). See `H12_INDEPENDENT_AUDIT.md` and `RECHECK_H12_Q20.json`.

A further DAG omission was found and corrected in the proposal: `Q20_CLASSIFICATION` depends on `LOWER_ORDER) because the pair-row inequality uses (R(2,24)=\varnothing). The corrected 27-node proposal has all parent references resolved and is acyclic. The frozen integration DAG remains unchanged.


## Further proof-DAG audit (2026-11-02)

The source-to-DAG crosswalk found another missing shared dependency: the h=13/h=14 shell matching lower bounds used by the frontend recurrence, and the h=13 lemma used by COVER q≥29. The q20 shell classification also uses the h=12 two-matching case. The corrected proposal now adds `SHELL_MATCHING_BOUNDS` and links it to `Q20_CLASSIFICATION`, `COVER_Q29_GENERAL`, and `RECURRENCE`.

The corrected proposal now has 28 nodes; a fresh DFS confirmed all parent references resolve and the graph is acyclic. This remains a proposal only: the frozen Astra integration DAG was not edited.


## E286 center-charge recheck (2026-11-02)

The formula (4) charge for two mixed points sharing a K9 and the three-point K10-star center accounting were expanded into explicit pointwise degree arguments in `E286_CENTER_CHARGE_AUDIT.md`. Both are additive under overlapping missing sets; no counterexample was found. The D-support case is already closed by the frozen Section9 pointwise inequality; the separate `E286_D_SUPPORT_REPAIR.md` is redundant. This is an analytic-reading result, not a Lean formalization.


## h13 q29/q30 audit update (2026-11-02)

The dedicated h13 audit found no concrete counterexample or fatal inequality defect in the q29/q30 chain. The d=10 branch and the |X|=2 K4-minus-edge branch have been expanded with explicit degree/charge derivations. The Family I row-triangle anticompleteness and Family II ten-pair independent-set arguments were rederived with all K-neighbor deletions counted. See `H13_Q29_Q30_INDEPENDENT_AUDIT.md`.

The arithmetic checker `RECHECK_H13_Q30_ARITHMETIC.py` passed. It is a finite arithmetic/structure check, not a formal proof of the analytic lemmas. The frozen integration theorem was not edited; all audit artifacts remain on this isolated branch.


## Frontend recurrence update (2026-11-02)

A third independent integer implementation exactly reproduces all 1,752 recurrence nodes, 13 maximum-order entries, 144 outer stops, and 61 T61 rows in the frozen replay. The unique survivor remains (d,j,a,n)=(11,6,5,61), 397<=e(F)<=408. See `FRONTEND_RECURRENCE_INDEPENDENT_AUDIT.md`, `RECHECK_FRONTEND_THIRD.js`, and `FRONTEND_THIRD_REPLAY_RESULT.json`.

The h=13 König-cover prose has a harmless one-edge overstatement (mixed cover at most13 rather than12 cross edges); the corrected total remains19<22, so the proof conclusion is unchanged. No frozen integration file was edited.


## Audit-note correction (2026-11-02)

The earlier note claiming an E286 Section2 minimum of302 was based on accidentally dropping the explicit (+8) in the frozen expression (p_3(47-q)+12q+8-\binom q2). The exact frozen text is correct and its minimum is310. That earlier typo allegation is withdrawn; no E286 correction is required for this inequality. See the correction and exact blob identity in `AUDIT_NOTES.md`.


## Frozen-source provenance update (2026-11-02)

All 26 entries of the integration `SOURCE_MANIFEST.json` match both (i) the destination Git blobs in the frozen integration snapshot and (ii) the source Git blobs at their declared commits. Zero mismatches. See `SOURCE_MANIFEST_AUDIT.json`.

A full clean-room run of the root `INDEPENDENT_VERIFIER.py` and independent recomputation of the package SHA256SUMS remain uncompleted in this audit session; the recurrence has been separately reimplemented and compared exactly.


## Dependency closure update (2026-11-02)

The corrected 28-node proposal is acyclic, every parent reference resolves, and a traversal from `K145_EMPTY` reaches all28 nodes. Q32/Q33 are intentionally omitted because LOW285 supplies the needed floor; GEN49 is intentionally outside the contextual K145 proof. The elementary shortest-odd-cycle/Mantel route supplies the 25-point bound for LOW285, so SECOND_TURAN is needed only for CONTEXTUAL49_EMPTY. See `DAG_COMPLETENESS_AUDIT.md`.


## Frozen package byte-integrity update (2026-11-02)

Independently recomputed SHA-256 from base64-decoded GitHub file bytes for all47 entries in the frozen integration root `SHA256SUMS.txt`: 47/47 exact matches, zero mismatches. The standard `abc` SHA-256 test vector passed. The 26-entry top-level `SOURCE_MANIFEST.json` source/destination Git blob audit also remains 26/26. See `PACKAGE_HASH_AND_VERIFIER_SCOPE_AUDIT.md`.

Important execution boundary: the root `INDEPENDENT_VERIFIER.py` has not been run from a clean local checkout in this session. Its saved `VERIFICATION_RESULT.json` is a prior output. Code inspection also confirms that the root verifier checks retained COVER states directly but does not rerun `reconstruct_bipartite`; it does not execute the E286 verifier. Nested COVER/E286 checksum manifests reference source-workstream files not vendored into the frozen integration directory (4/11 COVER entries and 11/14 E286 entries are absent there). These are packaging/scope limitations, not failures of the 47-entry root checksum list.


### Nested source-workstream checksum update

The two nested manifests were also verified at their original source commits: COVER 11/11 at `531e41c79e08dd2bb3892ca9ba8a491a56678565`, E286 14/14 at `c3d07b2ca5912b1b0c1c6998303c19c3c2911340`. Thus the unvendored nested files are present and checksum-authenticated in their original source workstreams; only the integration snapshot's selective vendoring is incomplete. Details are in `PACKAGE_HASH_AND_VERIFIER_SCOPE_AUDIT.md`.


## Finite verifier re-execution update (2026-11-02)

The exact byte-matched low-edge verifier source was executed in Python3.13.5; its source SHA-256 matches the frozen root checksum, and every numerical result matches the saved Python3.12.14 output. An independent transcription of the COVER enumerator reproduced all 19,448 row-count vectors for each q, exact counters (q27: 882/32,665/2; q28: 891/51,118/16), the 2/8 canonical states, 81,920 subset checks, and 104 repivot identities. An independent E286 transcription reproduced the saved support/scalar/intersection results, including 139,921 tuples and minimum14. See `FINITE_VERIFIER_REEXECUTION_AUDIT.md`.

The full root integration verifier is still not run from a clean local checkout. The new component-level executions do not change that limitation and do not constitute Lean certification or external peer review.


## Statement and dependency-DAG scope update

The public Problem617 statement is universally quantified over r>=3. The integrated theorem addresses only the fixed r=12 instance, K145/12 colors/13 vertices; it must not be described as solving the full all-r problem. See `STATEMENT_SCOPE_AUDIT.md`.

The frozen 25-node DAG is acyclic but omits explicit intermediate nodes for GATE47, D48 and SHELL_MATCHING_BOUNDS. The 28-node isolated proposal adds these dependencies and is acyclic with every node reachable from K145_EMPTY. The mathematical lemmas are present in the source documents; this is a dependency-map completeness/documentation correction, not an identified missing proof lemma. The root verifier checks acyclicity of the original DAG, not completeness of its edge set.


## External theorem and terminal-interface audit (2026-11-03)

The exact parameter substitutions for Turan, Kang–Pikhurko Theorem1, Andrasfai–Erdos–Sos Theorem1.1, and Brooks were checked. KP's two-regime condition is satisfied at (n,r)=(49,12); it gives the required 79-edge lower bound for each other color. Its (25,2) use gives145, and the low-edge source also supplies an elementary shortest-odd-cycle/Mantel proof of145, so the corrected DAG can designate the elementary route there. AES is applied at s=4,n=35 with22>21.875, exactly as required for CORE211. Brooks is applied only after the least color graph is shown12-regular with no K13 component.

The h12/h13 interfaces were rechecked at their exact orders: the h12 T61 branch uses actual48-cores and D48; h13 uses actual47-cores and GATE47+LOW285+EX286 to obtain287. No transport of the47-point floor to48 points occurs. The K2,2 exterior-attachment step in the h12 q20 classification has been expanded in the new audit file.

See `EXTERNAL_LEAVES_AND_TERMINAL_INTERFACE_AUDIT.md`. No frozen integration or sibling workstream files were changed. The full root clean-room execution, promotion of the corrected DAG, Lean kernel certification, and external referee review remain outstanding.


### Additional support-orbit and scalar-bound replay (2026-11-03)

A fresh independent enumeration of the four-seed support multisets reproduces the E286 orbit counts h=3:2, h=4:3, h=5:5 (ten total). Exact finite evaluation reproduces the scalar minima f11=6 at (2,2), f10,11=4 at (2,3), f9,11=2 at (2,4), f10,10=2 at (3,3), plus the three E286 star/completer minima6,5,5. The E286 independent-four-set lower bounds for q=1..8 are 350,346,342,337,331,325,318,310, all above286. Details are appended to `EXTERNAL_LEAVES_AND_TERMINAL_INTERFACE_AUDIT.md`.


Correction to the K2,2 attachment expansion: triangle-freeness alone forbids one exterior vertex from attaching to both bipartition sides (every cross-side pair is an edge of K2,2). Attachments on both sides must therefore come from distinct exterior vertices; those two attachment edges plus the opposite unused K2,2 edge form a3-matching. The audit file now states this concise correct argument.


## Complete theorem-source crosswalk (2026-11-03)

A node-by-node crosswalk has now been recorded in `THEOREM_SOURCE_CROSSWALK_20261103.md`. It maps all 28 corrected-DAG nodes to exact source files/sections, theorem contracts, parent nodes, and audit dispositions. It also maps the external leaves Brooks, Turan, AES, and Kang–Pikhurko to their local applications; König's lemma is proved inline, and Mantel is included in the Turán/elementary route.

The stale `front_end/T61_H13_LOW_LAYER.md` says E401–E408 remain open, but its last modification is 2026-10-21. It is not included in the frozen integration's SOURCE_MANIFEST and is not a dependency of the corrected DAG. The 2026-10-31 integration package contains later independent COVER Sections1–13 and E407/E408 final certificates. This is stale repository documentation, not a missing premise in the frozen proof; it should be updated or archived before public presentation.

The corrected 28-node proposal has all references resolved, is acyclic, and all nodes are reachable from K145_EMPTY. The original 25-node frozen DAG remains an incomplete dependency map. The corrected proposal treats the original counterexample hypothesis as an implicit input to COLOR_CAPS; a public diagram should label that input explicitly. No new mathematical counterexample or missing implication was identified in this crosswalk pass.


## Withdrawal of the alleged E286 D-support source gap (2026-11-03)

A previous audit pass incorrectly treated formula (5) as requiring an additional vertex completing the K10. The frozen E286 Section9 already proves the more general pointwise clique-vertex inequality, including all zero-missing-set cases:
`epsilon(v) >= max(0, sum(a_opposite-1)) >= sum max(0,a_opposite-2)`.
For K10, there are three support incidences and at most one negative increment (from the K10/K10 point); the two mixed incidences have nonempty opposite K11 missing sets. For K11, there are two incidences and the two-term shared-leaf inequality handles even two zero opposite missing sets.

Summing this pointwise inequality over the cliques yields, for every noncompleting mixed point with positive missing-set sizes a,b, the center charges `a max(0,b-2)+b max(0,a-2)`. Adding its own point excess `max(0,9-a-b)` gives formula (5), whose minimum is5. This is valid without a separate K10-completer. The D-case split in the frozen theorem is therefore exhaustive: if one K10 has two completing mixed points they cost at least7; otherwise at most one per K10 completes, leaving at least two noncompleting mixed points, each costing at least5. Thus T>=10.

The separate `E286_D_SUPPORT_REPAIR.md` proves a stronger completer-existence statement but is redundant. The proposed `E286_SOURCE_PATCH_GUIDE.md` is withdrawn; no E286 source patch is required for this issue. The frozen E286 theorem is self-contained on the D-support case as written. The 287-edge floor and downstream K145 conclusion are not conditional on that proposed repair.

## Correction to earlier h13 matching audit

The earlier claim that COVER Section4's mixed König-cover case should be bounded by13 rather than12 was incorrect. For S of size4 and unmatched I of size9, a cover {s,i} has at most12 incident cross edges if si is present (9+4-1), and at most11 if absent (8+3). The source's bound12 is valid; the previous claimed overcount is withdrawn. See the correction in `H13_Q29_Q30_INDEPENDENT_AUDIT.md`. This is not a proof defect.


## Focused adversarial E286 attack: two completers (2026-11-03)

The suspected joint-cost gap for two points completing the same K10 was attacked directly. The frozen weaker common-neighborhood estimate is valid, and a stronger exclusion follows.

Let u,v both complete a K10. They are nonadjacent (otherwise K12), and c(u,v)>=10. With total excess8, the common antineighborhood U has size 21+c-epsilon(u)-epsilon(v). If epsilon(u)+epsilon(v)<=6, |U|>=25 and the frozen 25-point density lemma contradicts e(W)>=155 versus e(W)<=154.

If the sum is7, |U|>=24 and at most one unit of excess remains outside u,v, so U contains at least23 zero-excess vertices. If the sum is8, |U|>=23 and all other vertices have zero excess. Choose a 23-set W of zero-excess vertices in either case. The complement of H[W] is triangle-free (alpha(H[W])<=2) and has minimum degree at least22-12=10>2*23/5. The triangle-free AES theorem forces it bipartite. Thus H[W] is the union of two cliques, each of order at most11, impossible on23 vertices. Therefore no two vertices can both complete the same K10 under the E286 hypotheses.

This is stronger than the source's used bound epsilon(u)+epsilon(v)>=7; it is an optional strengthening, not a repair required by the frozen proof.

Further focused checks:
- The D-support K10 pointwise inequality was exhaustively checked for a0 in0..10, a1,a2 in1..11 and all eight missing subsets: zero counterexamples. The K11 two-incidence inequality was checked for all a,b in0..10 and all four subsets: zero counterexamples.
- The shared K9 center charge with two K9-completers was checked for all b,b' in1..11 and all three membership types (A-only, A'-only, A cap A'): zero failures.
- Independent support orbit counts remain h=3:2, h=4:3, h=5:5 (10 total).
- Exact scalar minima reproduce f11=6@(2,2), f10,11=4@(2,3), f9,11=2@(2,4), f10,10=2@(3,3), formula(5)=5@(2,2), formula(4)=5 at (2..7,1), formula(3)=6 at (2..8,1).
- Shortest-odd-cycle/Mantel bounds independently reproduce triangle-free nonbipartite maxima n=19:82, n=23:122, n=24:133, n=25:145.

Artifacts:
- `E286_TWO_COMPLETER_ATTACK_20261103.md`
- `E286_TWO_COMPLETER_ATTACK.py`
- `E286_TWO_COMPLETER_ATTACK_RESULTS.json`

Disposition: **NO GAP FOUND** for the two-completer, D-support zero-completer, double-pair equality, and K9 shared-center subclaims. The stronger AES argument uses the triangle-free r=2 case (delta>2n/5); it does not change the frozen proof. This remains a focused sublemma audit, not certification of COVER, the frontend, or the entire K145 proof.


## Focused COVER attack: triangle channel and B1 cross-row argument (2026-11-03)

A near-witness was constructed for the q<=28 triangle single-edge case: a 13-vertex M with T={w,x,y} a triangle, one B-edge ab, N_T(a)={w,x}, N_T(b)={w,y}, seven further B-vertices adjacent to w,y, and one isolated B-vertex. Weights (t_w,t_x,t_y)=(11,3,10), (t_a,t_b)=(9,3), seven row weights2 and one0 give z=22, q=28, alpha(M)=10, omega(M)=3, and every M-edge satisfies EDGE12. This is a genuine near-counterexample to a weaker set of constraints, but it fails the required triangle row-union bound t_a+t_w+t_x>=24 (it equals23).

The two triangle constraints for {a,w,x} and {b,w,y}, together with t_a+t_b=12 and t_w+t_x+t_y=24, force t_w>=12. EDGE12 on xy gives t_x+t_y>=12, hence t_w=12 and t_x=t_b,t_y=t_a. Since t_a,t_b<=9, the eight other B-points can meet only w, giving z<=3+1+4+8=16<22. Thus the source's single-edge elimination is valid; the triangle row-union lemma is essential.

The compressed B1 q28 nonadjacency step was also expanded. If x is a base point of row class i, its shell weight9 gives d_F(x)=c_i+11. For a pivot p_j in any different row class j, x lies in C_{p_j}, and
`d_{C_{p_j}}(x)=d_F(x)-c_i-e_F(x,T_j)=11-e_F(x,T_j)`.
Every actual47-core has minimum degree11, so x is anticomplete to T_j. Applying this with the pivot in y's row class shows base points x,y from two distinct classes are nonadjacent. Taking p in a third class makes both degree11 in the same core C_p, contradicting the deficient-clique lemma. Therefore “nonadjacent by the same formula” is compressed but valid; no B1 gap remains.

A separately written enumerator was committed as `RECHECK_COVER_Q27_Q28_INDEPENDENT.py`; it enumerates all 19,448 row-count vectors, distributes all decorations, and directly checks the necessary shell conditions. It independently reproduces exactly2 q27 and8 q28 canonical states. Across those ten states it checks81,920 subset identities plus EDGE12, Hall, and regular INS11 conditions. Results are in `RECHECK_COVER_Q27_Q28_INDEPENDENT.json`.

Disposition:
- triangle single-edge near-witness: REJECTED by the triangle row-union bound;
- B1 cross-row anticompleteness: PROVED from the 47-core minimum-degree11 lemma;
- q27/q28 finite state classification: INDEPENDENTLY REPRODUCED;
- no fatal or repairable gap found in these attacked COVER subclaims.


## Further q30 adversarial attack: K4 terminal equality chain (2026-11-03)

The q30 no-middle-degree K4 case was expanded and checked. For a K4 S in M, its common antineighborhood in the 47-core is a clique (otherwise S plus two nonadjacent common nonneighbors is an independent6-set in F), hence has size<=11. The four C-neighborhood rows therefore have union>=36 and t(S)>=36. Equation(1) with q=30 and e_M(S)=6 forces t(S)=36, e_M(B)=0 and G_B=0: the other nine vertices B are independent and regular.

A K5 in M is impossible separately: its common antineighborhood in C is empty by alpha(F)<=5, so its five rows cover all47 vertices and equation(1) gives q>=47-10=37. Thus every b in B has at most3 M-neighbors in S. In the no-middle-degree branch, regularity forces d_M(b)<=2. Since z>=22, e(S,B)>=16, so some y in B has degree2. Its two neighbors s1,s2 are adjacent in M. Each t_s<=12 because the complementary triple in S is an M-triangle with row sum>=24. Equation(1) gives rho=31-(t_s1+t_s2)>=7; Formula(3) at beta12 gives q_y>=53-(t_s1+t_s2)>=29. Maximality Q=30 then licenses the new core's minimum degree12 (its edge count is287 or288). Each inserted s_i has degree t_s_i-e_F(s_i,D_y), so t_s_i>=12 and therefore t_s_i=12. The remaining pair in S has weight12, contradicting EDGE13. No hidden K4 gap was found.

The Q30 Family I/II cross-row anticompleteness was also explicitly checked: the pivot for proving x in T_i is anticomplete to T_j must be selected from row class j. The resulting core-degree formula is respectively 12-e_F(x,T_j)>=12 (Family I) or 13-1-e_F(x,T_j)>=12 (Family II), forcing no cross edges. The expanded argument is in `COVER_B1_AND_TRIANGLE_ATTACK_20261103.md`, Sections5–6.

Disposition: **NO GAP FOUND** in the q30 K4 terminal, Family I/II cross-row anticompleteness, or B1 argument. The frozen COVER source remains unchanged.


## E286 Section11: independent double-K11 intersection attack (2026-11-03)

A separate enumerator was written from the blocker relations and local degree bounds, without importing project code. For two mixed points z,z' on the same K11/K11 pair, let missing sets be A,B and A',B', with sizes a,b,a',b' and intersections r=|A∩A'|, s=|B∩B'|. Total excess T=8 implies each f11 blocker charge is at most8. Enumerating every resulting size/intersection state gives 3,387 states.

For each state, the checker separately considers z,z' adjacent and nonadjacent. Adjacent is rejected if they share at least10 vertices in either K11, because that would form K12. In the nonadjacent case it adds the T8 common-neighbor inequality c(z,z')<=3+epsilon(z)+epsilon(z'). Vertex charges on X and Y are calculated by the exact four-part partitions A\\A', A'\\A, A∩A', and their Y analogues; overlap B∩B' is counted once, avoiding double-counting.

Results:
- 2,748 states permit adjacency; 639 force nonadjacency by K12.
- Minimum forced charge in the nonadjacent case:15.
- Minimum forced charge in the adjacent case:14.
- Minimum over all allowed states and relations:14, attained by exactly five intersection parameter states (listed in E286_DOUBLE_K11_PAIR_ATTACK_20261103.md).
- Therefore the Section11 conclusion T>8 is independently confirmed with a substantial margin.

Artifacts: RECHECK_E286_DOUBLE_K11_PAIR.py, RECHECK_E286_DOUBLE_K11_PAIR.json, and E286_DOUBLE_K11_PAIR_ATTACK_20261103.md. This is a local charge audit only, not whole-E286 certification. The frozen source is unchanged.


## Lower-order M2b singleton-neighborhood extension (2026-11-03)

The exceptional vertex u in the K9,9-exterior, 121-edge case has one C5-neighbor p. The proof adds a second cycle edge u-q to place u into a valid two-neighbor type. A separate exhaustive check reconstructs all20 compatible nonempty type-set pairs (A,B) in the C5 type-compatibility graph and checks all55 possible p outside the union of B-types. Every case has q such that {p,q}=T_i is a valid two-neighbor type disjoint from all B-types; hence adding u-q creates no triangle. The |B|=1 case has a 3-vertex complement in which every p has an independent partner; the |B|=2 case has a 2-vertex independent complement.

Artifacts: RECHECK_LOWER_M2B_EXTENSION.py, RECHECK_LOWER_M2B_EXTENSION.json, LOWER_M2B_SINGLETON_EXTENSION_ATTACK_20261103.md. This is a focused finite check of M2b only; it does not certify the entire minimum-degree gate.


## Audit-note correction: h13 mixed König cover (2026-11-03)

A stale paragraph in FRONTEND_RECURRENCE_INDEPENDENT_AUDIT.md had claimed the mixed König cover could support13 cross edges. That correction was itself wrong: if s∈S and i∈I are nonadjacent, s has at most8 neighbors in I and i at most3 in S, giving11; if si is an edge, the two stars overlap and give at most9+4-1=12. Therefore the frozen COVER Section4 bound12 is correct. The erroneous audit paragraph has been withdrawn and replaced; no theorem source or proof statement needed correction.
