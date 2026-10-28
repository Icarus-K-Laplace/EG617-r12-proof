from itertools import product

FLOORS = {8: 12, 9: 7, 10: 2}
RANGES = {8: range(2, 4), 9: range(3, 5), 10: range(4, 6)}
EXPECTED = {
    (8, 2): {(4, 4), (4, 3)}, (8, 3): {(4, 4, 4)},
    (9, 3): {(4, 4, 4), (4, 4, 3)}, (9, 4): {(4, 4, 4, 4)},
    (10, 4): {(4, 4, 4, 4), (4, 4, 4, 3)}, (10, 5): {(4, 4, 4, 4, 4)},
}
for m, floor in FLOORS.items():
    cap = 47 - 4*m - floor
    assert cap == {8: 3, 9: 4, 10: 5}[m]
    for n in RANGES[m]:
        got = set()
        for xs in product((1, 2, 3, 4), repeat=n):
            if sum(xs) <= cap:
                got.add(tuple(sorted((5-x for x in xs), reverse=True)))
        assert got == EXPECTED[(m, n)]
allowed = {m: {n: [h for h in range(10) if max(0, 2*m-n-13+h) <= 1] for n in RANGES[m]} for m in (8, 9, 10)}
assert allowed == {8: {2: [0], 3: [0, 1]}, 9: {3: [], 4: [0]}, 10: {4: [], 5: []}}
print('V45_SOURCE_CORRECT_PROFILE_ARITHMETIC_OK')
