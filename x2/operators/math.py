# Copyright 2022 iiPython

# Modules
import random
from typing import Any
from types import NoneType

# Exceptions
class MissingArguments(Exception):
    pass

class InvalidArgument(Exception):
    pass

# x2 Operators
class XTOperators:
    def add(ctx) -> Any:
        """
        Adds two items together

        add <a> <b> [out]
        a - any
        b - any
        out - variable
        """
        if len(ctx.args) < 2:
            raise MissingArguments("required: a + b")

        val = ctx.args[0].value + ctx.args[1].value
        output = ctx.args[2] if len(ctx.args) > 2 else None
        if output is not None:
            output.set(val)

        return val

    def sub(ctx) -> int | float:
        """
        Subtracts two numbers from eachother

        sub <a> <b> [out]
        a - int or float
        b - int or float
        out - variable
        """
        if len(ctx.args) < 2:
            raise MissingArguments("required: a + b")

        elif [a for a in ctx.args[:2] if not isinstance(a.value, (int, float))]:
            raise InvalidArgument("a + b must both be number-like values")

        val = ctx.args[0].value - ctx.args[1].value
        output = ctx.args[2] if len(ctx.args) > 2 else None
        if output is not None:
            output.set(val)

        return val

    def mul(ctx) -> Any:
        """
        Multiplies two items together

        mul <a> <b> [out]
        a - any
        b - any
        out - variable
        """
        if len(ctx.args) < 2:
            raise MissingArguments("required: a + b")

        val = ctx.args[0].value * ctx.args[1].value
        output = ctx.args[2] if len(ctx.args) > 2 else None
        if output is not None:
            output.set(val)

        return val

    def div(ctx) -> int | float:
        """
        Divides two numbers from eachother

        div <a> <b> [out]
        a - int or float
        b - int or float
        out - variable
        """
        if len(ctx.args) < 2:
            raise MissingArguments("required: a + b")

        elif [a for a in ctx.args[:2] if not isinstance(a.value, (int, float))]:
            raise InvalidArgument("a + b must both be number-like values")

        val = ctx.args[0].value / ctx.args[1].value
        output = ctx.args[2] if len(ctx.args) > 2 else None
        if output is not None:
            output.set(val)

        return val

    def inc(ctx) -> int | float:
        """
        Increases a number by one

        inc <num> [out]
        num - int or float
        out - variable
        """
        if len(ctx.args) < 1:
            raise MissingArguments("required: num")

        elif not isinstance(ctx.args[0].value, (int, float)):
            raise InvalidArgument("num must be a number-like value")

        val = ctx.args[0].value + 1
        output = ctx.args[1] if len(ctx.args) > 1 else None
        if output is not None:
            output.set(val)

        else:
            ctx.args[0].set(val)

        return val

    def dec(ctx) -> int | float:
        """
        Decreases a number by one

        inc <num> [out]
        num - int or float
        out - variable
        """
        if len(ctx.args) < 1:
            raise MissingArguments("required: num")

        elif not isinstance(ctx.args[0].value, (int, float)):
            raise InvalidArgument("num must be a number-like value")

        val = ctx.args[0].value - 1
        output = ctx.args[1] if len(ctx.args) > 1 else None
        if output is not None:
            output.set(val)

        else:
            ctx.args[0].set(val)

        return val

    def rnd(ctx) -> int:
        """
        Rounds a float to the given precision

        rnd <num> [precision]
        num - number
        precision - int
        """
        if len(ctx.args) < 1:
            raise MissingArguments("required: num")

        elif not isinstance(ctx.args[0].value, (int, float)):
            raise InvalidArgument("num must be a number-like value")

        precision = ctx.args[1].value if len(ctx.args) > 1 else None
        if not isinstance(precision, (int, NoneType)):
            raise InvalidArgument("precision must be an integer")

        val = round(ctx.args[0].value, precision)
        ctx.args[0].set(val)
        return val

    def rng(ctx) -> int | float:
        """
        Generates a random number within a range

        rng <min> <max> [out]
        min - integer
        max - integer
        out - variable
        """
        if len(ctx.args) < 2:
            raise MissingArguments("required: min + max")

        elif [a for a in ctx.args[:2] if not isinstance(a.value, int)]:
            raise InvalidArgument("min and max must both be integers")

        val = random.randint(ctx.args[0].value, ctx.args[1].value)
        out = ctx.args[2] if len(ctx.args) > 2 else None
        if out is not None:
            out.set(val)

        return val

# Operator map
opmap = {
    "add": XTOperators.add, "sub": XTOperators.sub,
    "mul": XTOperators.mul, "div": XTOperators.div,
    "inc": XTOperators.inc, "dec": XTOperators.dec,
    "rnd": XTOperators.rnd, "rng": XTOperators.rng
}
