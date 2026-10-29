# EG617 fixed r=12 — root closure promotion audit

Updated: 2026-10-29 (supersession notice)
Status: **SUPERSEDED / RETRACTED IN PART; current root status OPEN / NOT_CERTIFIED.**

**WARNING — historical audit only. Do not use this file as the current root proof.** The E408 whole-layer closure depends on the retracted degree-nine exceptional-vertex premise. The claimed V12 independent replay is not reproducible from repository inputs: the source report says INDEPENDENT_REPLAY_PENDING and the original archive/manifest/verifier were not found in any of the 30 branch trees. E407 Q32 parent coverage remains OPEN, Q33 support promotion beyond |U|=31 remains OPEN, and E408 Q32 remains OPEN.

Historical headline (superseded):

> ~~No OPEN graph-theoretic T61/E407/E408 terminal remains in the audited fixed-r=12 chain.~~
>
> The project should not label this `PROVED` without qualification until the named machine-certified and external-theorem dependencies are accepted at the desired publication/formalization standard.

This file supersedes the earlier single-terminal reduction as the current root composition.

---

## 1. Assume a hypothetical balanced 12-color counterexample

Let G be a least-edge color graph in a hypothetical balanced 12-edge-coloring of K145. Then

\[
e(G)\le870,
\]

and every 13-set contains every color. In particular each color graph has independence number at most12, and the hereditary density caps used by the front-end follow from the eleven complementary colors.

The Line-A front-end recurrence is an exact finite reduction, not a heuristic search.

Current front-end receipt:

- package SHA256: `8f34097f195f53a6aac2999a655d3dc6a4ebc7c74f5764aedea65a79235a98ac`;
- manifest files checked: 73, errors: 0;
- recurrence nodes: 1752;
- outer stopping comparisons: 144;
- independent replay: PASS;
- unique surviving no-R(4,49) outer stop: `(d,j,a,n)=(11,6,5,61)` with edge interval 397..408.

The receipt historically records `bridge_status=OPEN` because, at the time it was issued, the surviving T61 obstruction was not yet eliminated. The recurrence/reduction itself is recorded as `PROVED` / `COMPUTATION_CERTIFIED` in the front-end ledger.

## 2. Front-end dichotomy

`FRONTEND_BRIDGE_THEOREM.md` proves:

\[
\text{balanced K145 counterexample}
\Longrightarrow
\begin{cases}
\text{an induced contextual }R(4,49),\\
\text{or an embedded T61 residual.}
\end{cases}
\]

The T61 branch has 61 vertices,

\[
397\le E=e(R)\le408,
\]

\[
\alpha(R)\le5,\qquad \omega(R)\le11,
\]

all inherited density caps, and actual minimum degree 12 or13.

The contextual R(4,49) branch is eliminated by `CONTEXTUAL_R449_FULL_COLOR_IMPOSSIBILITY.md`, relative to its explicitly cited Brouwer/extremal input. Hence any surviving original counterexample must enter T61.

No theorem asserting seven or eight unanchored outer K12 blocks is used at this root step.

## 3. T61 minimum-degree split

`T61_H12_CLOSURE.md` excludes the entire actual-minimum-degree-12 T61 branch under its stated contract.

Therefore every survivor has

\[
\delta(R)=13.
\]

## 4. T61 energy layers E397--E406

The current canonical front-end stack closes all lower h13 energies:

- E397--E400: `T61_H13_LOW_LAYER.md`;
- E401--E404: `E401_E404_CANONICAL_CLOSURE.md`;
- E405: `E405_FULL_CLOSURE_CANONICAL.md`;
- E406: `E406_FULL_CLOSURE.md`.

Thus any h13 survivor must lie in

\[
E\in\{407,408\}.
\]

These imports retain exactly the dependencies recorded in their own canonical files; this root composition does not silently strengthen them.

## 5. Entire E408 layer is impossible without charge casework

