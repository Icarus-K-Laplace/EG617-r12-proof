# E407 Q32 — delta=12 depth-2 C5 kernel, epsilon_U=2 terminal reduction

Date: 2026-10-27  
Status: **PROVED_CONDITIONAL strict reduction** under `DELTA12_AUGMENTATION_FRONTIER.md` and the registered 308-edge saturated-kernel classification. This does not yet exclude the final epsilon_U=2 terminal.

## 1. Classified depth-2 setup

We are in the delta=12 non-four-partite augmentation-depth-2 branch. Thus after adding two K5-safe edges `e1,e2`, the graph L_2 is the classified 308-edge saturated kernel and
\[
G_2=\overline{L_2}=K_7^A\dot\cup K_7^B\dot\cup\overline J,
\]
where J is the 15-vertex C5 blow-up with parts `(5,5,2,1,2)` and degree sequence `7^10,6^4,4^1`.

Write the unique degree-4 J point as d0 and the four degree-6 points as `C union E`. The two restored target edges in the original H[U] are exactly the two safe augmentation edges viewed in the complement. By support-edge exhaustion, each restored edge joins A or B to `C union E union {d0}`.

Let `t_0 in {0,1,2}` be the number of restored edges incident with d0. For a point c in C union E let t_c be its restored-edge incidence count. The exact W-degrees are
\[
d_W(d_0)=2+\epsilon_{d_0}-t_0,
\tag{1.1}
\]
\[
d_W(c)=4+\epsilon_c-t_c.
\tag{1.2}
\]
We now assume
\[
\epsilon_U=2.
\]

By the universal delta=12 low-W-degree lemma, every U vertex has at least three W-neighbours.

The W-side four-clique possibilities are exactly

1. `(3,4,5,6)`, q=0;
2. `(3,5,5,5)`, q=1;
3. `(4,4,4,6)`, q=1;
4. `(4,4,5,5)`, q=2.

We repeatedly use the pair rule: if two core vertices are H-nonadjacent, their common W-nonneighbours cannot contain an independent triple.

## 2. A small W deletion lemma

For any one of the four profiles above, if two H-nonadjacent core vertices have W-neighbourhood union of size at most six, then their common W-nonneighbours contain an independent triple.

Reason: deleting at most six vertices from the four clique parts cannot empty two parts. In the q=0 profile this immediately leaves at least three nonempty clique parts. In the q=1 profiles, the surviving product of choices from three nonempty parts has more than one transversal, so one cross edge cannot block all independent triples. In the q=2 `(4,4,5,5)` profile, after six deletions the worst three-part remainder has sizes at least `(2,5,5)` up to permutation after one K4 is emptied; two cross edges cannot block all 50 three-part choices. Thus an independent triple remains.

Similarly, if the neighbourhood union has size at most seven, all profiles except `(3,4,5,6),q=0` still contain an independent triple in the common nonneighbour set. In the exceptional q=0 profile, avoiding such a triple with union size seven forces the union to be exactly the K3 plus the K4.

## 3. Restored edges cannot hit d0

From (1.1) and `d_W(d0)>=3`,
\[
\epsilon_{d_0}\ge1+t_0.
\tag{3.1}
\]
Since the total U-excess is two, `t_0=2` is impossible.

Suppose `t_0=1`. Then (3.1) forces
\[
\epsilon_{d_0}=2,
\qquad d_W(d_0)=3,
\]
and all other U vertices have zero excess.

The second restored edge has a J-endpoint `c in C union E`. It has `t_c=1` and hence by (1.2)
\[
d_W(c)=3.
\]
The pair d0,c is H-nonadjacent in the C5 kernel. Their W-neighbourhood union has size at most six, contradicting the deletion lemma and the pair rule.

Therefore
\[
\boxed{t_0=0.}
\tag{3.2}
\]
Both restored J-endpoints lie in `C union E`.

