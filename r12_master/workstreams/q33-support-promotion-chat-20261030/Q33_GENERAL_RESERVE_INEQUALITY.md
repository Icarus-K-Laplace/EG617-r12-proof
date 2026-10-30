# Q33 U/W reserve and component-pair charge inequalities

Status: **PROVED_CONDITIONAL** under the registered seven-witness, exact-129 factor, gadget-independence, and 284-edge core contracts.

## 1. U reserve

Let n=11-m and rho_m=min(6,4n). The 7m selected witness K4s occupy42m distinct edges in L_U. Of these, 42m-6h are isolated-component witness edges owned by exact colors. For each selected gadget witness, each nonexact color is triangle-free on its four vertices, so all nonexact colors together can use at most min(6,4n) edges there. Every nonexact color needs p_12(v) U-edges. The remaining edges outside the selected witness blocks have capacity L_max(v)-42m. Therefore
\[
n p_{12}(v)\le L_{\max}(v)-42m+\rho_mh.
\]
For w>0,
\[
L_{\max}(v)=\binom v2-280+12w-p_4(w);
\]
for w=0, L_max=797.

## 2. W reserve

With f0(v),f1(v) defined by the exact 3- and 4-component profile minima, the W-side inequality is
\[
(m-h)f_0(v)+hf_1(v)+n p_{12}(w)\le t_4(w).
\]

## 3. New component-pair charge

For every k=0,...,4,
\[
\binom{4-k}{2}+2\binom{k}{2}\ge3.
\]
There are N=3m+h unselected isolated component four-sets. If X_U and X_W are their total internal pair costs on U and W, respectively, then
\[
X_W+2X_U\ge3N.
\]
The reserve bounds give
\[
X_U\le B_U=L_{\max}(v)-42m-np_{12}(v)+\rho_mh,
\]
\[
X_W\le B_W=t_4(w)-np_{12}(w).
\]
Hence
\[
\boxed{3(3m+h)\le B_W+2B_U.}
\]

This charge is independent of the f0/f1 minimization and strengthens the separate reserve tests when combined with them.

## 4. Exact first-survivor eliminations

- m=8,v=33: the separate U/W inequalities leave h=5; the charge inequality requires h>=7, contradiction.
- m=9,v=34: the separate U/W inequalities leave h in {4,5,6}; the charge inequality requires h>=7, contradiction.
- m=10,v=35: the separate U/W inequalities leave h in {2,...,8}; the charge inequality requires h=10, contradiction.

The next first survivors are m=8,v=34,h=4..7; m=9,v=35,h=3..9; m=10,v=36,h=3..10.

No graph-level completion is claimed.
