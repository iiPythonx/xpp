# Copyright 2022-2023 iiPython

# Modules
from copy import copy
from xpp.modules.iipython import cprint
from xpp.modules.ops.shared import (
    fetch_io_args,
    MissingArguments
)

# Initialization
print_ = copy(print)

# Operators class
class XOperators:
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
            raise MissingArguments("[x2 built-in jmp]\njmp <section> [args...] [?output]\nmissing required argument: section")

        ain, aout = fetch_io_args(ctx.args)
        results = ctx.mem.interpreter.run_section(ain[0].value if isinstance(ain[0].value, str) else ain[0].raw, [a.value for a in ain[1:]])
        outn = len(aout)
        for i, r in enumerate(results):
            if i > outn:
                break

            ctx.args[-(outn - i)].set(r)
