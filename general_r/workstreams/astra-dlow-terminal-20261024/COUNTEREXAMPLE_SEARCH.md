# Countermodel and source-proof audit

Updated 2026-10-25. No full contextual counterexample is claimed.

## 1. Product-cover quantifier audit

The frozen D source HP2 proof moves from "every transversal is hit"
to "every point in every coordinate is hit." This inference is
invalid. With two singleton coordinates {x1},{x2}, fixed nonedge uv,
and only the endpoint edge ux1, every transversal is hit although x2
has no endpoint edge. With endpoint events only, the correct conclusion
is that at least ONE coordinate is completely covered: otherwise an
uncovered choice in every coordinate makes an unhit transversal.

This toy refutes the proof step, not the full contextual terminal or
necessarily the conditional lemma's conclusion. Its other hypotheses
could force further structure. We therefore do not import the claimed
r-1 charge. The later weighted expectation inequality does not make
this quantifier error and is valid, but is not needed in our proof.

## 2. K6-free one-color split-cover model

For r>=3, start with disjoint ideal blocks: C of size six,
D of size five, and r-2 further K5 blocks. Write

    C={u,v,z1,z2,z3,z4}, D={w1,w2,w3,w4,w5}.

Delete uv from the clique on C. Add exactly

    uw1, uw2, vw3, vw4, vw5.

All other cross-block pairs are absent in this one-color graph Q.
The C union D core has alpha=2: an independent pair within C must
be {u,v}, and every point of D meets at least one of them. Each
block individually has independence at most two or one respectively.
No independent triple occurs. Its clique number is five: C-uv and
D each have maximum clique five; any mixed clique is smaller since
z1,...,z4 have no D-neighbors and neither u nor v sees all of D.
Thus alpha(Q)=2+(r-2)=r and omega(Q)=5.

The ideal edge total is 15+10(r-1)=10r+5. The actual edge total is
10r+9, its slack is four, and edit distance is six. A clean K5 cover
block blocks the sole missing pair by split endpoint ownership,
without introducing a second missing pair or K6.

This is an explicit countermodel to the local inference that every
cheap one-block cover must create K6 or another defect. Latest D's
canonical statement already recognizes split covers; some older
sections in its budget/closure files retain the stronger wording.
Our proof never uses that stronger claim.

## 3. Why it is not a terminal counterexample

Only one non-target color has been specified. For an explicit naive
completion, assign every remaining pair to color 0 and leave colors
2,...,r-1 empty. Unique ownership then holds, and alpha(G0)=5 follows
from omega(Q)=5. But omega(G0)=alpha(Q)=r exceeds r-1, and each empty
color has independence 5r+1>r. These precisely identified failures
exclude the completion from the contextual contract.

Our verifier exhaustively checks all 2^11 subsets of the core,
returning alpha=2, omega=5, 29 edges. The extension by disjoint K5
blocks is analytic for all r. This is not a SAT/ILP search over full
terminals and is not evidence that any necessary kernel type is
realized by a full coloring.

## 4. Other source safeguards

An r-partite complement only supplies a cover by r original cliques;
it does not forbid original cross-clique edges. The contextual cap
argument needs only the cover, and is valid without such a prohibition.

The latest design source withdraws its r>=6212 theorem because it
mistook ordinary clique vertices for an independent set. We do not
use that claim. In our construction the private-neighbor clique proof
uses two specifically NONADJACENT vertices and four explicitly
independent anchors, so that six-set inference has the required
pairwise nonedges.
