# Exact Kang–Pikhurko application in the 25-vertex common-neighborhood bound

**Status:** PROVED (direct application of Kang–Pikhurko, Theorem 1).  
**Source:** M. Kang and O. Pikhurko, *Maximum \(K_{r+1}\)-free graphs which are not \(r\)-partite*, Matematychni Studii 24 (2005), no. 1, 12–20, DOI 10.30970/ms.24.1.12-20. The primary PDF is linked from the journal page and states Theorem 1 on printed p. 13.

Let \(S\subseteq V(H)\) have \(|S|=25\), where \(H\) is a 47-vertex graph with \(\alpha(H)\leq4\) and \(\omega(H)\leq11\). Suppose \(\alpha(H[S])\leq2\), and put \(F=\overline{H[S]}\).

1. Since \(\alpha(H[S])\leq2\), the graph \(F\) is triangle-free.
2. The graph \(F\) is not bipartite. If it were bipartite with parts \(X,Y\), then both \(X\) and \(Y\) would be cliques in \(H[S]\). Since \(\omega(H)\leq11\), we would have \(|X|,|Y|\leq11\), contradicting \(|S|=25\).
3. Thus \(F\) is a 25-vertex \(K_3\)-free non-bipartite graph. Kang–Pikhurko Theorem 1 applies with \(n=25,r=2\), since \(25\geq2+3\) and \(2\leq(25-1)/2\). It gives
   \[
   e(F)\leq t_2(25)-\left\lfloor\frac{25}{2}\right\rfloor+1
   =156-12+1=145.
   \]
4. Consequently
   \[
   e(H[S])=\binom{25}{2}-e(F)\geq300-145=155.
   \]
5. If \(H\) has minimum degree at least 12 and total excess
   \[
   T=\sum_{v\in V(H)}(d(v)-12)=8,
   \]
   then
   \[
   2e(H[S])\leq\sum_{v\in S}d_H(v)\leq25\cdot12+8=308,
   \]
   so \(e(H[S])\leq154\), a contradiction.

Therefore no 25-set \(S\) can have \(\alpha(H[S])\leq2\).

For any nonedge \(uv\), its common antineighborhood among the other 45 vertices has size
\[
45-|N(u)\cup N(v)|
=21+c(u,v)-\epsilon(u)-\epsilon(v).
\]
It has independence number at most two, since an independent triple in it together with \(u,v\) would form an independent five-set in \(H\). It therefore has size at most 24, yielding
\[
c(u,v)\leq3+\epsilon(u)+\epsilon(v).
\]

This is the precise parameter check behind the common-neighborhood capacity used in the 286-edge equality proof. It does not use the stronger total-excess-six bound.
