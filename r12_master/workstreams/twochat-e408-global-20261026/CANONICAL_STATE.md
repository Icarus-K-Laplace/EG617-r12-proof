# EG617 fixed r=12 — canonical state of this workstream

Updated: 2026-10-27
Repository: `Icarus-K-Laplace/EG617-r12-proof`
Branch: `workstream/r12-twochat-e408-global-20261026`
Write scope: `r12_master/workstreams/twochat-e408-global-20261026/`

## Headline

**EG617(r=12): OPEN / NOT_CERTIFIED.**

Primary-source audit of the Kang--Pikhurko exact-129 equality construction found a load-bearing error in the previously promoted E408 exact-color-count closure: the Type-I exceptional gadget has no color-degree9 vertex. The affected E408-Q32 closure files are retracted in `KP_DEGREE9_RETRACTION_AND_E408_Q32_REOPEN.md`.

After fail-closing the root DAG, the unique currently identified live graph terminal is

\[
\boxed{E408\;/\;h13\;/\;Q_{\max}=32\;/\;e(H)=285\;/\;\text{core excess }6.}
\]

All other currently audited root branches remain closed relative to their named analytic/external/computation-certified inputs.

## What remains closed

A hypothetical balanced 12-color counterexample is reduced by Line A to contextual `R(4,49)` or T61.

- contextual `R(4,49)`: closed by the registered full-color impossibility theorem;
- T61 h12: closed;
- h13 E397--E400: closed;
- E401--E404: closed;
- E405: closed;
- E406: closed;
- E407 Q31: closed via V10/V11 + analytic common-K10 capacity;
- E407 Q32: closed by the one-unselected-color U-edge reserve contradiction;
- E408 Q31: remains closed by the V11 route under its named inputs;
- E408 Q33: remains closed by the component-capacity / nonexact-U reserve route, which does not use the false degree9 premise.

The E407 Q32 terminal remains especially strong and unaffected by the retraction. Its shortest contradiction is

\[
49\binom42=294,
\]
selected complement edges on `|U|=29`, while `e(overline{H[U]})<=310`. Since eleven non-target colors exist but only seven selected colors are used, choose one unselected color D. Then `alpha(D[U])<=12`, so

\[
e_D(U)\ge p_{12}(29)=22,
\]

and edge uniqueness forces

\[
e(overline{H[U]})\ge294+22=316>310.
\]

## Kang--Pikhurko source audit: valid part

The exact-129 factor theorem itself is source-verified.

For an exact-129 non-target color C on 61 vertices, the complement has1701 edges and is a `K13`-free non-12-partite equality graph for Kang--Pikhurko at `(n,r)=(61,12)`. The only equality part sequence compatible with `omega(C)<=5` is `(5^12)`.

Therefore every exact-129 color has the valid factorization

\[
10K_5\;\dot\cup\;G_{11},
\]

where the ten K5 are isolated components and `G_11` is the exceptional gadget containing two further 5-cliques and the added vertex x.

Companion verifier: `verify_kp_exact129_instance.py`.

## Kang--Pikhurko degree correction

Let `A` be the nonempty proper subset of one special 5-part in the published construction and put `a=|A| in {1,2,3,4}`. In the original exact-129 color graph:

- the ten isolated-K5 vertices have degree4;
- ordinary special-part vertices have degree5;
- the two variable vertices have degrees `4+a` and `9-a`.

Hence the variable degree pairs are

`(5,8), (6,7), (7,6), (8,5)`.

There is no degree9 vertex.

Therefore the following local closure routes are not valid as currently written:

- `Q32_GLOBAL_EXCEPTIONAL_INJECTIVITY.md`;
- `Q32_EXACT_COLOR_COUNT_COLLAPSE.md`;
- `E408_WHOLE_LAYER_EXACT_COUNT_CLOSURE.md`;
- `Q32_NONFULL_SUPPORT_SHELL_CAPACITY.md` insofar as it calls the exceptional-injectivity lemma.

They are historical audit artifacts, not current proved closures.

## Live E408-Q32 contract

For a maximum-Q32 degree-13 pivot in E408,

\[
e(H)=408-91-32=285.
\]

The strongest surviving 285-edge core interface is:

- `|H|=47`, `e(H)=285`, `alpha(H)<=4`, `delta(H)>=12`;
- total degree excess above12 equals6;
- eleven non-target residual colors have edge counts `129+s_C` with nonnegative `s_C` summing3;
- the number m of exact-129 colors lies in `{8,9,10}`;
- every exact color supplies at least ten pairwise-disjoint independent core4 witnesses;
- witness classes from distinct colors are pairwise linear;
- if N is the total witness count and U their union, then
  `6N <= e(overline{H[U]))`;
- exact 285-edge capacity:

\[
6N\le \binom v2-p_4(47-v)-12v+285-E_U,
\]

where `v=|U|`;
- the low-support triple-pair theorem strengthens the global support floor to

\[
\boxed{v\ge44}.
\]

At `v=44`, further structure survives; no contradiction has yet been certified.

Primary read-only source: `workstream/r12-e408-q32-excess6-20261025`, especially `CORE285_CAPACITY_THEOREM.md`.

## Front-end computation boundary

Line-A remains computation-certified:

- package SHA256 `8f34097f195f53a6aac2999a655d3dc6a4ebc7c74f5764aedea65a79235a98ac`;
- 73 manifest files checked, 0 errors;
- 1,752 recurrence nodes;
- 144 outer comparisons;
- unique no-R(4,49) stop `(11,6,5,61)` with `397<=E<=408`;
- independent replay PASS.

Historical `front_end/ASSUMPTION_LEDGER.md` remains untouched and is not silently upgraded.

## Current highest-leverage target

> Close E408-Q32 from the correct Type-I factorization and the 285-edge/core-excess-six witness-capacity system, without exceptional-degree9 or any imported excess-four identity.

Priority subtargets:

1. sharpen `v>=44` to a terminal contradiction or exact `v=44,45,46,47` normal forms;
2. exploit the correct variable gadget degrees `(5,8)/(6,7)/(7,6)/(8,5)` only through valid capacity constraints;
3. combine exact-color witness ownership with the remaining `11-m` nonexact colors on U;
4. use shell-support classification only after its assumptions are independently checked.

## Status policy

No root theorem promotion is allowed until E408-Q32 is closed from valid premises. A source audit that finds another hidden premise must fail-close the corresponding gate immediately.
