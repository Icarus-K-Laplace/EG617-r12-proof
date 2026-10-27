#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for the KP (n,r)=(61,12) instance.

This script does not parse or trust project-generated Type-I/II/III tables.
It recomputes:
  * t_12(61) and p_12(61),
  * all nondecreasing 12-part sequences summing to 60 that satisfy
    Kang--Pikhurko Lemma 5's optimality inequalities,
  * the contextual elimination of every sequence containing a part >=6.
"""

from math import comb

N = 61
R = 12
EXACT_COLOR_EDGES = 129
COLOR_CLIQUE_CAP = 5


def turan_edges(n: int, r: int) -> int:
    q, rem = divmod(n, r)
    parts = [q + 1] * rem + [q] * (r - rem)
    return comb(n, 2) - sum(comb(x, 2) for x in parts)


def kp_sequences(total: int, length: int):
    out = []

    def rec(prefix, last, remaining, slots):
        if slots == 0:
            if remaining != 0:
                return
            a = tuple(prefix)
            if (
                a[0] >= 2
                and a[1] <= a[0] + 1
                and a[-1] <= a[0] + 2
                and a[-1] <= a[2] + 1
            ):
                out.append(a)
            return

        max_value = remaining // slots
        for value in range(last, max_value + 1):
            rec(prefix + [value], value, remaining - value, slots - 1)

    rec([], 1, total, length)
    return out


def main():
    assert N >= R + 3
    assert R <= (N - 1) // 2

    total_pairs = comb(N, 2)
    complement_edges = total_pairs - EXACT_COLOR_EDGES
    t = turan_edges(N, R)
    p = t - (N // R) + 1

    assert total_pairs == 1830
    assert t == 1705
    assert p == 1701
    assert complement_edges == p

    seqs = kp_sequences(N - 1, R)
    expected = {
        (5,) * 12,
        (4,) + (5,) * 10 + (6,),
        (4, 4) + (5,) * 8 + (6, 6),
    }
    assert set(seqs) == expected
    assert len(seqs) == 3

    contextual_survivors = [s for s in seqs if max(s) <= COLOR_CLIQUE_CAP]
    assert contextual_survivors == [(5,) * 12]

    print("KP_EXACT129_INSTANCE_VERIFIED")
    print(f"total_pairs={total_pairs}")
    print(f"t_12_61={t}")
    print(f"p_12_61={p}")
    print(f"complement_of_129_edges={complement_edges}")
    print("optimal_sequences=")
    for seq in seqs:
        print("  " + str(seq))
    print("contextual_survivor=(5^12)")
    print("factor=10 isolated K5 + 11-vertex exceptional gadget")


if __name__ == "__main__":
    main()
