# Integration 1 source map

Status: provenance / consolidation map. Integration 1 is a historical source bundle, not itself a blanket proof certificate.

The complete Integration 1 upload has been inspected against the current canonical DAG. The following source regions contain mathematically useful proof bodies that are accepted only through the reconstructed files named below.

## Backend core and low layers

### CORE211

Integration 1 pp. roughly 389--392 (file `EG617 r12_整合1版_385-448`, local pages 5--7 and again local pages 22--24) contains the modern 210-edge contradiction:

1. establish the inherited minimum-degree input `delta(H)>=12` for `H in R(3,35)`;
2. if `e(H)=210`, H is 12-regular;
3. `L=bar(H)` is a 35-vertex 22-regular K4-free graph with `alpha(L)<=11`;
4. since `22 > (5/8)35`, Andrasfai--Erdos--Sos makes L 3-partite;
5. a part has size at least 12, contradicting `alpha(L)<=11`.

This proves `e(H)>=211` once the minimum-degree input has been independently licensed.

### E329 / E330

The same volume gives the short modern closure:

- E329 forces `(q,e(H))=(27,211)` or `(28,210)`; CORE211 removes the latter, and uniform q27 removes the former.
- E330 permits `(27,212)` or `(28,211)`; any q28 pivot has an undecorated missing-degree-3 witness whose repivot raises q by at least 2, contradicting CORE211 at the new pivot; hence all pivots would be q27, again impossible.

### Generic q29 good repivot and E331

Integration 1 pp. roughly 423--432 (file `385-448`, local pages 38--43) gives a clean generic q29 theorem. It explicitly derives

`q_y-q >= d(13-d)-[t(S)-e_M(S)]`

from `delta(H)>=12` and then handles all three missing-graph cases:

1. M contains K4;
2. M is triangle-free;
3. M contains a triangle but no K4.

The existence theorem does not use `e(H)=211`. The number 211 is used only after repivot, in the E331 fixed-edge-layer contradiction.

### E332 reduction

Immediately after E331, Integration 1 derives that any E332 survivor must contain a degree-13 pivot with

`q=30, e(H)=211`.

This matches the current canonical E332 frontier.

## Front end / T61

Integration 1 pp. roughly 449 onward reconstructs an earlier version of the h13 ladder:

- E397, E398, E399 closures;
- q24/q25 shell classifications;
- an analytic q26 attempt;
- the older O61/E405 q30 equality analysis.

The current repository files `front_end/E398_Q23_SHELL.md`, `front_end/E399_Q24_SHELL.md`, `front_end/E400_Q25_SHELL.md`, and `front_end/T61_H13_LOW_LAYER.md` supersede these historical formulations and should be cited for the modern proof.

## q30 historical outer equality machinery

Integration 1 pp. 577--636 contains the older 47-core q30 equality analysis, including equal-or-disjoint row classes and a full-colour contradiction. It is useful as a structural template only. Its core size, edge count, independence cap, and edge-threshold contract differ from the active backend E332 q30+211 system.

## Provenance rule

Do not cite an Integration 1 page as a canonical theorem merely because it says CLOSED/PROVED. Canonical use requires either:

- a current standalone proof file in this repository; or
- an explicitly named inherited theorem/certificate with scope and provenance.
