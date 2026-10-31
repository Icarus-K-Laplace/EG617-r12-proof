# Lift of the new boundary to the genuine T61 parent

Date: 2026-10-31. Status: **PROVED under the stated T61 contract**.

Assume a simple target graph F on 61 vertices, delta(F)=13, alpha(F)<=5, omega(F)<=11, and every inherited density cap D. Let p be ANY degree-13 vertex, A=N(p), and H=F minus (A union {p}). Then |A|=13, |H|=47. An independent five-set in H extends with p to an independent six-set; consequently alpha(H)<=4. Clique and hereditary density bounds restrict to H, so H belongs to R(4,47).

Set M=complement(F[A]), z=e(M), g_a=d_F(a)-13>=0, G=sum g_a, and q=z+G. Since d_F(a)=1+(12-d_M(a))+t_a, we have t_a=d_M(a)+g_a. Thus b=e_F(A,H)=2z+G=q+z and

    E = 13+(78-z)+(q+z)+e(H) = 91+q+e(H).

If (E,q)=(407,30) or (408,31), e(H)=286. The accepted low-edge minimum-degree gate gives delta(H)>=12. Theorem E286 in 286_EDGE_EQUALITY_CLASSIFICATION.md contradicts the resulting five abstract hypotheses. Both equality parent cells are therefore impossible, with no shell classification, Type-I classification, MS-29 support bridge, or V11/V12 seed assumption in this implication.

Combining E286 with the two previously accepted low-edge results gives e(H)>=287. Hence, for EVERY regular pivot,

    E407: q_p<=29;       E408: q_p<=30.

This is an upper bound on Q=max q_p too. It does not supply a lower bound Q>=31. The full-energy conclusion is separated in CHARGE_RANGE_COMPLETENESS.md.

The core is unconditional as an abstract theorem; the parent implication requires the real T61 hereditary-cap contract to invoke the accepted gate. The full-color degree and triple interfaces are additionally checked in the two companion files, although they are unnecessary for this shortest contradiction.
