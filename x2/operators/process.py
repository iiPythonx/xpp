# Copyright 2022 iiPython

# Modules
import os
from typing import Any
from time import sleep

# Exceptions
class MissingArguments(Exception):
    pass

class InvalidArgument(Exception):
    pass

# x2 Operators
class XTOperators:
    def cls(ctx) -> None:
        """
        Clears the screen

        cls
        """
        os.system("clear" if os.name != "nt" else "cls")

    def ext(ctx) -> None:
        """
        Exits the x2 process

        ext [code]
        code - int
        """
        code = 0 if not ctx.args else ctx.args[0].value
        if not isinstance(code, int):
            raise InvalidArgument("code must be an integer if specified")

        os._exit(code)

    def evl(ctx) -> Any:
        """
        Evaluates Python code from the x2 process

        evl <code> [out]
        code - str
        out - variable
        """
        if not ctx.args:
            raise MissingArguments("required: code")

        result = eval(compile(ctx.args[0].value, "<x2evl>", mode = "single"), {}, {"_x2": ctx.memory.interpreter})
        output = ctx.args[1] if len(ctx.args) > 1 else None
        if output:
            output.set(result)

        return result

    def read(ctx) -> str:
        """
        Reads a stream from stdin

        read [prompt] [out]
        prompt - str
        out - variable
        """
        prompt = ctx.args[0].value if ctx.args else ""
        output = ctx.args[1] if len(ctx.args) > 1 else None
        value = input(prompt)
        if output is not None:
            output.set(value)

        return value

    def wait(ctx) -> None:
        """
        Halts the process for a number of seconds

        wait <val>
        val - number-like
        """
        if not ctx.args:
            raise MissingArguments("required: val")

        val = ctx.args[0].value
        if not isinstance(val, (int, float)):
            raise InvalidArgument("val must be a number-like value")

        sleep(val)

# Operator map
opmap = {
    "cls": XTOperators.cls, "ext": XTOperators.ext,
    "evl": XTOperators.evl,
    "read": XTOperators.read, "wait": XTOperators.wait
}
