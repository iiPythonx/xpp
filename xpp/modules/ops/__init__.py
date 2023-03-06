# x++ Operator Loader
# Copyright 2022-2023 iiPython

# Modules
import os
from importlib.util import (
    module_from_spec, spec_from_file_location
)

# Class handler
def generate_opmap(ops) -> dict:
    overrides = getattr(ops, "overrides", {})
    return {overrides.get(obj, obj): getattr(ops, obj) for obj in dir(ops) if obj[0] != "_"}

# Initialization
supported_opmaps = [
    "XOperators",
    "XTOperators"  # For backwards compatibility
]
opmap = {}
for path, _, files in os.walk(os.path.abspath(os.path.dirname(__file__))):
    if "__pycache__" in path:
        continue

    for file in files:
        fp = os.path.join(path, file)
        if file[0] == "_" or not os.path.isfile(fp) or not file[-3:] == ".py":
            continue

        # Load operators
        spec = spec_from_file_location(f"xppops_{file[:-3]}", fp)
        module = module_from_spec(spec)
        spec.loader.exec_module(module)

        # Sanity checks
        for mapname in supported_opmaps:
            if not hasattr(module, mapname):
                continue

            opmap = opmap | generate_opmap(getattr(module, mapname))

        else:
            del spec, module
