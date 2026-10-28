# E407 Q32 — delta=12 depth-2 epsilon_U=3 q=0 closure

Date: 2026-10-28  
Status: **PROVED_CONDITIONAL / CLOSED for the two q=0 W profiles** under the registered 308-edge depth-2 kernel classification and `DELTA12_AUGMENTATION_FRONTIER.md`. The q=1 `(4,4,5,5)` profile remains OPEN; delta=12 and E407 Q32 remain OPEN.

## 1. Depth-2 setup

Use the classified depth-2 kernel
\[
G_2=K_7^A\dot\cup K_7^B\dot\cup\overline J,
\]
where the two restored target edges join `A\cup B` to J-points among the four degree-6 vertices `C\cup E` and the degree-4 point `d_0`.

For restored-incidence counts `t_0,t_c`,
\[
d_W(d_0)=2+\epsilon_{d_0}-t_0,
\qquad d_W(c)=4+\epsilon_c-t_c.
\]
At `epsilon_U=3` every U-vertex has W-degree at least three.

The two q=0 W profiles are
\[
K_3\dot\cup K_5\dot\cup K_5\dot\cup K_5,
\tag{P1}
\]
and
\[
K_4\dot\cup K_4\dot\cup K_4\dot\cup K_6.
\tag{P2}
\]

We use the pure graph pair rule: if two core vertices are nonadjacent, their common W-nonneighbours contain no independent triple. In a disjoint union of four cliques this means their W-neighbourhood union contains every vertex of at least two W-components.

## 2. Universal epsilon_U=3 endpoint rigidity in either q=0 profile

The point `d_0` is H-nonadjacent to each of the four points `c\in C\cup E`. In either (P1) or (P2), the two smallest W-components have total size eight. Hence
\[
d_W(d_0)+d_W(c)\ge8
\]
for every one of the four c-points.

Summing over the four c's gives
\[
4(2+\epsilon_0-t_0)+\sum_c(4+\epsilon_c-t_c)\ge32.
\]
Since `t_0+sum_c t_c=2`, this becomes
\[
4\epsilon_0+\sum_c\epsilon_c\ge10+3t_0.
\tag{2.1}
\]
But the total U-excess is three, so
\[
\sum_c\epsilon_c\le3-\epsilon_0.
\]
Thus
\[
3(\epsilon_0-t_0)\ge7.
\]
The only integer possibility is
\[
\boxed{t_0=0,\quad\epsilon_0=3.}
\tag{2.2}
\]
All U-excess lies on d0 and
\[
d_W(d_0)=5.
\]
Both restored J-endpoints therefore lie in `C\cup E`. They must be distinct: if one c carried both restored edges then `d_W(c)=2`, contradicting the three-neighbour floor. Call them `c_1,c_2`. Then
\[
\boxed{d_W(c_1)=d_W(c_2)=3.}
\tag{2.3}
\]
All vertices in the two K7 components have zero excess and
\[
d_W(v)=6-r_v\le6,
\tag{2.4}
\]
where `r_v` is restored-edge incidence. As before, at most one A/B-side vertex can be exceptional by being the common partner of both c1,c2.

# 3. Profile P1 = K3 + 3K5

For i=1,2, the nonadjacent pair `(d0,c_i)` has degree sum exactly eight. The pair rule can therefore only be satisfied by covering the K3 and one K5 exactly. The two unions must use the same K5, say `K5*`: two distinct choices would intersect only in K3, which has three vertices, but the five-point set `N_W(d0)` must lie in both unions.

Thus for one fixed 8-set
\[
R_8=K_3\dot\cup K_5^*,
\]
we have
\[
N_W(c_1)=N_W(c_2)=R_8\setminus N_W(d_0).
\tag{3.1}
\]
Put
\[
x=|N_W(d_0)\cap K_3|.
\]
Then `0<=x<=3`, d0 has `5-x` neighbours in K5*, and each c_i has `3-x` neighbours in K3 and x neighbours in K5*.

Let v be any non-exceptional vertex of A union B, and choose c_i to which v is nonadjacent. The pair `(v,c_i)` has degree sum at most nine, so it cannot cover two K5 components. It must cover K3 plus one K5.

It cannot cover the distinguished pair `K3+K5*`: that would force `N_W(d0) subset N_W(v)`, after which the pair `(v,d0)` has union of size at most six and cannot cover two components.

