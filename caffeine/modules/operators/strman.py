# Copyright 2023-2024 iiPython

# Modules
from . import convert_value, operator

# Operators
@operator("chr")
def operator_chr(func: object, args: list) -> None:
    if len(args) == 4:
        func.append(f"{args[3].lstrip('?')} = {convert_value(args[0])}[:({convert_value(args[2])} + 1)][{convert_value(args[1])}:]")

    else:
        func.append(f"{args[2].lstrip('?')} = {convert_value(args[0])}[{convert_value(args[1])}]")

@operator("flt")
def operator_flt(func: object, args: list) -> None:
    func.append(f"{args[1].lstrip('?')} = float({convert_value(args[0])})")

@operator("idx")
def operator_idx(func: object, args: list) -> None:
    func.append(f"{args[2].lstrip('?')} = {convert_value(args[0])}.index({convert_value(args[1])})")

@operator("int")
def operator_int(func: object, args: list) -> None:
    func.append(f"{args[1].lstrip('?')} = int({convert_value(args[0])})")

@operator(["len", "len_"])
def operator_len(func: object, args: list) -> None:
    func.append(f"{args[1].lstrip('?')} = len({convert_value(args[0])})")

@operator("lwr")
def operator_lwr(func: object, args: list) -> None:
    func.append(f"{args[1].lstrip('?')} = {convert_value(args[0])}.lower()")

@operator("str")
def operator_str(func: object, args: list) -> None:
    func.append(f"{args[1].lstrip('?')} = str({convert_value(args[0])})")

@operator("upr")
def operator_upr(func: object, args: list) -> None:
    func.append(f"{args[1].lstrip('?')} = {convert_value(args[0])}.upper()")

