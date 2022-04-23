# Copyright 2022 iiPython

# Modules
import re
from typing import Any

from ..modules import iipython

# Initialization
_format_regex = re.compile(r"\$\([^)]*\)")

# Memory class
class Memory(object):
    def __init__(self, interpreter, **kwargs) -> None:
        self.sections = {}
        self.variables = {"global": {
            "true": True, "false": False, "null": None
        }, "file": {}, "scope": {}}
        self.interpreter = interpreter

        # Garbage attributes
        [setattr(self, name, kwarg) for name, kwarg in kwargs.items()]

# Datastore class
class Datastore(object):
    def __init__(self, mem: Memory, raw: str) -> None:
        self.mem, self.raw = mem, raw

        # Handle variables
        last_stack = self.mem.interpreter.stack[-1]
        self.store = self.mem.variables["file"][last_stack.path] if self.raw[0] == "@" else self.mem.variables["scope"][last_stack.sid]

        # Load value
        self.refresh()

    def __repr__(self) -> str:
        return f"<DS value={repr(self.value)} raw='{self.raw}'>"

    def _parse(self) -> Any:

        # Check for strings
        if self.raw and self.raw[0] in ["\"", "("]:
            if self.raw[0] == "\"" and self.raw[-1] == "\"":
                value = self.raw[1:][:-1].replace("\\\"", "\"")
                for item in re.findall(_format_regex, value):
                    result = self.mem.interpreter.execute(item[2:][:-1])
                    value = value.replace(item, str(result if result is not None else ""))

                return value.encode("latin-1", "backslashreplace").decode("unicode-escape")  # String literal

            elif self.raw[0] == "(" and self.raw[-1] == ")":
                expr = self.raw[1:][:-1]
                if " " not in expr and expr in self.store and expr not in self.mem.interpreter.operators:
                    return self.store[expr]

                return self.mem.interpreter.execute(expr.replace("\\\"", "\""))

        # Check for ints/floats
        for c in [int, float]:
            try:
                return c(self.raw)

            except ValueError:
                pass

        # Handle variable
        return self.store.get(self.raw.lstrip("@"))

    def set(self, value: Any) -> None:
        self.store[self.raw.lstrip("@")] = value
        self.value = value

    def refresh(self) -> None:
        self.value = self._parse()
