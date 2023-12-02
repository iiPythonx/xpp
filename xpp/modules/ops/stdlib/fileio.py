# Copyright 2023-2024 iiPython

# Modules
from xpp.modules.ops.shared import (
    fetch_io_args, InvalidArgument
)

# Operators class
class XOperators:
    overrides = {}

    # Handlers
    def load(mem, args: list) -> str:
        ain, aout = fetch_io_args("load", "load <path> [encoding] [?output]", ["path"], args)
        if not isinstance(ain[0].value, str):
            raise InvalidArgument("load: path must be a string!")

        with open(
            ain[0].value,
            "r",
            encoding = ain[1].value if len(ain) > 1 else "utf8"
        ) as fh:
            value = fh.read()
            [out.set(value) for out in aout]
            return value

    def save(mem, args: list) -> None:
        ain, aout = fetch_io_args("save", "save <path> <value> [encoding]", ["path", "value"], args)
        if not isinstance(ain[0].value, str):
            raise InvalidArgument("save: path must be a string!")

        with open(
            ain[0].value,
            "w+",
            encoding = ain[2].value if len(ain) > 2 else "utf8"
        ) as fh:
            fh.write(str(ain[1].value))
