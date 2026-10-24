# Astra-2: robust low-offset terminal nonextension

Updated 2026-10-25. Branch: `workstream/astra-dlow-terminal-20261024`.

**D_LOW_PROVED for every integer r >= 221**, under the contextual
terminal contract explicitly stated in THEOREM.md. The high-degree
branch is already excluded for every r >= 209. The full requested
range starting at 67 remains OPEN below these thresholds.

## Main advance

A sparse actual non-target color on the common antineighbourhood
provides a large matching. The contextual degree budget extends the
original independent triple to five independent low-degree anchors.
They force five ACTUAL target cliques and a kernel of size 6 through 12.
An edge-disjoint, all-color cut count then gives

    r <= (3m^2+5m+2)/2 - epsilon*m - 3e_F(H).

This permits arbitrary target edges between the five cliques and
arbitrary multi-block cover networks. No exact-star, single-cover,
source-pair compatibility, or unproved hub-propagation lemma is used.

## Scope of the contextual contract

The ambient balanced coloring requires every (r+1)-set to contain
every color. Restriction to the terminal therefore gives alpha(G_i)<=r
for every non-target color. Distinct colors partition unordered pairs.
The extracted target additionally has alpha<=5 and omega<=r-1.
Consequently non-target graphs are K6-free, and every induced subset
X inherits e_F(X)<=C(|X|,2)-(r-1)p_r(|X|).

The strengthened cap used here is 2e(F)<=5r^2+7r+18, derived from
the retained Brouwer second-Turan input; see DEPENDENCY_DAG.md.
The near-anchor triple and its low-offset size are hypotheses of the
terminal interface, not conclusions of a naked target graph model.
An impossibility proof for this necessary contextual sub-contract
excludes the full embedded terminal, even though some additional
ambient constraints are not needed in the proof.

No assertion that the original coloring reaches this terminal is
made. A_ext* remains OPEN. The synthesis consequence is only
A_ext*(r) => P(r), for r>=221, relative to the retained synthesis.

## Status ledger

|Statement|Status|Scope|
|---|---|---|
|Sparse-color matching and five-anchor extension|PROVED|All nine windows, r>=67|
|Actual kernel 6<=m<=10+eta<=12|PROVED|Same contract|
|All-color unique-edge kernel capacity|PROVED|General five-clique partition|
|All nine low-offset windows excluded|PROVED|Every integer r>=221|
|All six high-degree windows excluded|PROVED|Every integer r>=209|
|Eta-specific improvements|PROVED|OFFSET_CLASSIFICATION.md|
|Full D_low for 67<=r<=220|OPEN|Only partial exclusions obtained|
|A_ext* and unconditional EG617|OPEN|Not resolved here|
|General cheap-cover propagation assertion|RETRACTED as a deduction|Split-cover countermodel|
|Sibling r>=6212 closure|RETRACTED in latest source|Not used|

## Source freeze and fresh-source audit

Initial source heads: design a314ffe1a86acea3fbac24e45e1fbf5d9ab22694;
asymptotic aa7fbbda16ff0170c9bf7c440ca961a7a8aab3c0.
The 2026-10-25 follow-up checked design
c3f6aa87344008fa1955e9e48075735c5f4c46da and asymptotic
fa6a5f2b8b5d2a0fe821d50a4421884a69dc5366.
Architecture cap source: a922c4d7646eb8d0087bde8547562c8aace02ee2.

Latest D records withdrawal of its r>=6212 argument and supplies a
valid weighted multi-block incidence inequality, still without a
global contradiction. Latest E records a forced large-incidence hub
and leaves low-offset nonextension open. Neither later development
changes the hypotheses or is required by our proof. No sibling file
has been modified. SOURCE_LOCK.json fixes all referenced versions.

## Verification

Run `python verify.py --write` in this directory to regenerate
CERTIFICATE.json, or `python verify.py` to compare it byte-semantically
as parsed JSON with an independent recomputation. The verifier uses
only the Python standard library. It checks exact polynomial algebra,
finite arithmetic tables, sparse-component regression, and the local
countermodel. The all-r theorem is proved in the text; finite tests
are not extrapolated to arbitrary r.
