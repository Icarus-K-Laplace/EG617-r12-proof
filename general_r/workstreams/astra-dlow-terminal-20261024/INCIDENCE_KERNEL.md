# Finite target kernel forced by five independent low-degree anchors

Date: 2026-10-24. Status: **PROVED**.

## 1. Actual partition and finite data

THEOREM.md produces an independent A={a_1,...,a_5} and a partition into
five actual target cliques C_i plus H, with

    6<=m=|H|<=10+eta<=12,
    |C_i|=r-1-d_i, d_i>=0, sum_i d_i=m-6<=6.

Thus all five clique sizes lie between r-7 and r-1.

For each h in H record the nonempty anchor mask

    Q(h)=N_F(h) intersect A,  2<=|Q(h)|<=5.

Let n_Q count each of the 26 possible masks. Write
s_i=d_F(a_i)-r and s=sum_i s_i. Exact identities are

    sum_Q n_Q=m,
    sum_Q (|Q|-1)n_Q=s+4<=10+eta,
    sum_(Q containing i)n_Q=s_i+d_i+2,
    sum_i d_i=m-6.

The original three s_i retain their actual degree pattern. In the low
branch the last two satisfy s_4+s_5<=6; in the high branch they satisfy
s_4+s_5<=3. No independence between these parameters is assumed.

This is a finite symbolic anchor-incidence system with at most twelve
kernel vertices, independent of r. It is exhaustive because it records
actual neighborhoods, not a chosen topology approximation.

## 2. What is and is not finite-classified

The target graph on H has at most 66 pairs. It obeys alpha<=5.
Its non-target-colored pairs form at most 66 nonempty color classes;
all other non-target colors are empty on H.

Modulo permutations of non-target color names, this internal kernel
has finitely many edge-color partitions (bounded by the Bell number
of 66), target subgraphs, and anchor masks. This is a finite coverage
statement, not a list of realized types.

Neighborhoods from H to the large C_i and edges BETWEEN distinct C_i
are not fully classified. They may vary with r. The capacity theorem
handles ALL of them through necessary independent-set inequalities
and exact edge ownership; their enumeration is unnecessary for r>=221.

In particular the assertion "bounded kernel implies a completely
classified finite family of graph completions" is NOT made.

## 3. Comparison with the older hub reduction

The design source's bounded hub theorem concerns target internal
deletions from an ideal partition. The present kernel has a different,
exact definition: vertices attached to at least two of five independent
anchors. Outside it the five groups are actual cliques. We do not
identify the two kernels or transfer a theorem between them.

There is no assumption that target cross edges are exact stars,
that non-target ideal blocks are clean transversals, or that ordinary
cross edges vanish.

## 4. Remaining small-r types

The capacity table in THEOREM.md is necessary for every type. For
67<=r<=220 it removes types whose m is too small, but does not certify
the remaining types realizable or unrealizable.

A useful next refinement is the exact sum of color-wise kernel
vertex-cover numbers in DEFECT_PROPAGATION.md (5), together with
the anchor-mask identities above. This targets genuine joint incidence
information rather than duplicating a growing graph enumeration.

