# Counterexample, gap and failed-check register

Date:2026-10-31. Source pinned at c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2.
No mathematical counterexample or unclosed load-bearing gap was found in this
audit. This is the result of the attacks recorded below, not a claim to have
searched all61-vertex graphs. The final mathematical status is given separately.

## G01 — failed local-byte integrity assertion, resolved

* Location: first version of this audit's INDEPENDENT_REPLAY.py, integrity();
  first file checked was integration ALL_ENERGY_LAYERS_COMPLETE_INVENTORY.md.
* Original check: the checked-out byte string must have the pinned Git blob SHA.
* Observed failure: AssertionError on the first run; all other then-implemented
  computation subtasks passed. This failed result was disclosed in chat and log.
* Cause: system Git core.autocrlf=true converted LF source blobs to CRLF at checkout.
  The clone command's temporary setting did not persist to the later checkout.
* Mathematical counterexample: none; the failed proposition concerned byte identity
  of the checkout, not a lemma. This is not evidence of source tampering.
* Repair: hash raw git show bytes; additionally require every checkout difference
  to be precisely LF-to-CRLF conversion. Compare frozen source bytes directly
  with their declared origin commit and blob. Preserve source files unchanged.
* Verification:48 pinned files,26 origin mappings,47 SHA256 entries pass. All
  frozen destinations are accounted for in the manifest. The checksum file
  itself has its Git blob authenticated and is not recursively self-hashed.
* Main theorem changed: no. Other workstreams affected: none.

The later default Git whitespace check also reported CR-at-EOL on generated
Windows text files. Rechecking with Git's explicit cr-at-eol option passed;
this recognizes valid CRLF bytes rather than changing or discarding content.
The delivery checksums preserve the exact committed bytes.

## G02 — scope ambiguity in requested support counts, resolved

* Locations: integration H12_AND_EXCEPTIONAL_PARENT_AUDIT.md sections2–4;
  frozen/eq286/286_EDGE_EQUALITY_CLASSIFICATION.md section2;
  frozen/low/DIRECT_UNIFORM_PROOF.md section1.
* Issue investigated: the requested2,3,5 support-orbit counts were mentioned in
  the h12 task, but in the actual files they classify the47-point four-seed
  partitions with h=3,4,5. They do not classify a12-shell.
* Resolution: independently reproduced those ten support orbits, including the
  actual canonical sets, AND independently derived/replayed the five q20
  K_(2,r) shell families for r=6..10. No count was used outside its domain.
* Counterexample or source error: none; this is a task-to-source mapping clarification.
* Main theorem changed: no. Other workstreams affected: none.

## G03 — first Brooks PDF retrieval failed, resolved

* Location: external reference in K145_TO_T61_FRONTEND_AUDIT.md.
* Failure: first direct PDF request timed out. This did not license assuming
  that the source had been inspected.
* Repair/evidence: subsequently retrieved the original Brooks paper reprint,
  AppendixA p537, and the Cambridge publisher DOI record. The actual theorem
  permits disconnected graphs and excludes K_(n+1) components at n>2.
* Main theorem changed: no; n=12 and the absence of K13 components are valid.

## Adversarial mathematical challenges and dispositions

|Source location at the pinned commit|Attack|Disposition and independent evidence|
|---|---|---|
|COVER_THEOREM.md section3, line62 onward|Wrong repivot signs; double-counted deleted internal edges; closed-walk summands set to zero|Exact independent edge partition C1 proves all signs.312 algebra instances passed. Zero terms arise only from maximum charge and nonnegative matching lower bounds.|
|COVER_THEOREM.md sections4–6|Omitted triangular shells, isolates, empty row types, decoration allocations or hub permutations|C3 handles all triangle and odd-cycle cases; C4 proves the mapping and exact quotient.19448 vectors per q,2/8 complete canonical sets.|
|COVER_THEOREM.md section7.2, line157|B1 row intersections or multiplicities silently assumed|C5 derives all-or-none intersection in each specified cover, then multiplicity2/3; degree formula forces the base-point contradiction.|
|COVER_THEOREM.md section8, line183|beta12 applied to arbitrary47-core|C6 first proves the <=288 gate. New cores in Q30 arguments are given q>=29 before receiving this gate.|
|COVER_THEOREM.md section10, line218|Additional q30 family at a missing degree or high-weight cardinality|C7 treats degrees4–9,3,10, then K4 and every X-size0,1,2,3. Exactly I/II remain.|
|COVER_THEOREM.md sections11–12, lines251,267|Overlapping excess or row classes from different parents|C8 uses one fixed F, disjoint row triangles and the exact23-unit total. FamilyII pairs are proved disjoint before the independence contradiction.|
|MINIMUM_DEGREE_GATE_SELF_CONTAINED.md M2–M4, lines22,66,85|Missing121-edge type or unjustified missing target cross edges|L1 independently enumerates compatible types and endpoint exceptions; L2 explicitly lower-bounds cross edges in the14-set.|
|DIRECT_UNIFORM_PROOF.md sections2–7, lines24 onward|T=0 omitted; complete K9/K10 attachments discarded; repeated excess|L4 includes q=0; L5 retains zero missing sets and proves pointwise shared accounting.|
|286_EDGE_EQUALITY_CLASSIFICATION.md sections1,3,7–11|Invalid import of nine-common-neighbor bound; double counting shared leaves or repeated pairs|L3 uses correct T8 bound11 and completion costs7/6; L6 separates all ten orbits and all repeated-pair intersections.|
|H12_AND_EXCEPTIONAL_PARENT_AUDIT.md sections2–5|Unsupported48-floor, omitted q20 cases, invalid inserted-degree bound|F3 independently derives delta48 and floor310; all five q20 families lead to inserted degree<=11 in a core proved to have delta>=12.|
|K145_TO_T61_FRONTEND_AUDIT.md sections1–4|Wrong Brooks exception, color balancing assumption, contextual-to-generic transfer or cyclic seed|F1–F4 verify original all-colors property, exact budget, contextual49 distinction and seed dependency order.|
|PROOF_DAG.json and final proof|Syntactically acyclic graph hiding a semantic cycle|Independent58-node DAG separates CORE211 and MATCH3 from terminal COVER. Each matrix row states the transported hypotheses; no seed depends on T61 emptiness.|

All source line numbers refer to raw pinned Git blobs. SOURCE_LOCATION_INDEX.json
records the heading positions and SHA256 of every source proof document.

## Remaining limits, not concealed proof gaps

There is no proof-assistant formalization in this package and no external human
peer review performed by this chat. The finite Q27/Q28 classification and
recurrence depend on ordinary Python execution, accompanied by analytic domain
and completeness proofs. Published external theorem statements are accepted
inputs. Generic uncolored R(4,49) high-energy classification remains OPEN and is
not needed for the contextual K145 contradiction. No original root file was
edited and no promotion/merge has been performed by this certificate.
