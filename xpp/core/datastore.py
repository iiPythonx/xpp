# Copyright 2022-2024 iiPython

# Modules
import re
from typing import Any

from .tokenizer import tokenize
from ..exceptions import InvalidSyntax
from ..modules.simpleeval import simple_eval

# Initialization
_format_regex = re.compile(r"\$\([^)]*\)")

# Memory class
class Memory(object):
    def __init__(self, **kwargs) -> None:
        self.sections = {}
        self.variables = {"file": {}, "scope": {}}

        # Garbage attributes
        [setattr(self, name, kwarg) for name, kwarg in kwargs.items()]

# Datastore class
class Datastore(object):
    def __init__(self, mem: Memory, raw: str) -> None:
        self.mem, self.raw, self.id_ = mem, raw, raw.lstrip("@?")

        # Handle variables
        last_stack = self.mem.interpreter.stack[-1]
        self.last_stack = last_stack
        self.store = self.mem.variables["file"][last_stack.path] if self.raw[0] == "@" else self.mem.variables["scope"][last_stack.sid]

        # Load value
        self.refresh()

    def __repr__(self) -> str:
        return f"<DS value={repr(self.value)} raw='{self.raw}'>"

    def _parse(self) -> Any:
        if not self.raw:
            return

        # Check for expression groups
        if self.raw[0] == "{" and self.raw[-1] == "}":
            statement = self.raw.strip("{}").strip()
            if statement.split(" ")[0] not in self.mem.interpreter.operators:  # This is very hacky, to be rewritten
                raise InvalidSyntax(
                    "bracket syntax can only store an operator statement",
                    0,
                    self.mem.interpreter.stack
                )

            return statement

        # Check for strings
        if self.raw[0] in ["\"", "'", "("]:
            if (self.raw[0] == "\"" and self.raw[-1] == "\"") or \
               (self.raw[0] == "'" and self.raw[-1] == "'"):
                value = self.raw[1:][:-1].replace("\\\"", "\"")
                for item in re.findall(_format_regex, value):
                    tokens, obj, reference = item[2:][:-1].split(" "), None, False
                    if len(tokens) < 2:
                        obj = Datastore(self.mem, tokens[0])
                        reference = obj.id_ in obj.store

                    result = self.mem.interpreter.execute(item[2:][:-1]) if not reference else obj.value
                    value = value.replace(item, str(result if result is not None else ""))

                return value.encode("latin-1", "backslashreplace").decode("unicode-escape")  # String literal

            elif self.raw[0] == "(" and self.raw[-1] == ")":
                expr = self.raw[1:][:-1]
                if expr.split(" ")[0] not in self.mem.interpreter.operators:
                    for token in tokenize(expr):
                        if token[0] != "(" or token[-1] != ")":
                            continue

                        elif token[1].isdigit() or token[1] in "+-":
                            break

                        expr = expr.replace(token, str(self.mem.interpreter.execute(token[1:][:-1])))

                    return simple_eval(expr, names = self.mem.variables["scope"][self.last_stack.sid])

                return self.mem.interpreter.execute(expr.replace("\\\"", "\""))

        # Check for ints/floats
        if self.raw[0].isdigit() or self.raw[0] in "+-":
            val = float(self.raw)
            if val.is_integer():
                return int(val)

            return val

        # Handle variable
        self.refresh = self.refreshv
        return self.refresh()

    def set(self, value: Any) -> None:
        self.store[self.id_] = value
        self.value = value

    def delete(self) -> None:
        if self.id_ in self.store:
            del self.store[self.id_]

    def refresh(self) -> Any:
        self.value = self._parse()
        return self.value

    def refreshv(self) -> Any:
        self.value = self.store.get(self.id_)
        return self.value
