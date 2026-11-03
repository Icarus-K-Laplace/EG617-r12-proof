# H13 q30 heavy-set branch and Family-II shell-scope clarification

Date: 2026-11-03  
Frozen source: `frozen/cover/COVER_THEOREM.md`, Sections 10–12, at integration snapshot `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`.

## Result

**NO GAP FOUND.** Two compressed statements in the q30 maximum-shell classification can be made explicit:
1. the `|X|=1, t_x>=12` 2-matching equality branch really does force z<=16, because the eight outside points are regular and therefore have missing degree at most2;
2. in Family II, u,v are the only decorated vertices *inside each relevant 13-shell*, not necessarily the only decorated vertices in the whole 61-vertex parent. The proof only needs the shell-local statement.

## 1. The `|X|=1, t_x>=12` branch

Assume E=408, Q=30, M is K4-free, no regular shell vertex has missing degree3..10, and X={x} with t_x>=12. Every other shell point has weight at most10. The 12-point set B=A\\{x} must contain a triangle or a 2-matching: if its matching number were at most1, it would be empty, a star, or a triangle plus isolates; the first two cases give an independent set of size at least11 in M, contrary to alpha(M)<=10.

### Triangle alternative

For an M-triangle T, the common-row bound gives t(T)>=24. K4-freeness gives e_M({x} union T)<=5: T contributes three edges and x can meet at most two of its vertices. Applying the subset identity (1) to {x} union T,
[
Q\ge t_x+t(T)-e_M(\{x\}\cup T)\ge12+24-5=31,
]
contradicting Q=30.

### 2-matching alternative

Let S consist of x and the four endpoints of a 2-matching in B. EDGE13 gives weight at least13 on each matching edge, so
[
t(S)\ge12+13+13=38.
]
Since M is K4-free, Turán gives e_M(S)<=ex(5,K4)=8. The subset identity yields
[
30=Q\ge t(S)-e_M(S)\ge38-8=30.
]
All inequalities are equalities. In particular:
- t_x=12 and both matching-edge endpoint sums are13;
- e_M(S)=8;
- the remaining eight points B\\S are M-independent and have zero decoration, hence are regular.

Because X={x}, the four endpoints S\\{x} have weights at most10. The eight remaining points are regular, and the no-middle-degree assumption therefore gives them missing degree at most2. EDGE13 forbids an M-edge from any of these eight points to S\\{x}, since 2+10<13. They are independent among themselves, so their only possible M-neighbor is x. Each can contribute at most one edge to x. Consequently
[
z=e(M)\le e_M(S)+8\le8+8=16,
]
contrary to z>=22. This completes the branch without an implicit assumption about the degrees of the eight outside points.

## 2. Family-II identification is shell-local

The source phrase “the globally decorated u,v must be the two exceptional lows in every view” should be read with the shell scope made explicit.

In the first Family-II view at pivot p:
- K={p} plus the nine ordinary lows consists of ten degree-13 vertices;
- u,v are two decorated vertices (their positive excesses sum to7);
- T_p is the pair of regular hubs.

For any v_i in K, its 13-shell consists of K\\{v_i}, u,v, and the two vertices T_i. The nine vertices K\\{v_i} are already known to have degree13, while u,v remain decorated in the full parent. If the q30 classification at v_i is Family II, its two exceptional low vertices must therefore be u,v; the two hub vertices T_i are regular by the Family-II normal form. This argument does **not** assert that the entire 47-core, or the entire 61-vertex parent, has only two decorated vertices. Other decorated vertices may lie in the core and are irrelevant to identifying the shell's two exceptional lows.

Once this shell-local identification is stated, the existing disjointness and anticompleteness argument is valid:
- T_i and T_j are disjoint, since a hub in T_i is nonadjacent to every other K-low in the view at v_i;
- for x in T_i and i!=j, x lies in the core C_j and
  [
  d_{C_j}(x)=13-1-e_F(x,T_j)\ge12,
  ]
  so e_F(x,T_j)=0;
- the ten pairs are pairwise anticomplete, yielding an independent transversal of size10, contrary to alpha(F)<=5.

## Disposition

No mathematical repair to the frozen COVER theorem is required. This note records the missing intermediate explanation and narrows the scope of the “two decorated vertices” wording. It does not certify the full root proof, Lean kernel verification, or external peer review.
