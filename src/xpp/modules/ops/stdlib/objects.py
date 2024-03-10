# Copyright 2024 iiPython

# Modules
from typing import Any

from xpp.modules.ops.shared import (
    fetch_io_args, ensure_arguments,
    InvalidArgument
)

# Initialization
typelist = {"list": list, "dict": dict}

# Operators class
class XOperators:
    overrides = {"set_": "set"}

    def new(mem, args: list) -> list | dict:
        ain, aout = fetch_io_args("new", "new <type> [?output]", ["type"], args)
        obj = typelist.get(ain[0].value, typelist.get(ain[0].raw))
        if obj is None:
            raise InvalidArgument("new: type must be one of 'list' or 'dict'!")

        obj = obj()
        if aout:
            aout[0].set(obj)

        return obj

    def psh(mem, args: list) -> None:
        ensure_arguments("psh", "psh <list> <value>", ["list", "value"], args)
        if not isinstance(args[0].value, list):
            raise InvalidArgument("psh: list must be of type list!")

        args[0].value.append(args[1].value)

    def pop(mem, args: list) -> Any:
        ain, aout = fetch_io_args("pop", "pop <list> [?output]", ["list"], args)
        if not isinstance(ain[0].value, list):
            raise InvalidArgument("pop: arg must be of type 'list'!")

        val = ain[0].value.pop()
        if aout:
            aout[0].set(val)

        return val

    def get(mem, args: list) -> Any:
        ain, aout = fetch_io_args("get", "get <object> <key> [?output]", ["object", "key"], args)
        if not isinstance(ain[0].value, (list, dict)):
            raise InvalidArgument("get: arg must be one of 'list' or 'dict'!")

        val = ain[0].value[ain[1].value]
        if aout:
            aout[0].set(val)

        return val

    def set_(mem, args: list) -> None:
        ain, aout = fetch_io_args("set", "set <dict> <key> <value>", ["dict", "key", "value"], args)
        if not isinstance(ain[0].value, dict):
            raise InvalidArgument("get: dict must be of type 'dict'!")

        k, v = ain[1].value, ain[2].value
        if (ain[2].raw == "null") and (k in ain[0].value):
            del ain[0].value[k]
            return

        ain[0].value[k] = v
