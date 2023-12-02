# x++ Operator Loader
# Copyright 2022-2024 iiPython

# Modules
import os
from importlib.util import (
    module_from_spec, spec_from_file_location
)

# Class handler
def generate_opmap(ops) -> dict:
    overrides = getattr(ops, "overrides", {})
    return {
        overrides.get(obj, obj): getattr(ops, obj)
        for obj in dir(ops)
        if obj[0] != "_" and obj != "overrides"
    }

# Module importer
supported_opmaps = [
    "XOperators",
    "XTOperators"  # For backwards compatibility
]

def import_opmap_from_file(ns: str, fp: str) -> dict:

    # Load operators
    spec = spec_from_file_location(f"{ns}_{fp.split(os.sep)[-1][:-3]}", fp)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)

    # Sanity checks
    opmap = {}
    for mapname in supported_opmaps:
        if not hasattr(module, mapname):
            continue

        opmap = generate_opmap(getattr(module, mapname))

    del spec, module
    return opmap

# Initialization
opmap = {}
for path, _, files in os.walk(os.path.abspath(os.path.dirname(__file__))):
    if "__pycache__" in path:
        continue

    for file in files:
        fp = os.path.join(path, file)
        if file[0] == "_" or not os.path.isfile(fp) or not file[-3:] == ".py":
            continue

        opmap = opmap | import_opmap_from_file("xpp", fp)
