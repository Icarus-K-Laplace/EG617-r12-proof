# E407 Q32 — delta=12 depth-2 epsilon_U=3 q=1 closure

Date: 2026-10-28  
Status: **PROVED_CONDITIONAL / CLOSED** under the registered 308-edge depth-2 kernel classification and the delta=12 low-W-degree lemma. Together with `DELTA12_DEPTH2_EPS3_Q0_CLOSURE.md`, this closes the entire depth-2 epsilon_U=3 layer. E407 Q32 remains OPEN.

## 1. W profile and the one-defect pair rule

The remaining epsilon_U=3 profile is a four-clique base of sizes
\[
4,4,5,5
\]
with exactly one H-cross edge `xy` joining two distinct base cliques.

For any subset `Z subset W`, `alpha(H[Z])<=2` has only two possibilities:

1. Z meets at most two base clique components; or
2. Z meets exactly three components, two of them are the components containing x and y, and
   \[
   Z\cap C_x=\{x\},\qquad Z\cap C_y=\{y\},
   \]
   while Z meets one further component and misses the fourth.

Indeed, with three occupied components an independent triple exists unless every choice from the two cross-edge components is forced to use the unique cross edge xy. With four occupied components one can choose three components avoiding at least one cross-edge endpoint pair.

### Corollary 1.1 — defect escape costs at least eleven union vertices

If a nonadjacent core pair `(u,v)` does not fully cover at least two W base components, then its common W-nonneighbour set must be of type (2) above. The largest possible such common nonneighbour set has size
\[
1+1+5=7,
\]
so
\[
|N_W(u)\cup N_W(v)|\ge18-7=11.
\tag{1.1}
\]

Therefore any nonadjacent pair with W-neighbourhood degree sum at most ten obeys the ordinary q=0 component-cover rule: its union must completely cover at least two base components.

## 2. Endpoint rigidity is unchanged

Let d0 be the degree-4 J point and C4=C union E the four degree-6 J points. Exactly as in the q=0 proof, d0 is H-nonadjacent to all four C4 points.

Every such pair needs union size at least eight; the defect escape requires at least eleven and is therefore irrelevant at this stage. Summing the four pair inequalities gives
\[
4\epsilon_{d0}+E_C\ge10+3t_0.
\]
Since epsilon_U=3,
\[
\boxed{t_0=0,\qquad\epsilon_{d0}=3,\qquad E_C=0.}
\tag{2.1}
\]
All U-excess lies on d0 and
\[
d_W(d0)=5.
\]
The two restored J-endpoints are distinct points c1,c2 in C4, each with W-degree three. Every A/B point has zero excess and W-degree
\[
d_W(v)=6-r_v\le6.
\tag{2.2}
\]

For i=1,2 the pair `(d0,c_i)` has degree sum exactly eight, below the defect threshold eleven. It must therefore cover the two K4 base components exactly. Hence for the fixed eight-set
\[
R_8=K_4^P\dot\cup K_4^Q
\]
we have
\[
N_W(c_1)=N_W(c_2)=R_8\setminus N_W(d0).
\tag{2.3}
\]
Put
\[
x=|N_W(d0)\cap K_4^P|,
\]
so `1<=x<=4`.

## 3. Every non-exceptional A/B point is K5-complete plus one common point

Let v lie in one of the two K7 components and suppose v is not simultaneously the restored partner of both c1 and c2. Choose c_i nonadjacent to v.

The pair `(v,c_i)` has degree sum at most nine, and `(v,d0)` has degree sum at most eleven. In the actual alternatives below their union is at most ten unless the q=1 defect pattern could be used. We first solve the c_i pair, where defect escape is impossible by Corollary 1.1.

The c_i pair cannot use the two distinguished K4s by forcing `N_W(d0) subset N_W(v)`: then `(v,d0)` has union at most six and violates both the ordinary and defect pair rules.

Thus `(v,c_i)` must cover one distinguished K4 and one K5. The degree bound `d_W(v)<=6` forces
\[
\boxed{x\in\{1,4\}.}
\tag{3.1}
\]
By symmetry take x=1. Then `N_W(d0)` contains one point q of K4^P and all four points of K4^Q, while each c_i sees the other three points of K4^P.

To cover K4^P plus a K5, v must contain q and all five vertices of one of the two K5 components. Thus
\[
\boxed{N_W(v)=\{q\}\cup K_5^j}
\tag{3.2}
\]
for a non-restored v. This six-set, together with `N_W(d0)`, already covers K4^Q and K5^j, so the d0 pair is legal. The case x=4 is symmetric.

In particular a restored A/B endpoint with `r_v=1` has W-degree five and cannot satisfy (3.2) if it is nonadjacent to one of c1,c2.

Therefore the two restored edges must share one common A/B-side endpoint z. This z is the unique possible exception, being adjacent to both c1 and c2. Every other one of the thirteen A/B vertices has neighbourhood of form (3.2).

## 4. Cross-K7 contradiction

Give each of the thirteen non-exceptional vertices the binary label j in {R,T} of the K5 component appearing in (3.2).

If labelled a in the first K7 and b in the second K7 have the same label, then
\[
N_W(a)\cup N_W(b)=\{q\}\cup K_5^j
\]
has size six. It fully covers only one base component and is far below the eleven-vertex defect-escape threshold. The pair a,b is H-nonadjacent, contradiction.

Hence every constrained cross-K7 pair has opposite labels. With only one exceptional vertex z, one K7 side still has all seven vertices labelled by the same K5. That K7 is complete to a W-clique K5, producing
\[
K_7\vee K_5=K_{12},
\]
contradicting `omega(H)<=11`.

Thus the q=1 profile is impossible.

## 5. Conclusion

Combining with the q=0 closure,
\[
\boxed{
\delta=12,\ \text{depth2},\ \epsilon_U=3\Longrightarrow\bot.
}
\]
under the registered 308-edge depth-2 kernel classification.

This terminal proof does not use Didin. It does not close epsilon_U=0,1,4, depth3, delta=12 four-partite-U, E407 Q32, or EG617(r=12).
