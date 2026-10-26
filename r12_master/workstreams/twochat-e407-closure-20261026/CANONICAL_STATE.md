# Canonical state — E407 Q32 global compatibility sprint

Date: 2026-10-26  
Repository: Icarus-K-Laplace/EG617-r12-proof  
Branch: workstream/r12-twochat-e407-closure-20261026  
Allowed write path: r12_master/workstreams/twochat-e407-closure-20261026/

## Headline

**E407 Q32: OPEN / NOT_CERTIFIED. EG617(r=12): OPEN / NOT_CERTIFIED.**

This workstream audits the current E407 frontier and strengthens the common labelled-incidence constraints for the five alternative V12 shell templates. It does not claim that all five alternative templates occur in one graph, nor that any template is globally impossible unless a complete proof is supplied.

## Frozen E407 Q32 core contract

Under the retained T61 / V12 boundary contract:

\[
|V(H)|=47,\quad e(H)=284,\quad \alpha(H)\le4,\quad
\omega(H)\le11,\quad \delta(H)\ge12,
\]
\[
\sum_{x\in H}\epsilon_x=4,\qquad
\epsilon_x=d_H(x)-12\ge0.
\]

The support set \(U\subseteq V(H)\) has \(|U|=29\), \(W=H\setminus U\) has \(|W|=18\), and there are 49 independent 4-set witnesses on U, pairwise linear, seven in each of seven exact-129 color classes. Set
\[
L_U=\overline{H[U]},\quad \delta=e(L_U)-294,\quad
\epsilon_U=\sum_{u\in U}\epsilon_u.
\]
The exact ledger is
\[
e(H[U])=112-\delta,\quad e_H(U,W)=124+\epsilon_U+2\delta,\quad
e(H[W])=48-\epsilon_U-\delta.
\]
The retained boundary inequalities are
\[
3\le\delta\le16,\quad \delta+\epsilon_U\le16,\quad
\epsilon_U+2\delta\ge9,\quad 0\le\epsilon_U\le4.
\]

## Contract classes — never conflate them

1. **Pure graph contract:** the 47-vertex H inequalities and edge/excess ledger above. The clique bound \(\omega(H)\le11\) is inherited from the T61 parent, not a consequence of \(e(H)=284\) alone.
2. **Labelled witness contract:** the 29-point support U, 49 linear independent 4-sets, seven per exact-129 color class, and the color/component labels. This additionally uses edge-color uniqueness and the exact-129 factorization.
3. **External-input-dependent contract:** the exact-129 component structure and the non-four-partite extremal classifications require their registered extremal theorem hypotheses. The \(\delta=14\) saturated branch additionally depends on the unaudited Didin 2026 preprint component-count step.
4. **Original-problem bridge:** the T61 residual and its 49 witnesses are conditional on the parent reduction and V12 lower-order seed contracts. The original \(K_{145}\)-to-T61 bridge is not certified closed by this workstream.

## Latest source heads read (read-only)

- Main branch: 3f42fcce5761ca2372140618adda56f95fcbe253
- E407 Q32 terminal: 79c1086efca893fad8933210a92a432457232410
- Unified witness capacity: faa8183c150dd78b000d0957fa8a63cebd52e146
- Emergency sprint: f4c3b06891d29238d4f9cca2588f442004b6dc97
- Ultimate closure: 1aa47d10edd5ece2b73a0891af7ac2ce37ecbb40

The current branch was created from main; all source branches remain read-only.

## Current strongest new result in this workstream

Under the exact-129 component contract, every exact-129 color has at least six B-labelled, no-S \(K_5\) components \(\{b\}\cup Q\). Combining this with the audited V12 high-k row floors yields a template-uniform per-color lower bound on high-k component witnesses:

