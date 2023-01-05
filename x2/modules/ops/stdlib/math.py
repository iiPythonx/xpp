# Copyright 2022-2023 iiPython

# Modules
from x2.modules.ops.shared import MissingArguments, InvalidArgument

# Operators class
class XTOperators:
    overrides = {}

    # Handlers
    def add(ctx) -> int | float | str:
        "add <a> <b> [output]"
        if len(ctx.args) < 2:
            raise MissingArguments(f"<add> takes at least two arguments, but {len(ctx.args)} were passed.")

        a, b = ctx.args[0].value, ctx.args[1].value
        if str in [type(a), type(b)] and type(a) != type(b):
            raise InvalidArgument("If passing a string to <add>, both arguments must be strings.")

        result = a + b
        if len(ctx.args) > 2:
            ctx.args[2].set(result)

        return result

    def sub(ctx) -> int | float:
        "sub <a> <b> [output]"
        if len(ctx.args) < 2:
            raise MissingArguments(f"<sub> takes at least two arguments, but {len(ctx.args)} were passed.")

        a, b = ctx.args[0].value, ctx.args[1].value
        result = a - b
        if len(ctx.args) > 2:
            ctx.args[2].set(result)

        return result

    def mul(ctx) -> int | float:
        "mul <a> <b> [output]"
        if len(ctx.args) < 2:
            raise MissingArguments(f"<mul> takes at least two arguments, but {len(ctx.args)} were passed.")

        a, b = ctx.args[0].value, ctx.args[1].value
        result = a * b
        if len(ctx.args) > 2:
            ctx.args[2].set(result)

        return result

    def div(ctx) -> int | float:
        "div <a> <b> [output]"
        if len(ctx.args) < 2:
            raise MissingArguments(f"<div> takes at least two arguments, but {len(ctx.args)} were passed.")

        a, b = ctx.args[0].value, ctx.args[1].value
        result = a / b
        if len(ctx.args) > 2:
            ctx.args[2].set(result)

        return result

    def pow(ctx) -> int | float:
        "pow <a> <b> [output]"
        if len(ctx.args) < 2:
            raise MissingArguments(f"<pow> takes at least two arguments, but {len(ctx.args)} were passed.")

        a, b = ctx.args[0].value, ctx.args[1].value
        result = a ** b
        if len(ctx.args) > 2:
            ctx.args[2].set(result)

        return result
