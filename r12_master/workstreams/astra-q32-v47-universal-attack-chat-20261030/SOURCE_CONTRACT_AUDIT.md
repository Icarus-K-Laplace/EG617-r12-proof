# Source contract audit

Status: PROVED_CONDITIONAL application to the named genuine T61/Q32 parent. The new core theorem itself needs only the five stated core hypotheses.

## 1. Target/non-target distinction

Let F be the target graph on the actual61-point T61 residual, p a target-degree13 pivot, A=N_F(p), and H=F[V minus N_F[p]]. The parent files front_end/FRONTEND_BRIDGE_THEOREM.md F7-F8 and front_end/T61_H13_FULL_COLOR_DEGREE_AND_ANTINEIGHBORHOOD.md Section1 at global b0459807 explicitly retain alpha(F)<=5, omega(F)<=11 and delta(F)=13. The Q32 terminal supplies |H|=47,e(H)=285,delta(H)>=12,alpha(H)<=4.

A non-target clique of order6 would be target-independent of order6. Therefore omega(C)<=5 on this SAME61-point residual. Balancedness gives alpha(C)<=12. This is not an assertion that every arbitrary61-point induced subcoloring of a balanced graph has omega(C)<=5.

The current A-branch audit correctly says bare balancedness does not imply that cap, and correctly retracts omega(H)<=5. Its local example5K6+3K5+4K4 has alpha12 and129 edges but violates the retained target-alpha5 coupling. It is not a counterexample to the genuine T61 inference. We independently read the parent statements rather than import either side's status declaration.

**Never used:** omega(H)<=5, a universal degree9 exceptional vertex, exceptional-point injectivity, a canonical source partition shared by different colors, or a source witness forced through a selected pivot without proof.

## 2. Exact129 classification — PROVED relative to Kang-Pikhurko

Primary source: M. Kang and O. Pikhurko, Maximum K_(r+1)-free graphs which are not r-partite, Matematychni Studii24 (2005),12-20. https://opikhurko.warwick.ac.uk/E/KangPikhurko05ms.pdf . Theorem1 gives the extremal size; Theorem4 gives the equality construction. The primary PDF was read directly.

For a non-target C, its complement G is K13-free. It cannot be12-partite: its parts would be C-cliques of size at most5 and could cover at most60 vertices. Hence

    e(C)>=binomial(61,2)-[t12(61)-5+1]=129.

At equality, Theorem4 supplies an added point x and twelve old independent parts of G, whose sizes sum to60. Each is a C-clique of size at most5; therefore ALL sizes are5. This directly excludes both size-six profiles and the12-partite case under the genuine T61 coupling, without assuming them away from balancedness alone.

In C the ten ordinary parts are isolated K5 components. The two special K5s Ns,Nt and x form an11-point gadget. Choose y in Nt and a nonempty proper A0 subset Ns, with a=|A0| in1,2,3,4. Besides the two K5 interiors, the gadget edges are y-A0, x-(Ns minus A0), and x-(Nt minus {y}). It has29 edges. The variable degrees are d(y)=4+a and d(x)=9-a; all other gadget vertices have degree5 and ordinary vertices degree4. There is no degree9 point.

## 3. Every exceptional position and outside profile

Put O={p} union A, |O|=14. Every K5 factor meets O because its H intersection is target-independent and alpha(H)<=4.

- x in O: factor outside counts are(2,1^11), in12 labeled positions; H part sizes are4^11,3.
- x in H: either(2,2,1^10), in66 labeled positions, or(3,1^11), in12 labeled positions. H part sizes are respectively4^10,3,3,{x}, or4^11,2,{x}.

The total90 aggregate assignments preserve the identities of both special factors; no isolated or special double/triple placement is removed. Aggregate counts do not specify which of y,A0,x is inside a part and do not certify a colored completion. All four source parameters remain legal.

The new theorem has no source-position premise at all. Thus none of these placements is lost in its application.

## 4. Counts and exact parent variables

All colors partition1830 edges. Since e(F)=408, the non-target total is1422=11*129+3. Consequently m=8,9,10 with nonexact counts respectively(130,130,130),(130,131),(132). This follows from the129 floor and integrality.

In the full extension, pH has no target edge and pA is entirely target. There are123 target edges outside the core; after the13 pivot-star edges,110 target edges remain on A or A-H. Full-target degree constraints and all inherited parent restrictions must still be checked. A core witness is not a61-point colored witness or a145-point balanced-coloring counterexample.
