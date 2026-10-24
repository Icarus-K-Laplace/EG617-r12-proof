# Forcing-to-master contract: proved coverage and exact open bridge

Status: **PARTIALLY PROVED; FULL FORCING-TO-MASTER BRIDGE OPEN**.  
Scope: fixed r=12 legal R(4,49) backend, with the front-end E407/E408 terminal kept as a separate obligation.

This file does not rename the remaining gap as a theorem. It separates the structural machinery already proved under explicit contracts from the exact extraction statement still required for every arbitrary maximal-pivot shell.

## 1. Frozen maximal-pivot contract

Let F be a legal 49-point residual satisfying

- `alpha(F)<=4`, `omega(F)<=11`, `delta(F)=13`;
- all inherited induced-set caps;
- for every degree-13 pivot p, its 35-point core H has `alpha(H)<=3`, `omega(H)<=11`, `delta(H)>=12`.

Choose p lexicographically maximal in `(q,tau)`. With shell A, missing graph M, and core H,

`E=91+q+e(H)`.

For a regular shell vertex y, write `S_y=N_M(y)`, `D_y=N_H(y)`, `d_y=|S_y|=|D_y|`. The exact row formula is

`q_y=d_y(13-d_y)+B_y+kappa(D_y)+mu(D_y)+e_F(S_y,D_y)`,

with every term after the base term nonnegative. Hence every legal row has `q_y<=q`, but this alone does not imply common missing sets or low cross-density.

## 2. The anchor branch is genuinely closed

If a legal 35-core contains three pairwise nonadjacent degree-12 vertices, then the connector/excess chain

- `GLOBAL_THREE_ANCHOR_EXCESS_LOWER_BOUND.md`;
- `GLOBAL_THREE_ANCHOR_K4_EQUALITY_CLOSURE.md`;
- `GLOBAL_THREE_ANCHOR_K6_FULL_CLOSURE.md`;

gives `K>=8`, equivalently `e(H)>=214`. Therefore

> **Anchor envelope:** `q<=E-305`.

This part is proved under the stated core contract. What is not automatic is the existence of those anchors in every arbitrary survivor.

## 3. The common-S master theorem is conditional, but strong

For a common-S owner family with support size d, row allowance a, charge `w_v=kappa_v+e_F(v,S)`, and row closure `e_H(v,D)<=w_v`, the following are proved under their exact contracts:

1. Boundary one-loss rows `Delta(D)=d-1` with the relevant low-cross bounds enter the Global Support-Compatibility Master Theorem.
2. Three zero-charge incidence signatures give three independent degree-12 anchors.
3. At most two signatures collapse the boundary one-loss system to at most three canonical sunflower patterns.
4. Hereditary packing bounds each nontrivial pattern's owner multiplicity (d2 at most9; low-charge d3 at most8).
5. The first-high-slack decomposition controls the plateau, exact one-loss and deeper-loss layers when `a=d`.

The dependencies are `backend/GLOBAL_SUPPORT_COMPATIBILITY_MASTER_THEOREM.md`, `GLOBAL_FIRST_HIGH_SLACK_MASTER_REDUCTION.md`, `GLOBAL_FORCING_TO_MASTER_ALLOWANCE_COVERAGE.md`, and the linked signature/transversal/packing theorems.

**Contract warning:** the master theorem assumes a common-S family, boundary one-loss equality, and the appropriate low-cross bounds. It does not prove that every arbitrary shell survivor has these properties.

## 4. Exact common-S coverage already available

For a common-S family with `s=|S intersect X|<d`, let `ell_y=q-q_y` and `a` be the ambient allowance. The loss-layer theorem proves:

- `ell_y>a-(d-1)`: the support is disjoint from every distinct support class;
- `ell_y=a-(d-1)`: every proper overlap is endpoint-saturated and all shared charge is zero;
- only `1<=ell_y<=a-d` can retain genuine shallow-loss overlap freedom for repeated supports.

Thus the known common-S residual windows are exact:

| support size | already covered common-S regimes | remaining common-S window |
|---:|---|---|
| d=2 | `a<=1` subcritical; `a=2` first-high-slack decomposition | `a>=3`, repeated rows with `1<=ell<=a-2` |
| d=3, non-triangular S | `a<=2` subcritical; `a=3` first-high-slack decomposition | `a>=4`, repeated rows with `1<=ell<=a-3` |
| d=3, S an independent triple | allowance through `a<=6` enters the anchor envelope via the independent-triple theorem | only `a=7,8` can remain; the no-anchor transport equality patterns are (1,1,2) at a=7 and (1,1,3)/(1,2,2) at a=8 |
| d=4 or d=9, q<=38 | non-fully-decorated systems are subcritical; fully-decorated multi-leftover Bridge C is closed | no new common-S Bridge-C case remains |

