"""Exhaustive local obstruction search, NOT enumeration of 47-vertex graphs.

Every hypothetical double-K11-pair core yields one of these parameters.
The analytic theorem does not depend on this supplementary search.
"""
import json
from pathlib import Path


def run():
    count, best, witnesses = 0, 1000, []
    for a in range(1, 11):
        for aa in range(a, 11):
            for b in range(1, 11):
                for bb in range(1, 11):
                    for r in range(max(0, a + aa - 10), min(a, aa) + 1):
                        for s in range(max(0, b + bb - 10), min(b, bb) + 1):
                            for adjacent in (0, 1):
                                if adjacent and min(a + aa - r, b + bb - s) <= 1:
                                    continue  # otherwise the two points complete a K12
                                x = (a-r)*max(0,b-1)+(aa-r)*max(0,bb-1)+r*max(0,b+bb-s-2)
                                y = (b-s)*max(0,a-1)+(bb-s)*max(0,aa-1)+s*max(0,a+aa-r-2)
                                z = max(0,10-a-b+adjacent)+max(0,10-aa-bb+adjacent)
                                if not adjacent:
                                    z = max(z, 19-a-aa-b-bb+r+s)
                                bound = x+y+z
                                count += 1
                                if bound < best:
                                    best, witnesses = bound, []
                                if bound == best and len(witnesses) < 8:
                                    witnesses.append([a,aa,b,bb,r,s,adjacent])
    return {"scope":"local intersection parameters only; no whole-graph search",
            "tuples":count,"minimum_excess_bound":best,"sample_minimizers":witnesses,
            "parameters_with_bound_at_most_8":0 if best > 8 else "UNRESOLVED"}


if __name__ == '__main__':
    result = run()
    Path(__file__).with_name('LOCAL_SEARCH_RESULT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
