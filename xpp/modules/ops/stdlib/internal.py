# Copyright 2022-2023 iiPython

# Modules
import os
from copy import copy as copyobj
from xpp import load_sections, config
from xpp.modules.ops.shared import (
    fetch_io_args, ensure_arguments,
    InvalidArgument
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

    def var(ctx) -> None:
        ensure_arguments("var", "var <name> <value>", ["name", "value"], ctx.args)
        ctx.args[0].set(ctx.args[1].value)

    def jmp(ctx) -> None:
        ain, aout = fetch_io_args("jmp", "jmp <section> [args...] [?output]", ["section"], ctx.args)
        results = ctx.mem.interpreter.run_section(ain[0].value if isinstance(ain[0].value, str) else ain[0].raw, [a.value for a in ain[1:]])
        outn = len(aout)
        for i, r in enumerate(results):
            if i > outn:
                break

            ctx.args[-(outn - i)].set(r)

    def rem(ctx) -> None:
        [arg.delete() for arg in ctx.args]

    def rep(ctx) -> None:
        ain, aout = fetch_io_args("rep", "rep <amount> <section> [args...] [?output]", ["amount", "section"], ctx.args)
        if not isinstance(ain[0].value, int):
            raise InvalidArgument("rep: amount must be an integer!")

        for _ in range(ain[0].value):
            [a.refresh() for a in ain[2:]]
            results = ctx.mem.interpreter.run_section(ain[1].value if isinstance(ain[1].value, str) else ain[1].raw, [a.value for a in ain[2:]])
            outn = len(aout)
            for i, r in enumerate(results):
                if i > outn:
                    break

                aout[-i].set(r)
