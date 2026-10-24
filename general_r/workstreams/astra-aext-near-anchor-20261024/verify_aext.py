"""Exact algebra and compressed-graph checks. Standard library only.
The all-r proof is THEOREM.md. Finite loops are regression checks, not closure.
Run: python verify_aext.py
"""
from fractions import Fraction as F
from itertools import product, combinations
import json
from pathlib import Path

class P:
    """Sparse Q[r,a,s]; equality compares expanded coefficients exactly."""
    def __init__(self, value=0):
        self.d = value if isinstance(value, dict) else ({(0,0,0): F(value)} if value else {})
        self.d = {k:F(v) for k,v in self.d.items() if v}
    def __add__(self, other):
        other=other if isinstance(other,P) else P(other)
        d=self.d.copy()
        for k,v in other.d.items(): d[k]=d.get(k,F(0))+v
        return P(d)
    __radd__=__add__
    def __neg__(self): return P({k:-v for k,v in self.d.items()})
    def __sub__(self,other): return self+-as_p(other)
    def __rsub__(self,other): return as_p(other)+-self
    def __mul__(self,other):
        other=as_p(other);d={}
        for i,x in self.d.items():
            for j,y in other.d.items():
                k=tuple(u+v for u,v in zip(i,j))
                d[k]=d.get(k,F(0))+x*y
        return P(d)
    __rmul__=__mul__
    def __truediv__(self,scalar): return self*F(1,scalar)
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        ans=P(1)
        for _ in range(n): ans=ans*self
        return ans
def as_p(x): return x if isinstance(x,P) else P(x)
def eq(x,y): assert not (as_p(x)-as_p(y)).d, (as_p(x)-as_p(y)).d
def c(n): return n*(n-1)/2
r=P({(1,0,0):1}); a=P({(0,1,0):1}); s=P({(0,0,1):1})
B=lambda s:(a*r*r-a*r+r*r+2*r*s-r-s*s+s)/2
eq(B(1)*c(a*r+s)-B(s)*c(a*r+1),
   r*(s-1)*(a*a*r*(s-2)+2*a*r*r+a*r*s+r*s+s)/4)
pa=a*c(r)+r
pr=r*c(a)+a
S=(c(a)-1)*r+a
eq(c(a*r+1)-pa-(r-1)*pr,S)
L=r*(c(a-1)-2)+2*a
eq(S-(r-1)-(r-1)*(a-1),L)
U=c(a*r+1)-(r-1)*(pr+a-1)
eq(U-pa, r*(c(a-1)-1)+2*a-1)
eq(U-pa-(r-1), L)
eq(B(1)-pa,c(r))
# alpha saturation: multiply away the denominator 2(a-1)
eq((a*r+1)*(a*r+1-(a-1))-2*(a-1)*B(1),
   r*r+a*r+r-a+2)
# critical polynomial at q=3r-1: an arithmetic checkpoint only
t=r-1; ell=2
critical=r*r*(-ell*ell+3*ell+t-1)+r*(-2*ell*t-2*ell-t*t+2*t+1)-2*t+2
eq(critical,-4*r+4)

def choose2(n): return n*(n-1)//2
def p(k,n):
    q,b=divmod(n,k)
    return k*choose2(q)+b*q
def cap(r,n): return choose2(n)-(r-1)*p(r,n)

# Five types: u, B1-u, v, B2-v, w. Each is a clique.
adj={(0,1),(2,3),(0,2),(1,4),(3,4)}
def is_edge(i,j): return tuple(sorted((i,j))) in adj
for av in range(3,31):
    weights=[1,av-1,1,av-1,1]
    omega=0;alpha=0
    for mask in range(32):
        idx=[i for i in range(5) if mask>>i&1]
        if all(is_edge(i,j) for i,j in combinations(idx,2)):
            omega=max(omega,sum(weights[i] for i in idx))
        if all(not is_edge(i,j) for i,j in combinations(idx,2)):
            alpha=max(alpha,len(idx))
    assert (omega,alpha)==(av,2)
    edges=sum(choose2(w) for w in weights)+sum(weights[i]*weights[j] for i,j in adj)
    assert edges==av*av+av-1
    degrees=[weights[i]-1+sum(weights[j] for j in range(5) if j!=i and is_edge(i,j)) for i in range(5)]
    assert max(degrees)==2*av-2
    for rv in [2*av*(av-1)+2,2*av*(av-1)+3,100000+av]:
        n=av*rv+1
        assert edges+(rv-2)*choose2(av)==p(rv,n)+av-1
        assert (av-1)*n<=choose2(rv)
# Exhaustive small-parameter cap monotonicity and scalar ledgers.
for rv in range(7,151):
    for n in range(rv,6*rv+1):
        assert cap(rv,n+1)-cap(rv,n)==n-(rv-1)*(n//rv)>=0
    x=[rv-1,5+8*rv+12]+[5]*(rv-2)
    assert len(x)==rv and sum(x)==14*rv+6
    assert p(6,6*rv+1)+x[0]<=rv*(7*rv-5)//2
report={
    "status":"EXACT_IDENTITIES_AND_CONSTRUCTION_CHECKED",
    "polynomial_identities":"coefficient-exact over Q[r,a,s]",
    "graph_check":"5-type gadget; a=3..30; analytic proof supplies all a",
    "claim_scope":"single-colour sharpness, not a compatible colouring",
    "A_ext_star":"OPEN",
    "external_theorems_checked_by_script":False,
}
Path(__file__).with_name("VERIFICATION_REPORT.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
print(json.dumps(report,indent=2))
