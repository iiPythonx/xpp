"""
SimpleEval - (C) 2013-2023 Daniel Fairhead
-------------------------------------

An short, easy to use, safe and reasonably extensible expression evaluator.
Designed for things like in a website where you want to allow the user to
generate a string, or a number from some other input, without allowing full
eval() or other unsafe or needlessly complex linguistics.

-------------------------------------

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

-------------------------------------

Initial idea copied from J.F. Sebastian on Stack Overflow
( http://stackoverflow.com/a/9558001/1973500 ) with
modifications and many improvements.

-------------------------------------
Contributors:
- corro (Robin Baumgartner) (py3k)
- dratchkov (David R) (nested dicts)
- marky1991 (Mark Young) (slicing)
- T045T (Nils Berg) (!=, py3kstr, obj.
- perkinslr (Logan Perkins) (.__globals__ or .func_ breakouts)
- impala2 (Kirill Stepanov) (massive _eval refactor)
- gk (ugik) (Other iterables than str can DOS too, and can be made)
- daveisfera (Dave Johansen) 'not' Boolean op, Pycharm, pep8, various other fixes
- xaled (Khalid Grandi) method chaining correctly, double-eval bugfix.
- EdwardBetts (Edward Betts) spelling correction.
- charlax (Charles-Axel Dein charlax) Makefile and cleanups
- mommothazaz123 (Andrew Zhu) f"string" support, Python 3.8 support
- lubieowoce (Uryga) various potential vulnerabilities
- JCavallo (Jean Cavallo) names dict shouldn't be modified
- Birne94 (Daniel Birnstiel) for fixing leaking generators, star expressions
- patricksurry (Patrick Surry) or should return last value, even if falsy.
- shughes-uk (Samantha Hughes) python w/o 'site' should not fail to import.
- KOLANICH packaging / deployment / setup help & << + >> & other bit ops
- graingert (Thomas Grainger) packaging / deployment / setup help
- bozokopic (Bozo Kopic) Memory leak fix
- daxamin (Dax Amin) Better error for attempting to eval empty string
- smurfix (Matthias Urlichs) Allow clearing functions / operators / etc completely

-------------------------------------
Basic Usage:

>>> s = SimpleEval()
>>> s.eval("20 + 30")
50

You can add your own functions easily too:

if file.txt contents is "11"

>>> def get_file():
...     with open("file.txt", 'r') as f:
...         return f.read()

>>> s.functions["get_file"] = get_file
>>> s.eval("int(get_file()) + 31")
42

For more information, see the full package documentation on pypi, or the github
repo.

-----------

If you don't need to re-use the evaluator (with it's names, functions, etc),
then you can use the simple_eval() function:

>>> simple_eval("21 + 19")
40

You can pass names, operators and functions to the simple_eval function as
well:

>>> simple_eval("40 + two", names={"two": 2})
42

"""

import ast
import operator as op
import sys
import warnings

########################################
# Module wide 'globals'

MAX_STRING_LENGTH = 100000
MAX_COMPREHENSION_LENGTH = 10000
MAX_POWER = 4000000  # highest exponent
MAX_SHIFT = 10000  # highest << or >> (lshift / rshift)
MAX_SHIFT_BASE = int(sys.float_info.max)  # highest on left side of << or >>
DISALLOW_PREFIXES = ["_", "func_"]
DISALLOW_METHODS = ["format", "format_map", "mro"]

# Disallow functions:
# This, strictly speaking, is not necessary.  These /should/ never be accessable anyway,
# if DISALLOW_PREFIXES and DISALLOW_METHODS are all right.  This is here to try and help
# people not be stupid.  Allowing these functions opens up all sorts of holes - if any of
# their functionality is required, then please wrap them up in a safe container.  And think
# very hard about it first.  And don't say I didn't warn you.
# builtins is a dict in python >3.6 but a module before
DISALLOW_FUNCTIONS = {type, isinstance, eval, getattr, setattr, repr, compile, open, exec}
if hasattr(__builtins__, "help") or (
    hasattr(__builtins__, "__contains__") and "help" in __builtins__  # type: ignore
):
    # PyInstaller environment doesn't include this module.
    DISALLOW_FUNCTIONS.add(help)

