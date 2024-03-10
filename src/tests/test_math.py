# Copyright (c) 2024 iiPython

# Modules
from xpp.modules.ops.stdlib.math import XOperators

from . import run, full_evaluate

# Begin test definitions
def test_add():
    full_evaluate(XOperators.add, [1, 2, 3], 6)

def test_dec():
    full_evaluate(XOperators.dec, [5], 4)

def test_div():
    full_evaluate(XOperators.div, [1, 2], .5)

def test_inc():
    full_evaluate(XOperators.inc, [5], 6)

def test_mul():
    full_evaluate(XOperators.mul, [5, 3], 15)

def test_pow():
    full_evaluate(XOperators.pow, [5, 2], 25)

def test_rnd():
    full_evaluate(XOperators.rnd, [0.3], 0)
    full_evaluate(XOperators.rnd, [0.7], 1)
    full_evaluate(XOperators.rnd, [0.5666, 2], .57)
    full_evaluate(XOperators.rnd, [0.203, 3], .203)

def test_rng():
    assert isinstance(run(XOperators.rng, [1, 5]), int)
    full_evaluate(XOperators.rng, [1, 1], 1)

def test_sub():
    full_evaluate(XOperators.sub, [1, 2], -1)
