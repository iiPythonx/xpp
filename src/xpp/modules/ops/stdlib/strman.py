# Copyright 2022-2024 iiPython

# Modules
from typing import Any, List
from types import FunctionType

from xpp.modules.ops.shared import (
    fetch_io_args, InvalidArgument
)
from xpp.core.datastore import Datastore

# Handle type conversion
def convert_value(ain: List[Datastore], aout: List[Datastore], handler: FunctionType) -> Any:
    try:
        value = handler(ain[0].value)
        [out.set(value) for out in aout + [ain[0]]]
        return value

    except ValueError:
        raise InvalidArgument(f"specified value '{ain[0].value}' is not able to be converted to a {handler.__name__}!")

# Operators class
class XOperators:
    overrides = {
        "chr_": "chr", "str_": "str", "flt_": "flt",
        "int_": "int", "len_": "len"
    }

    # Handlers
    def chr_(mem, args: list) -> str:
        ain, aout = fetch_io_args("chr", "chr <string> <index> [stop] [?output]", ["string", "index"], args)
        val, index, stop = ain[0].value, ain[1].value, ain[2].value if len(ain) >= 3 else None
        if not isinstance(val, str):
            raise InvalidArgument("chr: first argument must be a string!")

        vl = len(val)
        if (index > vl) or ((stop is not None) and (stop > vl)):
            raise InvalidArgument("chr: index or stop is larger then string size!")

        res = val[index] if stop is None else val[:(stop + 1)][(index):]
        [out.set(res) for out in aout]
        return res

    def flt_(mem, args: list) -> float:
        ain, aout = fetch_io_args("flt", "flt <value> [?output]", ["value"], args)
        return convert_value(ain, aout, float)

    def idx(mem, args: list) -> int:
        ain, aout = fetch_io_args("idx", "idx <string> <substr> [?output]", ["string", "substr"], args)
        if any([not isinstance(x.value, str) for x in ain]):
            raise InvalidArgument("idx: both arguments must be strings!")

        val = ain[0].value.index(ain[1].value)
        [out.set(val) for out in aout]
        return val

    def int_(mem, args: list) -> int:
        ain, aout = fetch_io_args("int", "int <value> [?output]", ["value"], args)
        return convert_value(ain, aout, int)

    def len_(mem, args: list) -> int:
        ain, aout = fetch_io_args("len", "len <string> [?output]", ["string"], args)
        if not isinstance(ain[0].value, str):
            raise InvalidArgument("len: argument must be a string!")

        val = len(ain[0].value)
        [out.set(val) for out in aout]
        return val

    def lwr(mem, args: list) -> str:
        ain, aout = fetch_io_args("lwr", "lwr <string> [?output]", ["string"], args)
        val = str(ain[0].value).lower()
        if aout:
            [out.set(val) for out in aout]

        else:
            ain[0].set(val)

        return val

    def str_(mem, args: list) -> str:
        ain, aout = fetch_io_args("str", "str <value> [?output]", ["value"], args)
        return convert_value(ain, aout, str)

    def upr(mem, args: list) -> str:
        ain, aout = fetch_io_args("upr", "upr <string> [?output]", ["string"], args)
        val = str(ain[0].value).upper()
        if aout:
            [out.set(val) for out in aout]

        else:
            ain[0].set(val)

        return val
