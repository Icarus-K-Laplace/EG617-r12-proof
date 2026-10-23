# Global d=3 A2 Two-Block M=7 Closure

Status: `PROVED_ANALYTIC`.

Dependencies:

- `GLOBAL_D3_A2_TWO_BLOCK_INCIDENCE_BUDGET.md`;
- common-S row closure;
- `alpha(H)<=3`.

Purpose: remove the highest-weight maximal-matching window in the final fully-decorated q32 d3 equality state.

## 1. Setup

Let D,E be a maximal disjoint support pair in the final nine-owner fully-decorated allowance-two system.

Write

`M=m_D+m_E`,

and let b be the total owner multiplicity on bridge support classes meeting both D and E.

The global two-block incidence budget is

`2M+b+e_H(D union E)<=17`.                                  (M1)

Every d3 support at allowance2 has at least one internal target edge.

Assume for contradiction

`M=7`.

Then

> `b+e_H(D union E)<=3`.                                    (M2)

Since D,E are disjoint and each has an internal edge,

`e_H(D union E)>=2`.

Thus `b<=1`.

## 2. The case b=1

If b=1, (M2) gives

`e_H(D union E)<=2`.

Hence equality is forced:

- `e_H(D)=e_H(E)=1`;
- `e_H(D,E)=0`.

A one-edge 3-support has missing-edge defect2. Since the row allowance is2, its common-S charge is zero.

Each of D,E therefore contains an internal target-nonedge pair, and the two supports are target-anticomplete.

Choosing an internal nonedge pair from each gives an independent4-set in H, contradicting `alpha(H)<=3`.

Therefore

> `b!=1`.                                                     (M3)

## 3. The case b=0

Now (M2) gives

`e_H(D union E)<=3`.                                        (M4)

Let

`e_D=e_H(D)`, `e_E=e_H(E)`.

Each lies in `{1,2,3}`.

If either support has one internal edge, say e_D=1, then its support charge is zero. Row closure therefore gives

`e_H(D,E)=0`.                                                (M5)

If also `e_E<=2`, both D and E contain internal nonedge pairs. Together with (M5), the two pairs form an independent4-set.

Thus avoiding independent4 would require `e_E=3`, i.e. E is a target K3. But then

`e_H(D union E)>=1+3=4`,

contradicting (M4).

Therefore neither support can have one internal edge.

Hence

`e_D,e_E>=2`,

so

`e_H(D union E)>=4`,

again contradicting (M4).

Thus the case b=0 is impossible.

## 4. Conclusion

Both possible bridge multiplicities have been excluded.

Therefore

> **M=7 two-block closure:**
>
> no maximal disjoint support pair in the final fully-decorated q32 d3 equality state can carry seven owners.   (M6)

Equivalently

> `m_D+m_E<=6`.                                               (M7)

Since the full system has nine owners, every maximal disjoint pair leaves at least three owner rows on support classes meeting its six-point transversal.

This is a strict strengthening of the general two-block incidence budget and is another step toward the weighted two-block bridge theorem.
