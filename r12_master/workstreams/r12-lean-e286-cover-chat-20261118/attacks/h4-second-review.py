"""Finite diagnostics for the second h4 orbit. Lean imports no test data."""
from itertools import product

def pos(value):
    return max(0, value)

def scalar(a, b):
    return pos(9-a-b) + a*pos(b-2) + b*pos(a-2)

def main():
    costs = {(a,b): scalar(a,b) for a,b in product(range(1,11),range(1,12))}
    assert min(costs.values()) == 5
    minimizers = [ab for ab, cost in costs.items() if cost == 5]
    assert scalar(0,9) == 0  # completion requires its own case
    cases = 0
    for a,c in product(range(11),range(12)):
        for b,d in product(range(12),repeat=2):
            for overlap in range(max(0,b+d-11),min(b,d)+1):
                distinct_cost = (overlap*pos(a+c-2) + (b-overlap)*pos(a-1)
                                 + (d-overlap)*pos(c-1))
                assert distinct_cost >= b*pos(a-2) + d*pos(c-2)
                cases += 1
    print(f"Positive mixed pairs: {len(costs)}, minimum: 5, minimizers: {minimizers}")
    print(f"Shared-leaf size/intersection tuples checked: {cases}")
    print("Zero K10 missing set negative control: cost(0,9)=0")
    print("Diagnostic scope: integer parameters only.")

if __name__ == "__main__":
    main()
