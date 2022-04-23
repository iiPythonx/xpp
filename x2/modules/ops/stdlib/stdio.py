# Copyright 2022 iiPython

# Modules
from copy import copy
from x2.modules.iipython import cprint

# Exceptions
class MissingArguments(Exception):
    pass

class InvalidArgument(Exception):
    pass

# Initialization
print_ = copy(print)

# Operators class
class XTOperators:
    def prt(ctx) -> None:
        (print_ if not ctx.mem.cli_vals["color"] else cprint)(*[v.value for v in ctx.args])

    def var(ctx) -> None:
        if not len(ctx.args) >= 2:
            raise MissingArguments("required: var + value")

        ctx.args[0].set(ctx.args[1].value)

    def jmp(ctx) -> None:
        if not ctx.args:
            raise MissingArguments("required: section")

        ctx.mem.interpreter.run_section(ctx.args[0].raw)

# Operator map
opmap = {
    "prt": XTOperators.prt, "var": XTOperators.var,
    "jmp": XTOperators.jmp
}
