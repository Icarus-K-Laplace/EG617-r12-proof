# Q33 support-promotion progress log

## 2026-10-30 — audit and repair of component-core profile assumption

Audited the source-verified exact-129 factorization and found that it certifies ten isolated K5s plus an 11-vertex gadget, but does not by itself assert one shell vertex in every K5. The cross-gadget source explicitly warns that components may have multiple shell vertices. The earlier fixed c_i=4 screen is therefore conditional only.

Replaced it with a variable-core model:
- each isolated K5 has c_i in {0,...,4} core vertices; c_i=5 would contradict alpha(H)<=4;
- gadget core size g=47-sum c_i lies in [7,11];
- the three/four unselected components have total core size in [8,12]/[12,16], depending on whether seven component witnesses or six plus a gadget witness were selected;
- each unselected component has U-incidence k_i in [0,c_i];
- gadget core U/W subsets contribute p2(s_U),p2(r_W) exact-color edges, with at most six U edges subtracted for the already selected gadget witness.

The variable-core profile DP excludes:
- m=8: v=31,32,33,34;
- m=9: v=32,33,34;
- m=10: v=34,35,36,37.

First profile survivors:
- m=8,v=35,h=6,7,8;
- m=9,v=35,h=9;
- m=10,v=38,h=10.

Product and recursive per-color option generators agree. The verifier covers all47 (m,v) cells. No graph-level completion is claimed.
