# Outer-Budget Dominance — H+I Joint Audit

Date: 2026-10-24  
Status: **EXACT GAP FORMULA PROVED; uniform dominance OPEN; no $r_0$ certified.**

## 1. Exact reparameterization

For an outer state let
`a=r-1-j`, `d\le r-1`, and `t=r-d\in\{1,\ldots,r\}`. Then
$$
n=r^2-d-jr=ar+t.
$$
The anchor/block budget is
$$
U_r(d,j)=\frac{r(r^2+1)}2-\binom{d+1}{2}-j\binom r2.
$$
Substituting $d=r-t$ and $j=r-1-a$ gives the exact form
$$
\boxed{U_r(d,j)=\frac{(a+1)r(r-1)}2+rt-\binom t2.}
$$

Write $b=t\bmod a$, with $0\le b<a$. The exact balanced Turán floor is
$$
p_a(ar+t)=a\binom r2+rt+\frac{t(t-a)}{2a}+\frac{b(a-b)}{2a}.
$$
Consequently,
$$
\boxed{U_r(d,j)-p_a(n)=
\binom r2-\frac{(a+1)t^2}{2a}+t-\frac{b(a-b)}{2a}.}
$$
These identities hold for integer $r>3$, $a\ge2$, and $1\le t\le r$; the $a=0,1$ rows are handled by the recurrence's base/cutoff rules.

## 2. What the elementary envelope closes

The elementary envelope $B_r(a,n)\ge p_a(n)$ beats the outer budget only where the displayed gap is negative. For fixed $a$ and large $r$, the sign changes at leading order near
$$
t\approx r\sqrt{\frac{a}{a+1}}.
$$
This is only a leading-order guide; exact decisions must use the boxed integer formula including $b$ and lower-order terms. It does not close the states with small $t$.

At the anchor boundary $t=1$,
$$
\boxed{U_r-p_a(ar+1)=\binom r2.}
$$
Thus the recurrence must generate a genuinely stronger floor at this boundary if that state is to be excluded. The multicolor transfer lemma in `ASYMPTOTIC_SEED_ENVELOPE.md` has not supplied that lower floor.

For the two intended terminal coordinates, $t=1$ and:
- $a=4$: $n=4r+1$, the extraction coordinate excluded only under the contextual reductio;
- $a=5$: $n=5r+1$, the design-like terminal deliberately retained.

At $r=12$, the second coordinate has $p_5(61)=342$ and $U=408$, a gap of $66=\binom{12}{2}$. This matches the exact formula; it is not an all-r closure.

## 3. Seed/cutoff obligations and status

To establish a general outer-dominance theorem, one still needs:
1. sound general-r lower-order cutoffs $M_r(2)\le2r-1$ and $M_r(3)\le3r$;
2. lower floors at $(2,2r-1)$, $(3,3r-1)$, $(3,3r)$, $(4,4r-1)$, $(4,4r)$ stronger than $p_a(n)$ by amounts justified uniformly in $r$;
3. proof that recurrence propagation of those floors beats $U_r(d,j)$ for every admissible nonterminal $(d,j)$, including all integer-rounding cases.

The contextual $M_r(4)\le4r$ statement is a reductio assumption against the desired extraction, not an independent theorem.

## 4. Verdict

**No uniform outer-budget dominance theorem and no explicit $r_0$ have been proved.** The exact gap formula localizes the difficult region: small $t=r-d$, where the required excess over $p_a(n)$ is approximately $\binom r2$. The H+I transfer inequality is valid on induced residuals but presently gives an upper constraint, not the needed lower edge floor.

Do not mark H3 as achieved until the remaining seed envelope and all-state integer comparison are proved.

## Round 2 — Outer-state closure gained at t=1 (2026-10-24)

The cutoff theorems in `LOW_ORDER_CUTOFF_THEOREMS.md` eliminate two t=1 states for every integer r >= 6:

- (a,n) = (2,2r+1) is empty by M_r(2) <= 2r-1.
- (a,n) = (3,3r+1) is empty by M_r(3) <= 3r.

At the a=3 boundary, the minimum-degree pivot gives h >= r+1, so
`e(J) >= (3r+1)(r+1)/2`, while
`D_r(3r+1) = (3r^2+3r+6)/2`.
The lower bound exceeds the cap by (r-5)/2, which is positive for r >= 6.

The (a,n) = (4,4r+1) coordinate remains the intended extraction residual, not an unconditional state to eliminate. It is empty only under the contextual no-extraction reductio. The (a,n) = (5,5r+1) design terminal remains deliberately retained.

Thus the exact gap formula is now paired with real elimination results, but all-state dominance is still OPEN: the remaining seed excesses and other admissible outer states have not been uniformly closed. No r_0 for EG617 is claimed.
