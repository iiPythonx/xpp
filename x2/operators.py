# Copyright 2022 iiPython

# Modules
import os
import string
import random
from typing import Any
from types import FunctionType

# Exceptions
class MissingArguments(Exception):
    pass

class InvalidArgument(Exception):
    pass

# Operator handlers
def expr_eval(ctx, a: Any, b: Any, op: str, ifcb: FunctionType = None, elsecb: FunctionType = None) -> bool:
    _checkmap = {
        "==": lambda a, b: a == b,
        "!=": lambda a, b: a != b,
        ">=": lambda a, b: a >= b,
        "<=": lambda a, b: a <= b,
        ">": lambda a, b: a > b,
        "<": lambda a, b: a < b,
        "in": lambda a, b: a in b,
        "xin": lambda a, b: a not in b,
        "is": lambda a, b: isinstance(a, {"int": int, "str": str, "float": float}[b])
    }
    if op not in _checkmap:
        raise InvalidArgument("unknown operation!")

    elif _checkmap[op](a, b):
        if ifcb is not None:
            ctx.memory._inter.execute(ctx.memory._parser.parse_lines(ifcb)[0])

        return True

    else:
        if elsecb is not None:
            ctx.memory._inter.execute(ctx.memory._parser.parse_lines(elsecb)[0])

        return False

