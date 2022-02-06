# Imports
from types import NoneType

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
interpreter = None

# Functions    
def deleteVariable(key, scope = -2):
    if not isinstance(key, str):
        raise Exception("Package <stdlib> - Internal Runtime Error: Variable key must be a string")
    if isConstant(key, scope = scope):
        raise Exception("Package <stdlib> - Internal Runtime Error: Cannot delete a constant value")
    if key[0] == "#":
        return interpreter.memory.vars["globals"].pop(key[1:], None)
    if key[0] == "@":
        return interpreter.memory.vars["file"][interpreter.linetrk[scope][0]].pop(key[1:], None)
    return interpreter.memory.vars["local"][interpreter.linetrk[scope][1]].pop(key, None)
    
def fetchVariable(key, scope = -2):
    if not isinstance(key, str):
        raise Exception("Package <stdlib> - Internal Runtime Error: Variable key must be a string")
    return interpreter.getvar(key, section_override = interpreter.linetrk[scope][1])

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

def init(x2):
    global interpreter
    if not interpreter:
        interpreter = x2

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