`E408_WHOLE_LAYER_EXACT_COUNT_CLOSURE.md` gives a Q-independent contradiction.

On a genuine 61-point E408 residual, the eleven non-target colors use

\[
\binom{61}{2}-408=1422=11\cdot129+3
\]

edges. Writing

\[
e_C(R)=129+s_C,
\]

gives

\[
\sum_C s_C=3.
\]

Hence the exact-129 color count is m in {8,9,10}.

Using the exact-129 Type-I degree structure, exceptional-vertex injectivity, the registered pointwise degree floors, and the Brouwer--Kang--Pikhurko induced-subgraph bounds:

- a 130-edge color has at most four degree-three vertices;
- a 132-edge color has at most nine degree-two vertices;
- a 131-edge color has minimum degree at least three.

Then:

- m=10 forces at least ten degree-two vertices in the unique132 color, impossible;
- m=9 forces at least nine degree-three vertices in a130 color, impossible;
- m=8 requires at least16 degree-three incidences across three130 colors, but capacity is at most12.

Therefore

\[
\boxed{E408\text{ is impossible}.}
\]

This shortest E408 route does **not** require q=32/q=33, a 284/285-edge core, seven outer K12 blocks, or the V11/V12 charge classification.

## 6. E407 charge ceiling

For a degree-13 pivot p in an E407 h13 T61 residual,

\[
407=91+q_p+e(H_p).
\]

The legal 47-core floor gives

\[
e(H_p)\ge284,
\]

hence

\[
q_p\le32.
\]

Let Q be the maximum charge over degree-13 pivots.

The independently audited V9 chain, relative to its retained seeds, removes the lower-Q branches and leaves exactly

\[
\boxed{Q\in\{31,32\}}.
\]

Its retained small Ramsey/core inputs are registered as `PROVED` in the front-end assumption ledger; the finite V9 verification remains computation-certified.

## 7. E407 maximum Q=31 is impossible

`V10_V11_Q31_INDEPENDENT_REPLAY_AUDIT.md` directly audits the original V10 and V11 archives.

### V10

Archive SHA256:

`e83e2907d541b38304746e855af52b5e21b6500a35cb0fdb676a4f6a7601303a`

Fresh manifest check: all entries PASS.

Independent replay:

- 12 labelled-cut rows;
- 16 local-neighbourhood cases;
- 14 row-budget cases;
- 1 shell witness;
- d3/d10 Q31 incidence theorem reproduced.

The package contains the V8 exchange/flat-boundary proof consumed by V10, rather than merely an opaque status flag.

### V11

Archive SHA256:

`27ecec92d43a27fb132c60aa7b374131a860547c236d8ed3d83d3cf0eab9f0a4`

Fresh manifest check: all entries PASS.

Independent replay:

- 684 kernel weight assignments;
- 349 outside-count states;
- 259 labelled necessary shells;
- Family A: 252;
- Family B: 7;
- certificate SHA256: `0baffc39ee481b27af53fda36a8fe40b8cd8c527103b5126060857c4eaacd09b`.

The finite certificate only proves necessary-state coverage. The two terminal families are then excluded analytically by the common-K10 support-capacity theorem: support multiplicity at most2, support union at least17, zero-capacity remainder a matching of size at most10, hence an independent set of size at least7>5.

Therefore

\[
\boxed{E407,\ Q=31\text{ is impossible}}
\]

relative to the named V6/V8/core/extremal inputs.

Status: **PROVED_CONDITIONAL + COMPUTATION_CERTIFIED**.

## 8. Historical V12 finite-replay claim — not reproduced; superseded

Historical claim (superseded): an earlier version asserted that the original V12 archive was independently materialized and replayed. The current audit cannot reproduce that claim because the archive, manifest, and verifier are absent from all 30 branch trees; the current source report explicitly says INDEPENDENT_REPLAY_PENDING. The figures below are retained as reported source metadata only.

