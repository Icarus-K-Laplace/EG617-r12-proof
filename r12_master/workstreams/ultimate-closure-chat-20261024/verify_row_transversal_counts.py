#!/usr/bin/env python3
"""Exact arithmetic audit for E407 template and E408 Q33 high-k row floors.

Uses only Python's standard library. This verifies finite count arithmetic,
not graph realization or the analytic T61 input contracts.
"""

def e407_profiles():
    out = {}
    # A: n0+n1+n3=10, 3n0+2n1<=8
    vals = []
    for n0 in range(11):
        for n1 in range(11 - n0):
            n3 = 10 - n0 - n1
            if 3*n0 + 2*n1 <= 8:
                vals.append((n3, (n0, n1, n3)))
    minimum = min(v for v, _ in vals)
    out["A"] = (minimum, sorted(p for v, p in vals if v == minimum))

    # B: n0+n2+n3=10, 3n0+n2<=8
    vals = []
    for n0 in range(11):
        for n2 in range(11 - n0):
            n3 = 10 - n0 - n2
            if 3*n0 + n2 <= 8:
                vals.append((n2+n3, (n0, n2, n3)))
    minimum = min(v for v, _ in vals)
    out["B"] = (minimum, sorted(p for v, p in vals if v == minimum))

    # C: n0+n1+n3=10, 3n0+2n1<=9
    vals = []
    for n0 in range(11):
        for n1 in range(11 - n0):
            n3 = 10 - n0 - n1
            if 3*n0 + 2*n1 <= 9:
                vals.append((n3, (n0, n1, n3)))
    minimum = min(v for v, _ in vals)
    out["C"] = (minimum, sorted(p for v, p in vals if v == minimum))

    # D: n0+na+nb+n3=10, 3n0+na+nb<=9
    vals = []
    for n0 in range(11):
        for na in range(11 - n0):
            for nb in range(11 - n0 - na):
                n3 = 10 - n0 - na - nb
                if 3*n0 + na + nb <= 9:
                    vals.append((na+nb+n3, (n0, na, nb, n3)))
    minimum = min(v for v, _ in vals)
    out["D"] = (minimum, sorted(p for v, p in vals if v == minimum))

    # E: n0+n1+n2+n3=10, 3n0+2n1+n2<=10
    vals = []
    for n0 in range(11):
        for n1 in range(11 - n0):
            for n2 in range(11 - n0 - n1):
                n3 = 10 - n0 - n1 - n2
                if 3*n0 + 2*n1 + n2 <= 10:
                    vals.append((n2+n3, (n0, n1, n2, n3)))
    minimum = min(v for v, _ in vals)
    out["E"] = (minimum, sorted(p for v, p in vals if v == minimum))
    return out


def q33_profiles():
    # (n0,n1,n2,n3), sum=10, c_S=n1+2*n2+3*n3 >=22-beta.
    all_counts = []
    for n0 in range(11):
        for n1 in range(11 - n0):
            for n2 in range(11 - n0 - n1):
                n3 = 10 - n0 - n1 - n2
                c_s = n1 + 2*n2 + 3*n3
                high = n2 + n3
                all_counts.append((high, c_s, (n0, n1, n2, n3)))
    out = {}
    for beta in range(4):
        feasible = [x for x in all_counts if x[1] >= 22 - beta]
        h_min = min(x[0] for x in feasible)
        profiles = sorted(x[2] for x in feasible if x[0] == h_min)
        out[beta] = (h_min, profiles)
    return out


def main():
    e = e407_profiles()
    q = q33_profiles()
    expected_e = {"A": 6, "B": 8, "C": 6, "D": 7, "E": 5}
    expected_q = {0: 6, 1: 6, 2: 5, 3: 5}

    for template, (minimum, profiles) in e.items():
        print(f"E407 {template}: minimum high-k rows={minimum}; profiles={profiles}")
        assert minimum == expected_e[template]
    for beta, (minimum, profiles) in q.items():
        print(f"Q33 beta={beta}: minimum high-k rows={minimum}; profiles={profiles}")
        assert minimum == expected_q[beta]

    assert e["E"][1] == [(0, 5, 0, 5)]
    assert q[2][1] == [(0, 5, 0, 5)]
    assert q[3][1] == [(0, 5, 0, 5), (0, 5, 1, 4), (1, 4, 0, 5)]
    print("ALL EXACT COUNT CHECKS PASSED")


if __name__ == "__main__":
    main()
