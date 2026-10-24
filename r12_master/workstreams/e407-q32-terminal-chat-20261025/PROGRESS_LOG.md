# E407 Q32 terminal — progress log

## 2026-10-25 — Round 1

### New mathematical result

**Proved conditionally:** the delta=16 minimum-support boundary is automatically four-partite and reduces to one labelled core kernel.

The proof uses the 49 linear K4 witnesses, the exact core ledger, Brouwer's second-Turan bound, equality in Turan on 18 vertices, and the total degree-excess budget. It excludes endpoint splits (4,1) and (3,2) for the five cross edges in H[U].

The sole surviving endpoint allocation is (5,0): all five distinct D-endpoints have the same K4 as their exact W-neighbourhood, and that K4 is complete to D. Each vertex in the other three W-components must be complete to a 7-part; labels may vary within a component, and no component-wide bijection is proved.

### Verification

Ran the local arithmetic/kernel audit script. Output: E407_DELTA16_STRUCTURAL_KERNEL_ARITHMETIC_OK.

The script checks exact edge ledgers, integer partition profiles, and finite excess inequalities. It does not verify graph realization, all graph-theoretic lemmas, or the original K145 theorem.

### Global effect

- New closed contracts: 1 structural reduction (delta=16 boundary).
- Fully excluded E407 templates: 0.
- Remaining E407 minimum-support branches: delta<=15 (four-partite and non-four-partite), plus the surviving delta=16 kernel.
- E408 Q32/Q33: untouched.
- Original T61-to-K145 bridge: still OPEN / NOT_CERTIFIED.

### Next attack

Combine the forced delta=16 part-to-component assignment with the exact row/hub requirements of templates A-E. In parallel, use the near-Turan classification for delta=14,15 to bound the remaining cross edges in H[W]. Do not claim any template closed until an actual incompatibility proof is obtained.
