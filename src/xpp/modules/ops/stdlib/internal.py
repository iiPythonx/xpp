# Copyright 2022-2024 iiPython

# Modules
from typing import List, Any

from xpp import __version__
from xpp.modules.ops.shared import (
    fetch_io_args, ensure_arguments,
    InvalidArgument
)

# Operators class
class XOperators:
    overrides = {"if_": "if", "try_": "try"}

    # Handlers
    def evl(mem, args: list) -> Any:
        ain, aout = fetch_io_args("evl", "evl <expr>", ["expr"], args)
        if not isinstance(ain[0].value, str):
            raise InvalidArgument("evl: expression must be a string!")

        eval(compile(ain[0].value, "<xpp>", mode = "exec"), {
            "mem": mem, "interpreter": mem.interpreter,
            "vars": mem.variables, "version": __version__
        })

    def if_(mem, args: list) -> Any:
        ain, aout = fetch_io_args("if", "if <expr1> <branch1> [expr_n] [branch_n] [...] [else_branch]", ["expr1", "branch1"], args)
        for statement in [ain[i:i + 2] for i in range(0, len(ain), 2)]:
            if len(statement) == 2:
                if not statement[0].value:
                    continue

                statement = statement[1:]

            if not isinstance(statement[0].value, str):
                raise InvalidArgument("if: all branches must be strings!")

            return mem.interpreter.execute(statement[0].value)

    def jmp(mem, args: list) -> List[Any] | Any:
        ain, aout = fetch_io_args("jmp", "jmp <section> [args...] [?output]", ["section"], args)
        results = mem.interpreter.run_section(ain[0].value if isinstance(ain[0].value, str) else ain[0].raw, [a.value for a in ain[1:]])
        outn = len(aout)
        for i, r in enumerate(results):
            if i > outn:
                break

            args[-(outn - i)].set(r)

        return results[0] if len(results) == 1 else results

    def rem(mem, args: list) -> None:
        for arg in args:
            arg.delete()

    def ret(mem, args: list) -> None:
        section = mem.interpreter.stack[-1]
        section.active = False  # Make it return next line tick
        if args:
            section.return_value = [a.value for a in args]

    def rep(mem, args: list) -> Any:
        ain, aout = fetch_io_args("rep", "rep <amount> <expression> [?output]", ["amount", "expression"], args)
        if not isinstance(ain[0].value, int):
            raise InvalidArgument("rep: amount must be an integer!")

        elif not isinstance(ain[1].value, str):
            raise InvalidArgument("rep: expression must be a string!")

        for _ in range(ain[0].value):
            result = mem.interpreter.execute(ain[1].value)

        [out.set(result) for out in aout]
        return result

    def try_(mem, args: list) -> None:
        ain, aout = fetch_io_args("try", "try <expr> [error_branch]", ["expr"], args)
        try:
            mem.interpreter.execute(str(ain[0].value))

        except Exception:
            if len(ain) == 1:
                return

            mem.interpreter.execute(ain[1].value)

    def var(mem, args: list) -> None:
        ensure_arguments("var", "var <name> <value>", ["name", "value"], args)
        args[0].set(args[1].value)

    def whl(mem, args: list) -> None:
        ain, aout = fetch_io_args("whl", "whl <expr> <branch>", ["expr", "branch"], args)
        if not isinstance(ain[1].value, str):
            raise InvalidArgument("whl: branch must be a string!")

        while ain[0].value:
            mem.interpreter.execute(ain[1].value)
            ain[0].refresh()