Archive SHA256:

`0c3c69a7baf94a816eff29f3a079b97ac7750d0e8b8fd2773330469c4b8c5e36`

Historical replay-log claim (unverified in the current audit): “Fresh manifest check before execution: all entries PASS.” This is not accepted as a current certification result.

The historical report claimed that an independent verifier reproduced:

- 8,677 kernel weight vectors;
- 17,957 count states;
- 1,984 labelled necessary shells;
- 90 d3/rho1 exclusions;
- 1,192 near-K12 capacity exclusions;
- 148 K9 pair-row refinements;
- 554 OPEN finite-screen entries;
- every one of the 554 has a rho=0 d3 candidate and maps to one of five exact K11 triple-row shell templates;
- V12 certificate SHA256: `cab4e67bc501fe51c06f8fc008443b870aebf8794528af1a3045e83be7d6db30`.

The V12 certificate itself does not claim those 554 states impossible.

## 9. Template-local common support contract — conditional interface, not finite-screen certification

The later E407 workstream proves that every legal completion of any of the five V12 shell templates must be completed against the same frozen support object:

\[
|H|=47,\quad e(H)=284,
\]

\[
U\subset H,\quad |U|=29,
\]

with 49 selected independent four-set blocks, seven in each of seven distinct selected exact-129 color classes. The blocks are vertex-disjoint within a selected color and pairwise linear across selected colors.

For

\[
L_U=\overline{H[U]},
\]

the exact ledger is

\[
\boxed{e(L_U)=294+\delta,\qquad 3\le\delta\le16}.\tag{1}
\]

`SUPPORT_BLOCK_ANCHOR_IDENTITY.md` closes the previous label firewall for the selected 49 blocks: every selected block is exactly the H-four-set of an isolated monochromatic K5 component of its assigned exact-129 color.

Therefore the six pairs inside every selected block genuinely have that selected color.

Because the 49 blocks are pairwise linear/disjoint at pair level, they own exactly

\[
49\binom42=294
\]

distinct edges of L_U.

## 10. E407 Q32 local reserve contradiction under the contract; V12 parent mapping remains OPEN

There are eleven non-target colors total. The frozen V12 support system uses seven distinct selected colors. Therefore four other non-target colors remain.

For every such color D,

\[
\alpha(D[U])\le12.
\]

Turan's theorem on 29 vertices gives

\[
e_D(U)\ge p_{12}(29)
=5\binom32+7\binom22
=22.
\]

The four unselected colors therefore require at least

\[
4\cdot22=88
\]

additional pairwise-disjoint U-edges. By unique edge ownership these edges are also disjoint from the 294 selected-color support edges.

Thus any completion would require

\[
e(L_U)\ge294+88=382.
\]

But (1) gives

\[
e(L_U)\le294+16=310.
\]

Hence

\[
\boxed{382>310},
\]

a contradiction with a gap of72 edges.

Therefore any legal completion already shown to satisfy one of the five template contracts is contradicted by this reserve. This does not independently certify that every legal parent is covered by the V12 finite screen and mapped to a template; that composite parent-coverage edge remains OPEN until V12 source/manifest/verifier replay and the analytic screen assumptions are audited.

Thus

\[
\boxed{E407,\ Q=32\text{ is impossible}.}
\]

This terminal proof does not use the Didin-dependent low-delta branch, template-by-template row casework, or an additional exact color.

## 11. Historical terminal-composition claim — superseded 2026-10-29

The prior claim that every T61 branch had been exhausted is withdrawn. E407 Q32 parent coverage is OPEN pending V12 source/replay and the parent-to-29-point/49-block contract proof. E408 Q33 is closed only on its exact 31-point/56-witness contract; the support theorem does not force equality and the higher-support cases are not closed by the audited scalar reserve. E408 Q32 remains OPEN under the 285-edge/excess-six contract.

## 12. Current root status

