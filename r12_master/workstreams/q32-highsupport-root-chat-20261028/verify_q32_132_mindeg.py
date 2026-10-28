from math import comb

# Registered KP second-Turan arithmetic for r=11.
values = {
    58: {"C": comb(58, 2), "t": comb(58, 2) - (3 * comb(6, 2) + 8 * comb(5, 2))},
    59: {"C": comb(59, 2), "t": comb(59, 2) - (4 * comb(6, 2) + 7 * comb(5, 2))},
    60: {"C": comb(60, 2), "t": comb(60, 2) - (5 * comb(6, 2) + 6 * comb(5, 2))},
}
expected = {58: (1653, 1528, 1524, 129), 59: (1711, 1581, 1577, 134), 60: (1770, 1635, 1631, 139)}
for n, row in values.items():
    t = row["t"]
    p = t - n // 11 + 1
    floor = row["C"] - p
    assert (row["C"], t, p, floor) == expected[n]

# Degree 0/1 contradict the induced non-neighborhood edge floor.
assert expected[60][3] > 132
assert expected[59][3] > 131

# For degree 2, equality at 129 is ruled out by KP Theorem 4 plus omega<=5:
# the eleven old parts would have total size 57 but each size <=5 (sum <=55).
# Hence e(D[N]) >=130; adding the two incident edges exhausts 132,
# leaving no edge to raise either neighbor from degree 1 to degree >=2.
assert expected[58][3] == 129
assert expected[58][3] + 1 == 130
assert 130 + 2 == 132
assert 13 + 10 * 4 + 3 == 56
assert 60 - (13 + 10 * 4 + 3) == 4
print("Q32_132_MINDEG_ARITHMETIC_OK")
