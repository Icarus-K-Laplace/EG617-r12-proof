# E408 Q32: close the remaining v=45 and v=46, m=9 rows

Date: 2026-10-28
Status: PROVED_CONDITIONAL under the registered 285-edge Q32 contract, corrected Type-I/multiplicity theorems, valid nonexact degree floors, and `Q32_130_NO_CORE_ONLY_DEG4.md`.

## 1. Imported local obstruction

The source-correct 130-edge theorem proves that no vertex u in H can have degree four in a 130-edge non-target color D while all four D-neighbors of u lie in H. Its proof is recorded locally in `Q32_130_NO_CORE_ONLY_DEG4.md`.

The valid pointwise nonexact floor for m=9 is `L_9=7`: the 130-edge color has minimum degree four, and the 131-edge color has minimum degree three. Any upstream summary that assigns the 130-edge color only a degree-three floor and states `L_9=6` is stale for the current theorem stack.

## 2. Support v=45, m=9

Here `W={w1,w2}`. The corrected zero-shell multiplicity theorem and pointwise budget force, at each W-point:

- exactly four exact colors have special point w;
- all four special parameters are a=4;
- the target color has no w–A edge, so the core excess at w is one;
- five non-special exact colors use exactly two w–A edges each;
- three special exact colors use one w–A edge each;
- the remaining special exact color uses no w–A edge and owns pw;
- neither nonexact color uses a w–A edge;
- the nonexact degrees at w are four for the 130-edge color D and three for the 131-edge color.

Because the zero-shell special color owns pw, the 130-edge color D does not own pw. It also has no neighbor from w into A. Thus d_D(w)=4 and all four D-neighbors of w lie in H.

This contradicts `Q32_130_NO_CORE_ONLY_DEG4.md`. Therefore

> **Q32 / v=45 / m=9 is CLOSED.**

This argument does not need the separate W-pair rigidity step or the 731-edge U-complement accounting; those remain useful cross-checks but are no longer load-bearing for the contradiction.

## 3. Support v=46, m=9

Here `W={w}`. The same source-correct zero-shell bound forces exactly four special exact colors at w, all with a=4, and target shell degree zero. The five non-special exact colors consume ten w–A edges; three special colors consume one each; the unique zero-shell special color owns pw. Both nonexact colors have no w–A edge, and the 130-edge color D has degree four at w while the 131-edge color has degree three.

Again D cannot own pw because the zero-shell special exact color owns it. Therefore all four D-neighbors of w lie in H. This is a core-only degree-four vertex in a 130-edge color, contradicting `Q32_130_NO_CORE_ONLY_DEG4.md`.

Therefore

> **Q32 / v=46 / m=9 is CLOSED.**

## 4. Updated non-full-support frontier

The source-correct branch results now close all m-cases at v=45 and v=46:

- v=45: m=8 closed by weighted special-incidence capacity; m=9 by the no-core-only degree-four theorem; m=10 by zero-shell multiplicity.
- v=46: m=8 closed by weighted special-incidence capacity; m=9 by the no-core-only degree-four theorem; m=10 by zero-shell multiplicity.
- v=44: closed for m=8,9,10 in the sibling workstream.

No retracted degree-nine premise or exceptional-vertex injectivity is used. The only remaining Q32 support size is full support `|U|=47`, which remains OPEN.
