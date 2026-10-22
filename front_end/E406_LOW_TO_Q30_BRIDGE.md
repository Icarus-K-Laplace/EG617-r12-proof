# E406 low-to-q30 bridge

Status: `PROVED`.

This theorem closes the last logical gap between the certified S31 descent pivot and the independently closed q30->q31 boundary classes.

## Statement

Assume the explicit E406 T61 parent contract:

- `|R|=61`, `e(R)=406`, `delta(R)=13`;
- `alpha(R)<=5`, `omega(R)<=11`;
- all inherited density caps;
- every degree-13 pivot has the standard 13-shell / 47-core decomposition.

Let `p` be any degree-13 pivot with `q_p<=30`.

Then the same parent contains a degree-13 pivot `r` with

`q_r=30`.

Moreover the route from p to r can be chosen as a sequence of regular repivots whose charges never need to pass through q31.

## 1. q22 and q23 are impossible; q24--q26 promote

By `E406_LOW_Q_PROMOTION_22_26.md`:

- q22 and q23 shells are impossible;
- every q24, q25 or q26 pivot has a regular witness y with `q_y>=27`;
- the witness has missing degree2 or3.

The q27 and q28 levels themselves are impossible by `E406_Q27_Q28_ELIMINATION.md`.

Thus a low-charge promotion witness from q24--q26 can only land at

`q_y in {29,30,31}`.

We now exclude the direct jump to31.

### 1a. A d3 witness cannot jump directly to q31

Let the old charge be q<=26 and suppose a regular d3 witness y had q_y=31. The new 47-core has284 edges and hence minimum degree at least12.

For a regular repivot with missing side S of size d, the inserted-excess sum is the exact identity

`eta = q-d(13-d)-rho-e_M(S)-e_R(S,D)`,

where every term except q is nonnegative once the new core has minimum degree12.

For d=3,

`d(13-d)=30>q`,

so eta<0, contradiction.

Hence a d3 low-charge witness cannot land at q31.

### 1b. Triangle-channel d2 witnesses cannot jump to q31

In the triangle channel of the q24--q26 promotion theorem, the ten-point outside set is M-independent and a regular d2 witness y misses two vertices `i,j` of a missing triangle T.

Every triangle vertex has weight at least9, while

`t(T)<=q+3<=29`.

Therefore

`t_i+t_j<=20`.

If y jumped to q31, its new284-edge core would have minimum degree at least12. For d=2 with the two missing neighbours adjacent in M, the exact inserted-excess identity becomes

`eta=t_i+t_j-24-e_R({i,j},D)`.

Thus eta>=0 would require `t_i+t_j>=24`, contradiction.

### 1c. Triangle-free d2 witnesses cannot jump to q31

In the triangle-free channel, König gives a size-3 cover `X={i,j,k}` and an independent 10-side Y. Let y in Y be the regular d2 witness with `N_M(y)={i,j}` and put

`m=1_{ij in E(M)}`.

If y jumped to q31, the new core minimum-degree condition gives

`t_i+t_j >= 22+2m+e_R({i,j},D) >=22+2m`.       (A)

Because Y is M-independent,

`t_i+t_j+t_k = q+e_M(X)-G_Y`.

Since M is triangle-free, `e_M(X)<=2`. From (A),

`t_k <= q+2-G_Y-22-2m <= 6-G_Y`.

The cover vertex k must have an M-neighbour b in Y; otherwise `Y union {k}` is an M-independent11-set, which together with the pivot would create a forbidden target K12.

But

`t_b<=3+g_b<=3+G_Y`,

so

`t_k+t_b<=9<11`,

contradicting the inherited EDGE11 missing-edge row bound.

Therefore no d2 low-charge promotion witness can jump directly to31.

Consequently every q24--q26 pivot promotes to q29 or q30.

## 2. q29 necessarily produces q30, not q31

At q29 the 47-core has286 edges and hence minimum degree at least12. Also

`G<=q-22<=7`.

The canonical uniform shell promotion theorem (`Q26_UNIFORM_SHELL_THEOREM` logic, hypothesis-level) applies: there exists an undecorated witness with

`3<=d_M(y)<=10`

and

`q_y>=30`.

The E406 universal ceiling is q_y<=31.

If q_y=31, the new core has284 edges and minimum degree at least12. The exact inserted-excess identity gives

`eta = 29-d(13-d)-rho-e_M(S)-e_R(S,D)`.

For 3<=d<=10,

`d(13-d)>=30`,

so eta<0, contradiction.

Hence

`q_y=30`.

Thus every q29 pivot has a regular route to a genuine q30 pivot.

## 3. Conclusion

Let p be any degree-13 pivot with q_p<=30.

- q22,q23 are impossible;
- q24--q26 promote to q29 or q30, never directly to31;
- q27,q28 are impossible;
- q29 promotes exactly to q30;
- q30 is already the target level.

Therefore the same E406 parent always contains a genuine q30 degree-13 pivot.

## E406 consequence

The audited S31 theorem supplies at least one degree-13 pivot with q<=30. By the present theorem, every E406 parent therefore contains q30.

The independently replayed canonical q30 hereditary promotion theorem then reaches q31 in at most two regular repivots. The last step is necessarily a genuine adjacent boundary edge

`q30 -> q31`.

All six possible boundary distances are independently closed elsewhere. Hence this bridge supplies the missing global connection needed for the full E406 contradiction.
