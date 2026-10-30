# V47 exact-color source gap and 69/70 near-Turan normal form

**Status: PROVED_CONDITIONAL structural reduction. No Q32 closure claimed.**

## 1. Contract

Fix an exact-129 Type-I color C in the full-support E408/Q32 terminal:
- H has 47 vertices, alpha(H)<=4;
- C has 129 edges on the 61-point residual;
- C has alpha(C)<=12 and omega(C)<=5;
- the twelve source K5 factors partition the 60 points other than the special point x;
- each source K5 factor meets O={p} union A, |O|=14;
- Ns and Nt are the two special K5 factors; A0 is a nonempty proper subset of Ns, a=|A0| in {1,2,3,4};
- the nine gadget edges are y--A0, x--(Ns\A0), and x--(Nt\{y}).

The pivot p has all pA edges target-colored. Hence the unique source K5 factor containing p (or Nt when p=x) is single-outside and supplies one of the witness K4s.

## 2. Exact H-edge count from source labels

For each K5 factor K_i, put b_i=|K_i intersect O|. Its H-interior is a clique of size 5-b_i and contributes C(5-b_i,2) C-edges. The gadget contributes exactly

G_C^H = 1_{x in H} ( |(Ns\A0) intersect H| + |(Nt\{y}) intersect H| ) + 1_{y in H}|A0 intersect H|.

Therefore

e_C(H) = sum_{i=1}^{12} C(5-b_i,2) + G_C^H.

This identity is encoded directly in q32_fullsupport_m89_solver.py and independently follows from the reconstructed Type-I edge set in the candidate verifier.

## 3. Source-profile gap bounds

Every b_i>=1.

### 3.1 x in O

The twelve factors contain the other thirteen O-points, and each has at most two outside points. Thus the profile is (2,1^11). The K5 interiors contribute

C(3,2)+11*C(4,2)=3+66=69.

All gadget edges incident with x leave H; only y--A0 can be an H-H gadget edge. Thus

69 <= e_C(H) <= 69+a <= 73.

### 3.2 x in H, two-double profile

The profile is (2,2,1^10). K5 interiors contribute

2*C(3,2)+10*C(4,2)=6+60=66.

Let b_s=|Ns intersect O| and b_t=|Nt intersect O|. Both special factors meet O, and b_s+b_t<=4. The nine gadget edges have at least 10-a-b_s-b_t H-H edges, hence at least 6-a. At least one gadget edge leaves H, so at most eight gadget edges are H-H. Therefore

max(69,72-a) <= e_C(H) <= 74.

### 3.3 x in H, triple profile

The profile is (3,1^11). K5 interiors contribute

C(2,2)+11*C(4,2)=1+66=67.

The same gadget argument gives at least 6-a H-H gadget edges and at most eight. Thus

max(69,73-a) <= e_C(H) <= 75.

These bounds are **PROVED_CONDITIONAL** on the source-correct Type-I factorization and its registered gadget-placement count. They use no degree-nine exceptional-vertex claim.

## 4. 69/70 near-Turan partition theorem for every non-target color

Let C be any non-target color and D=C[H]. Since alpha(C)<=12, alpha(D)<=12 and its complement J=bar D is K13-free. Since alpha(H)<=4, omega(D)<=4: a C-colored K5 inside H would be a target-independent 5-set.

We have C(47,2)=1081 and t_12(47)=1012.

- If e(D)=69, then e(J)=1012=t_12(47), so Turán equality gives a complete 12-partite graph.
- If e(D)=70, then e(J)=1011. The registered Brouwer/Kang--Pikhurko second-Turán bound says a non-12-partite K13-free graph on 47 vertices has at most 1010 edges. Hence J is 12-partite.

The 12 parts are cliques in D, so each has size at most four. They cover 47 vertices; therefore their sizes are exactly 4^11,3.

The internal D-edges in these parts total 11*C(4,2)+C(3,2)=69. Consequently the number of D-edges crossing the parts is exactly e(D)-69, i.e. zero or one.

A D-colored K4 crossing two parts needs at least three cross-part edges (the cheapest split is 3+1). Since there is at most one, every D-colored K4 lies wholly inside one size-four part.

Thus every non-target color in the 69/70 layer has an 11K4+K3 partition. For exact colors, every source single-outside witness K4 occupies one of the size-four parts. With eleven witnesses they occupy all eleven size-four parts; with ten witnesses they occupy ten, and the remaining seven vertices split into the remaining K4 part and the K3 part.

**Status: PROVED_CONDITIONAL** on the registered second-Turán theorem and the Q32 source contract.

## 5. CSP and verifier implementation

The isolated solver:
1. encodes the exact source-core identity e_C(H)=B_C+G_C^H for exact colors;
2. encodes the x-in-O / two-double / triple source gap bounds for exact colors;
3. introduces conditional part labels for every non-target color whenever e_C(H)<=70;
4. requires eleven parts of size four and one of size three;
5. forces all within-part pairs to have color C and allows exactly e_C(H)-69 cross-part C-edges;
6. for exact colors, places every single-outside source K4 wholly inside one size-four part.

The independent verifier reconstructs the partition from the color graph: in the 69-layer it takes connected components; in the 70-layer it deletes the unique cross-part edge and takes connected components. It verifies part sizes and cross-edge count for all non-target colors, then checks source-witness alignment for exact colors.

These are necessary conditions only. Colors with 71+ H-edges remain outside this partition normal form, and the complete m=8/9 full-support CSP remains **OPEN**.
