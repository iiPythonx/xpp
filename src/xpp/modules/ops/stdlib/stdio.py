# Copyright 2022-2024 iiPython

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
    def cls(mem, args: list) -> None:
        print("\033c\033[3J", end = "")

    def exit_(mem, args: list) -> None:
        sys.exit(args[0].value if args else 0)

    def prt(mem, args: list) -> None:
        print(*[v.value for v in args])

    def read(mem, args: list) -> None:
        ain, aout = fetch_io_args("read", "read [prompt] [?output]", [], args)
        res = input(str(ain[0].value) if ain else "")
        [out.set(res) for out in aout]

    def thrw(mem, args: list) -> None:
        raise Exception(args[0].value if args else "exception thrown in xpp thread.")

    def wait(mem, args: list) -> None:
        ain, aout = fetch_io_args("wait", "wait <time>", ["time"], args)
        if not isinstance(ain[0].value, (int, float)):
            raise InvalidArgument("wait: time must be either an integer or float!")

        sleep(ain[0].value)
