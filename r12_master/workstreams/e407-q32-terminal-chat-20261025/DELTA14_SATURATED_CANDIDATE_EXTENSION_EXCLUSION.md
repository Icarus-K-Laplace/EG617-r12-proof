# Audit correction: candidate-specific saturated extension exclusion

Date: 2026-10-25  
Status: **WITHDRAWN AS A PROOF.** The prior version claimed that the explicit ((5,5,2,1,2)) blow-up local model has no 47-core extension for every (epsilon_Uin{0,1,2}). That conclusion was not established because two common-neighbour cardinality bounds were invalid.

## 1. Invalid inference

The prior proof used
[
|S_P|le 11-|P|,
qquad S_P={uin U:u	ext{ is adjacent to every vertex of }P},
]
as a bound on the total number of common neighbours of a clique part (Psubseteq W), based only on (omega(H)le11). This is false: (S_P) need not itself be a clique. The clique-number condition bounds the size of a clique inside (S_P), not (|S_P|) itself.

This invalidates:
- the (epsilon_U=1) exclusions for (H[W]=K_3dotcup3K_5) and (H[W]=3K_4dotcup K_6), which used total cover bounds of 26;
- the final (epsilon_U=2) contradiction, which treated (7,6,6) as cardinality capacities for all common neighbours of the three W parts and then counted the four (C/E) vertices together with (d_0) as consuming a single common-neighbour capacity.

The latter is invalid for the same reason: (d_0) is anticomplete to (Ccup E), so these five common neighbours are not a clique. A cardinality budget cannot be inferred from (omega(H)) alone.

## 2. What remains valid

The following limited deductions survive the audit, under the stated 47-core contract and the explicit local candidate:

1. The local candidate has (d_{H[U]}(d_0)=10), so
   [
   d_H(d_0,W)=2+epsilon_{d_0}.
   ]
2. Brouwer/Turán profile arithmetic gives the listed W profiles for each (epsilon_U), conditional on the retained hypotheses.
3. For (epsilon_U=1), the ((4,4,5,5))-part profile with one W-cross-edge is excluded: (d_0) has at most three W-neighbours, and the four clique parts have an independent transversal avoiding those neighbours, producing an independent 5-set.
4. For (epsilon_U=2), (e(H[W])=32) forces (H[W]=K_4dotcup K_4dotcup K_5dotcup K_5); the degree of (d_0) forces (epsilon_{d_0}=2) and (d_0) complete to a K4 part.
5. In that (epsilon_U=2) profile, the pairwise-independent-set argument for (ain A,bin B,d_0) does establish that no A/B pair can be assigned to the same W part or to the (d_0)-neighbour K4. Since A and B are cliques, the per-side clique bounds then force one of A/B to be assigned entirely to the other K4, while the other side is assigned across the two K5 parts. This does **not** yet contradict the full core constraints.

The arithmetic verifier only checks finite profile/counting arithmetic; it does not verify the invalid common-neighbour bounds or establish graph nonexistence. Its output must not be cited as certification of the withdrawn theorem.

## 3. Correct current status

- (epsilon_U=0) for the explicit local candidate: excluded by the independent-transversal proof in DELTA14_SATURATED_TRANSVERSAL_REDUCTION.md.
- (epsilon_U=1): the one-cross-edge W profile is excluded; the two no-cross-edge profiles are **OPEN**.
- (epsilon_U=2): the W profile and A/B assignment reduction above are established, but the full extension contradiction is **OPEN**.
- General saturated non-four-partite (delta=14) branch: **OPEN**, because the local 15-vertex graph (J) is not classified.
- (deltale13), all five shell templates, and the original (K_{145})-to-T61 bridge: **OPEN / NOT_CERTIFIED**.

No claim that E407 Q32 or EG617((r=12)) is solved is made.
