# Copyright 2022-2023 iiPython

# Modules
import os
from typing import List, Any
from copy import copy as copyobj

from xpp import (
    load_sections, config,
    __version__
)
from xpp.modules.ops import (
    import_opmap_from_file
)
from xpp.modules.ops.shared import (
    fetch_io_args, ensure_arguments,
    InvalidArgument
)

# Initialization
pkgs_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../pkgs"))
main_namespace = config.get("main", "main").replace("\\", "/").split("/")[-1].removesuffix(".xpp")

# Operators class
class XOperators:
    overrides = {"if_": "if"}

    # Handlers
    def evl(ctx) -> Any:
        ain, aout = fetch_io_args("evl", "evl <expr>", ["expr"], ctx.args)
        if not isinstance(ain[0].value, str):
            raise InvalidArgument("evl: expression must be a string!")

        eval(compile(ain[0].value, "<xpp>", mode = "exec"), {
            "ctx": ctx, "mem": ctx.mem, "interpreter": ctx.mem.interpreter,
            "vars": ctx.mem.variables, "version": __version__
        })

    def if_(ctx) -> Any:
        ain, aout = fetch_io_args("if", "if <expr> <branch> [false_branch]", ["expr", "branch"], ctx.args)
        if not isinstance(ain[1].value, str):
            raise InvalidArgument("if: branch must be a string!")

        false_branch = len(ain) > 2
        if false_branch and not isinstance(ain[2].value, str):
            raise InvalidArgument("if: false_branch must be a string!")

        # Perform check
        if ain[0].value:
            return ctx.mem.interpreter.execute(ain[1].value)

        elif false_branch:
            return ctx.mem.interpreter.execute(ain[2].value)

    def imp(ctx) -> None:
        ensure_arguments("imp", "imp <module[.py]> [as <namespace>]", ["module"], ctx.args)
        module, module_location = ctx.args[0].value, None

        # Python module import
        if module[-3:] == ".py":
            if not os.path.isfile(module):
                raise InvalidArgument(f"python module '{module}' does not exist!")

            opmap = import_opmap_from_file("", module)  # _module (import name)
            ctx.mem.interpreter.operators = ctx.mem.interpreter.operators | opmap  # merge operators
            return

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

    def jmp(ctx) -> List[Any] | Any:
        ain, aout = fetch_io_args("jmp", "jmp <section> [args...] [?output]", ["section"], ctx.args)
        results = ctx.mem.interpreter.run_section(ain[0].value if isinstance(ain[0].value, str) else ain[0].raw, [a.value for a in ain[1:]])
        outn = len(aout)
        for i, r in enumerate(results):
            if i > outn:
                break

            ctx.args[-(outn - i)].set(r)

        return results[0] if len(results) == 1 else results

    def rem(ctx) -> None:
        for arg in ctx.args:
            arg.delete()

    def ret(ctx) -> None:
        section = ctx.mem.interpreter.stack[-1]
        section.active = False  # Make it return next line tick
        if ctx.args:
            section.return_value = [a.value for a in ctx.args]

    def rep(ctx) -> Any:
        ain, aout = fetch_io_args("rep", "rep <amount> <expression> [?output]", ["amount", "expression"], ctx.args)
        if not isinstance(ain[0].value, int):
            raise InvalidArgument("rep: amount must be an integer!")

        elif not isinstance(ain[1].value, str):
            raise InvalidArgument("rep: expression must be a string!")

        for _ in range(ain[0].value):
            result = ctx.mem.interpreter.execute(ain[1].value)

        [out.set(result) for out in aout]
        return result

    def var(ctx) -> None:
        ensure_arguments("var", "var <name> <value>", ["name", "value"], ctx.args)
        ctx.args[0].set(ctx.args[1].value)
