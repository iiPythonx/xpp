# Copyright 2022-2023 iiPython

# Modules
import sys

# Operators class
class XOperators:
    overrides = {"exit_": "exit"}

    # Handlers
    def prt(ctx) -> None:
        print(*[v.value for v in ctx.args])

    def cls(ctx) -> None:
        print("\033c\033[3J", end = "")

    def exit_(ctx) -> None:
        sys.exit(ctx.args[0].value if ctx.args else 0)
