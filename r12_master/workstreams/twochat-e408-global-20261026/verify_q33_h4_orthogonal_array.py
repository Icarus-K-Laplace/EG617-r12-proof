#!/usr/bin/env python3
"""Exhaustive finite check that OA(4,4,2,2) does not exist."""
from itertools import combinations, product


def balanced_columns():
    return [x for x in product((0, 1), repeat=4) if sum(x) == 2]


def orthogonal(a, b):
    pairs = [(a[i], b[i]) for i in range(4)]
    return len(set(pairs)) == 4


def max_orthogonal_family(columns):
    for size in range(len(columns), 0, -1):
        for family in combinations(columns, size):
            if all(orthogonal(a, b) for a, b in combinations(family, 2)):
                return size, family
    return 0, ()


def main():
    columns = balanced_columns()
    assert len(columns) == 6
    max_size, family = max_orthogonal_family(columns)
    assert max_size == 3, (max_size, family)
    assert all(sum(col) == 2 for col in columns)
    assert all(not orthogonal(a, b) for a, b in combinations(columns, 2)
               if a == tuple(1 - x for x in b) or a == b)
    print("PASS: OA(4,4,2,2) obstruction")
    print("balanced binary columns:", len(columns))
    print("maximum pairwise-orthogonal family size:", max_size)
    print("required for h=4 endpoint:", 4)
    print("UNSAT: no four balanced binary columns can be pairwise orthogonal")


if __name__ == "__main__":
    main()
