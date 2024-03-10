# Copyright 2022-2024 iiPython
# Shared x++ operator classes and functions

# Modules
from typing import List, Tuple

# Exceptions
class MissingArguments(Exception):
    pass

class InvalidArgument(Exception):
    pass

class OutputVariableMismatch(Exception):
    pass

# ensure_arguments
def ensure_arguments(
    operator: str,
    usage: str,
    required_args: list,
    args: list
) -> None:
    if len(args) < len(required_args):
        raise MissingArguments("\n".join([
            f"missing required argument(s): {', '.join(required_args[len(args):])}",
            f"usage: {usage}"
        ]))

# fetch_io_args
def fetch_io_args(
    operator: str,
    usage: str,
    required_args: list,
    args: list
) -> Tuple[List, List]:
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
        args = args[:-nout]

    ensure_arguments(operator, usage, required_args, args)
    return args, out