Hence `(v,c_i)` must cover K3 plus one of the other two K5 components. Since c_i supplies only `3-x` K3 vertices and no vertex of that other K5, v must contain all five vertices of that K5 plus the x missing K3 vertices. This requires `5+x<=6`, so x<=1.

Now use the pair `(v,d0)`. If x=1, its union contains the chosen other K5, but d0 has only four of K5* and one point of K3, while v has the same required K3 point and no remaining degree slot. No second W-component is fully covered. Contradiction. Therefore
\[
\boxed{x=0.}
\tag{3.2}
\]
Thus
\[
N_W(d_0)=K_5^*,\qquad N_W(c_1)=N_W(c_2)=K_3.
\tag{3.3}
\]
Every non-exceptional A/B vertex is complete to exactly one of the two remaining K5 components; call this its binary label.

For labelled a in A and b in B, the pair is H-nonadjacent. If they have the same label, each has at most one W-neighbour outside that K5, so their union cannot cover any second component. The pair rule forces opposite labels across every constrained A-B pair.

If the restored A/B endpoints are distinct, all seven vertices on each K7 side are labelled; one side is uniformly complete to a K5, giving K7+K5=K12. If the two restored edges share one A/B-side endpoint, one side has six labelled vertices and the opposite side has all seven; opposite-label forcing makes the seven-vertex side uniformly complete to a K5, again giving K12. Hence (P1) is impossible.

# 4. Profile P2 = 3K4 + K6

For i=1,2, `(d0,c_i)` again has degree sum eight. It must therefore cover exactly two of the three K4 components, say `K4^a union K4^b`, with disjoint neighbourhoods. Both i use the same pair, because two different K4-pairs intersect in at most four vertices while `|N_W(d0)|=5`.

Let
\[
x=|N_W(d_0)\cap K_4^a|,
\]
so `1<=x<=4` and d0 has `5-x` neighbours in K4^b. The common three-set `N_W(c_i)` is the complement of `N_W(d0)` in these two K4s.

Take a non-exceptional v and a c_i nonadjacent to it. Since `d_W(v)+d_W(c_i)<=9`, their union cannot cover K4+K6. It must cover two K4 components.

It cannot cover the distinguished pair `K4^a+K4^b`, because that would force `N_W(d0) subset N_W(v)` and make `(v,d0)` too small to cover two components. Therefore it must use the third K4, call it `K4^c`, together with one distinguished K4.

- Using `K4^a+K4^c` costs `4+x` neighbours of v, so x<=2.
- Using `K4^b+K4^c` costs `9-x`, so x>=3.

Now impose the pair `(v,d0)`. In the first branch only x=1 can work, because then d0 already contains all of K4^b; x=2 leaves neither distinguished K4 complete. In the second branch only x=4 can work, symmetrically. Hence
\[
\boxed{x\in\{1,4\}.}
\tag{4.1}
\]

In either case every constrained v is complete to K4^c and contains the same one distinguished mandatory point q; it has at most one additional W-neighbour. Therefore for any constrained a in A and b in B,
\[
N_W(a)\cup N_W(b)
\]
contains K4^c but has at most three vertices outside K4^c: the shared q plus at most two optional points. It cannot completely cover another K4, let alone K6. This contradicts the pair rule for the nonadjacent A-B pair.

There are constrained vertices on both sides even if the two restored edges share one A/B endpoint, so the contradiction is unavoidable. Thus (P2) is impossible.

## 5. Conclusion

Both q=0 epsilon_U=3 depth-2 profiles are excluded:
\[
\boxed{
\delta=12,\ \text{depth2},\ \epsilon_U=3,\ q=0\Longrightarrow\bot.
}
\]

The only remaining epsilon_U=3 W-profile is `(4,4,5,5)` with one W-cross edge (`q=1`). That case needs a defect-aware version of the component-cover pair rule and is not claimed closed here.

## 6. Dependency audit

This proof uses:
1. the registered 308-edge depth-2 saturated-kernel classification;
2. the delta=12 low-W-degree lemma from `DELTA12_AUGMENTATION_FRONTIER.md`;
3. pure graph `alpha(H)<=4`, `omega(H)<=11`, exact degree/excess accounting, and the nonadjacent-pair rule.

It does not use Didin. It does not close epsilon_U=3 q=1, any other delta=12 branch, E407 Q32, or EG617(r=12).
