# Q33 KP gadget-core profile refinement

Date: 2026-10-30
Status: PROVED_CONDITIONAL under the source-verified KP Type-I factorization and alpha(H)<=4.

The 11-vertex KP Type-I gadget consists of two special 5-vertex parts P,Q, each inducing a C-colored K5, and one exceptional vertex x. Put a=|A_KP| for the nonempty proper subset parameter in the published construction, so a in {1,2,3,4}. The source-audited degrees are: all five P-vertices have degree5; the four vertices of Q minus y have degree5; d_C(y)=4+a; d_C(x)=9-a.

Each of P intersect H and Q intersect H is an independent set in H, hence has size at most4. The exceptional vertex contributes at most one further core vertex. Therefore 7<=g_C<=9. The lower bound follows because the ten isolated K5 components have at most four core vertices each and together with the gadget partition the47-point core.

For the seven selected component K4s and three remaining component core sizes c_1,c_2,c_3,
\[
g_C=47-28-\sum_i c_i=19-\sum_i c_i.
\]
Thus
\[
\boxed{10\le\sum_i c_i\le12}.
\]
This supersedes the earlier shell-only interval9..12.

The possible gadget core profiles are:
- g=9: x is core and (|P cap H|,|Q cap H|)=(4,4);
- g=8: x is core with (3,4) up to order, or x is shell with (4,4);
- g=7: x is core with (2,4) or (3,3), up to order, or x is shell with (3,4), up to order.

These are necessary core-size profiles only. They do not yet encode shell labels or the KP cross-edge pattern. The updated profile screen has the same aggregate exclusion frontier; see Q33_COMPONENT_ONLY_SUPPORT_SCREEN.md. Q33 remains OPEN.
