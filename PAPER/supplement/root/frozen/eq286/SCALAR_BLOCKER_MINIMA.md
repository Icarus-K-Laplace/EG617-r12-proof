# Scalar blocker minima: complete integer case splits

**Status:** PROVED. All variables below are positive integers.  
**Scope:** The seven scalar inequalities used in the 286-edge equality proof.

Write \(x_+=\max(0,x)\).

## 1. Pair blockers

### \(f_{11}\)

\[
f_{11}(a,b)=(10-a-b)_+ +a(b-2)_+ +b(a-2)_+.
\]
- If \(a=1\), the expression is \((9-b)_++(b-2)_+\geq7\).
- If \(a=2\), it is \((8-b)_++2(b-2)_+\geq6\), with equality only at \(b=2\).
- If \(a\geq3,b=1\), it is \((9-a)_++(a-2)\geq7\).
- If \(a\geq3,b=2\), it is \((8-a)_++2(a-2)\geq7\).
- If \(a,b\geq3\), then \(a(b-2)\geq a\) and \(b(a-2)\geq b\), so
  \[
  f_{11}(a,b)\geq(a+b)+(10-a-b)_+\geq10.
  \]
Thus \(f_{11}\geq6\), with equality only at \((a,b)=(2,2)\).

### \(f_{10,11}\)

\[
f_{10,11}(a,b)=(9-a-b)_+ +a(b-3)_+ +b(a-2)_+.
\]
- If \(a=1\), \((8-b)_++(b-3)_+\geq5\).
- If \(a=2\), \((7-b)_++2(b-3)_+\geq4\), with equality only at \(b=3\).
- If \(a\geq3,b=1\), \((8-a)_++(a-2)\geq6\).
- If \(a\geq3,b=2\), \((7-a)_++2(a-2)\geq6\).
- If \(a\geq3,b\geq3\), then \(b(a-2)\geq b\). For \(a=3\), this term plus \((6-b)_+\) is at least six; for \(a\geq4\), it is at least \(2b\geq6\).
Thus \(f_{10,11}\geq4\), with equality only at \((2,3)\).

### \(f_{9,11}\)

\[
f_{9,11}(a,b)=(8-a-b)_+ +a(b-4)_+ +b(a-2)_+.
\]
- If \(a=1\), \((7-b)_++(b-4)_+\geq3\).
- If \(a=2\), \((6-b)_++2(b-4)_+\geq2\), with equality only at \(b=4\).
- If \(a\geq3,b=1\), \((7-a)_++(a-2)\geq5\).
- If \(a\geq3,b=2\), \((6-a)_++2(a-2)\geq5\).
- If \(a\geq3,b=3\), \((5-a)_++3(a-2)\geq5\).
- If \(a\geq3,b\geq4\), then for \(a=3\) the expression is at least \(b+(5-b)_+\geq5\); for \(a\geq4\), \(b(a-2)\geq2b\geq8\).
Thus \(f_{9,11}\geq2\), with equality only at \((2,4)\).

### \(f_{10,10}\)

\[
f_{10,10}(a,b)=(8-a-b)_+ +a(b-3)_+ +b(a-3)_+.
\]
- If \(a=1\), \((7-b)_++(b-3)_+\geq4\).
- If \(a=2\), \((6-b)_++2(b-3)_+\geq3\).
- If \(a=3\), \((5-b)_++3(b-3)_+\geq2\), with equality only at \(b=3\).
- If \(a\geq4,b=1\), \((7-a)_++(a-3)\geq4\).
- If \(a\geq4,b=2\), \((6-a)_++2(a-3)\geq4\).
- If \(a\geq4,b=3\), \((5-a)_++3(a-3)\geq4\).
- If \(a,b\geq4\), \(a(b-3)+b(a-3)\geq a+b\geq8\).
Thus \(f_{10,10}\geq2\), with equality only at \((3,3)\).

## 2. Simultaneous-incidence blockers

### Three star pairs on a \(K_{10}\)

\[
g_{\rm star}(a,b)=(9-a-b)_+ +a(b-1)+b(a-2)_+.
\]
If \(b=1\), this is \((8-a)_++(a-2)_+\), whose minimum is six, attained exactly for \(2\leq a\leq8\). If \(b\geq2,a=1\), it is \((8-b)_++(b-1)\geq7\). If \(b\geq2,a=2\), it is \((7-b)_++2(b-1)\geq7\). If \(a\geq3,b\geq2\), then \(a(b-1)\geq a\), \(b(a-2)\geq b\), and
\[
g_{\rm star}(a,b)\geq a+b+(9-a-b)_+\geq9.
\]
Thus \(g_{\rm star}\geq6\), with equality exactly at \(b=1,\,2\leq a\leq8\).

### Two mixed \(K_9\)--\(K_{11}\) pairs and two fixed \(K_9\)-completers

\[
g_{\rm two}(a,b)=(8-a-b)_+ +a(b-1)+b(a-2)_+.
\]
If \(b=1\), this is \((7-a)_++(a-2)_+\), whose minimum is five, attained exactly for \(2\leq a\leq7\). If \(b\geq2,a=1\), it is \((7-b)_++(b-1)\geq6\). If \(b\geq2,a=2\), it is \((6-b)_++2(b-1)\geq6\). If \(a\geq3,b\geq2\), then \(a(b-1)\geq a\), \(b(a-2)\geq b\), and
\[
g_{\rm two}(a,b)\geq a+b+(8-a-b)_+\geq8.
\]
Thus \(g_{\rm two}\geq5\), with equality exactly at \(b=1,\,2\leq a\leq7\).

### One mixed \(K_{10}\)--\(K_{11}\) pair with an additional \(K_{10}\)-completer

\[
g_{\rm diamond}(a,b)=(9-a-b)_+ +a(b-2)_+ +b(a-2)_+.
\]
If \(a=1\) or \(b=1\), the expression is at least six. If \(a=2\), it is \((7-b)_++2(b-2)_+\), whose minimum is five only at \(b=2\) and is at least six for \(b\geq3\). If \(a\geq3,b=2\), it is \((7-a)_++2(a-2)\geq6\). If \(a,b\geq3\), then \(a(b-2)\geq a\), \(b(a-2)\geq b\), so the expression is at least
\[
a+b+(9-a-b)_+\geq9.
\]
Thus \(g_{\rm diamond}\geq5\), with equality only at \((2,2)\).

These case splits prove all scalar minima used in the main text; the finite verifier independently checks the same values over the allowed clique-size ranges.
