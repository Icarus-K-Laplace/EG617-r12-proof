# E407 Q32 — delta=12 depth-2 epsilon_U=1 closure

Date: 2026-10-28  
Status: **PROVED_CONDITIONAL / CLOSED** under the registered 308-edge depth-2 kernel classification and the published Brouwer/Kang–Pikhurko 18-vertex equality theorem. This closes only the depth-2 epsilon_U=1 layer; E407 Q32 remains OPEN / NOT_CERTIFIED.

## 1. U-side endpoint rigidity

Work in the classified depth-2 kernel. For the unique degree-4 J point d0 and the four degree-6 points c in C union E,
\[
d_W(d_0)=2+\epsilon_{d_0}-t_0,
\qquad d_W(c)=4+\epsilon_c-t_c.
\]
At delta=12 with epsilon_U=1, the universal low-W-degree lemma gives
\[
d_W(u)\ge3\quad\text{for every }u\in U.
\]
Hence
\[
2+\epsilon_{d_0}-t_0\ge3.
\]
Since the total U-excess is one,
\[
\boxed{t_0=0,\qquad\epsilon_{d_0}=1.}
\tag{1.1}
\]
All other U-points have zero excess.

The two restored target edges therefore have their J-endpoints in C union E. They cannot share one J-endpoint: if t_c=2 then
\[
d_W(c)=4-2=2<3.
\]
Thus they hit two distinct points c1,c2 and
\[
\boxed{d_W(d_0)=d_W(c_1)=d_W(c_2)=3.}
\tag{1.2}

In the depth-2 C5 kernel, d0 is H-nonadjacent to every point of C union E. Therefore d0,c_i is an H-nonadjacent pair whose W-neighbourhood union has size at most six.

## 2. W is one of five KP equality kernels

The exact W ledger gives
\[
e(H[W])=36-\epsilon_U=35.
\]
Put J_W=bar(H[W]). Then J_W is K5-free on18 vertices and
\[
e(J_W)=153-35=118.
\]

If J_W were four-partite, H[W] would be a disjoint union of four nonempty cliques with sizes n1+...+n4=18 and
\[
\sum_i\binom{n_i}{2}=35.
\]
There is no positive integer solution. Hence J_W is non-four-partite.

Since
\[
t_4(18)-\lfloor18/4\rfloor+1=121-4+1=118,
\]
J_W attains equality in the registered Brouwer/Kang-Pikhurko bound. Therefore H[W] is one of the five explicit equality kernels already listed in `DELTA13_EPS0_KP_KERNEL_REDUCTION.md`:

- base `(3,4,5,5)` with `a=1,2`;
- base `(4,4,4,5)` with `a=1,2,3`.

## 3. Six-deletion lemma for all five equality kernels

### Lemma 3.1

For every one of the five KP equality kernels H[W] and every set D subset W with
\[
|D|\le6,
\]
the graph H[W\D] contains an independent triple.

### Proof

Use the equality representation in the complement J_W. There are four base parts N1,N2,N3,N4 on17 vertices and an exceptional vertex x. Among the base vertices, J_W contains every cross-edge except the edges yA0, where y in N2 and A0 is a nonempty proper subset of N1.

An independent triple in H is exactly a triangle in J_W. It is enough to find a triangle using only base vertices.

After deleting at most six vertices, at least three base parts remain nonempty: emptying two base parts costs at least
\[
3+4=7
\]
in family `(3,4,5,5)` and at least
\[
4+4=8
\]
in family `(4,4,4,5)`.

If three surviving nonempty parts include a triple of parts other than the special combination involving both N1 and N2 only, every choice of one vertex from those three parts gives a J_W-triangle because all relevant base cross-edges are present.

Therefore the only possible way to avoid a base triangle is:

1. at most one of N3,N4 remains nonempty;
2. N2 is reduced to the single vertex y;
3. every surviving N1 vertex lies in A0, so all surviving N1-y edges are exactly the omitted yA0 edges.

The minimum deletion cost of this configuration is
\[
\min(|N_3|,|N_4|)+(|N_2|-1)+(|N_1|-|A_0|).
\]
For `(3,4,5,5)` and a=1,2 this cost is respectively 10 and9. For `(4,4,4,5)` and a=1,2,3 it is respectively 10,9,8. Every value exceeds six.

Thus a base triangle always survives after deleting at most six vertices, equivalently H[W\D] contains an independent triple. QED.

## 4. Terminal contradiction

Take the H-nonadjacent pair d0,c1. By (1.2),
\[
|N_W(d_0)\cup N_W(c_1)|\le6.
\]
Set
\[
D=N_W(d_0)\cup N_W(c_1).
\]
Lemma 3.1 gives an independent triple in H[W\D]. These three vertices are simultaneously nonadjacent to d0 and c1. Hence together with the nonadjacent pair {d0,c1} they form an independent 5-set in H, contradicting
\[
\alpha(H)\le4.
\]

Therefore
\[
\boxed{
\delta=12,\ \text{non-four-partite depth2},\ \epsilon_U=1
\Longrightarrow\bot.
}
\]

## 5. Dependency and scope audit

The proof uses:

1. the registered 308-edge depth-2 C5 kernel classification;
2. the delta=12 low-W-degree lemma;
3. the published Brouwer/Kang-Pikhurko 18-vertex equality classification for the W complement at 118 edges;
4. pure graph `alpha(H)<=4` and exact degree accounting.

It does **not** use Didin. The finite verifier checks the no-35-four-clique partition arithmetic and the five equality-kernel deletion costs; it does not re-prove the external KP equality theorem.

This theorem does not close depth-2 epsilon_U=0, depth-3, delta=12 four-partite U, delta<=11, the five-template compatibility problem, E407 Q32, or EG617(r=12).
