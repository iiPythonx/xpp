# Copyright 2022 iiPython

# Modules
import os
from importlib.util import (
    spec_from_file_location, module_from_spec
)

# Initialization
rootf = os.path.abspath(os.path.dirname(__file__))
operator_files = [x[:-3] for x in os.listdir(rootf) if x[0] != "_" and x.endswith(".py")]

# Load operators
opmap = {}
for opf in operator_files:
    spec = spec_from_file_location(f"x2ops_{opf}", os.path.join(rootf, opf + ".py"))
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    opmap = {**opmap, **module.opmap}
