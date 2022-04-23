# x2 Operator Loader
# Copyright 2022 iiPython

# Modules
import os
from importlib.util import (
    module_from_spec, spec_from_file_location
)

# Initialization
opmap = {}
for path, _, files in os.walk(os.path.abspath(os.path.dirname(__file__))):
    if "__pycache__" in path:
        continue

    for file in files:
        fp = os.path.join(path, file)
        if file[0] == "_" or not os.path.isfile(fp) or not file[-3:] == ".py":
            continue

        # Load operators
        spec = spec_from_file_location(f"x2ops_{file[:-3]}", fp)
        module = module_from_spec(spec)
        spec.loader.exec_module(module)
        opmap = opmap | module.opmap
