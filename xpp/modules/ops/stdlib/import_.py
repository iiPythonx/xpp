# Copyright 2022-2024 iiPython

# Modules
import os
import json
from pathlib import Path
from copy import copy as copyobj

from xpp import config, load_sections
from xpp.exceptions import BrokenPackage
from xpp.modules.ops import import_opmap_from_file
from xpp.modules.ops.shared import ensure_arguments, InvalidArgument

# Initialization
search_locations = [
    str(Path(__file__).parents[4] / "pkgs"),  # Global pkgs folder (assuming module install)
    str(Path("pkgs").absolute())  # Local pkgs folder (relative to cwd)
]
main_namespace = config.get("main", "main").split(os.sep)[-1].removesuffix(".xpp")

# Operators class
class XOperators:
    def imp(mem, args: list) -> None:
        ensure_arguments("imp", "imp <module[.py]> [as <namespace>]", ["module"], args)
        module, module_location = args[0].value, None

        # Python module import
        def process_python_import(filepath: str) -> None:
            if not os.path.isfile(filepath):
                raise InvalidArgument(f"python module '{module}' does not exist!")

            opmap = import_opmap_from_file("", filepath)  # _module (import name)
            mem.interpreter.operators = mem.interpreter.operators | opmap  # merge operators
            return

        if module[-3:] == ".py":
            if module.startswith("./"):
                module = os.path.join(
                    os.path.dirname(mem.interpreter.stack[-1].path),
                    module[2:]
                )

            process_python_import(module)

        # Check the parent module
        orig_module = copyobj(module)
        if module.startswith("./"):
            module = module[2:].rstrip(".xpp")
            module_location = os.path.dirname(mem.interpreter.stack[-1].path)

        else:
            for location in search_locations:
                module_location = os.path.join(location, module.split(".")[0])
                if os.path.isdir(module_location):
                    location = None
                    break

            module_location = module_location if location is None else None

        if module_location is None:
            raise InvalidArgument(f"referenced non-existant package '{orig_module}'")

        # Check the module to run
        module_files, custom_entrypoint = [], None
        if "." not in module:
            if orig_module.startswith("./"):
                module_location = os.path.dirname(mem.interpreter.stack[-1].path)

            xconfig, xc = os.path.join(module_location, ".xconfig"), {}
            if os.path.isfile(xconfig) and module_location != os.getcwd():
                try:
                    with open(xconfig, "r") as fh:
                        xc = json.loads(fh.read())

                except (OSError, json.JSONDecodeError):
                    pass

            mainfile = xc.get("main", f"{module}.xpp")
            if mainfile == xc.get("main"):
                custom_entrypoint = xc["main"]

            # Handle module
            if mainfile[-3:] == ".py":
                return process_python_import(os.path.join(module_location, mainfile))

            module_files.append(os.path.join(module_location, mainfile))

        else:
            struct = module.split(".")
            if struct[1:]:
                module_files += [os.path.join(module_location, *struct[1:][:-1] + [f"{struct[-1]}.xpp"])]

            else:
                module_files += [os.path.join(module_location, f"{struct[0]}.xpp")]

        namespace = module

        # Check additional arguments
        if len(args) >= 2:
            operation = args[1].raw
            value = (args[2].value or args[2].raw) if len(args) == 3 else None

            # Check operations
            if operation == "as":
                if value is None:
                    raise InvalidArgument("expected a namespace to be specified, got nothing")

                namespace = value

        # Load module
        loaded = False
        for path in module_files:
            if not os.path.isfile(path):
                continue

            with open(path, "r") as fh:
                source = fh.read()

            # Load to RAM
            mem.interpreter.sections += load_sections(source, path, namespace)
            mem.interpreter.run_section(f"{namespace}.main")
            loaded = True
            break

        if not loaded:
            if custom_entrypoint:
                raise BrokenPackage(f"package '{orig_module}' attempted to run entrypoint '{custom_entrypoint}', which doesn't exist!")

            raise InvalidArgument(f"referenced non-existant package '{orig_module}'!")
