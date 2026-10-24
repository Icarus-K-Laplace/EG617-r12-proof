# Dependency DAG and theorem scope

Updated 2026-10-25.

## Directed proof graph

    Hypothetical balanced coloring
        |
        +-- A_ext* [OPEN, external] --> contextual residual/terminal
        |                                  |
        |                    retained near-anchor extraction
        |                                  |
        |                         specified nine low-offset cells
        |                                  |
        +--> each color alpha<=r; exclusive edge ownership
                                           |
    target alpha<=5, omega<=r-1 ------------+
        |                                  |
        +--> non-target K6-free             |
        |         |                        |
        |   Brouwer second-Turan           |
        |         |                        |
        |   contextual target cap ---------+
        |                                  |
        +--> W-complement triangle-free    |
                  |                        |
             sparse-color matching --------+
                                           |
                              five low-degree independent anchors
                                           |
                                five actual cliques + m<=12 kernel
                                           |
                      all-color kernel cut capacity + random-order floor
                                           |
                                    r<=220 (low), r<=208 (high)
                                           |
                            D_low(r) for every integer r>=221
                                           |
                        retained synthesis + A_ext* --> P(r)

No arrow returns from P(r), terminal impossibility, or an OPEN
classification to any preceding input.

## Contextual cap: exact use of the retained theorem

Let C be any non-target color on 5r+1 vertices. Since alpha(F)<=5,
C is K6-free. Its complement is K_(r+1)-free because alpha(C)<=r.
Its complement cannot be r-partite: an r-partition would cover V by
r cliques of C, each of size at most five, short of 5r+1 vertices.
The retained Brouwer second-Turan bound therefore gives

    e(C) >= p_r(5r+1)+floor((5r+1)/r)-1 = 10r+9.

Summing over r-1 non-target colors and using exclusive ownership,

    2e(F) <= (5r+1)5r - 2(r-1)(10r+9)
           = 5r^2+7r+18.

This exact classical extremal theorem is an explicit imported input,
not a new theorem certified by our finite verifier. Alternatively,
THEOREM.md is a self-contained implication from the stated cap.
The architecture source proves the same specialization at (k,s)=(5,1).

## Imported inputs and unused historical assets

|Input or asset|Status here|Use|
|---|---|---|
|Full pair ownership and color independence bounds|CONDITIONAL on terminal input|Essential|
|Brouwer second-Turan|Retained theorem dependency|Derives contextual cap|
|Kernel edge floor p_5 for 6<=m<=12|PROVED by random-order independent set|Complete proof in THEOREM.md|
|Near-anchor extraction|External retained dependency|Supplies T, not reproved|
|A_ext*|OPEN|Only needed for the original problem|
|Exact-star derangement|CONDITIONAL|Not used|
|Source-pair product inequality|CONDITIONAL|Not used|
|Furedi ideal partitions and edit budgets|Retained but not needed|Not used|
|HP2 claimed per-label r-1 charge|OPEN after local proof audit|Not used|
|General one-cover propagation|RETRACTED as a deduction|Not used|
|Sibling attempted r>=6212 closure|RETRACTED by source|Not used|
|Our all-r capacity calculation|PROVED|No computational search needed|

The source route states a direct near-anchor threshold 67; the older
three-anchor AES inequality has threshold 68 and is a different route.
Our theorem assumes the extracted triple, so neither numerical
extraction proof is silently substituted for the other.

## Remaining proof work

The all-large-r downstream nonextension obligation has a finite
explicit threshold 221. Lowering it to 67 requires stronger joint
kernel constraints in the finite interval, not an unbounded-r graph
enumeration. A_ext* remains a separate main-theorem obligation even
if every smaller terminal window is subsequently excluded.
