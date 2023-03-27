# Copyright 2022-2023 iiPython

# Modules
import os
from copy import copy as copyobj
from xpp import load_sections, config
from xpp.modules.ops.shared import (
    ensure_arguments, InvalidArgument
)

# Initialization
pkgs_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../pkgs"))
main_namespace = config.get("main", "main").replace("\\", "/").split("/")[-1].removesuffix(".xpp")

# Operators class
class XOperators:
    overrides = {}

    # Handlers
    def imp(ctx) -> None:
        ensure_arguments("imp", "imp <module> [as <namespace>]", ["module"], ctx.args)
        module, module_location = ctx.args[0].value, None
        orig_module = copyobj(module)
        if module.startswith("./"):
            module = module[2:]
            module_location = os.path.join(os.getcwd(), module.split(".")[0])

        else:
            module_location = os.path.join(pkgs_folder, module.split(".")[0])

        if module_location is None:
            raise InvalidArgument(f"referenced non-existant package '{orig_module}'")

        # Check the module to run
        module_files = []
        if "." not in module:
            module_files.append(os.path.join(module_location, f"{module}.xpp"))
            if orig_module.startswith("./"):
                module_files.append(os.path.join(os.getcwd(), f"{module}.xpp"))

        else:
            struct = module.split(".")
            if struct[1:]:
                module_files += [os.path.join(module_location, *struct[1:][:-1] + [f"{struct[-1]}.xpp"])]

            else:
                module_files += [os.path.join(module_location, f"{struct[0]}.xpp")]

        namespace = module

        # Check additional arguments
        if len(ctx.args) >= 2:
            operation = ctx.args[1].raw
            value = (ctx.args[2].value or ctx.args[2].raw) if len(ctx.args) == 3 else None

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
            ctx.mem.interpreter.sections += load_sections(source, path, namespace)
            ctx.mem.interpreter.run_section(f"{namespace}.main")
            loaded = True
            break

        if not loaded:
            raise InvalidArgument(f"referenced non-existant package '{orig_module}'")

    def ret(ctx) -> None:
        section = ctx.mem.interpreter.stack[-1]
        section.active = False  # Make it return next line tick
        if ctx.args:
            section.return_value = [a.value for a in ctx.args]
