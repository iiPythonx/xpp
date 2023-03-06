# Copyright 2022-2023 iiPython

# Modules
from xpp.modules.ops.shared import (
    fetch_io_args,
    MissingArguments, InvalidArgument
)

# Operators class
class XOperators:
    overrides = {
        "chr_": "chr"
    }

    # Handlers
    def chr_(ctx) -> None:
        "chr <string> <index> [stop] [?output]"
        if len(ctx.args) < 2:
            raise MissingArguments("required: string, index")

        ain, aout = fetch_io_args(ctx.args)
        val, index, stop = ain[0].value, ain[1].value, ain[2].value if len(ain) >= 3 else None
        if not isinstance(val, str):
            raise InvalidArgument("chr: first argument must be a string!")

        vl = len(val)
        if (index > vl) or ((stop is not None) and (stop > vl)):
            raise InvalidArgument("chr: index or stop is larger then string size!")

        res = val[index] if stop is None else val[:stop][index:]
        if aout:
            aout[0].set(res)

        return res
