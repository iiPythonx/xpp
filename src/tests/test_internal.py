# Copyright (c) 2024 iiPython

# Modules
from xpp.modules.ops.stdlib.internal import XOperators

from . import run, global_mem, FakeDatastore

# Begin test definitions
def test_evl():
    run(XOperators.evl, ["mem.variables['_test'] = True"])
    assert global_mem.variables.get("_test") is True

def test_if():
    run(XOperators.if_, [True, "_1"])
    assert global_mem.interpreter.recently_executed[-1] == "_1"
    run(XOperators.if_, [False, "_2"])
    assert global_mem.interpreter.recently_executed[-1] == "_1"
    run(XOperators.if_, [False, "_3", True, "_4"])
    assert global_mem.interpreter.recently_executed[-1] == "_4"
    run(XOperators.if_, [True, "_5", False, "_6"])
    assert global_mem.interpreter.recently_executed[-1] == "_5"

def test_jmp():
    assert run(XOperators.jmp, ["_", "a", 1, .25, True]) == ["a", 1, .25, True]

def test_rem():
    variable = FakeDatastore("hello world")
    run(XOperators.rem, [variable])
    assert variable.deleted is True

def test_ret():
    run(XOperators.ret, [1, 2])
    assert global_mem.interpreter.stack[-1].active is False
    assert global_mem.interpreter.stack[-1].return_value == [1, 2]

def test_rep():
    run(XOperators.rep, [5, "ooga booga"])
    assert global_mem.interpreter.recently_executed[-5:] == ["ooga booga"] * 5

def test_try():
    run(XOperators.try_, ["_RAISE"])
    assert global_mem.interpreter.recently_executed[-1] != "_RAISE"

    run(XOperators.try_, ["_RAISE", "_try"])
    assert global_mem.interpreter.recently_executed[-1] == "_try"

def test_var():
    variable = FakeDatastore(None)
    run(XOperators.var, [variable, "hello world"])
    assert variable.value == "hello world" and variable.raw is None

def test_whl():
    variable = FakeDatastore(True)
    run(XOperators.whl, [variable, "whip and nae nae"])
    assert variable.value is False and global_mem.interpreter.recently_executed[-1] == "whip and nae nae"
