# Dependency audit — E408 global incidence sprint

Updated: 2026-10-27

## 1. Source branch heads checked

| Source | HEAD checked | Role |
|---|---|---|
| workstream/r12-e408-q33-global-compat-20261025 | 0cb2ff3968f005c9cb255958df7c02b220678701 | Q33 seven-block ledger and 31-point/56-witness terminal |
| workstream/r12-e408-q32-excess6-20261025 | a0ba6db26c7e8b00a4217dcbcbf298895dff93ce | Q32 285-edge / Type-I / shell-support source |
| workstream/r12-unified-witness-capacity-20261025 | faa8183c150dd78b000d0957fa8a63cebd52e146 | labelled witness-capacity audit only |
| workstream/r12-witness-packing-chat-20261025 | f5d3daa07403877ede9885e1bd5c2f46b16d81da | witness-packing sibling |
| workstream/r12-zero-excess-witness-20261025 | c8c4833c7830370a703d228ee23e3b88484d6baa | zero-excess sibling |
| workstream/r12-ultimate-closure-20261024 | 1aa47d10edd5ece2b73a0891af7ac2ce37ecbb40 | root proof DAG / retained contracts |

Sibling workstreams remain read-only.

## 2. Q33 local profile ledger

- (6,2,1^5): PROVED_CONDITIONAL excluded.
- (7,1^6): PROVED_CONDITIONAL excluded.
- (4,4,1^5), (4,3,2,1^4): locally OPEN in the all-component-edge-present branch.

These last two are bypassed by the global Q33 terminal contradiction; no colorwise P_C<=48 theorem is claimed.

## 3. Historical inference firewall

The statement that a monochromatic K12 has no external edge of its own color is false; the correct bound is at most one such edge from an outside vertex. None of the load-bearing Q33/Q32 closures below uses the false statement.

## 4. Q33 dependency chain

`Q33_M10_EXACT_COLOR_CAPACITY_EXCLUSION.md` proves m!=10 and h<=4 under the registered 31-point/56-witness Q33 terminal.

`Q33_NONEXACT_U_RESERVE_CLOSURE.md` proves:

1. every non-target color on U has at least p_12(31)=26 edges;
2. 56-h selected component witnesses own 336-6h distinct exact-color U-edges;
3. all nonexact colors together have at most delta+6h U-edge slots;
4. therefore 26(11-m)<=delta+6h;
5. with delta<=17,h<=4 and m in {8,9}, the available maximum41 is below the required52 or78.

Status: **PROVED_CONDITIONAL impossible** for the registered Q33 minimum-support terminal.

No sharing/double-counting gap was found: component witness K4 edges are uniquely exact-colored; gadget witness edges are deliberately left free in the generous capacity upper bound.

## 5. Q32 dependency chain — support audit

The Q32 source contract is 47 core vertices, 285 target edges, total core excess six, q=32. The sibling proves |U|>=44.

This branch proves `Q32_GLOBAL_EXCEPTIONAL_INJECTIVITY.md`: exact Type-I exceptional vertices are globally distinct.

`Q32_NONFULL_SUPPORT_SHELL_CAPACITY.md` then excludes every nonfull support v=44,45,46 by showing any w outside U would require at least 2(m-1)>=14 distinct shell neighbors in a 13-point shell. This theorem is valid, but the final Q32 closure no longer depends on support size.

## 6. Q32 dependency chain — decisive exact-color-count theorem

Load-bearing theorem: `Q32_EXACT_COLOR_COUNT_COLLAPSE.md`.

### 6.1 External extremal input

For a graph G with alpha(G)<=r, omega(G)<=5 and n>5r, the complement is K_{r+1}-free and non-r-partite. Brouwer/Kang--Pikhurko therefore gives

\[
e(G)\ge p_r(n)+\lfloor n/r\rfloor-1.
\]

The proof uses this at (n,r)=(58,11),(57,11),(53,10). It also uses the elementary Turan floor p_8(49)=126.

### 6.2 Internal pointwise inputs

The independently proved full-color degree theorem gives:

- exact129: degree >=4, with Type-I exceptional degree9;
- 130-edge (s=1): degree >=3;
- 131/132-edge (s>=2): degree >=2.

The Q32 injectivity theorem makes exact exceptional vertices distinct.

### 6.3 Derived low-degree structure

- 131-edge colors actually have minimum degree >=3.
- Degree-3 vertices of a 130-edge color form isolated K4 components.
- Two isolated K4s in a 130-edge color are impossible: deleting them leaves 53 vertices and118 edges, below the Brouwer lower bound119 for alpha<=10,omega<=5. Hence at most four degree-3 vertices exist.
- Degree-2 vertices of a 132-edge color form isolated K3 components; four triangles would leave49 vertices,120 edges with alpha<=8, below p_8(49)=126. Hence at most nine degree-2 vertices exist.

### 6.4 Exact-color-count collapse

Outer equality forces m in {8,9,10}.

- m=10: ten distinct exact exceptions force ten degree-2 vertices in the sole132-edge color; capacity is at most9. Contradiction.
- m=9: nine exceptions force nine degree-3 vertices in the130-edge color; capacity is at most4. Contradiction.
- m=8: each of eight exceptions requires at least two degree-3 incidences among three130-edge colors, demand16; total capacity is at most3*4=12. Contradiction.

Thus all possible m are excluded and the registered E408 Q32 terminal is **PROVED_CONDITIONAL impossible**.

Arithmetic regression: `verify_q32_exact_color_count_collapse.py`.

## 7. Contract firewalls

Q33 closure does not use:
- Q32's 285-edge core;
- support-41;
- the false K12 external-isolation claim.

Q32 closure does not use:
- Q33's 284-edge core or U=31 identities;
- support-41;
- an M[B]=empty shell split;
- any SAT/ILP nonexistence claim.

The unified support-41 theorem remains separate and non-load-bearing.

## 8. Promotion scope

- Registered E408 Q33 terminal: **PROVED_CONDITIONAL impossible**.
- Registered E408 Q32 terminal: **PROVED_CONDITIONAL impossible**.
- Under the current registered E408 reduction ledger, this branch has no remaining E408 terminal.
- The original EG617(r=12) theorem is **OPEN / NOT_CERTIFIED** because E407, the K145-to-T61/front-end bridge, and other sibling backend obligations are outside this workstream and retain their own statuses.