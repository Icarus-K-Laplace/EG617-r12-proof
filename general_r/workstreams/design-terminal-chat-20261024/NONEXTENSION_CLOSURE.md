# Nonextension closure: exact identities and the remaining obstruction

## Status

- **PROVED_ANALYTIC:** exact affine/net nonextension under its exact partition hypotheses (upstream result).
- **PROVED_ANALYTIC:** the naive exact (RTD(5,r)+) one-point completion is invalid.
- **PROVED_ANALYTIC:** low-incidence off-hub defects force the HP-LI edit charge.
- **OPEN:** robust nonextension for every terminal satisfying the current near-design contract.
- **OPEN:** exclusion or global completion of high-incidence local traps.

## 1. Exact cross-pair budget

Let (a_j=|B_j|), (n=5r+1), and
[
C=\sum_{j<k}a_ja_k
]
be the number of cross-group pairs. Let (D) be the number of target-ideal internal edges deleted from the actual target graph, and (A) the number of actual target edges between distinct target groups. Let (S_{\rm non}=\sum_{i>0}s_i), and
[
\Delta_0=\sum_j\binom{a_j}{2}-p_5(n).
]
Then
[
s_0=\Delta_0-D+A,
\qquad
\boxed{A=C+D-(r-1)(10r+5)-S_{\rm non}.}
]
Using the exact total slack identity, this is equivalently
[
\boxed{A=9r+5-\Delta_0+D-S_{\rm non}.}
]
Since (s_0\ge r), one also has the exact necessary bound
[
\boxed{A\ge r-\Delta_0+D.}
]
These identities count each actual edge once. A target-deleted internal pair belongs to exactly one non-target color; it is not a target cross edge.

The cylinder lemma supplies a separate lower bound (A\ge H_r\) for each chosen target internal deletion, but those inequalities cannot simply be summed over all deletions: multiple deleted edges can share the same high-degree hub and reuse the same cross-edge star. This is why the bounded-hub conclusion does not imply (A=\Omega(rD)).

## 2. What exact nonextension currently proves

The existing exact affine/net result is usable only if its exact orthogonal-partition hypotheses have been established. The current terminal gives a partial resolvable (TD(5,r)) with (r^2-O(r)) clean blocks and a bounded set controlling target internal deletions. It does not give an exact net, nor two exact orthogonal partitions on the needed point set.

The exact (RTD(5,r)+) one-point completion was already rejected: it violates the target clique cap and, even with that cap ignored, creates a target-independent six-set. This rules out that particular exact template, not all near-design completions.

## 3. Robustness gap

The explicit (d_i=6) local block system in `HUB_PROPAGATION_THEOREM.md` has (s_i=9) and only ten local edge edits while placing its repeated-group pairs outside (X). The scalar bound (S_{\rm non}\le8r+5) allows such a pattern in up to
[
\left\lfloor\frac{8r+5}{9}\right\rfloor=\Theta(r)
]
color slots. The target cross-pair identity alone does not rule this out; one needs to show that these local patterns cannot coexist pairwise edge-disjointly with the other colors and the target cross-cover.

This is not a full terminal construction, and no global counterexample is claimed. It is an audit showing why exact nonextension cannot be inferred from stability distance alone.

## 4. Minimal remaining theorem

The sharp missing statement is a global **trap-completion inequality**:

> For every family of non-target ideal partitions satisfying the exact pair-ownership rule, target (\alpha\le5), target (\omega\le r-1), and the inherited density caps, the total cost of high-incidence traps plus target cross-cover exceeds the available budget; or else an omitted-color ((r+1))-set exists.

A useful proof must count cross-pairs across colors without double-counting and account for target edges that are unavailable to every non-target color. No such inequality has yet been proved. Therefore the robust nonextension target remains **OPEN**, and no sufficiently-large-(r) terminal closure is claimed.
