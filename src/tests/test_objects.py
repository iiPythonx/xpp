# Copyright (c) 2024 iiPython

# Modules
from xpp.modules.ops.stdlib.objects import XOperators

from . import run, full_evaluate, FakeDatastore

# Begin test definitions
def test_new():
    assert isinstance(run(XOperators.new, ["list"]), list)
    assert isinstance(run(XOperators.new, ["dict"]), dict)

    full_evaluate(XOperators.new, ["list"], [])
    full_evaluate(XOperators.new, ["dict"], {})

def test_psh():
    variable = FakeDatastore([1, 2])
    run(XOperators.psh, [variable, 3])
    assert variable.value == [1, 2, 3]

def test_pop():
    full_evaluate(XOperators.pop, [[1, 2, 3]], 3)

def test_get():
    full_evaluate(XOperators.get, [{"a": 5}, "a"], 5)

def test_set():
    variable = FakeDatastore({"a": 5})
    assert variable.value["a"] == 5
    run(XOperators.set_, [variable, "a", 6])
    assert variable.value["a"] == 6
    