# Copyright 2023-2024 iiPython

# Modules
from typing import List

from xpp.core.tokenizer import tokenize
from xpp.core.sections import load_sections

from .exceptions import ConversionError

# Load operators
from .operators import operators

# Initialization
T = " " * 4  # Configured tab size

# Function handling class
class PythonFunction(object):
    def __init__(self, section: dict) -> None:
        self.section = section
        self.name, self.lines = section["sid"], []
        self.is_main = self.name == "main.main"
        self.T = T if not self.is_main else ""

    def append(self, line: str) -> None:
        self.lines.append(self.T + line)

    def prepend(self, line: str) -> None:
        self.lines.insert(0, self.T + line)

    def construct(self) -> List[str]:
        return (
            [f"def {self.name.split('.')[1]}({', '.join(self.section['args'])}):"]
            if not self.is_main else []
        ) + self.lines

# Handle converting xpp to python
def convert_line(function: PythonFunction, line: str, indent: int = 1) -> None:
    original_indent = function.T
    args, function.T = [a for a in tokenize(line)], function.T * indent

    # Handle all operators
    if args[0] not in operators.mapping:
        raise ConversionError(f"Specified operator '{args[0]}' is not convertable.")

    operators.mapping[args[0]](function, args[1:])
    function.T = original_indent

def to_python(source: str) -> str:
    tree = []
    for section in load_sections(source, "main.xpp"):

        # Create Python function
        function = PythonFunction(section)
        for line in section["lines"]:
            if not isinstance(line, str):
                continue  # This is whitespace

            setattr(function, "_convert", convert_line)
            convert_line(function, line)

        # Append function layout
        tree += function.construct()

    # Move all function calls in the global scope
    # to the bottom of the file (top-down)
    functions = [
        (idx, line.split("def ")[1].split("(")[0])
        for idx, line in enumerate(tree) if line.startswith("def")
    ]
    updated_global, cut_index = [], (functions or [(0,)])[0][0]
    for line in tree[:cut_index]:
        if not ("(" in line and ")" in line):
            updated_global.append(line)
            continue

        is_call = False
        for func in functions:
            if line.startswith(f"{func[1]}("):
                tree.append(line)
                is_call = True
                break

        if is_call:
            continue

        updated_global.append(line)

    return "\n".join(updated_global + tree[cut_index:])
