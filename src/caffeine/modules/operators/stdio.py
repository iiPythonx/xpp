# Copyright 2023-2024 iiPython

# Modules
from . import convert_value, operator

# Operators
@operator("cls")
def operator_cls(func: object, args: list) -> None:
    func.append("print(\"\\033c\\033[3J\", end = \"\")")

@operator("exit")
def operator_exit(func: object, args: list) -> None:
    func.append(f"exit({convert_value(args[0]) if args else '0'})")

@operator("prt")
def operator_prt(func: object, args: list) -> None:
    args = [a.replace("@", "_GL") if a[0] == "@" else a for a in args]
    func.append(f"print({', '.join(args)})")

@operator("read")
def operator_read(func: object, args: list) -> None:
    if len(args) == 2:
        func.append(f"{args[1].lstrip('?')} = input({args[0]})")

    else:
        func.append(f"input({args[0]})")

@operator("thrw")
def operator_thrw(func: object, args: list) -> None:
    func.append(f"raise Exception({convert_value(args[0]) if args else ''})")

@operator("wait")
def operator_wait(func: object, args: list) -> None:
    func.append(f"time.sleep({convert_value(args[0])})")
