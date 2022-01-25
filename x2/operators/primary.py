# Copyright 2022 iiPython

# Modules
from typing import Any

# Exceptions
class MissingArguments(Exception):
    pass

class InvalidArgument(Exception):
    pass

# Handlers
def _section_call(memory, section: str, args: list, output = None) -> Any:
    section = memory.interpreter.find_section(section)
    sectionargs = memory.interpreter.sections[section]["args"]
    if len(args) < len(sectionargs):
        raise MissingArguments(f"section '{section}' takes {', '.join(sectionargs)}")

    for i, arg in enumerate(sectionargs):
        memory.vars[arg] = args[i].value

    retvalue = memory.interpreter.run_section(section)
    if output is not None:
        output.set(retvalue)

    return retvalue

# x2 Operators
class XTOperators:
    def psh(ctx) -> None:
        """
        Pushes a value into a variable

        psh <val> <out>
        val - any
        out - variable
        """
        if len(ctx.args) < 2:
            raise MissingArguments("required: val + output")

        ctx.args[1].set(ctx.args[0].value)

    def out(ctx) -> None:
        """
        Writes output to the terminal

        out [*vals]
        vals - any
        """
        print(*[
            str(a.value).encode(
                "latin-1", "backslashreplace"
            ).decode("unicode-escape")
            for a in ctx.args
        ])

    def pop(ctx) -> Any:
        """
        Pops a variable's value

        pop <val> [out]
        val - str, or raw
        out - variable
        """
        if not ctx.args:
            raise MissingArguments("required: val")

        val = ctx.args[0]
        if "var" not in val.flags:
            val.value = ctx.memory.vars.get(val.value, None)
            if val.value is None:
                raise InvalidArgument("invalid or unknown variable")

        val = val.value
        if len(ctx.args) > 1:
            ctx.args[1].set(val)

        return val

    def jmp(ctx) -> None:
        """
        Jumps to a section

        jmp <section>
        section - str, or raw
        """
        if not ctx.args:
            raise MissingArguments("required: section")

        section = ctx.args[0].value or ctx.args[0].raw
        ctx.memory.interpreter.run_section(section)

    def imp(ctx) -> None:
        """
        Imports another x2 file

        imp <path>
        path - str
        """
        if not ctx.args:
            raise MissingArguments("required: path")

        path = ctx.args[0].value.replace("\\", "/")
        if not path.endswith(".xt"):
            path += ".xt"

        with open(path, "r", encoding = "utf-8") as f:
            code = f.read()

        ctx.memory.interpreter.load_sections(
            code,
            path.split("/")[-1],
            external = True
        )

    def rem(ctx) -> None:
        """
        Removes a variable

        rem <var>
        val - str, or raw
        """
        if not ctx.args:
            raise MissingArguments("required: val")

        var = ctx.args[0]
        if "var" not in var.flags:
            if var.value in ctx.memory.vars:
                del ctx.memory.vars[var.value]
                return

        del ctx.memory.vars[var.raw]

    def rep(ctx) -> None:
        """
        Repeats a branch a certain number of times

        rep <num> <branch>
        num - int
        branch - str
        """
        if len(ctx.args) < 2:
            raise MissingArguments("required: num + branch")

        elif not isinstance(ctx.args[0].value, int):
            raise InvalidArgument("num must be an integer")

        branch = ctx.args[1].value
        if not isinstance(branch, str):
            raise InvalidArgument("branch must be a string")

        [ctx.memory.interpreter.execute(branch) for i in range(ctx.args[0].value)]

    def ret(ctx) -> None:
        """
        Sets the current section's return value and ends the section

        ret <val>
        val - any
        """
        if not ctx.args:
            raise MissingArguments("required: val")

        ctx.memory.interpreter.sections[ctx.memory.interpreter.linetrk[-1][1]]["return"] = ctx.args[0].value
        XTOperators.end(ctx)

    def pvk(ctx) -> Any:
        """
        Provokes the section with the provided arguments

        pvk <section> [*args]
        section - str
        *args - any
        """
        if not ctx.args:
            raise MissingArguments("required: section")

        return _section_call(ctx.memory, ctx.args[0].value or ctx.args[0].raw, ctx.args[1:])

    def call(ctx) -> Any:
        """
        Calls the section with the provided arguments and returns the result

        call <section> <*args> <output>
        section - str
        *args - any
        output - variable
        """
        if not ctx.args:
            raise MissingArguments("required: section")

        call_args, output = ctx.args[1:], None
        if call_args:
            call_args, output = call_args[:-1], call_args[-1]
            if "var" not in output.flags:
                raise InvalidArgument("output must be a variable")

        return _section_call(ctx.memory, ctx.args[0].value or ctx.args[0].raw, call_args, output)

    def skp(ctx) -> None:
        """
        Acts as either a placeholder within a section or as a gate

        skp
        """
        return

    def end(ctx) -> None:
        """
        Ends the current section jump without a return value

        end
        """
        ctx.memory.interpreter.linetrk[-1][3] = True

# Operator map
opmap = {
    "psh": XTOperators.psh, "pop": XTOperators.pop,
    "out": XTOperators.out, "jmp": XTOperators.jmp,
    "imp": XTOperators.imp, "rem": XTOperators.rem,
    "rep": XTOperators.rep, "ret": XTOperators.ret,
    "pvk": XTOperators.pvk, "skp": XTOperators.skp,
    "end": XTOperators.end, "call": XTOperators.call
}
