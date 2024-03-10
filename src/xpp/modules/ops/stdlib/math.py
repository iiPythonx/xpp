# Copyright 2022-2024 iiPython

# Modules
import operator
from typing import List
from random import randint
from types import FunctionType

from xpp.core.datastore import Datastore
from xpp.modules.ops.shared import (
    fetch_io_args, InvalidArgument
)

# perform_operation
def perform_operation(
    start: int,
    items: List[int | float | str],
    operation: FunctionType,
    outputs: List[Datastore],
    error: str = "All arguments must be either integers or floats."
) -> int | float | str:
    try:
        for item in items:
            start = operation(start, item.value)

        [out.set(start) for out in outputs]
        return start

    except (TypeError, ValueError):
        raise InvalidArgument(error.format(type(start).__name__, item.raw, type(item.value).__name__))

# Operators class
class XOperators:
    overrides = {}

    # Handlers
    def add(mem, args: list) -> int | float | str:
        ain, aout = fetch_io_args("add", "add <a> <b> [args...] [?output]", ["a", "b"], args)
        return perform_operation(
            0 if isinstance(ain[0].value, (int, float)) else "",
            ain,
            operator.add,
            aout,
            "All arguments must be of the same datatype:\n  Current type: {} | Attempted to add: {} ({})"
        )

    def dec(mem, args: list) -> int | float:
        ain, aout = fetch_io_args("dec", "dec <args...> [?output]", ["args"], args)
        if aout and len(ain) > 1:
            raise InvalidArgument("dec: can only process one input if output variable is specified!")

        for val in ain:
            if not isinstance(val.value, (int, float)):
                raise InvalidArgument("dec: all values must be either an integer or a float!")

            val.set(val.value - 1)

        if aout:
            [out.set(val.value) for out in aout]
            return val.value

    def div(mem, args: list) -> int | float:
        ain, aout = fetch_io_args("div", "div <a> <b> [args...] [?output]", ["a", "b"], args)
        return perform_operation(ain[0].value, ain[1:], operator.truediv, aout)

    def inc(mem, args: list) -> int | float:
        ain, aout = fetch_io_args("inc", "inc <args...> [?output]", ["args"], args)
        if aout and len(ain) > 1:
            raise InvalidArgument("inc: can only process one input if output variable is specified!")

        for val in ain:
            if not isinstance(val.value, (int, float)):
                raise InvalidArgument("inc: all values must be either an integer or a float!")

            val.set(val.value + 1)

        if aout:
            [out.set(val.value) for out in aout]
            return val.value

    def mul(mem, args: list) -> int | float:
        ain, aout = fetch_io_args("mul", "mul <a> <b> [args...] [?output]", ["a", "b"], args)
        return perform_operation(
            ain[0].value,
            ain[1:],
            operator.mul,
            aout,
            "All arguments must be multipliable:\n  Current type: {} | Attempted to mul: {} ({})"
        )

    def pow(mem, args: list) -> int | float:
        ain, aout = fetch_io_args("pow", "pow <a> <b> [args...] [?output]", ["a", "b"], args)
        return perform_operation(ain[0].value, ain[1:], operator.pow, aout)

    def rnd(mem, args: list) -> int:
        ain, aout = fetch_io_args("rnd", "rnd <value> [precision] [?output]", ["value"], args)
        if not isinstance(ain[0].value, (float)):
            raise InvalidArgument("rnd: value must be a float!")

        precision = ain[1].value if len(ain) > 1 else 0
        if not isinstance(precision, int):
            raise InvalidArgument("rnd: precision must be an integer!")

        val = round(ain[0].value, precision or None)
        [out.set(val) for out in aout + [ain[0]]]
        return val

    def rng(mem, args: list) -> int:
        ain, aout = fetch_io_args("rng", "rng <min> <max> [?output]", ["min", "max"], args)
        if any([not isinstance(x.value, int) for x in ain]):
            raise InvalidArgument("rng: min and max must both be integers!")

        val = randint(ain[0].value, ain[1].value)
        [out.set(val) for out in aout]
        return val

    def sub(mem, args: list) -> int | float:
        ain, aout = fetch_io_args("sub", "sub <a> <b> [args...] [?output]", ["a", "b"], args)
        return perform_operation(ain[0].value, ain[1:], operator.sub, aout)
