#!/usr/bin/env python3
"""Finite parity replay for residual six-set injectivity.

This checks only the 2x2 matching-orientation step. The proof additionally
depends on the single-outside holonomy-cost theorem, t_C <= 1, and
pair-projection injectivity.
"""
from itertools import product


def parity(bits):
    return sum(bits) % 2  # 0: two triangles; 1: one six-cycle


checked = 0
for bits in product((0, 1), repeat=3):
    complementary = tuple(1 - bit for bit in bits)
    p, q = parity(bits), parity(complementary)
    assert p != q
    assert (p ^ q) == 1
    checked += 1

assert checked == 8
print("orientation triples checked:", checked)
print("complementary pair matchings always toggle triangle/six-cycle parity")
print("V47_Z01_RESIDUAL_SIGNATURE_PARITY_OK")
print("Scope: finite orientation step only; no global Q32 UNSAT claim.")