The front-end dichotomy still reduces the original hypothetical K145 counterexample to the contextual R(4,49) branch or a T61 residual, under the registered assumptions. The contextual R(4,49) branch and the listed lower T61 layers retain their named conditional statuses. However, the remaining dependencies above have not been closed.

Accordingly:

\[
\boxed{\text{EG617 fixed }r=12:\ \textbf{OPEN / NOT\_CERTIFIED}.}
\]

No root promotion is authorized.

## 13. Historical qualifier rationale (superseded by the 2026-10-29 fail-closed audit)

This root promotion is intentionally not labelled bare `PROVED` because the proof stack still includes:

1. the exact 1752-node front-end recurrence and 144 stopping comparisons as a machine-certified finite certificate;
2. V9/V10/V11/V12 exact finite coverage certificates;
3. ordinary analytic proofs whose interfaces consume named external extremal/Ramsey results, including Brouwer/Kang--Pikhurko/Andrasfai--Erdos--Sos-type inputs where recorded;
4. the registered exact-129 Type-I factor theorem;
5. the later E407 selected-component/support identity, currently recorded as conditional on that factorization/minimum-support interface.

The relevant finite packages have independent exact replays; no floating-point optimization or heuristic solver output is used in the load-bearing root chain described here.

For publication-grade promotion to an unqualified theorem, the remaining work is proof engineering/review rather than discovery of a missing graph case: consolidate the named external theorem statements, freeze all source hashes, independently rerun every finite certificate from clean environments, and ideally formalize the short root composition and the new capacity contradictions.

## 14. Historical status notes (superseded)

Several sibling files still say `OPEN / NOT_CERTIFIED`. Those statuses were correct when written and should not be silently edited in place. They predate one or more of:

- the whole-layer E408 exact-count contradiction;
- direct V10/V11 package replay;
- the selected-support color identity;
- the E407 four-color U-reserve contradiction.

This audit does not rewrite sibling history. It provides the new branch-local promotion layer that composes those later assets.


## 15. Independent root-promotion audit — 2026-10-29

This addendum is authoritative over the historical claims above.

- E407 Q32 local arithmetic: 294+22=316>310, conditional on the 29-point/49-block contract. The V12 archive SHA256 reported historically is 0c3c69a7baf94a816eff29f3a079b97ac7750d0e8b8fd2773330469c4b8c5e36 and certificate SHA256 is cab4e67bc501fe51c06f8fc008443b870aebf8794528af1a3045e83be7d6db30; these remain unverified source reports.
- Repository search: all 30 branch trees checked; no T61_H13_V12.zip, matching manifest, or verifier; only consolidation/V12_V8_SOURCE_REPORTED_AUDIT.md appears as V12-named source, and it records INDEPENDENT_REPLAY_PENDING. Releases count 0; exact archive path commit-history count 0.
- Q33: exact 31-point / 56-witness reserve is PROVED_CONDITIONAL. The support lower bound |U|>=31 is not an equality theorem. The independent scalar reserve audit excludes m=8,9 at v=31 and m=8 at v=32; all listed remaining higher-support cases remain OPEN under that reserve.
- E408 Q32: OPEN / NOT_CERTIFIED. Degree-nine exceptional-vertex and exceptional-injectivity claims remain RETRACTED.
- Current root: OPEN / NOT_CERTIFIED. No promotable root receipt is issued.


## 16. Explicit boundary of the historical V12 sections

Sections 8–10 above must be read as two different statements:
1. the template-local 29-point/49-block support and anchor interface is PROVED_CONDITIONAL under the registered minimum-support and exact-129 assumptions;
2. the assertion that the complete V12 finite screen exhausts every legal E407 Q32 parent and maps every survivor to A-E is OPEN because the original archive, manifest, and verifier are unavailable.

The local reserve contradiction cannot certify its own parent coverage. The root status remains OPEN / NOT_CERTIFIED.
