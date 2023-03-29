# Copyright 2022-2023 iiPython

# Modules
import sys
from time import sleep
from xpp.modules.ops.shared import (
    fetch_io_args, InvalidArgument
)

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

    def wait(ctx) -> None:
        ain, aout = fetch_io_args("wait", "wait <time>", ["time"], ctx.args)
        if not isinstance(ain[0].value, (int, float)):
            raise InvalidArgument("wait: time must be either an integer or float!")

        sleep(ain[0].value)
