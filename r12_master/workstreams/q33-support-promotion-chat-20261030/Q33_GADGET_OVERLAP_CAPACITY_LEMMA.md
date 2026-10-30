# Q33 gadget-witness overlap capacity: aggregate four-edge bound

Status: **PROVED_CONDITIONAL** under the retained exact-129 gadget contract.

Let C be the exact-129 color whose exceptional gadget has core set G_C, and let Q be a selected gadget witness. The registered witness contract gives
\[
Q\subseteq G_C,\qquad |Q|=4,\qquad \alpha(C[G_C])\le2.
\]
Therefore \(\alpha(C[Q])\le2\). A graph on four vertices with independence number at most two has at least two edges: with zero or one edge, three vertices remain independent. Hence
\[
e_C(Q)\ge2.
\]

All six pairs of Q are non-H edges and have unique colors. At least two are already colored C, so all colors other than C together can occupy at most
\[
6-e_C(Q)\le4
\]
pairs of Q. In particular, the aggregate of all nonexact colors on Q is at most four, regardless of whether there are one, two, or three nonexact colors.

Thus, for h selected gadget witnesses, the total nonexact-color overlap with their six-pair blocks is at most \(4h\). The correct uniform reserve coefficient is
\[
\boxed{\rho_m=4\quad\text{for }m=8,9,10.}
\]

This supersedes the coarser aggregate allowance \(\min(6,4(11-m))h\) in the first support-screen commit. The older allowance was a valid but weaker upper bound; the present four-edge bound follows from the exact color's own at-least-two edges on each gadget witness.
