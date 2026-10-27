#!/usr/bin/env python3
"""Finite arithmetic audit for SUPPORT_BLOCK_ANCHOR_IDENTITY.md.

Checks only anchor-set cardinality consequences. The component identity and
row-transversal implication are analytic/source-contract statements.
"""

TEMPLATES = {
    "A": 6,
    "B": 8,
    "C": 6,
    "D": 7,
    "E": 5,
}


def main():
    selected = 7
    non_b_labels = 4  # pivot + three S labels
    b_labels = 10
    b_selected_floor = selected - non_b_labels
    assert b_selected_floor == 3
    assert 7 * b_selected_floor == 21

    selected_high_k = {}
    for name, h in TEMPLATES.items():
        floor = max(0, h + b_selected_floor - b_labels)
        selected_high_k[name] = floor
    assert selected_high_k == {"A": 0, "B": 1, "C": 0, "D": 0, "E": 0}

    # Seven selected components cover 28 U vertices and seven outside-core
    # anchors. The complement has 26 vertices: one omitted U point, 18 W
    # points, and seven unselected outside-core labels.
    assert 7 * 4 == 28
    assert 61 - 7 * 5 == 26
    assert 1 + 18 + 7 == 26
    # The complement is exactly three remaining K5 components plus the
    # 11-vertex exceptional gadget.
    assert 3 * 5 + 11 == 26

    print("E407_SUPPORT_BLOCK_ANCHOR_ARITHMETIC_OK")
    print("B-anchored selected blocks per exact-129 color >= 3")
    print("B-anchored support-block occurrences across seven colors >= 21")
    print("selected high-k anchor floor A/B/C/D/E =", selected_high_k)
    print("Scope: cardinality audit only; component identity is analytic/source-dependent.")


if __name__ == "__main__":
    main()
