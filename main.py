# Copyright 2022 iiPython
# x2.2b3 Codename Lightspeed

# Modules
import os
import re
import sys
import json
import string
from typing import Any

# Initialization
__version__ = "x2.2b3"

sys.argv = sys.argv[1:]
xt_folder = os.path.join(os.path.dirname(__file__), "x2")

if "-h" in sys.argv or "--help" in sys.argv:
    print("usage: x2 [-h] [file]\nflags:\n    -h  shows this message and exits\n\nif path is '.', tries to load entrypoint from .xtconfig")
    sys.exit(0)

# Load x2 operators
try:
    from importlib.util import (
        spec_from_file_location, module_from_spec
    )

    def load_module(path: str) -> None:
        spec = spec_from_file_location(f"x2.{path[:-3]}", os.path.join(xt_folder, path))
        module = module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    opmap = load_module("__init__.py").__opmap

except Exception as e:
    opmap = {}
    print(f"[WARN] x2: failed to load builtin operators ({type(e).__name__})")

# Load x2 configuration
config = {}
if os.path.isfile(".xtconfig"):
    with open(".xtconfig", "r") as f:
        config = json.loads(f.read())

# Exceptions
class UnknownOperator(Exception):
    pass

class InvalidSection(Exception):
    pass

class IllegalSectionName(Exception):
    pass

# x2 Memory Handlers
class XTMemory(object):
    def __init__(self) -> None:
        self.vars = {}

class XTDatastore(object):
    def __init__(self, mem: XTMemory, raw: str) -> None:
        self.mem = mem
        self.raw = raw
        self.flags = []

        self.refresh()

    def __repr__(self) -> str:
        return f"<XTDS val={repr(self.value)}>"

    def _parse(self) -> Any:
        if len(self.raw) > 1 and self.raw[0] == "\"" and self.raw[-1] == "\"":
            value = self.raw[1:][:-1].replace("\\\"", "\"")
            for item in re.findall(re.compile(r"\$\([^)]*\)"), value):
                result = self.mem.interpreter.execute(item[2:][:-1])
                value = value.replace(item, str(result if result is not None else ""))

            return value.encode("latin-1", "backslashreplace").decode("unicode-escape")  # String literal

        # Integer/float literal
        for check in [int, float]:
            try:
                return check(self.raw)

            except ValueError:
                pass

        # Provided variable
        self.flags.append("var")
        return self.mem.vars.get(self.raw)

    def set(self, value: str) -> Any:
        self.value = value
        if "var" in self.flags:
            self.mem.vars[self.raw] = value

        return value

    def refresh(self) -> None:
        self.value = self._parse()

class XTContext(object):
    def __init__(self, memory: XTMemory, args: list) -> None:
        self.memory = memory
        self.args = [XTDatastore(memory, a) for a in args]

    def __repr__(self) -> str:
        return f"<XTCTX Arguments={repr(self.args)}>"