########################################
# Exceptions:


class InvalidExpression(Exception):
    """Generic Exception"""

    pass


class FunctionNotDefined(InvalidExpression):
    """sorry! That function isn't defined!"""

    def __init__(self, func_name, expression):
        self.message = "Function '{0}' not defined," " for expression '{1}'.".format(
            func_name, expression
        )
        setattr(self, "func_name", func_name)  # bypass 2to3 confusion.
        self.expression = expression

        super(InvalidExpression, self).__init__(self.message)


class NameNotDefined(InvalidExpression):
    """a name isn't defined."""

    def __init__(self, name, expression):
        self.name = name
        self.message = "'{0}' is not defined for expression '{1}'".format(name, expression)
        self.expression = expression

        super(InvalidExpression, self).__init__(self.message)


class AttributeDoesNotExist(InvalidExpression):
    """attribute does not exist"""

    def __init__(self, attr, expression):
        self.message = "Attribute '{0}' does not exist in expression '{1}'".format(
            attr, expression
        )
        self.attr = attr
        self.expression = expression

        super(InvalidExpression, self).__init__(self.message)


class OperatorNotDefined(InvalidExpression):
    """operator does not exist"""

    def __init__(self, attr, expression):
        self.message = "Operator '{0}' does not exist in expression '{1}'".format(attr, expression)
        self.attr = attr
        self.expression = expression

        super(InvalidExpression, self).__init__(self.message)


class FeatureNotAvailable(InvalidExpression):
    """What you're trying to do is not allowed."""

    pass


class NumberTooHigh(InvalidExpression):
    """Sorry! That number is too high. I don't want to spend the
    next 10 years evaluating this expression!"""

    pass


class IterableTooLong(InvalidExpression):
    """That iterable is **way** too long, baby."""

    pass


class AssignmentAttempted(UserWarning):
    """Assignment not allowed in SimpleEval"""

    pass


class MultipleExpressions(UserWarning):
    """Only the first expression parsed will be used"""

    pass

########################################
# Defaults for the evaluator:

DEFAULT_OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.FloorDiv: op.floordiv,
    ast.RShift: op.rshift,
    ast.LShift: op.lshift,
    ast.Pow: op.pow,
    ast.Mod: op.mod,
    ast.Eq: op.eq,
    ast.NotEq: op.ne,
    ast.Gt: op.gt,
    ast.Lt: op.lt,
    ast.GtE: op.ge,
    ast.LtE: op.le,
    ast.Not: op.not_,
    ast.USub: op.neg,
    ast.UAdd: op.pos,
    ast.BitXor: op.pow,
    ast.BitOr: op.or_,
    ast.BitAnd: op.and_,
    ast.Invert: op.invert,
    ast.Is: lambda a, b: isinstance(a, {"int": int, "str": str, "null": None, "float": float}[b]),
    ast.In: lambda a, b: a in b,
    ast.NotIn: lambda a, b: a not in b
}

DEFAULT_NAMES = {"true": True, "false": False, "null": None}

ATTR_INDEX_FALLBACK = True


########################################
# And the actual evaluator:


