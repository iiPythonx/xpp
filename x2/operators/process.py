# Copyright 2022 iiPython

# Modules
import os
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

    def evl(ctx) -> None:
        """
        Evaluates Python code from the x2 process

        evl <code>
        code - str
        """
        if not ctx.args:
            raise MissingArguments("required: code")

        _x2 = ctx.memory.interpreter
        eval(compile(ctx.args[0].value, "<x2evl>", mode = "exec"), {}, {
            "x2": _x2, "setvar": _x2.setvar, "getvar": _x2.getvar,
            "config": _x2._config, "version": _x2._version
        })

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

    def thrw(ctx) -> None:
        """
        Throws an exception with the given message

        thrw <message>
        message - str
        """
        raise Exception(str(ctx.args[0].value))

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
    "evl": XTOperators.evl, "read": XTOperators.read,
    "thrw": XTOperators.thrw, "wait": XTOperators.wait
}