| Template | High-k rows forced | High-k B-labelled no-S components per exact-129 color |
|---|---:|---:|
| A | at least 6, including at least 6 k=3 rows | at least 2 high-k witnesses and at least 2 k=3 witnesses; the latter hit all three S rows |
| B | at least 8 | at least 4, each hitting at least two S rows |
| C | at least 6, including at least 6 k=3 rows | at least 2 high-k witnesses and at least 2 k=3 witnesses; the latter hit all three S rows |
| D | at least 7 | at least 3, each hitting at least two S rows |
| E | at least 5 | at least 1, each hitting at least two S rows |

There are at least seven exact-129 colors. The selected component witnesses are pairwise linear across colors and disjoint within a color; witnesses carrying the same B label in different colors are disjoint. Every such Q hits at least three shell rows in total. This is a stricter labelled-incidence constraint, **not yet a contradiction**.

Crucial firewall: the exact-129 no-S component witnesses are kept as separately labelled objects unless a proof identifies them with the selected 49 support blocks. No equality of witness sets is assumed.

## Round 3 proved refinements

- **A/C component packing:** among the six B-labelled no-S component quadruples in each exact-129 color, at least three are hub-complete in templates A/C. Proof: if h=n3≥6 full B rows, each non-hub-complete quadruple must hit at least h distinct B rows; the six quadruples are disjoint, while the total B-to-core incidence is \(c_S=3h+n_1\le2h+10<4h\). Thus at most three of the six can be non-hub-complete. This gives at least 21 hub-complete component witnesses across the seven exact-129 colors. These are component witnesses, not automatically members of the 49-block support family.
- **Support omission–degree identity:** for \(r_u\) color classes omitting \(u\in U\) and \(x_u\) extra support-complement edges incident to u,
  \[
  \sum_U r_u=7,\quad \sum_U x_u=2\delta,\quad
  d_H(u,W)=5+\epsilon_u-3r_u+x_u.
  \]
  At least 22 U-points have \(r_u=0\), hence \(d_H(u,W)\ge5\). This is proved in FIVE_TEMPLATE_GLOBAL_COMPATIBILITY.md, Section 5 and arithmetically replayed by verify_support_omission_identity.py.
- **Label-join contract:** LABEL_JOIN_SYSTEM.md now specifies the support-block variables, shell-row variables, exact-129 component variables, and the missing mapping between the two witness families. The mapping is deliberately left OPEN; no unsupported identity is imposed.


## Current frontier

- \(\delta=16\): excluded under the four-partite boundary reduction and inherited core contract.
- \(\delta=15\): four-partite and non-four-partite branches excluded under their registered extremal contracts.
- \(\delta=14\): four-partite branch excluded; non-four-partite saturated branch is conditional on the Didin-dependent alpha-critical reduction.
- \(\delta=13\): four-partite \(\epsilon_U=1\) row is excluded; four-partite \(\epsilon_U=2\) retains the \((4,4,5,5)\)-plus-one-cross-edge W-profile; \(\epsilon_U=0\), non-four-partite cases, and \(\delta\le12\) remain open.
- Five shell templates A–E: all remain OPEN as global same-core completion questions.
- Original \(K_{145}\)-to-T61 bridge: OPEN / NOT_CERTIFIED.
- Root main still lists E407/E408 and abstract backend E333–E340 as independent obligations; sibling documents contain a conditional alternative treatment of the \(R(4,49)\) branch, so the root proof DAG is not promoted here.

See FIVE_TEMPLATE_GLOBAL_COMPATIBILITY.md, LOW_DELTA_TERMINAL_TABLE.md, PROOF_DEPENDENCY_AUDIT.md, and OPEN_CONTRACTS.md.


## Round 2 audit update (2026-10-26)

- Exact integer feasibility: **56** \((\delta,\epsilon_U)\) profiles, independently replayed; the verifier's prior count 57 was corrected.
- Template incidence arithmetic: independently replayed the h-4 high-k component floor and all A–E totals. A/C have at least two k=3 no-S witnesses per exact-129 color; aggregate S-row hit floors are \(42,56,42,42,14\), while total shell-row hit floors are \(42,84,42,63,21\).
- Verification scope is arithmetic only. No graph realization, template exclusion, or original theorem closure is certified by these scripts.
