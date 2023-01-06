# Copyright 2022-2023 iiPython

# Modules
from copy import copy
from x2.modules.iipython import cprint
from x2.modules.ops.shared import MissingArguments

# Initialization
print_ = copy(print)

# Operators class
class XTOperators:
    overrides = {}

    # Handlers
    def prt(ctx) -> None:
        (print_ if not ctx.mem.cli_vals["color"] else cprint)(*[v.value for v in ctx.args])

    def var(ctx) -> None:
        if not len(ctx.args) >= 2:
            raise MissingArguments("required: var + value")

        ctx.args[0].set(ctx.args[1].value)

    def jmp(ctx) -> None:
        if not ctx.args:
            raise MissingArguments("[x2 built-in jmp]\njmp <section> [args...] [?output]")

        cargs, has_out = ctx.args[1:], False
        if str(ctx.args[-1].raw)[0] == "?":
            ctx.args[-1].raw = ctx.args[-1].raw[1:]
            cargs = cargs[:-1]
            has_out = True

        args = []
        for a in cargs:
            args.append(a.value)

        result = ctx.mem.interpreter.run_section(ctx.args[0].raw, args)
        if has_out:
            ctx.args[-1].set(result)
