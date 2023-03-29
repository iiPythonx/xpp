# Copyright 2022-2023 iiPython

# Modules
import sys

# Operators class
class XOperators:
    overrides = {"exit_": "exit"}

    # Handlers
    def cls(ctx) -> None:
        print("\033c\033[3J", end = "")

    def exit_(ctx) -> None:
        sys.exit(ctx.args[0].value if ctx.args else 0)

    def prt(ctx) -> None:
        print(*[v.value for v in ctx.args])

    def thrw(ctx) -> None:
        raise Exception(ctx.args[0].value if ctx.args else "exception thrown in xpp thread.")
