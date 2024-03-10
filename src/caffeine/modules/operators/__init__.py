# Copyright 2023-2024 iiPython

# Modules
from typing import Any, List
from types import FunctionType

# Helper methods
def convert_value(value: str) -> Any:
    try:
        value = float(value)
        if value.is_integer():
            value = int(value)
    
        return value

    except ValueError:
        if value[0] not in ["'", "\""]:
            value = value.replace("@", "_GL")

        return value

# Operator handling
class OperatorHandler(object):
    def __init__(self) -> None:
        self.mapping = {}

    def operator(self, names: List[str] | str) -> FunctionType:
        names = [names] if not isinstance(names, list) else names
        def internal_callback(operator: FunctionType):
            for name in names:
                self.mapping[name] = operator

        return internal_callback

operators = OperatorHandler()

# Quick reference to the decorator
operator = operators.operator

# Load rest of operators
from . import (  # noqa: E402
    fileio, internal, math, objects, stdio, strman  # noqa: F401
)
