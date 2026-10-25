#!/usr/bin/env python3
"""Arithmetic replay for the explicit saturated-candidate W-extension exclusion.

Checks only the finite W-profile enumeration, transversal fractions, and
component-capacity assignment counts. It does not verify the analytic
independent-set arguments or classify all admissible local J graphs.
"""
from itertools import product, combinations

def t(parts):
    return sum(parts[i] * parts[j] for i in range(4) for j in range(i+1,4))

def partitions4(n=18):
    out=[]
    for a in range(1,n+1):
        for b in range(a,n+1):
            for c in range(b,n+1):
                d=n-a-b-c
                if d>=c and d>=1:
                    out.append((a,b,c,d))
    return out

expected={
    1:[((3,5,5,5),120,0),((4,4,4,6),120,0),((4,4,5,5),121,1)],
    2:[((4,4,5,5),121,0)]
}
for eps in (1,2):
    got=[]
    target=119+eps
    for p in partitions4():
        val=t(p)
        if val>=target:
            got.append((p,val,val-target))
    assert got==expected[eps], (eps,got)

# Common-neighbour capacity sums for the two no-cross-edge eps_U=1 profiles.
assert (11-3)+3*(11-5)==26 < 29
assert 3*(11-4)+(11-6)==26 < 29

# For a single cross-edge in parts (4,4,5,5), deleting any set of <=3
# vertices leaves an independent transversal: the edge forbids fraction
# 1/(remaining_i * remaining_j) of the Cartesian product.
def removals(total, n=4):
    if n==1:
        yield (total,)
        return
    for x in range(total+1):
        for rest in removals(total-x,n-1):
            yield (x,)+rest
parts=(4,4,5,5)
worst=0.0
for s in range(4):
    for rem in removals(s):
        left=tuple(parts[i]-rem[i] for i in range(4))
        assert min(left)>=1
        for i,j in combinations(range(4),2):
            frac=1/(left[i]*left[j])
            worst=max(worst,frac)
            assert frac<1
assert worst <= 0.25

# eps_U=2: count all disjoint-support A/B assignments within capacities
# P1(K4), P2(K5), P3(K5), each side has 7 vertices.
caps=(7,6,6)
solutions=[]
for A in product(*(range(c+1) for c in caps)):
    if sum(A)!=7:
        continue
    for B in product(*(range(c-A[i]+1) for i,c in enumerate(caps))):
        if sum(B)==7 and all(not (A[i] and B[i]) for i in range(3)):
            solutions.append((A,B))
assert len(solutions)==12, len(solutions)
assert all(
    (A==(7,0,0) and B[0]==0) or
    (B==(7,0,0) and A[0]==0)
    for A,B in solutions
)
# After d0 and four C/E vertices occupy 5 of P0's 7 slots,
# and one side occupies P1's 7 slots, the remaining capacity for X/Y
# is at most 2 + 0 + (12 - 7) = 7 < 10.
assert 2 + 0 + (6+6-7) == 7 < 10

print("DELTA14_SATURATED_CANDIDATE_EXTENSION_EXCLUSION_ARITHMETIC_OK")
print("eps_U=1: 3 W profiles; eps_U=2: unique W profile")
print("cross-edge transversal forbidden fraction <= 1/4")
print("eps_U=2: 12 A/B assignment patterns; all leave X/Y capacity <= 7 < 10")
