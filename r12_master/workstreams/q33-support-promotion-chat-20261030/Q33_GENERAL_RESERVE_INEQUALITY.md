# Q33 U/W reserve and component-pair charge inequalities

Status: **PROVED_CONDITIONAL** under the registered seven-witness, exact-129 factor, gadget-independence, and 284-edge core contracts.

## 1. Sharp gadget overlap

For a selected gadget witness Q inside G_C, the exact gadget condition alpha(C[G_C])<=2 implies alpha(C[Q])<=2. Therefore e_C(Q)>=2. Unique edge ownership leaves at most four of the six pairs of Q for all other colors combined. The aggregate nonexact-color overlap per gadget witness is consequently at most four, not six.

## 2. U reserve

Let n=11-m. The 7m selected witness K4s occupy42m distinct edges in L_U; 42m-6h are component-witness edges owned by exact colors. The h gadget witnesses allow at most4h nonexact-color overlaps in total. Every nonexact color needs p_12(v) U-edges. Hence
\[
n p_{12}(v)\le L_{\max}(v)-42m+4h.
\]
For w>0,
\[
L_{\max}(v)=\binom v2-280+12w-p_4(w);
\]
for w=0, L_max=797.

## 3. W reserve

With f0(v),f1(v) defined by the exact 3- and 4-component profile minima,
\[
(m-h)f_0(v)+hf_1(v)+n p_{12}(w)\le t_4(w).
\]

## 4. Component-pair charge

For each unselected component K4 with k vertices in U:
\[
\binom{4-k}{2}+2\binom{k}{2}\ge3.
\]
There are 3m+h such K4s. If their total U- and W-pair costs are X_U,X_W, then X_W+2X_U>=3(3m+h). The reserve bounds give
\[
X_U\le B_U=L_{\max}(v)-42m-np_{12}(v)+4h,\quad
X_W\le B_W=t_4(w)-np_{12}(w).
\]
Thus
\[
\boxed{3(3m+h)\le B_W+2B_U.}
\]

## 5. Result

The sharp coefficient rho=4 plus the charge inequality excludes:
- m=8: v=31,32,33;
- m=9: v=32,33,34;
- m=10: v=34,35.

First scalar/profile survivors are:
- m=8,v=34,h=7;
- m=9,v=35,h=5,...,9;
- m=10,v=36,h=3,...,10.

No graph-level completion is claimed.
