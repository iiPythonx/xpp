# Copyright 2022-2023 iiPython

# Modules
import operator
from typing import List
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
    def add(ctx) -> int | float | str:
        ain, aout = fetch_io_args("add", "add <a> <b> [args...] [?output]", ["a", "b"], ctx.args)
        return perform_operation(
            0 if isinstance(ain[0].value, (int, float)) else "",
            ain,
            operator.add,
            aout,
            "All arguments must be of the same datatype:\n  Current type: {} | Attempted to add: {} ({})"
        )

    def sub(ctx) -> int | float:
        ain, aout = fetch_io_args("sub", "sub <a> <b> [args...] [?output]", ["a", "b"], ctx.args)
        return perform_operation(ain[0].value, ain[1:], operator.sub, aout)

    def mul(ctx) -> int | float:
        ain, aout = fetch_io_args("mul", "mul <a> <b> [args...] [?output]", ["a", "b"], ctx.args)
        return perform_operation(
            ain[0].value,
            ain[1:],
            operator.mul,
            aout,
            "All arguments must be multipliable:\n  Current type: {} | Attempted to mul: {} ({})"
        )

    def div(ctx) -> int | float:
        ain, aout = fetch_io_args("div", "div <a> <b> [args...] [?output]", ["a", "b"], ctx.args)
        return perform_operation(ain[0].value, ain[1:], operator.div, aout)

    def pow(ctx) -> int | float:
        ain, aout = fetch_io_args("pow", "pow <a> <b> [args...] [?output]", ["a", "b"], ctx.args)
        return perform_operation(ain[0].value, ain[1:], operator.pow, aout)

    def inc(ctx) -> int | float:
        ain, aout = fetch_io_args("inc", "inc <value> [?output]", ["value"], ctx.args)
        if not isinstance(ain[0].value, (int, float)):
            raise InvalidArgument("inc: value must be either an integer or a float!")

        ain[0].set(ain[0].value + 1)
        [out.set(ain[0].value) for out in aout]

    def dec(ctx) -> int | float:
        ain, aout = fetch_io_args("dec", "dec <value> [?output]", ["value"], ctx.args)
        if not isinstance(ain[0].value, (int, float)):
            raise InvalidArgument("dec: value must be either an integer or a float!")

        ain[0].set(ain[0].value - 1)
        [out.set(ain[0].value) for out in aout]
