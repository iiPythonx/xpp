# Copyright 2022 iiPython

# Modules
import re
from typing import Any
from types import NoneType

from .memory import XTMemory
from .exceptions import ConstantVariable

# Datastore class
class XTDatastore(object):
    def __init__(self, mem: XTMemory, raw: str, section_override: str = None) -> None:
        self.mem, self.raw, self.flags = mem, raw, []

        self.active_file = self.mem.interpreter.linetrk[-1][0]
        self.active_section = section_override or self.mem.interpreter.linetrk[-1][1]

        self.keydict = {
            "#": self.mem.vars["globals"],
            "@": self.mem.vars["file"][self.active_file]
        }[self.raw[0]] if self.raw[0] in ["#", "@"] else self.mem.vars["local"][self.active_section]
        self.refresh()

    def __repr__(self) -> str:
        return f"<XTDS val={repr(self.value)}>"

    def _parse(self) -> Any:
        if self.raw:
            if self.raw[0] == "(" and self.raw[-1] == ")":
                expression = self.raw[1:][:-1].replace("\\\"", "\"")
                result = self.mem.interpreter.execute(expression)
                return result if result is not None else ""

            elif self.raw[0] == "\"" and self.raw[-1] == "\"":
                value = self.raw[1:][:-1].replace("\\\"", "\"")
                for item in re.findall(re.compile(r"\$\([^)]*\)"), value):
                    result = self.mem.interpreter.execute(item[2:][:-1])
                    value = value.replace(item, str(result if result is not None else ""))

                return value.encode("latin-1", "backslashreplace").decode("unicode-escape")  # String literal

        # Integer/float literal
        for check in [int, float]:
            try:
                return check(self.raw)

            except ValueError:
                pass

        # Provided variable
        val = self.keydict.get(self.raw[1:] if self.raw[0] in ["#", "@"] else self.raw)
        self.flags.append("var")
        if not isinstance(val, (tuple, NoneType)):
            raise RuntimeError("variable value was not a tuple or None, are variables being tampered with?")

        elif val is not None:
            if val[1]:
                self.flags.append("const")

            return val[0]  # 0 is the value, 1 is whether its a constant

        return None

    def set(self, value: str) -> Any:
        if "const" in self.flags:
            raise ConstantVariable(f"the constant {self.raw} cannot be reassigned")

        self.value = value
        if "var" in self.flags:
            if self.active_file not in self.mem.vars["file"] and self.raw[0] == "@":
                self.mem.vars["file"][self.active_file] = {}

            self.keydict[self.raw[1:] if self.raw[0] in ["#", "@"] else self.raw] = (value, False)

        return value

    def setconst(self) -> None:
        self.flags.append("const")
        self.keydict[self.raw[1:] if self.raw[0] in ["#", "@"] else self.raw] = (self._parse(), True)

    def delete(self) -> None:
        if "const" in self.flags:
            raise ConstantVariable("cannot delete a constant variable")

        elif "var" in self.flags:
            del self.keydict[self.raw[1:] if self.raw[0] in ["#", "@"] else self.raw]

    def refresh(self) -> None:
        self.value = self._parse()

# Context object
class XTContext(object):
    def __init__(self, memory: XTMemory, args: list) -> None:
        self.memory = memory
        self.args = [XTDatastore(memory, a) for a in args]

    def __repr__(self) -> str:
        return f"<XTCTX Arguments={repr(self.args)}>"