## 4. epsilon_d0=1 is impossible

With t0=0, (1.1) and the three-neighbour floor give `epsilon_d0>=1`.

Assume `epsilon_d0=1`. Then
\[
d_W(d_0)=3,
\]
and only one excess unit remains outside d0.

If the two restored edges have distinct J-endpoints c1,c2 in C union E, at least one of them has zero excess. For that c, `t_c=1` and (1.2) gives `d_W(c)=3`. The nonadjacent pair d0,c again has neighbourhood union at most six, contradiction.

If both restored edges share the same J-endpoint c, then `t_c=2`. The three-neighbour floor applied to (1.2) forces `epsilon_c>=1`; hence the unique remaining excess is on c and
\[
d_W(c)=3.
\]
Again d0,c have union at most six, contradiction.

Thus
\[
\boxed{\epsilon_{d_0}=2.}
\tag{4.1}
\]
All U-excess lies on d0, and
\[
d_W(d_0)=4.
\tag{4.2}
\]

## 5. The restored J-endpoints are distinct and have W-degree three

Since all excess is on d0, every c in C union E has epsilon_c=0.

If both restored edges shared one c, then t_c=2 and (1.2) would give `d_W(c)=2`, contradicting the universal three-neighbour floor. Therefore their J-endpoints are two distinct vertices
\[
c_1,c_2\in C\cup E,
\qquad c_1\ne c_2,
\]
with
\[
d_W(c_1)=d_W(c_2)=3.
\tag{5.1}
\]

For each i, d0 and c_i are H-nonadjacent. Their W-neighbourhood union has size at most seven. By the strengthened deletion lemma, every W profile except `(3,4,5,6),q=0` violates the pair rule.

Hence
\[
\boxed{H[W]=K_3\dot\cup K_4\dot\cup K_5\dot\cup K_6.}
\tag{5.2}
\]

In this q=0 profile, every U vertex must be complete to one whole W component; otherwise one nonneighbour from each of the four components gives an independent five-set with that U vertex.

Since c_i has W-degree exactly three, it must be complete to the unique K3:
\[
\boxed{N_W(c_1)=N_W(c_2)=K_3.}
\tag{5.3}
\]
To make the common nonneighbours of d0 and c_i occupy only two W components, the degree-four neighbourhood of d0 must be exactly the K4:
\[
\boxed{N_W(d_0)=K_4.}
\tag{5.4}
\]

## 6. The other two C-union-E vertices also contain the K3

Let c be either of the two points of `C union E` not used as a restored J-endpoint. It has zero excess and no restored incidence, so
\[
d_W(c)=4.
\]
The pair d0,c is H-nonadjacent. Since `N_W(d0)=K4`, the pair rule says that the common W-nonneighbours cannot meet all three remaining components `K3,K5,K6`.

The vertex c has only four W-neighbours and therefore cannot exhaust K5 or K6. It must exhaust K3. Hence
\[
\boxed{K_3\subseteq N_W(c)\quad\text{for every }c\in C\cup E.}
\tag{6.1}
\]
The two restored J-endpoints have exactly K3; the other two have K3 plus one additional W-neighbour.

## 7. Unique epsilon_U=2 depth-2 terminal

Every epsilon_U=2 depth-2 survivor must satisfy simultaneously:

- both restored edges avoid d0;
- all two U-excess units lie on d0;
- the two restored J-endpoints are distinct points c1,c2 in `C union E`;
- `H[W]=K3 dotcup K4 dotcup K5 dotcup K6` with no cross edges;
- `N_W(d0)=K4`;
- `N_W(c1)=N_W(c2)=K3`;
- all four points of `C union E` are complete to the same K3.

This is now a single labelled full-core terminal. The remaining contradiction must use the A/B/X/Y part of the C5 kernel, W-side U-degree capacities, `omega(H)<=11`, or exact degree-excess accounting.

No delta=12 or E407 closure is claimed here.