# x2 Interpreter
class XTInterpreter(object):
    def __init__(self, opmap: dict = {}) -> None:

        # Memory initialization
        self.memory = XTMemory()
        self.memory.interpreter = self

        self.linetrk = []
        self.sections = {}

        self._opmap = opmap
        self._live = False

    def execute(self, line: str) -> Any:
        try:
            tokens = self.parseline(line)
            operator = tokens[0]
            if operator not in self._opmap:
                raise UnknownOperator(operator)

            return self._opmap[operator](XTContext(self.memory, tokens[1:]))

        except Exception as e:
            print("Exception occured in x2 thread!")
            for tracker in self.linetrk:
                line = self.sections[tracker[1]]["lines"][tracker[2] - self.sections[tracker[1]]["start"] - 1].lstrip()
                print(f"{tracker[0]} line {tracker[2]}, in {tracker[1].split('.')[1]}:\n  > {line}")

            print(f"\n{type(e).__name__}: {e}")
            if not self._live:
                os._exit(1)

    def parseline(self, line: str) -> list:
        data = {"val": "", "qt": False, "line": []}
        for idx, char in enumerate(line):
            if char == " " and not data["qt"]:
                if not data["val"]:
                    continue

                data["line"].append(data["val"])
                data["val"] = ""

            elif char == "\"" and (idx > 0 and line[idx - 1] != "\\"):  # Enables quoting with backslash
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
        return data["line"]

    def load_sections(self, code: str, filename: str, namespace: str = None, external: bool = False) -> None:
        if not hasattr(self, "_entrypoint"):
            self._entrypoint = filename

        fileid = (namespace or filename).removesuffix(".xt")
        dt = {
            "active": "global",
            "code": [],
            "sections": {f"{fileid}.global": {"lines": [], "file": filename, "start": 0, "args": [], "ret": None, "as": fileid}}
        }
        for lno, line in enumerate(code.split("\n")):
            if line.strip():
                if line[0] == ":" and line[:2] != "::":
                    ns, sid = f"{fileid}.{dt['active']}", line[1:].split(" ")[0]
                    if [c for c in sid if c not in string.ascii_letters + string.digits + "_"]:
                        raise IllegalSectionName(f"section '{sid}' contains invalid characters")

                    elif "_" in sid and sid[0] != "_":
                        raise IllegalSectionName("section names can only begin with a underscore if they contain one")

                    dt["sections"][ns]["lines"] = dt["code"]
                    dt["sections"][f"{fileid}.{sid}"] = {
                        "file": filename, "start": lno + 1, "lines": [],
                        "args": line.split(" ")[1:], "ret": None, "as": fileid
                    }
                    dt["code"] = []
                    dt["active"] = sid
                    continue

            dt["code"].append(line.lstrip())

        if dt["code"]:
            dt["sections"][f"{fileid}.{dt['active']}"]["lines"] = dt["code"]

        self.sections = {**self.sections, **dt["sections"]}
        if external:
            self.run_section(f"{fileid}.global")
            del self.sections[f"{fileid}.global"]  # Save memory

    def run_section(self, section: str) -> Any:
        current_file = (self.linetrk or [(self._entrypoint,)])[-1][-1].removesuffix(".xt")
        if "." not in section:
            section = f"{current_file}.{section}"

        if section not in self.sections:
            raise InvalidSection(section)

        secdata = section.split(".")
        if secdata[1][0] == "_" and secdata[0] != current_file:
            raise InvalidSection(f"{secdata[1]} is a private section and cannot be called")

        s = self.sections[section]
        self.linetrk.append([s["file"], section, s["start"], False, s["as"]])
        for line in s["lines"]:
            self.linetrk[-1][2] += 1
            if line.strip() and line[:2] != "::":
                self.execute(line)
                if self.linetrk[-1][3]:
                    break

        self.linetrk.pop()
        return s["ret"]

# Handler
inter = XTInterpreter(opmap)
if not sys.argv:
    print(f"{__version__} Copyright (c) 2022 iiPython")
    inter._live, linedata = True, ""
    inter.load_sections(":global\n", "<stdin>")
    while True:
        try:
            line = input(f"{'>' if not linedata else ':'} ")
            if line[:2] == "::":
                continue

            elif not line.strip():
                continue

            elif linedata and not line.strip():
                inter.load_sections(linedata, "<stdin>")
                linedata = ""

            elif line[0] == ":" and line[:2] != "::":
                linedata = line + "\n"

            elif linedata:
                linedata += line + "\n"

            else:
                inter.execute(line)

        except KeyboardInterrupt:
            os._exit(0)

else:
    file = sys.argv[0]
    if file == ".":
        file = config.get("entrypoint", "main.xt")

    try:
        with open(file, "r", encoding = "utf-8") as f:
            code = f.read()

    except Exception:
        print("x2: failed to load file")
        os._exit(1)

    inter.load_sections(code, file.replace("\\", "/").split("/")[-1])
    [inter.run_section(s) for s in ["global", "main"]]