class SimpleEval(object):  # pylint: disable=too-few-public-methods
    """A very simple expression parser.
    >>> s = SimpleEval()
    >>> s.eval("20 + 30 - ( 10 * 5)")
    0
    """

    expr = ""

    def __init__(self, operators=None, names=None):
        """
        Create the evaluator instance.  Set up valid operators (+,-, etc)
        functions (add, random, get_val, whatever) and names."""

        if operators is None:
            operators = DEFAULT_OPERATORS.copy()
        if names is None:
            names = DEFAULT_NAMES.copy()

        self.operators = operators
        self.names = names

        self.nodes = {
            ast.Expr: self._eval_expr,
            ast.Num: self._eval_num,
            ast.Str: self._eval_str,
            ast.Name: self._eval_name,
            ast.UnaryOp: self._eval_unaryop,
            ast.BinOp: self._eval_binop,
            ast.BoolOp: self._eval_boolop,
            ast.Compare: self._eval_compare,
            ast.Constant: self._eval_constant
        }

        # Defaults:
        self.ATTR_INDEX_FALLBACK = ATTR_INDEX_FALLBACK

    def __del__(self):
        self.nodes = None

    @staticmethod
    def parse(expr):
        """parse an expression into a node tree"""

        parsed = ast.parse(expr.strip())

        if not parsed.body:
            raise InvalidExpression("Sorry, cannot evaluate empty string")
        if len(parsed.body) > 1:
            warnings.warn(
                "'{}' contains multiple expressions. Only the first will be used.".format(expr),
                MultipleExpressions,
            )
        return parsed.body[0]

    def eval(self, expr, previously_parsed=None):
        """evaluate an expresssion, using the operators, functions and
        names previously set up."""

        # set a copy of the expression aside, so we can give nice errors...
        self.expr = expr

        return self._eval(previously_parsed or self.parse(expr))

    def _eval(self, node):
        """The internal evaluator used on each node in the parsed tree."""

        try:
            handler = self.nodes[type(node)]
        except KeyError:
            raise InvalidExpression()

        return handler(node)

    def _eval_expr(self, node):
        return self._eval(node.value)

    @staticmethod
    def _eval_num(node):
        return node.n

    @staticmethod
    def _eval_str(node):
        if len(node.s) > MAX_STRING_LENGTH:
            raise IterableTooLong(
                "String Literal in statement is too long!"
                " ({0}, when {1} is max)".format(len(node.s), MAX_STRING_LENGTH)
            )
        return node.s

    @staticmethod
    def _eval_constant(node):
        if hasattr(node.value, "__len__") and len(node.value) > MAX_STRING_LENGTH:
            raise IterableTooLong(
                "Literal in statement is too long!"
                " ({0}, when {1} is max)".format(len(node.value), MAX_STRING_LENGTH)
            )
        return node.value

    def _eval_unaryop(self, node):
        try:
            operator = self.operators[type(node.op)]
        except KeyError:
            raise OperatorNotDefined(node.op, self.expr)
        return operator(self._eval(node.operand))

    def _eval_binop(self, node):
        try:
            operator = self.operators[type(node.op)]
        except KeyError:
            raise OperatorNotDefined(node.op, self.expr)
        return operator(self._eval(node.left), self._eval(node.right))

    def _eval_boolop(self, node):
        to_return = False
        if isinstance(node.op, ast.And):
            for value in node.values:
                to_return = self._eval(value)
                if not to_return:
                    break
        elif isinstance(node.op, ast.Or):
            for value in node.values:
                to_return = self._eval(value)
                if to_return:
                    break
        return to_return

    def _eval_compare(self, node):
        right = self._eval(node.left)
        to_return = True
        for operation, comp in zip(node.ops, node.comparators):
            if not to_return:
                break
            left = right
            right = self._eval(comp)
            to_return = self.operators[type(operation)](left, right)
        return to_return

    def _eval_name(self, node):
        try:
            # This happens at least for slicing
            # This is a safe thing to do because it is impossible
            # that there is a true exression assigning to none
            # (the compiler rejects it, so you can't even
            # pass that to ast.parse)
            if hasattr(self.names, "__getitem__"):
                return self.names[node.id]
            if callable(self.names):
                return self.names(node)
            raise InvalidExpression(
                'Trying to use name (variable) "{0}"'
                ' when no "names" defined for'
                " evaluator".format(node.id)
            )

        except KeyError:
            raise NameNotDefined(node.id, self.expr)

def simple_eval(expr, names=None):
    """Simply evaluate an expresssion"""
    s = SimpleEval(names=names)
    return s.eval(expr)
