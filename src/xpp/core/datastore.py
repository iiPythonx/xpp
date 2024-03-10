# Copyright 2022-2024 iiPython

# Modules
import re
import string
from typing import Any

from .tokenizer import tokenize, block_ends, block_starts

from ..exceptions import InvalidSyntax
from ..modules.simpleeval import simple_eval

# Initialization
_FORMAT_REGEX = re.compile(r"\$\([^)]*\)")
_NUMBER_START = string.digits + "+-"

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
        if self.raw[0] not in block_starts:
            if self.raw[0] in _NUMBER_START:
                val = float(self.raw)
                if val.is_integer():
                    return int(val)

                return val

            # Handle variable
            self.refresh = self.refreshv
            return self.refresh()

        # Match statements
        if self.raw[-1] != block_ends[block_starts.index(self.raw[0])]:
            raise InvalidSyntax("open block was not closed", len(self.raw) - 1, self.mem.interpreter.stack)

        match self.raw[0]:
            case "{":
                statement = self.raw[1:][:-1].strip()
                if statement.split(" ")[0] not in self.mem.interpreter.operators:
                    raise InvalidSyntax(
                        "bracket syntax can only store a valid x++ expression",
                        0,
                        self.mem.interpreter.stack
                    )

                return statement

            case "\"" | "'":
                value = self.raw[1:][:-1].replace("\\\"", "\"")
                for item in re.findall(_FORMAT_REGEX, value):
                    tokens, obj, reference = item[2:][:-1].split(" "), None, False
                    if len(tokens) < 2:
                        obj = Datastore(self.mem, tokens[0])
                        reference = obj.id_ in obj.store

                    result = self.mem.interpreter.execute(item[2:][:-1]) if not reference else obj.value
                    value = value.replace(item, str(result if result is not None else ""))

                return value.encode("latin-1", "backslashreplace").decode("unicode-escape")  # String literal

            case "(":
                expr = self.raw[1:][:-1]
                if expr.split(" ")[0] not in self.mem.interpreter.operators:
                    for token in tokenize(expr):
                        if token[0] != "(" or token[-1] != ")":
                            continue

                        elif token[1].isdigit() or token[1] in "+-":
                            break

                        new_data = self.mem.interpreter.execute(token[1:][:-1])
                        if isinstance(new_data, str):
                            new_data = f"\"{new_data}\""

                        expr = expr.replace(token, str(new_data))

                    return simple_eval(expr, names = self.mem.variables["scope"][self.last_stack.sid])

                return self.mem.interpreter.execute(expr.replace("\\\"", "\""))

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