# Built-in X2 operators
class XTBuiltinOperators:
    def out(ctx) -> None:
        """Writes all provided arguments to the screen"""
        print(*[str(a.value).encode("latin-1", "backslashreplace").decode("unicode-escape") for a in ctx.args])

    def psh(ctx) -> None:
        """Assigns a variable a value"""
        if len(ctx.args) != 2:
            raise MissingArguments("missing value or variable!")

        val = ctx.args[1]
        val = val.content if val.isvar else val.value
        if str(val)[0] not in string.ascii_letters + "-":
            raise InvalidArgument("variable name is invalid!")

        ctx.memory.vars[val] = ctx.args[0].value

    def pop(ctx) -> Any:
        """Returns a variables value"""
        if not ctx.args:
            raise MissingArguments("missing value!")

        key = ctx.args[0].content if ctx.args[0].isvar else str(ctx.args[0].value)
        if key not in ctx.memory.vars:
            raise InvalidArgument("unknown or nonexistant variable provided!")

        val = ctx.memory.vars[key]
        if len(ctx.args) > 1:
            dest = ctx.args[1]
            if not dest.isvar:
                raise InvalidArgument("last argument must be variable if provided!")

            dest.set(val)

        return val

    def jmp(ctx) -> None:
        """Jumps to a different section"""
        if not ctx.args:
            raise MissingArguments("missing section to jump to!")

        ctx.memory._inter.run_section(ctx.args[0].value or ctx.args[0].content)

    def imp(ctx) -> None:
        """Imports another x2 module"""
        if not ctx.args:
            raise MissingArguments("missing package to load!")

        path = ctx.args[0].value
        if not path.endswith(".xt"):
            path += ".xt"

        if not os.path.isfile(path):
            raise InvalidArgument(f"no such package: '{path}'!")

        sections = ctx.memory._parser.sectionize(ctx.memory._parser.parse_lines(open(path, "r", encoding = "utf-8").read()))
        ctx.memory._inter.execute_lines(sections["global"])
        del sections["global"]

        ctx.memory._inter.sections = ctx.memory._inter.sections | sections

    def evl(ctx) -> None:
        """Evaluates an expression"""
        if len(ctx.args) < 4:
            raise MissingArguments("required: a, operator, b, and callback!")

        a, b, op, ifcb = ctx.args[0].value, ctx.args[2].value, ctx.args[1].content, ctx.args[3].value
        try:
            elsecb = ctx.args[4].value

        except IndexError:
            elsecb = None

        expr_eval(ctx, a, b, op, ifcb, elsecb)

    def ext(ctx) -> None:
        """Exits the process"""
        os._exit(0)

    def add(ctx) -> Any:
        """Adds two literals or variables together"""
        if not len(ctx.args) == 3:
            raise MissingArguments("required: a, b, and c!")

        elif ctx.args[0].value is None or ctx.args[1].value is None:
            raise InvalidArgument("a + b cannot be null!")

        return ctx.args[2].set(ctx.args[0].value + ctx.args[1].value)

    def sub(ctx) -> Any:
        """Subtracts two literals or variables"""
        if not len(ctx.args) == 3:
            raise MissingArguments("required: a, b, and c!")

        elif ctx.args[0].value is None or ctx.args[1].value is None:
            raise InvalidArgument("a + b cannot be null!")

        return ctx.args[2].set(ctx.args[0].value - ctx.args[1].value)

    def mul(ctx) -> Any:
        """Multiplies two literals or variables"""
        if not len(ctx.args) == 3:
            raise MissingArguments("required: a, b, and c!")

        elif ctx.args[0].value is None or ctx.args[1].value is None:
            raise InvalidArgument("a + b cannot be null!")

        return ctx.args[2].set(ctx.args[0].value * ctx.args[1].value)

    def div(ctx) -> Any:
        """Divides two literals or variables"""
        if not len(ctx.args) == 3:
            raise MissingArguments("required: a, b, and c!")

        elif ctx.args[0].value is None or ctx.args[1].value is None:
            raise InvalidArgument("a + b cannot be null!")

        return ctx.args[2].set(ctx.args[0].value / ctx.args[1].value)

    def rnd(ctx) -> int:
        """Rounds a number to a precision"""
        if not ctx.args:
            raise MissingArguments("missing number to round!")

        elif len(ctx.args) > 1:
            precision = ctx.args[1].value
            if not isinstance(precision, int):
                raise InvalidArgument("precision must be an integer!")

        else:
            precision = None

        # Check value
        val = ctx.args[0].value
        if not isinstance(val, (int, float)):
            raise InvalidArgument("must be a number-like value!")

        val = round(val, precision)  # Round
        if ctx.args[0].isvar:
            ctx.args[0].set(val)

        return val

    def lwr(ctx) -> str:
        """Lowers a string"""
        if not ctx.args:
            raise MissingArguments("missing string to lower!")

        val = str(ctx.args[0].value).lower()
        if ctx.args[0].isvar:
            ctx.args[0].set(val)

        return val

    def upr(ctx) -> str:
        """Uppercases a string"""
        if not ctx.args:
            raise MissingArguments("missing string to upper!")

        val = str(ctx.args[0].value).upper()
        if ctx.args[0].isvar:
            ctx.args[0].set(val)

        return val

    def rng(ctx) -> int:
        """Generates a random number fron n1 to n2"""
        try:
            n1 = ctx.args[0].value
            n2 = ctx.args[1].value
            if not isinstance(n1, (int, float)):
                raise InvalidArgument("n1 must be a number-like value!")

            elif not isinstance(n2, (int, float)):
                raise InvalidArgument("n2 must be a number-like value!")

            # Check c
            if len(ctx.args) > 2:
                if not ctx.args[2].isvar:
                    raise InvalidArgument("c must be a variable!")

        except IndexError:
            raise MissingArguments("required: n1, n2, and c!")

        # Generate number
        val = random.randint(n1, n2)
        if len(ctx.args) > 2:
            ctx.args[2].set(val)

        return val

    def cls(ctx) -> None:
        """Clears the screen"""
        os.system("cls" if os.name == "nt" else "clear")

    def read(ctx) -> str:
        """Reads a stream from stdin"""
        prompt, var = "", None
        if ctx.args:
            prompt = str(ctx.args[0].value)
            if len(ctx.args) > 1:
                var = ctx.args[1]
                if not var.isvar:
                    raise InvalidArgument("2nd parameter must be a variable if specified!")

        data = input(prompt)
        if var is not None:
            var.set(data)

        return data

    def call(ctx) -> Any:
        """Calls a section with arguments"""
        if not ctx.args:
            raise MissingArguments("missing the section to call!")

        ds = ctx.args[-1]
        if not ds.isvar:
            raise InvalidArgument("last parameter must not be a literal!")

        fn = ctx.args[0].content
        if not isinstance(fn, str):
            raise InvalidArgument("section to call must be a string!")

        ctx.args = ctx.args[:-1][1:]
        for i, arg in enumerate(ctx.args):
            ctx.memory.vars[f"_a{i + 1}"] = arg.value

        # Call section and grab return value
        val = ctx.memory._inter.run_section(fn)
        ds.set(val)

        # Clean up variables
        for i in range(1, len(ctx.args)):
            if f"_a{i}" in ctx.memory.vars:
                del ctx.memory.vars[f"_a{i}"]

        return val

    def ret(ctx) -> Any:
        """Sets a sections return value"""
        if not ctx.args:
            raise MissingArguments("missing return value!")

        ctx.memory._inter._sectionrets[-1] = ctx.args[0].value

    def rep(ctx) -> None:
        """Repeats a section call n amount of times"""
        try:
            amount = ctx.args[0].value
            if not isinstance(amount, int):
                raise InvalidArgument("amount must be an integer!")

            section = ctx.args[1].content

        except IndexError:
            raise MissingArguments("required: amt + section!")

        [ctx.memory._inter.run_section(section) for i in range(amount)]

    def whl(ctx) -> None:
        """Repeats a section call while the expression is True"""
        if len(ctx.args) < 4:
            raise MissingArguments("required: a, operator, b, and callback!")

        a, b, op, ifcb = ctx.args[0], ctx.args[2], ctx.args[1].content, ctx.args[3].content
        while expr_eval(ctx, a.value, b.value, op):
            a.refresh()
            b.refresh()
            ctx.memory._inter.run_section(ifcb)

    def num(ctx) -> int:
        """Turns items into integers"""
        if not ctx.args:
            raise MissingArguments("missing item to convert!")

        try:
            ctx.args[0].set(int(ctx.args[0].value))
            return ctx.args[0].value

        except ValueError:
            raise InvalidArgument("provided argument cannot be converted!")

    def tstr(ctx) -> str:
        """Turns items into strings"""
        if not ctx.args:
            raise MissingArguments("missing item to convert!")

        ctx.args[0].set(str(ctx.args[0].value))
        return ctx.args[0].value

    def rem(ctx) -> None:
        """Deletes an item from internal variable memory"""
        if not ctx.args:
            raise MissingArguments("missing variable to delete!")

        key = ctx.args[0].content if ctx.args[0].isvar else str(ctx.args[0].value)
        if key not in ctx.memory.vars:
            raise InvalidArgument("unknown or nonexistant variable provided!")

        del ctx.memory.vars[key]

    def inc(ctx) -> int:
        """Increases a variable by 1"""
        if not ctx.args:
            raise MissingArguments("variable missing!")

        var = ctx.args[0] if ctx.args[0].isvar else None
        val = ctx.args[0].value + 1
        if var:
            var.set(val)

        return val

    def dec(ctx) -> int:
        """Decreases a variable by 1"""
        if not ctx.args:
            raise MissingArguments("variable missing!")

        var = ctx.args[0] if ctx.args[0].isvar else None
        val = ctx.args[0].value - 1
        if var:
            var.set(val)

        return val

    def pause(ctx) -> None:
        """Pauses until an enter keypress is received"""
        input()

    def inm(ctx) -> int:
        """Returns 1 if an object is a number, 0 otherwise"""
        if not ctx.args:
            raise MissingArguments("missing object to check!")

        var = ctx.args[1] if len(ctx.args) > 1 else None
        val = int(isinstance(ctx.args[0].value, int))
        if var:
            var.set(val)

        return val

    def inms(ctx) -> int:
        """Returns 1 if an object is a number, 0 otherwise; this operator allows strings as well: eg. '5' -> 1"""
        if not ctx.args:
            raise MissingArguments("missing object to check!")

        try:
            int(ctx.args[0].value)
            val = 1

        except ValueError:
            val = 0

        var = ctx.args[1] if len(ctx.args) > 1 else None
        if var:
            var.set(val)

        return val