The d3 triangle statement uses `GLOBAL_INDEPENDENT_TRIPLE_MIN_ANCHOR_THEOREM.md`, `GLOBAL_INDEPENDENT_TRIPLE_H3_THEOREM.md`, and the exact anchor-transport identity. For `a=7,8`, if any transported excess is zero or any support intersection creates a zero transported degree, the anchor branch applies; only the all-positive listed distributions avoid that immediate route.

This table is exhaustive **inside the stated common-S / decoration contracts**, not for arbitrary multi-S shell systems.

## 5. New multi-S d3 extraction theorem through q=38

The new workstream theorem `R12_D3_MULTIS_EXTRACTION_BOUND.md` proves a useful extension of the q32 extraction:

- any family Y of regular d3 shell vertices is a target clique, so `N=|Y|<=10`;
- all missing triples lie in `Q=A\Y`;
- if a common-S class has size n, then its common-S allowance obeys
  `a_S<=q-30-N+n`;
- hence every nonempty class has `n>=N+30-q`.

Examples:
- N=9, q<=34: all nine rows have one common missing triple;
- N=9, q=35: at most two classes, each subcritical;
- N=9, q=36: at most three classes; only a class of size at least6 can reach allowance3;
- N=9, q=38: classes of size at most3 are subcritical, and a size-4 class has allowance at most3.

This is a genuine extraction/allowance theorem. It still leaves lower owner counts, fully-decorated classes, and the macroscopic shallow-loss classes to their separate contracts.

## 6. The new `R12_D3_DISJOINT_SUPPORT_COMPATIBILITY.md` sharpens the disjoint-support branch: if two d3 supports are disjoint and their missing triples differ, then the exact second-view charge gives `e_H(D_i,D_j)<=q-36`. Hence the distinct-type block transversal has at most 3 blocks for q=36,37 and at most 6 for q=38; for q<=35, every disjoint-support subsystem is common-S. This reduces the disjoint-support multi-S branch to a bounded number of distinct missing-set types, but repeated blocks inside one common-S class remain governed by the shallow-loss contracts below.

## 6. The multi-S identity does not by itself close extraction

Without a common-S assumption, `GLOBAL_MULTI_S_REPIVOT_COMPATIBILITY.md` proves the exact identity

`sum_y(q-q_y)=sum_y a_y-Phi_multi`,

where

`Phi_multi=sum_v lambda_v kappa_v + sum_y mu(D_y) + sum_y e_F(S_y,D_y)`,

and

`g_v>=kappa_v+lambda_v-1`.

It also gives the repetition-to-loss inequality. These are global accounting constraints, but the charges depend on the row missing sets and do not supply one shared incidence-signature partition. The identity alone does not imply one common S, three zero-charge signatures, or the low-cross hypotheses required by the master theorem.

## 7. Exact unresolved forcing contract

The missing theorem must begin with the frozen maximal-pivot contract in Section 1 and cover **all** regular shell rows, not just a selected common-S subsystem.

For each active row y define

- `S_y`, `D_y`, `d_y`;
- `B_y=e_M(T_y)+G_(T_y)`;
- `a_y=q-d_y(13-d_y)-B_y`;
- `kappa_v=d_H(v)-12`, `lambda_v=#{y:v in D_y}`;
- `mu_y=C(d_y,2)-e_H(D_y)`.

The accepted constraints include

`q-q_y=a_y-kappa(D_y)-mu_y-e_F(S_y,D_y)>=0`,

`sum_y(q-q_y)=sum_y a_y-Phi_multi`,

`g_v>=kappa_v+lambda_v-1`,

plus the all-pivot row-closure and exact decoration-transport identities.

**Required conclusion:** prove that every such legal survivor satisfies at least one of:

1. a legal core contains three pairwise nonadjacent degree-12 vertices, so `q<=E-305`);
2. an active subsystem has one common S, `s<d`, and the exact boundary one-loss/low-cross contract, or descends to it through a rigorously bounded finite higher-slack equality layer;
3. a finite incidence kernel is obtained with every constraint derived from the original graph contract, and that kernel is independently eliminated.

The current assets prove this conclusion only for specific subfamilies (including the q<=38 d3 large-owner cases above), not for every legal survivor.

### Minimal open variables / barriers

- **Multi-S extraction:** no proof yet covers all d2 systems or d3 systems with fewer owners / fully decorated classes at every q layer.
- **Low-support shallow loss:** d2 `1<=ell<=a-2`; d3 non-triangular `1<=ell<=a-3`; plus the d3 triangular `a=7,8` near-anchor equality distributions.
- **Low-cross certification:** for an extracted family, the pairwise cross bounds used by the block-transversal theorem must be derived from its actual allowance/exchange identities, not assumed.
- **Fully-decorated branch:** `s=d` cannot be passed through the `s<d` plateau/strict-loss lemmas. The d4/d9 common-S escape is closed, but this is not a general extraction theorem for every fully-decorated d2/d3 multi-S system.

This is the smallest current theorem-level gap statement supported by the inspected assets. It does not certify E335--E340, E407/E408, or the original EG617 theorem.
