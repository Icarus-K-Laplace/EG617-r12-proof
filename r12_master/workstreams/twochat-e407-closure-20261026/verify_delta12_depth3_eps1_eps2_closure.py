#!/usr/bin/env python3
"""Arithmetic audit for DELTA12_DEPTH3_EPS1_EPS2_CLOSURE.md."""


def main():
    # epsilon_U=1: degree-sum lower bound 6 and exact formula force
    # eps_x+eps_y=1 and I_x=I_y=0.
    survivors = []
    for eps_x in range(2):
        eps_y = 1 - eps_x
        for I_x in range(4):
            for I_y in range(4):
                s = 5 + eps_x + eps_y - I_x - I_y
                if s >= 6:
                    survivors.append((eps_x, eps_y, I_x, I_y, s))
    assert survivors == [(0, 1, 0, 0, 6), (1, 0, 0, 0, 6)]

    # epsilon_U=2: restoring xy would count once at each endpoint and drive
    # the degree sum below the universal 6 lower bound.
    assert 5 + 2 - 2 == 5 < 6

    # In the (3,5,5,5)+one-cross profile an unsaturated vertex needs at
    # least 3+5-2=6 neighbours, so degree3/4 x,y must saturate K3.
    assert 3 + 5 - 2 == 6

    # In the no-cross survivor, a P3/P4 point has degree<=6 and cannot
    # simultaneously saturate K3 and K4.
    assert 3 + 4 > 6
    assert 5 + 6 > 6

    print("DELTA12_DEPTH3_EPS1_EPS2_CLOSURE_OK")
    print("Scope: arithmetic only; registered equality/profile reductions are inputs.")


if __name__ == "__main__":
    main()
