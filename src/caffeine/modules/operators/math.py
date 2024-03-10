# Copyright 2023-2024 iiPython

# Modules
from . import convert_value, operator

# Operators
@operator("add")
def operator_add(func: object, args: list) -> None:
    value1, value2 = convert_value(args[0]), convert_value(args[1])
    return func.append(f"{args[2].lstrip('?')} = {value1} + {value2}")

@operator("dec")
def operator_dec(func: object, args: list) -> None:
    for arg in args:
        if arg[0] == "@" and not func.is_main:
            func.prepend(f"global {arg[1:]}")

        func.append(f"{arg.lstrip('@')} -= 1")

@operator("div")
def operator_div(func: object, args: list) -> None:
    value1, value2 = convert_value(args[0]), convert_value(args[1])
    return func.append(f"{args[2].lstrip('?')} = {value1} / {value2}")

@operator("inc")
def operator_inc(func: object, args: list) -> None:
    for arg in args:
        if arg[0] == "@" and not func.is_main:
            func.prepend(f"global {arg[1:]}")

        func.append(f"{arg.lstrip('@')} += 1")

@operator("mul")
def operator_mul(func: object, args: list) -> None:
    value1, value2 = convert_value(args[0]), convert_value(args[1])
    return func.append(f"{args[2].lstrip('?')} = {value1} * {value2}")

@operator("pow")
def operator_pow(func: object, args: list) -> None:
    value1, value2 = convert_value(args[0]), convert_value(args[1])
    return func.append(f"{args[2].lstrip('?')} = {value1} ** {value2}")

@operator("rnd")
def operator_rnd(func: object, args: list) -> None:
    if len(args) == 3:
        return func.append(f"{args[2].lstrip('?')} = round({convert_value(args[0])}, {convert_value(args[1])})")

    func.append(f"{args[1].lstrip('?')} = round({convert_value(args[0])})")

@operator("rng")
def operator_rng(func: object, args: list) -> None:
    func.prepend("import random")
    func.append(f"{args[2].lstrip('?')} = random.randint({convert_value(args[0])}, {convert_value(args[1])})")

@operator("sub")
def operator_sub(func: object, args: list) -> None:
    value1, value2 = convert_value(args[0]), convert_value(args[1])
    return func.append(f"{args[2].lstrip('?')} = {value1} - {value2}")
