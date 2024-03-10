# Copyright 2023-2024 iiPython

# Modules
from . import convert_value, operator
from ..exceptions import InvalidObjectType

# Operators
@operator("new")
def operator_new(func: object, args: list) -> None:
    match convert_value(args[0]):
        case "dict":
            obj = "{}"

        case "list":
            obj = "[]"

        case _:
            raise InvalidObjectType("available types are 'list' or 'dict'!")

    func.append(f"{args[1].lstrip('?')} = {obj}")

@operator("psh")
def operator_psh(func: object, args: list) -> None:
    func.append(f"{convert_value(args[0])}.append({convert_value(args[1])})")

@operator("pop")
def operator_pop(func: object, args: list) -> None:
    start = f"{args[1].lstrip('?')} = " if len(args) > 1 else ""
    func.append(f"{start}{convert_value(args[0])}.pop()")

@operator("get")
def operator_get(func: object, args: list) -> None:
    func.append(f"{args[2].lstrip('?')} = {convert_value(args[0])}[{convert_value(args[1])}]")

@operator("set")
def operator_set(func: object, args: list) -> None:
    if args[2] == "null":
        return func.append(f"del {convert_value(args[0])}[{convert_value(args[1])}]")

    func.append(f"{convert_value(args[0])}[{convert_value[args[1]]}] = {convert_value(args[2])}")
