# Copyright 2022-2023 iiPython

# Modules
from xpp.modules.ops.shared import (
    fetch_io_args, InvalidArgument
)

# Operators class
class XOperators:
    overrides = {
        "chr_": "chr"
    }

    # Handlers
    def chr_(ctx) -> None:
        ain, aout = fetch_io_args("chr", "chr <string> <index> [stop] [?output]", ["string", "index"], ctx.args)
        val, index, stop = ain[0].value, ain[1].value, ain[2].value if len(ain) >= 3 else None
        if not isinstance(val, str):
            raise InvalidArgument("chr: first argument must be a string!")

        vl = len(val)
        if (index > vl) or ((stop is not None) and (stop > vl)):
            raise InvalidArgument("chr: index or stop is larger then string size!")

        res = val[index] if stop is None else val[:(stop + 1)][(index):]
        if aout:
            aout[0].set(res)

        return res
