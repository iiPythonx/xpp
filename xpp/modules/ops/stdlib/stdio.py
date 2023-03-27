# Copyright 2022-2023 iiPython

# Modules
from xpp.modules.ops.shared import (
    fetch_io_args, ensure_arguments
)

# Operators class
class XOperators:
    overrides = {}

    # Handlers
    def prt(ctx) -> None:
        print(*[v.value for v in ctx.args])

    def var(ctx) -> None:
        ensure_arguments("var", "var <name> <value>", ["name", "value"], ctx.args)
        ctx.args[0].set(ctx.args[1].value)

    def jmp(ctx) -> None:
        ain, aout = fetch_io_args("jmp", "jmp <section> [args...] [?output]", ["section"], ctx.args)
        results = ctx.mem.interpreter.run_section(ain[0].value if isinstance(ain[0].value, str) else ain[0].raw, [a.value for a in ain[1:]])
        outn = len(aout)
        for i, r in enumerate(results):
            if i > outn:
                break

            ctx.args[-(outn - i)].set(r)
