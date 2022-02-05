# Imports
from types import NoneType
from pkg.stdlib.scripts.exports import interpreter

# Variables
constants = [
    [ "#array", list ],
    [ "#boolean", bool ],
    [ "#false", False ],
    [ "#float", float ],
    [ "#interger", int ],
    [ "#null", None ],
    [ "#object", dict ],
    [ "#string", str ],
    [ "#true", True ],
    [ "#void", NoneType ]
]
conversion = {
    "boolean": bool,
    "float": float,
    "integer": int,
    "null": lambda x: None,
    "string": str
}
initialized = False

# Functions
def convert(value, target):
    return conversion[target](value) if target in conversion else value

def deleteVariable(key, scope = -2):
    if not isinstance(key, str):
        raise Exception("Package <stdlib> - Internal Runtime Error: Variable key must be a string")

    elif isConstant(key, scope = scope):
        raise Exception("Package <stdlib> - Internal Runtime Error: Cannot delete a constant value")

    value = None
    if key[0] == "#":
        value = interpreter.memory.vars["globals"].pop(key[1:])

    elif key[0] == "@":
        value = interpreter.memory.vars["file"][interpreter.linetrk[scope][0]].pop(key[1:])

    else:
        value = interpreter.memory.vars["local"][interpreter.linetrk[scope][1]].pop(key)

    return value[0]

def fetchVariable(key, scope = -2):
    if not isinstance(key, str):
        raise Exception("Package <stdlib> - Internal Runtime Error: Variable key must be a string")

    return interpreter.getvar(key, section_override = interpreter.linetrk[scope][1])

def init():
    if not interpreter:
        raise Exception("Package <stdlib> - Internal Fatal Error: Exports not executed! Please do not tamper with the standard library source code")

    global initialized
    if not initialized:
        for pair in constants:
            setConstant(pair[0], pair[1])

        initialized = True

def getClass(value):
    return value.__class__

def getType(value):
    return {
        bool: "boolean",
        float: "float",
        int: "integer",
        str: "string",
        NoneType: "null"
    }.get(type(value), "object")

def getVariable(key, scope = -2):
    if not isinstance(key, str):
        raise Exception("Package <stdlib> - Internal Runtime Error: Variable key must be a string")
    variable = fetchVariable(key, scope = scope)
    return variable.value

def hasVariable(key, scope = -2):
    if not isinstance(key, str):
        raise Exception("Package <stdlib> - Internal Runtime Error: Variable key must be a string")
    if key[0] == "#":
        return key[1:] in interpreter.memory.vars["globals"]
    if key[0] == "@":
        return key[1:] in interpreter.memory.vars["file"][interpreter.linetrk[scope][0]]
    return key in interpreter.memory.vars["local"][interpreter.linetrk[scope][1]]

def isConstant(key, scope = -2):
    if not isinstance(key, str):
        raise Exception("Package <stdlib> - Internal Runtime Error: Variable key must be a string")
    variable = fetchVariable(key, scope = scope)
    return "const" in variable.flags

def setConstant(key, value, scope = -2):
    if not isinstance(key, str):
        raise Exception("Package <stdlib> - Internal Runtime Error: Variable key must be a string")
    interpreter.setvar(key, value, section_override = interpreter.linetrk[scope][1])
    interpreter.getvar(key, section_override = interpreter.linetrk[scope][1]).setconst()
    return value

def setVariable(key, value, scope = -2):
    if not isinstance(key, str):
        raise Exception("Package <stdlib> - Internal Runtime Error: Variable key must be a string")
    interpreter.setvar(key, value, section_override = interpreter.linetrk[scope][1])
    return value