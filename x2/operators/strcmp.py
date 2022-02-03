# Copyright 2022 iiPython

# Exceptions
class MissingArguments(Exception):
    pass

class InvalidArgument(Exception):
    pass

# x2 Operators
class XTOperators:
    def lwr(ctx) -> str:
        """
        Fully lowercases a given string

        lwr <val> [out]
        val - str
        out - variable
        """
        if not ctx.args:
            raise MissingArguments("required: val")

        elif not isinstance(ctx.args[0].value, str):
            raise InvalidArgument("val must be a string")

        val = ctx.args[0].value.lower()
        ctx.args[1 if len(ctx.args) > 1 else 0].set(val)
        return val

    def upr(ctx) -> str:
        """
        Fully uppercases a given string

        upr <val> [out]
        val - str
        out - variable
        """
        if not ctx.args:
            raise MissingArguments("required: val")

        elif not isinstance(ctx.args[0].value, str):
            raise InvalidArgument("val must be a string")

        val = ctx.args[0].value.upper()
        ctx.args[1 if len(ctx.args) > 1 else 0].set(val)
        return val

    def num(ctx) -> int:
        """
        Converts a string to an integer

        num <val> [out]
        val - str
        out - variable
        """
        if not ctx.args:
            raise MissingArguments("required: val")

        elif not isinstance(ctx.args[0].value, str):
            raise InvalidArgument("val must be a string")

        try:
            val = int(ctx.args[0].value)
            ctx.args[1 if len(ctx.args) > 1 else 0].set(val)
            return val

        except ValueError:
            raise InvalidArgument("val isn't a stringified integer")

    def flt(ctx) -> int:
        """
        Converts a string to an float

        num <val> [out]
        val - str
        out - variable
        """
        if not ctx.args:
            raise MissingArguments("required: val")

        elif not isinstance(ctx.args[0].value, str):
            raise InvalidArgument("val must be a string")

        try:
            val = float(ctx.args[0].value)
            ctx.args[1 if len(ctx.args) > 1 else 0].set(val)
            return val

        except ValueError:
            raise InvalidArgument("val isn't a stringified float")

    def str_(ctx) -> str:
        """
        Converts a value to a string

        str <val> [out]
        val - any
        out - variable
        """
        if not ctx.args:
            raise MissingArguments("required: val")

        val = str(ctx.args[0].value)
        ctx.args[1 if len(ctx.args) > 1 else 0].set(val)
        return val

    def len(ctx) -> int:
        """
        Returns the length of a string

        len <val> [out]
        val - str
        out - variable
        """
        if not ctx.args:
            raise MissingArguments("required: val")

        elif not isinstance(ctx.args[0].value, str):
            raise InvalidArgument("val must be a string")

        val = len(ctx.args[0].value)
        if len(ctx.args) > 1:
            ctx.args[1].set(val)

        return val

    def slc(ctx) -> str:
        """
        Slices a string using the given range

        slc <r1> <r2> <val> [out]
        r1 - int
        r2 - int
        val - str
        out - variable
        """
        if len(ctx.args) < 3:
            raise MissingArguments("required: r1, r2 + val")

        elif [a for a in ctx.args[:2] if not isinstance(a.value, int)]:
            raise InvalidArgument("r1 and r2 must both be integers")

        elif not isinstance(ctx.args[2].value, str):
            raise InvalidArgument("val must be a string")

        val = ctx.args[2].value[ctx.args[0].value:ctx.args[1].value]
        if len(ctx.args) > 3:
            ctx.args[3].set(val)

        return val

    def idx(ctx) -> int:
        """
        Grabs the index of one string in another string

        idx <str1> <str2> [out]
        str1 - str
        str2 - str
        out - variable
        """
        if len(ctx.args) < 2:
            raise MissingArguments("required: str1, str2")

        elif [a for a in ctx.args[:2] if not isinstance(a.value, str)]:
            raise InvalidArgument("str1 and str2 must both be strings")

        val = ctx.args[1].value.index(ctx.args[0].value)
        if len(ctx.args) > 2:
            ctx.args[2].set(val)

        return val

    def char(ctx) -> str:
        """
        Returns the character of a string at the given index

        char <idx> <val> [out]
        idx - int
        val - str
        out - variable
        """
        if len(ctx.args) < 2:
            raise MissingArguments("required: idx + val")

        elif not isinstance(ctx.args[0].value, int):
            raise InvalidArgument("idx must be an integer")

        elif not isinstance(ctx.args[1].value, str):
            raise InvalidArgument("val must be a string")

        try:
            val = ctx.args[1].value[ctx.args[0].value]
            if len(ctx.args) > 2:
                ctx.args[2].set(val)

            return val

        except IndexError:
            raise InvalidArgument("invalid string index")

# Operator map
opmap = {
    "lwr": XTOperators.lwr, "upr": XTOperators.upr,
    "num": XTOperators.num, "flt": XTOperators.flt,
    "slc": XTOperators.slc, "idx": XTOperators.idx,
    "len": XTOperators.len, "char": XTOperators.char,
    "str": XTOperators.str_
}
