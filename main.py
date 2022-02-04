# Copyright 2022 iiPython
# x2.3b0 Codename Goos

# Modules
import os
import sys
import json
import string
from typing import Any, Tuple

from x2 import (
    opmap,
    XTMemory, XTDatastore, XTContext,
    UnknownOperator, InvalidSection, IllegalSectionName
)

# Initialization
__version__ = "x2.3b0"

sys.argv = sys.argv[1:]
xt_folder = os.path.join(os.path.dirname(__file__), "x2")

if "-h" in sys.argv or "--help" in sys.argv:
    print("usage: x2 [-h] [file]\nflags:\n    -h  shows this message and exits\n\nif path is '.', tries to load entrypoint from .xtconfig")
    sys.exit(0)

# Load x2 configuration
config = {}
if os.path.isfile(".xtconfig"):
    with open(".xtconfig", "r") as f:
        config = json.loads(f.read())

# x2 Interpreter
class XTInterpreter(object):
    def __init__(self, opmap: dict = {}) -> None:

        # Memory initialization
        self.memory = XTMemory()
        self.memory.interpreter = self

        self.linetrk = []
        self.sections = {}

        self._live = False
        self._opmap = opmap

        # Data attributes
        self._config = config
        self._version = __version__

    def setvar(self, name: str, value: Any, **kwargs) -> Any:
        return XTDatastore(self.memory, name, **kwargs).set(value)

    def getvar(self, name: str) -> XTDatastore:
        return XTDatastore(self.memory, name)

    def execute(self, line: str, raise_error: bool = False) -> Any:
        try:
            tokens = self.parseline(line)
            try:
                trkdata = self.linetrk[-1]
                prevline = self.sections[trkdata[1]]["lines"][trkdata[2] - self.sections[trkdata[1]]["start"] - 2]
                if prevline[-2:] in [" \\", ".."]:
                    return None

            except IndexError:
                pass

            operator = tokens[0]
            if operator not in self._opmap:
                raise UnknownOperator(operator)

            return self._opmap[operator](XTContext(self.memory, tokens[1:]))

        except Exception as e:
            if raise_error or True:
                raise e

            elif config.get("quiet", False):
                return None

            print("Exception occured in x2 thread!")
            for tracker in self.linetrk:
                line = self.sections[tracker[1]]["lines"][tracker[2] - self.sections[tracker[1]]["start"] - 1].lstrip()
                print(f"{tracker[0]} line {tracker[2]}, in {tracker[1].split('.')[1]}:\n  > {line}")

            print(f"\n{type(e).__name__}: {e}")
            if not self._live:
                os._exit(1)

    def parseline(self, line: str, multiline_offset: int = 0) -> list:
        data = {"val": "", "flags": [], "expridx": 0, "line": []}
        for idx, char in enumerate(line):
            if char == ":" and "qt" not in data["flags"]:
                if idx != len(line) - 1 and line[idx + 1] == ":":
                    break

            if char == ")" and "expr" in data["flags"]:
                if data["expridx"] > 1:
                    data["val"] += ")"

                elif data["expridx"] == 1:
                    data["flags"].remove("expr")
                    data["line"].append(f"({data['val']})")
                    data["val"] = ""

                data["expridx"] -= 1

            elif char == "(" and "qt" not in data["flags"]:
                if "expr" not in data["flags"]:
                    data["flags"].append("expr")

                data["expridx"] += 1
                if data["expridx"] > 1:
                    data["val"] += "("

            elif "expr" in data["flags"]:
                data["val"] += char

            elif char == " " and "qt" not in data["flags"]:
                if not data["val"]:
                    continue

                data["line"].append(data["val"])
                data["val"] = ""

            elif char == "\"" and (line[idx - 1] != "\\" if idx > 0 else True):  # Enables quoting with backslash
                if "qt" in data["flags"]:
                    data["line"].append(data["val"] + "\"")
                    data["val"] = ""
                    data["flags"].remove("qt")

                else:
                    data["flags"].append("qt")
                    data["val"] += "\""

            else:
                data["val"] += char

        # Construct missing data
        if data["val"]:
            data["line"].append(data["val"])
            data["val"] = ""

        # Push lines
        if data["line"][-1] in ["\\", ".."]:
            trkdata = self.linetrk[-1]
            nextline = self.parseline(self.sections[trkdata[1]]["lines"][trkdata[2] - self.sections[trkdata[1]]["start"] + multiline_offset], multiline_offset + 1)
            if data["line"][-1] == "..":
                data["line"][-2], nextline = data["line"][-2][:-1] + "\n" + nextline[0][1:], nextline[1:]

            data["line"] = data["line"][:-1]
            data["line"] = data["line"] + nextline

        return data["line"]

    def load_sections(self, code: str, filename: str, namespace: str = None, external: bool = False) -> None:
        if not hasattr(self, "_entrypoint"):
            self._entrypoint = filename

        self.memory.vars["file"][filename] = {}

        fileid = (namespace or filename).removesuffix(".xt")
        dt = {
            "active": "global",
            "code": [],
            "sections": {f"{fileid}.global": {"lines": [], "priv": False, "file": filename, "start": 0, "args": [], "ret": None, "as": fileid}}
        }
        for lno, line in enumerate(code.split("\n")):
            if line.strip():
                if line[0] == ":" and line[:2] != "::":
                    ns, sid, priv = f"{fileid}.{dt['active']}", line[1:].split(" ")[0], False
                    if [c for c in sid if c not in string.ascii_letters + string.digits + "@"]:
                        raise IllegalSectionName(f"section '{sid}' contains invalid characters")

                    elif "@" in sid:
                        if sid[0] != "@":
                            raise IllegalSectionName("section name cannot contain a '@' unless it indicates a private section")

                        priv, sid = True, sid[1:]

                    dt["sections"][ns]["lines"] = dt["code"]
                    dt["sections"][f"{fileid}.{sid}"] = {
                        "file": filename, "start": lno + 1, "lines": [], "priv": priv,
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

    def find_section(self, section: str) -> Tuple[str, str]:
        current_file = (self.linetrk or [(self._entrypoint,)])[-1][-1].removesuffix(".xt")
        if "." not in section:
            section = f"{current_file}.{section}"

        if section not in self.sections:
            raise InvalidSection(section)

        return section, current_file

    def run_section(self, section: str) -> Any:
        section, current_file = self.find_section(section)
        secdata = section.split(".")
        s = self.sections[section]
        if s["priv"] and current_file + ".xt" != s["file"]:
            raise InvalidSection(f"{secdata[1]} is a private section and cannot be called")

        if section not in self.memory.vars["local"]:
            self.memory.vars["local"][section] = {}

        self.linetrk.append([s["file"], section, s["start"], False, s["as"]])
        for line in s["lines"]:
            self.linetrk[-1][2] += 1
            if line.strip() and line[:2] != "::":
                self.execute(line)
                if self.linetrk[-1][3]:
                    break

        del self.memory.vars["local"][section]

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

            elif linedata and not line.strip():
                inter.load_sections(linedata, "<stdin>")
                linedata = ""

            elif not line.strip():
                continue

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
        file = config.get("main", "main.xt")

    try:
        with open(file, "r", encoding = "utf-8") as f:
            code = f.read()

    except Exception:
        print("x2: failed to load file")
        os._exit(1)

    inter.load_sections(code, file.replace("\\", "/").split("/")[-1])
    [inter.run_section(s) for s in ["global", "main"]]
