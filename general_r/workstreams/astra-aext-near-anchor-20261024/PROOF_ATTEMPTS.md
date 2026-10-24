# Attempts and exact stopping points
Status: PARTIAL.

1. Re-extracted the minimum anchor, exact pivot identity, induced normalization, and genuine-clique deletion from the original colouring. All cross-layer edges remain in the ledger. Integer a is a valid terminating potential. It supplies no reason to skip a>=6.

2. Strengthened the contextual cap comparison by imposing second-Turan on the target as well as all non-target colours. Exact residual excess is L_a(r)=r*(binom(a-1,2)-2)+2a. For a=6 it is 8r+12. Increasing r cannot reverse this sign.

3. Tried to strengthen individual non-target floors using omega<=a and inherited D_r caps. The explicit H_(a,r) in THEOREM section 5 disproves any universal increase above p_r(ar+1)+a-1 under precisely those assumptions. Its r original a-cliques and one extra vertex also mimic a single colour's z_i=1 label partition. No simultaneous predecessor colouring has been constructed.

4. Checked CHAT A's near-complete transversal-design route. Its theorem fixes a while r grows. The prerequisites include r>=binom(a,2)+a+1 and a genuine predecessor. These do not cover arbitrary a<=r-1. In particular substituting a=r-1 makes that numerical prerequisite fail for every r>=4, and no predecessor is guaranteed at the initial state. This is a scope obstruction, not a refutation of the fixed-a theorem.

5. Checked CHAT H's well-founded potential (r^2+2)a+n and symbolic recurrence. Strict descent of dependencies proves the recurrence can be evaluated. It does not establish its required lower-bound dominance over every outer budget. Finite r=12 seeds cannot be substituted without an all-r proof.

6. The contextual 4r+1 cap itself is sound: U=2r^2+r+7. WITH delta>=r+1 its degree floor exceeds U by (3r-13)/2. The delta hypothesis and extraction legality remain separate obligations. This calculation does not eliminate high stops.

Next mathematical task: exploit the impossibility of simultaneously packing the near-extremal colour graphs/label systems, or prove an induced descent that works without a predecessor. Do not strengthen a demonstrably sharp single-colour bound or invoke D_low to conceal this gap.
