# Copyright 2022 iiPython
# x2 - a minimalistic programming language
# Revision 2.1b3

# Modules
import os
import re
import sys
import json
from typing import Any, Union
from types import FunctionType

# Load configuration
config = {"entrypoint": "main.xt"}
try:
    with open("config.json", "r") as f:
        config = json.loads(f.read())

except Exception:
    pass

argv = sys.argv[1:]
if argv:
    config["entrypoint"] = argv[0]

# Load built-in operators
try:

    # Import from the full path of x2/operators.py
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "operators",
        os.path.abspath(os.path.join(os.path.dirname(__file__), config["operators_file"]))
    )

    # Initialize the operators module
    opmodule = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(opmodule)
    operators = opmodule.XTBuiltinOperators

except ImportError:

    # Nice silent fail, you just won't have any operators
    class operators:
        pass

# Exceptions
class Immutable(Exception):
    pass

class SectionConflict(Exception):
    pass

class UnknownVariable(Exception):
    pass

class UnknownOperator(Exception):
    pass

# Memory Handler
class XTMemory(object):
    def __init__(self) -> None:
        self.vars = {}
        self._sectionret = None

# Context Handler
class XTContext(object):
    def __init__(self, memory: XTMemory, args: list) -> None:
        self.args = args
        self.memory = memory

    def __repr__(self) -> str:
        return f"<XTContext args={repr(self.args)}>"

# Datastore
class XTDataStore(object):
    def __init__(self, memory: XTMemory, content: str) -> None:
        self.memory = memory
        self.content = content

        self.isvar = False
        self.value = self._process(content)

    def __repr__(self) -> str:
        return f"""<XTDS {f"var name='{self.content}'" if self.isvar else "literal"} val={repr(self.value)}"""

    def _process(self, content: str) -> Union[str, int]:
        content = content.replace("\\\"", "\"")
        if content[0] == "\"" and content[-1] == "\"":
            value = content[1:][:-1]
            for item in re.findall(re.compile(r"\$\([^)]*\)"), value):
                evaluated = self.memory._inter.execute(self.memory._parser.parse_lines(item[2:][:-1])[0])
                value = value.replace(item, str((evaluated or "") if evaluated != 0 else 0))

            return value

        try:
            return int(content)

        except ValueError:
            try:
                return float(content)

            except ValueError:
                self.isvar = True
                return self.memory.vars.get(content, None)

    def refresh(self) -> None:
        self.value = self._process(self.content)

    def set(self, value: Union[str, int]) -> None:
        if not self.isvar:
            raise Immutable

        self.value = value
        self.memory.vars[self.content] = value
        return value

# Parser
class XTParser(object):
    def __init__(self, memory: XTMemory) -> None:
        self.memory = memory

    def sectionize(self, tokens: list) -> dict:
        dt = {"sections": {"global": []}, "active": "global"}
        for line in tokens:
            if line[0][0] != ":":
                dt["sections"][dt["active"]].append(line)
                continue

            sid = line[0][1:]
            if sid in dt["sections"]:
                raise SectionConflict(f"section '{sid}' already exists!")

            dt["active"], dt["sections"][sid] = sid, []

        return dt["sections"]

    def parse_lines(self, code: str) -> list:
        lines = []
        for block in [line.lstrip() for line in code.split("\n")]:
            if not block.strip() or block[:2] == "::":
                continue

            # Process block
            data = {"val": "", "qt": False, "line": []}
            for idx, char in enumerate(block):
                if char == " " and not data["qt"]:
                    if not data["val"]:
                        continue

                    data["line"].append(data["val"])
                    data["val"] = ""

                elif char == "\"" and (idx > 0 and block[idx - 1] != "\\"):  # Enables quoting with backslash
                    if data["qt"]:
                        data["line"].append(data["val"] + "\"")
                        data["val"] = ""
                        data["qt"] = False

                    else:
                        data["qt"] = True
                        data["val"] += "\""

                else:
                    data["val"] += char

            # Construct missing data
            if data["val"]:
                data["line"].append(data["val"])
                data["val"] = ""

            # Push lines
            lines.append(data["line"])

        return lines

# Interpreter
class XTInterpreter(object):
    def __init__(self, memory: XTMemory, sections: dict, operators: dict = {}) -> None:
        self.memory = memory
        self.sections = sections
        self.operators = operators

        self._sectiontrk = []
        self._sectionrets = []

    def run(self) -> None:
        self.run_section("global")
        self.run_section("main")

    def operator(self, name: str) -> FunctionType:
        def internal_cb(cb: FunctionType) -> None:
            self.operators[name] = cb

        return internal_cb

    def execute(self, tokens: list) -> Any:
        try:
            operator = tokens[0]
            if operator not in self.operators:
                raise UnknownOperator(operator)

            return self.operators[operator](XTContext(self.memory, [XTDataStore(self.memory, t) for t in tokens[1:]]))

        except Exception as e:
            print(f"{type(e).__name__}: {e}\n  > {' '.join(tokens)}")
            return sys.exit(1)

    def execute_lines(self, lines: list) -> None:
        [self.execute(line) for line in lines]

    def run_section(self, section: str) -> Any:
        if section not in self.sections:
            raise SectionConflict(f"no such section: '{section}'!")

        self._sectiontrk.append(section)
        self._sectionrets.append(None)
        self.execute_lines(self.sections[section])
        self._sectiontrk.pop()
        retval = self._sectionrets.pop()
        return retval

# Handler
memory = XTMemory()
parser = XTParser(memory)
if not os.path.isfile(config["entrypoint"]):
    print("x2: no such file")
    sys.exit(1)

with open(config["entrypoint"], "r", encoding = "utf-8") as file:
    sections = parser.sectionize(parser.parse_lines(file.read()))

inter = XTInterpreter(memory, sections, {f: getattr(operators, f) for f in dir(operators) if callable(getattr(operators, f)) and not f[0] == "_"})
memory._parser, memory._inter = parser, inter
try:
    inter.run()

except KeyboardInterrupt:
    print("x2 exited: code 0")
