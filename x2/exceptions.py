# Copyright 2022-2023 iiPython

# Master class
class x2Exception(Exception):
    pass

# Subexceptions
class UnknownSection(x2Exception):
    pass

class UnknownOperator(x2Exception):
    pass

class SectionConflict(x2Exception):
    pass

class InvalidSyntax(x2Exception):
    pass
