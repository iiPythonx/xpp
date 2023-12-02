# Copyright 2022-2024 iiPython

# Modules
import sys
from typing import List

# Master class
class XPPException(Exception):
    def __init__(self, message: str, index: int | range = None, stack: list = None) -> None:
        super().__init__(message)
        self.index = index
        self.stack = stack

# Subexceptions
class UnknownSection(XPPException):
    pass

class UnknownOperator(XPPException):
    pass

class SectionConflict(XPPException):
    pass

class InvalidSection(XPPException):
    pass

class InvalidSyntax(XPPException):
    pass

class MissingParameter(XPPException):
    pass

class BrokenPackage(XPPException):
    pass

class MiscError(XPPException):
    pass

# Handler
def handle_exception(e: Exception | XPPException, stack: List[dict]) -> None:
    xpp = isinstance(e, XPPException)
    if xpp and e.stack is not None:
        stack = e.stack

    # Handle stack processing
    if len(stack) > 10:
        print(f"... last {len(stack) - 10} stack entries ommitted")

    for s in stack[-10:]:
        line, last = s.line_content, s == stack[-10:][-1]
        print(f"x++ file {s.path} in {s.sid} on line {s.current_line}:")
        print(f"  > {line}", end = "\n" if last else "\n\n")
        if last and xpp and (e.index is not None):
            saferange = e.index if isinstance(e.index, range) else range(e.index, e.index)
            print(
                " " * 4,
                "".join([("^" if (isinstance(e.index, int) and (i == e.index)) else " " if i not in saferange else "^") for i in range(len(line))]),
                sep = ""
            )

    print(f"\n{type(e).__name__}: {e}")
    if "-D" in sys.argv:
        print("\nPython traceback:")
        raise e
