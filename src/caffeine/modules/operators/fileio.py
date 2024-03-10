# Copyright 2023-2024 iiPython

# Modules
from . import convert_value, operator

# Operators
@operator("load")
def operator_load(func: object, args: list) -> None:
    func.append(f"with open({convert_value(args[0])}, \"r\") as fh:")
    func.append(f"{func.T}{args[1].lstrip('?')} = fh.read()")

@operator("save")
def operator_save(func: object, args: list) -> None:
    func.append(f"with open({convert_value(args[0])}, \"w+\") as fh:")
    func.append(f"{func.T}fh.write({convert_value(args[1])})")
