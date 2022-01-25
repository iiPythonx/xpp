# Copyright 2022 iiPython

# Modules
import os

# Exceptions
class MissingArguments(Exception):
    pass

class InvalidArgument(Exception):
    pass

# x2 Operators
class XTOperators:
    def load(ctx) -> str:
        """
        Loads a UTF-8 decodable file into a variable

        load <path> [out]
        path - str
        out - variable
        """
        if not ctx.args:
            raise MissingArguments("required: path")

        elif not isinstance(ctx.args[0].value, str):
            raise InvalidArgument("path must be a string")

        path = ctx.args[0].value
        if not os.path.isfile(path):
            raise InvalidArgument(f"invalid path: '{path}'")

        with open(path, "r", encoding = "utf-8") as f:
            val = f.read()

        if len(ctx.args) > 1:
            if "var" not in ctx.args[1].flags:
                raise InvalidArgument("val must be a variable")

            ctx.args[1].set(val)

        return val

    def save(ctx) -> None:
        """
        Saves UTF-8 encodable text into a file

        load <path> <val>
        path - str
        val - str, or variable
        """
        if not ctx.args:
            raise MissingArguments("required: path")

        elif not isinstance(ctx.args[0].value, str):
            raise InvalidArgument("path must be a string")

        elif not isinstance(ctx.args[1].value, str):
            raise InvalidArgument("val must be a string")

        with open(ctx.args[0].value, "w+", encoding = "utf-8") as f:
            f.write(ctx.args[1].value)

# Operator map
opmap = {
    "load": XTOperators.load, "save": XTOperators.save
}
