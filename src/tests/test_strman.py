# Copyright (c) 2024 iiPython

# Modules
from xpp.modules.ops.stdlib.strman import XOperators

from . import run, full_evaluate

# Begin test definitions
def test_chr():
    full_evaluate(XOperators.chr_, ["hello", 0], "h")
    full_evaluate(XOperators.chr_, ["hello", 0, 2], "hel")

def test_flt():
    full_evaluate(XOperators.flt_, ["0.5"], 0.5)
    full_evaluate(XOperators.flt_, ["-0.5"], -0.5)

def test_idx():
    full_evaluate(XOperators.idx, ["hello world", "world"], 6)

def test_int():
    full_evaluate(XOperators.int_, ["5"], 5)

def test_len():
    full_evaluate(XOperators.len_, ["hello"], 5)

def test_lwr():
    full_evaluate(XOperators.lwr, ["HELLO"], "hello")

def test_str():
    assert run(XOperators.str_, [1]) == "1"
    assert run(XOperators.str_, [0.5]) == "0.5"

def test_upr():
    full_evaluate(XOperators.upr, ["hello"], "HELLO")
