# Copyright (c) 2024 iiPython

# Modules
from typing import Any, List
from types import FunctionType

# Fake classes
class FakeDatastore():
    def __init__(self, value: Any) -> None:
        self.raw, self.value = value, value
        self.deleted = False

    def set(self, value: Any) -> None:
        self.value = value

    def delete(self) -> None:
        self.deleted = True

    def refresh(self) -> None:
        if isinstance(self.value, bool):
            self.value = not self.value

class FakeSection():
    def __init__(self) -> None:
        self.active = True
        self.return_value = []

class FakeInterpreter():
    def __init__(self) -> None:
        self.stack = [FakeSection()]
        self.recently_executed = []

    def execute(self, data: Any) -> None:
        if data == "_RAISE":
            raise ValueError

        self.recently_executed.append(data)

    def run_section(self, section: str, args: List[Any]) -> List[Any]:
        return args

class FakeMemory():
    def __init__(self) -> None:
        self.interpreter = FakeInterpreter()
        self.variables = {}

# Initialization
global_mem = FakeMemory()

# Handle running
def run(function: FunctionType, args: List[Any]) -> Any:
    args = [
        FakeDatastore(a) if not isinstance(a, FakeDatastore) else a
        for a in args
    ]
    return function(global_mem, args)

def full_evaluate(function: FunctionType, args: List[Any], expect: Any) -> None:
    output = FakeDatastore("?")
    assert run(function, args + [output]) == expect
    assert output.value == expect
