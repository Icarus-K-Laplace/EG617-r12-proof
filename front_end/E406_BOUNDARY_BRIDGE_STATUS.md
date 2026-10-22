# E406 boundary-bridge status

Status: `LOCAL_BOUNDARY_COMPLETE / GLOBAL_BRIDGE_OPEN`.

This file records the exact remaining obligation for the T61 `E=406`, `delta=13` parent after the assistant-owned coexistence analysis.

## 1. Global charge window

For every degree-13 pivot p,

`406 = 91 + q_p + e(C_p)`

with the 47-core floor `e(C_p)>=284`. Hence

`22 <= q_p <= 31`.

The proved S31 theorem supplies at least one degree-13 pivot with

`q_p <= 30`.

## 2. Complete local boundary classification

Assume there is an adjacent legal repivot edge

`q=30 -> q=31`.

The exact q30/q31 exchange reduction shows that its missing distance must lie in

`d in {1,2,3,10,11,12}`.

Each of these six classes is now `PROVED EMPTY` under the explicit E406 boundary contract:

- `d=1`: `front_end/E406_D1_FULL_CLOSURE.md`;
- `d=2`: closure chain `E406_D2_*`;
- `d=3`: complete Type-A/Type-B closure, including O5 and all O4 multiplicity families;
- `d=10`: `front_end/E406_Q31_PLATFORM_SUPPORT_RIGIDITY.md`;
- `d=11`: `front_end/E406_D11_FULL_CLOSURE.md`;
- `d=12`: `front_end/E406_D12_FULL_CLOSURE.md`.

Therefore

> **No legal q30--q31 pivot-graph boundary edge exists in E406.**

## 3. The only remaining E406 obligation

E406 is not yet upgraded to `PROVED EMPTY` solely because one global implication remains to be independently replayed/reconstructed:

> **Boundary-forcing bridge.** Every E406 parent satisfying the T61 hereditary-cap contract and S31 must produce an adjacent legal q30--q31 boundary edge.

The source-reported V6/V7 ladder claims exactly the ingredients needed for this bridge:

- low-charge promotion;
- q<=29 promotion to q30 in the licensed range;
- q30 no-immediate-rise classification and at-most-two-repivot promotion to q31.

However the current repository only stores summary/result files for V6/V7, not a complete independently replayed bridge proof. Hence the correct status is

`E406 = CONDITIONAL_EMPTY_ON_BOUNDARY_FORCING_BRIDGE`,

not yet canonical `PROVED EMPTY`.

## 4. Research target

Do not reopen any of the six distance classes. The sole assistant-owned target is now:

`E406 parent -> actual adjacent q30--q31 boundary edge`.

Once this implication is independently certified, E406 closes immediately by the six local closure theorems above.
