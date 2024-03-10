# Copyright 2023-2024 iiPython

# Modules
from . import convert_value, operator

# Operators
@operator("evl")
def operator_evl(func: object, args: list) -> None:
    statement = args[0]
    if statement[0] in ["'", "\""]:
        return func.append(statement[1:][:-1])

    func.append(f"eval({convert_value(statement)})")

@operator("if")
def operator_if(func: object, args: list) -> None:
    func.append(f"if {args[0]}:")

    # Process arguments
    awaiting = True
    for idx, arg in enumerate(args[1:]):
        if arg[0] == "(":
            func.append(f"elif {arg}:")
            awaiting = True

        else:
            if (idx + 1 == len(args) - 1) and not awaiting:
                func.append("else:")

            awaiting = False
            func._convert(func, arg[1:][:-1].strip(), 2)

@operator("jmp")
def operator_jmp(func: object, args: list) -> None:
    assign = ", ".join([a[1:] for a in args[1:] if a[0] == "?"])
    assign += " = " if assign else ""
    func.append(f"{assign}{args[0]}({', '.join([a for a in args[1:] if a[0] != '?'])})")

@operator("rem")
def operator_rem(func: object, args: list) -> None:
    for arg in args:
        func.append(f"del {convert_value(arg)}")

@operator("ret")
def operator_ret(func: object, args: list) -> None:
    func.append(f"return {' '.join([convert_value(a) for a in args])}")

@operator("rep")
def operator_rep(func: object, args: list) -> None:
    func.append(f"for i in range({convert_value(args[0])}):")
    func._convert(func, args[1][1:][:-1].strip(), 2)

@operator("try")
def operator_try(func: object, args: list) -> None:
    func.append("try:")
    func._convert(func, args[0][1:][:-1].strip(), 2)
    if len(args) > 1:
        func.append("except:")
        func._convert(func, args[1][1:][:-1].strip(), 2)

@operator("var")
def operator_var(func: object, args: list) -> None:
    key, value, is_global = args[0].replace("@", "_GL"), convert_value(args[1]), args[0][0] == "@"
    if is_global and not func.is_main:
        func.prepend(f"global {key}")

    func.append(f"{key} = {value}")

@operator("whl")
def operator_whl(func: object, args: list) -> None:
    func.append(f"while {args[0]}:")
    func._convert(func, args[1][1:][:-1].strip(), 2)
