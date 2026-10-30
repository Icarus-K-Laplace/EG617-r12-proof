# Independent audit of the exact 285-edge theorem

Date: 2026-10-30. Status: **PROVED** for the abstract five-hypothesis theorem.

## Frozen input

Original theorem commit: c5062fcdf5ac83ea9d0d51b9bc34a8f9f3619c0f.
Latest Q32 branch head read: f56cc9eba646e71d63c4b55f468a2340bcdd64c2.
Source: astra-q32-v47-universal-attack-chat-20261030/UNIVERSAL_Q32_THEOREM.md.
The compare from the original commit to this head contains ten commits; the theorem file itself is unchanged. Later audit files distinguish the valid abstract graph theorem from an unresolved parent minimum-degree source.

The proof was re-read from the frozen remote blob and re-derived here. The new verifier imports neither the old verifier nor a sibling status assertion. This is a new proof audit and implementation, not a claim of external peer review or proof-assistant formalization.

## Eight-step audit

| Step | Required hypotheses and check | Outcome |
|---|---|---|
|Independent degree12 four-set|epsilon>=0, total6; q<=6; complementary Turan plus incident-edge count, subtracting e(exceptional set) only once|PROVED; all six original lower bounds exceed285|
|Private clique partition|alpha<=4 makes every private class a clique; seed degrees12 give exactly five surplus incidences; omega<=11 bounds class sizes|PROVED; h=3,4,5 exhaustive|
|Common-neighbor bound|25-set degree upper153 versus non-bipartite triangle-free complement upper145, giving target lower155|PROVED; reconstructed in C1/C2|
|Two K11 pair|Positive missing sets are forced by omega<=11; independent5 blocker; disjoint vertex charges have unique minimum6 at a=b=2|PROVED; all excess on the pair point|
|h=3 rotation|The chosen missing vertex has exactly ten clique neighbors and two forced opposite neighbors, hence no uncounted neighbor; replacement seeds remain independent and degree12|PROVED; original two K11 private classes remain full because they cannot enlarge|
|h=4 and h=5 reductions|Zero missing sets on K10/K9 retained; degree12 endpoint bounds used only after the equality trigger; repeated support pairs included|PROVED; only P and D survive|
|P terminal|Each doubled mixed pair has a point not complete to K10; two selected clique pairs are disjoint|PROVED; required excess8>6|
|D terminal|Different support edges enter different opposite cliques; negative increments controlled pointwise before summation|PROVED; required excess10>6; no duplicated excess|

The finite checker reconstructs support orbits2/3/5, scalar minima6/6/4/5, and8,400 pointwise D cases. The graph implications remain analytic; the finite checks do not substitute for them.

## Parent gap and its replacement

The latest Q32 audit correctly withholds parent promotion because its earlier R(3,35) degree seed lacked a recovered proof body. A theorem conditional on delta(H)>=12 does not establish that minimum degree for a parent core. This audit does not assume that missing implication.

Instead, MINIMUM_DEGREE_GATE_SELF_CONTAINED.md reconstructs the general source gate J in R(4,47), e(J)<=286 => delta(J)>=12, including the 121/122-neighborhood classification and the 14-point contradiction. CROSS_ROOT_PARENT_CONTRACT_AUDIT.md separately supplies all inherited caps for each real parent. Thus the old parent gap is discharged by a new audited route in THIS directory; the original Q32 files are not changed.

## Augmentation acceptance

The exact285 theorem needs only order47, edge count285, minimum degree12, independence at most4 and clique number at most11. It does not require hereditary caps, a parent extension, an exact-color partition, a special-point placement or a particular m. Therefore the terminal augmented graph supplies precisely its full hypothesis list. The augmentation route has no circular dependence on the new low-edge theorem.
