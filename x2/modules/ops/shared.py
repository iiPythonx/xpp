# Copyright 2022-2023 iiPython
# Shared x2 operator classes and functions

# Modules
from typing import List, Tuple

# Exceptions
class MissingArguments(Exception):
    pass

class InvalidArgument(Exception):
    pass

class OutputVariableMismatch(Exception):
    pass

# fetch_io_args
def fetch_io_args(args: list) -> Tuple[List, List]:
    isout, out = False, []
    for arg in args:
        if not isout and (str(arg.raw)[0] == "?"):
            isout = True

        if isout:
            if not str(arg.raw)[0] == "?":
                raise OutputVariableMismatch("Misplaced (possible input?) variable after output")

            arg.raw = arg.raw[1:]
            out.append(arg)

    nout = len(out)
    if nout:
        return args[:-nout], out

    return args, []
