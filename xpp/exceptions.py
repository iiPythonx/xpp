# Copyright 2022-2023 iiPython

# Master class
class xppException(Exception):
    pass

# Subexceptions
class UnknownSection(xppException):
    pass

class UnknownOperator(xppException):
    pass

class SectionConflict(xppException):
    pass

class InvalidSection(xppException):
    pass

class InvalidSyntax(xppException):
    pass

class MissingParameter(xppException):
    pass

class BrokenPackage(xppException):
    pass
