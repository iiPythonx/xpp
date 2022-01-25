# Copyright 2022 iiPython

# Exceptions
class MissingArguments(Exception):
    pass

class InvalidArgument(Exception):
    pass

# Comparator
_expr_map = {
    "==": lambda a, b: a == b,
    "!=": lambda a, b: a != b,
    ">=": lambda a, b: a >= b,
    "<=": lambda a, b: a <= b,
    ">": lambda a, b: a > b,
    "<": lambda a, b: a < b,
    "in": lambda a, b: a in b,
    "xin": lambda a, b: a not in b,
    "is": lambda a, b: isinstance(a, {"str": str, "float": float, "int": int, "null": None}[b])
}

# x2 Operators
class XTOperators:
    def cmp(ctx) -> None:
        """
        Evaluates an expression and executes a branch

        cmp <a> <expr> <b> <branch> [else]
        a - any
        expr - expression
        b - any
        branch - str
        else - str
        """
        if len(ctx.args) < 4:
            raise MissingArguments("required: a, expr, b, + branch")

        a, b, expr, branch1, branch2 = ctx.args[0].value, ctx.args[2].value, ctx.args[1].raw, ctx.args[3].value, (ctx.args[4].value if len(ctx.args) > 4 else None)
        if expr not in _expr_map:
            raise InvalidArgument("invalid expression")

        if _expr_map[expr](a, b):
            ctx.memory.interpreter.execute(branch1)

        elif branch2 is not None:
            ctx.memory.interpreter.execute(branch2)

    def whl(ctx) -> None:
        """
        Executes a branch while the provided expression is true

        whl <a> <expr> <b> <branch>
        a - any
        expr - expression
        b - any
        branch - str
        """
        if len(ctx.args) < 4:
            raise MissingArguments("required: a, expr, b, + branch")

        a, b, expr, branch = ctx.args[0], ctx.args[2], ctx.args[1].raw, ctx.args[3].value
        if expr not in _expr_map:
            raise InvalidArgument("invalid expression")

        while _expr_map[expr](a.value, b.value):
            ctx.memory.interpreter.execute(branch)
            [_.refresh() for _ in [a, b]]

    def inm(ctx) -> int:
        """
        Evaluates whether an object is an integer

        inm <obj> [out]
        obj - any
        out - variable
        """
        if not ctx.args:
            raise MissingArguments("required: object")

        val = int(isinstance(ctx.args[0].value, int))
        if len(ctx.args) > 1:
            ctx.args[1].set(val)

        return val

    def inms(ctx) -> int:
        """
        Evaluates whether an object is an integer (this includes stringified integers)
        For example, <inms "5"> will return 1 as "5" is counted as an int

        inms <obj> [out]
        obj - any
        out - variable
        """
        if not ctx.args:
            raise MissingArguments("required: object")

        if isinstance(ctx.args[0].value, str):
            try:
                int(ctx.args[0].value)
                val = 1

            except ValueError:
                val = 0

        else:
            val = int(isinstance(ctx.args[0].value, int))

        if len(ctx.args) > 1:
            ctx.args[1].set(val)

        return val

# Operator map
opmap = {
    "cmp": XTOperators.cmp,
    "whl": XTOperators.whl,
    "inm": XTOperators.inm,
    "inms": XTOperators.inms
}
