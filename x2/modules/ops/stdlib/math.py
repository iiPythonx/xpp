# Copyright 2022-2023 iiPython

# Modules
from x2.modules.ops.shared import (
    fetch_io_args,
    MissingArguments, InvalidArgument
)

# Operators class
class XTOperators:
    overrides = {}

    # Handlers
    def add(ctx) -> int | float | str:
        "add <a> <b> [output]"
        if len(ctx.args) < 2:
            raise MissingArguments(f"<add> takes at least two arguments, but {len(ctx.args)} were passed.")

        ain, aout = fetch_io_args(ctx.args)
        res = 0 if isinstance(ain[0].value, (int, float)) else ""
        try:
            for n in ain:
                res += n.value

        except (TypeError, ValueError):
            raise InvalidArgument(f"All arguments must be of the same datatype:\n  Current type: {type(res).__name__} | Attempted to add: {n.raw} ({type(n.value).__name__})")

        if aout:
            aout[0].set(res)

        return res

    def sub(ctx) -> int | float:
        "sub <a> <b> [output]"
        if len(ctx.args) < 2:
            raise MissingArguments(f"<sub> takes at least two arguments, but {len(ctx.args)} were passed.")

        ain, aout = fetch_io_args(ctx.args)
        res = ain[0].value
        try:
            for n in ain[1:]:
                res -= n.value

        except (TypeError, ValueError):
            raise InvalidArgument(f"All arguments must be either integers or floats.")

        if aout:
            aout[0].set(res)

        return res

    def mul(ctx) -> int | float:
        "mul <a> <b> [output]"
        if len(ctx.args) < 2:
            raise MissingArguments(f"<mul> takes at least two arguments, but {len(ctx.args)} were passed.")

        ain, aout = fetch_io_args(ctx.args)
        res = ain[0].value
        try:
            for n in ain[1:]:
                res *= n.value

        except (TypeError, ValueError):
            raise InvalidArgument(f"All arguments must be multipliable:\n  Current type: {type(res).__name__} | Attempted to mul: {n.raw} ({type(n.value).__name__})")

        if aout:
            aout[0].set(res)

        return res

    def div(ctx) -> int | float:
        "div <a> <b> [output]"
        if len(ctx.args) < 2:
            raise MissingArguments(f"<div> takes at least two arguments, but {len(ctx.args)} were passed.")

        ain, aout = fetch_io_args(ctx.args)
        res = ain[0].value
        try:
            for n in ain:
                res /= n.value

        except (TypeError, ValueError):
            raise InvalidArgument(f"All arguments must be either integers or floats.")

        if aout:
            aout[0].set(res)

        return res

    def pow(ctx) -> int | float:
        "pow <a> <b> [output]"
        if len(ctx.args) < 2:
            raise MissingArguments(f"<pow> takes at least two arguments, but {len(ctx.args)} were passed.")

        ain, aout = fetch_io_args(ctx.args)
        res = ain[0]
        try:
            for n in ain:
                res **= n.value

        except (TypeError, ValueError):
            raise InvalidArgument(f"All arguments must be either integers or floats.")

        if aout:
            aout[0].set(res)

        return res
