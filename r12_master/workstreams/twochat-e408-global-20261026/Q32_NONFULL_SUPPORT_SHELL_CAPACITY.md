# E408 Q32: all nonfull witness supports are impossible

Date: 2026-10-27  
Status: **PROVED_CONDITIONAL** under the registered Q32 285-edge residual contract, exact-129 Type-I classification, and the definition of U as the union of all exact-color single-outside K5 witnesses.  
Conclusion: \(|U|=47\). Combined with the sibling support floor, this closes \(v=44,45,46\) simultaneously.

## 1. Exact-color decomposition outside the witness union

For an exact-129 color C, the Type-I factor consists of twelve disjoint K5 cliques and an exceptional vertex x_C.

Every K5 clique meets the 14-point set \(\{p\}\cup A\), because \(\alpha(H)\le4\). The shell-support classification gives exactly one of:

1. x_C∈H, ten K5s have exactly one outside-H vertex and two K5s have two outside-H vertices;
2. x_C∉H, eleven K5s have exactly one outside-H vertex and one K5 has two outside-H vertices;
3. x_C∈H, eleven K5s have exactly one outside-H vertex and one K5 has three outside-H vertices.

Deleting the unique outside vertex from every single-outside K5 gives all ten or eleven four-point witnesses of C. Thus, if a core vertex w does not lie in U, then for every exact color C exactly one of the following holds:

- w=x_C; or
- w lies in the core part of a K5 with at least two outside-H vertices.

A multi-outside non-target K5 cannot contain p together with a shell vertex a∈A, because pa is a target-color edge. Therefore every outside-H vertex of such a K5 lies in A. Consequently, in the second alternative w has at least two distinct C-neighbors in A.

## 2. Exceptional injectivity

By `Q32_GLOBAL_EXCEPTIONAL_INJECTIVITY.md`, a residual vertex can be x_C for at most one exact color. Hence for any w∈H\U, among the m≥8 exact-129 colors at least m−1 colors put w in a multi-outside K5.

For each such color, w has at least two C-colored neighbors in A. For two different colors these shell neighbors cannot reuse the same vertex a∈A, because the edge wa has a unique color. Therefore w would need at least
\[
2(m-1)\ge14
\]
distinct neighbors in the 13-point set A.

Contradiction.

Thus
\[
\boxed{H\setminus U=\varnothing},
\qquad\boxed{|U|=47}.
\]

## 3. Consequences

The sibling Q32 capacity theorem previously gave only |U|≥44. The new shell-neighbor capacity closes all three nonfull supports:
\[
\boxed{|U|\notin\{44,45,46\}}.
\]
The sole remaining Q32 support terminal is
\[
\boxed{U=H,\quad |U|=47.}
\]

This strictly subsumes the earlier v=44 exceptional-degree closure and the v=45 two-point reduction, although those proofs remain valid independent cross-checks.

## 4. Firewall

No Q33 284-edge equation is used. The proof uses only:
- the Q32 exact-129 Type-I equality structure;
- the shell-support classification of single/double/triple outside K5 cliques;
- the exact definition of U as the union of all single-outside core K4 witnesses;
- global exceptional-vertex injectivity;
- unique edge ownership;
- |A|=13 and m≥8.

The remaining task is the full-support v=47 Q32 terminal.