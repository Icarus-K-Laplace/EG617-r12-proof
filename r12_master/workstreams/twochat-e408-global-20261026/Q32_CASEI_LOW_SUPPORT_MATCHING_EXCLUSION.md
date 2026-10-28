# E408 Q32 — Case-I low-support matching exclusion

Date: 2026-10-28  
Status: **PROVED_CONDITIONAL under the registered E408 Q32 / exact-129 factor / Case-I shell contract.**

## 1. Contract

Use the Q32 notation of `Q32_CORRECTED_NONFULL_SUPPORT_MULTIPLICITY.md` and the source-registered shell split in `SHELL_SUPPORT_CLASSIFICATION.md`.

Let A=N_F(p), |A|=13, and M=bar(F[A]). In **Case I**, M contains an independent 10-set B. Put S=A\B, so |S|=3 and M[B]=empty.

Let U be the union of all single-outside exact-color core-4 witnesses and W=H\U. Let m in {8,9,10} be the number of exact-129 colors. For w in W, let n_w count exact colors whose Type-I special vertex x_C equals w.

## 2. Matching lemma at one uncovered core point

### Lemma 2.1

For every w in W,

\[
\boxed{\nu(M)\ge m-n_w},
\]

where nu(M) is the matching number of the shell missing graph M.

### Proof

Fix an exact color C with x_C != w. As in the corrected multiplicity theorem, w lies in one of the twelve color-C K5s. Since w is not in U, this K5 cannot be single-outside. Therefore it contains at least two shell vertices from A. Any two such shell vertices are joined by a color-C edge, hence by an edge of M.

Choose one shell edge e_C from that K5.

For two different exact colors C,D with x_C != w and x_D != w, the chosen shell edges e_C and e_D are vertex-disjoint. Indeed, if they shared a shell vertex a, then wa would simultaneously be a color-C and a color-D edge because w and a lie in both corresponding monochromatic K5s. Edge-color uniqueness forbids this.

Thus the edges e_C form a matching of size m-n_w in M. QED.

## 3. Case-I matching cap

Because M[B]=empty and S=A\B has only three vertices, every edge of M touches S. Hence every matching in M has size at most three:

\[
\boxed{\nu(M)\le3.}
\]

Combining with Lemma 2.1 gives, for every w in W,

\[
\boxed{n_w\ge m-3.}\tag{3.1}
\]

Each exact color has only one special vertex, so

\[
\sum_{w\in W}n_w\le m.
\]

Therefore

\[
|W|(m-3)\le m.\tag{3.2}
\]

## 4. Exclude v=44 and v=45 in Case I

If v=44, then |W|=3. Equation (3.2) gives

\[
3(m-3)\le m,
\]

or 2m<=9, impossible for m>=8.

If v=45, then |W|=2. Equation (3.2) gives

\[
2(m-3)\le m,
\]

or m<=6, again impossible for m>=8.

Hence

\[
\boxed{\text{Case I }\Longrightarrow |U|\ge46.}
\]

This conclusion is uniform over m=8,9,10.

## 5. The v=46 Case-I residue

If v=46, W={w}. The same argument gives

\[
n_w\ge m-3.
\]

Thus all but at most three exact colors must use the unique uncovered core point w as their Type-I special vertex. This is a rigid surviving terminal but not yet a contradiction.

## 6. Firewall

- No 284-edge identity is used.
- No degree-9 special vertex is used.
- No exceptional-vertex injectivity is assumed.
- No assumption M[B]=empty is transferred to Case II. The theorem is explicitly Case I only.
- The result does not exclude Case II (alpha(M)<=9), nor v=46,47 in Case I.

Current consequence: the Q32 source split can be sharpened to

- Case I: v>=46;
- Case II: v>=44, with v=44,m=10 already excluded by the corrected multiplicity theorem.
