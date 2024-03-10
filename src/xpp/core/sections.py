# Copyright 2022-2024 iiPython

# Modules
import os
from typing import Any

from .datastore import Memory
from ..exceptions import SectionConflict, InvalidSection, InvalidSyntax

# Section class
class Section(object):
    """
    x++ Section Class
    Holds all section data: id, path, lines, etc.
    """
    def __init__(self, sid: str, path: str, lines: list, start: int, args: list) -> None:
        self.active = True
        self.sid = sid
        self.path = os.path.abspath(path)
        self.lines = lines
        self.start = start
        self.args = args

        self.return_value = [None]
        self.current_line = sum([i if isinstance(i, int) else 1 for i in lines]) + start - 1
        self.line_content = lines[-1] if lines else ""

    def __repr__(self) -> str:
        return f"<Section ID='{self.sid}' SourcePath='{self.path}' StartLine={self.start}>"

    def initialize(self, mem: Memory) -> None:
        self._mem = mem
        if self.path not in self._mem.variables["file"]:
            self._mem.variables["file"][self.path] = {}

        self._mem.variables["scope"][self.sid] = {}
        self.current_line = self.start

    def trash(self) -> Any:
        if self.path in self._mem.variables["file"]:

            # Check that this is the last running scope in our file before garbage collecting
            ns = self.path.replace("\\", "/").split("/")[-1].removesuffix(".xpp")
            if [s for s in self._mem.variables["scope"] if s.split(".")[0] == ns] == [self.sid]:
                del self._mem.variables["file"][self.path]

        if self.sid in self._mem.variables["scope"]:
            del self._mem.variables["scope"][self.sid]

        return self.return_value

# Section loader
def load_sections(source: str, filepath: str, namespace: str = None) -> list:
    """
    Takes an x++ source file and breaks it into a list of sections.
    """

    # Calculate file name
    filename = namespace or filepath.split(os.sep)[-1].removesuffix(".xpp")

    # Initialization
    data = {"sections": [{"sid": f"{filename}.main", "path": filepath, "lines": [], "start": 1, "args": []}], "active": 0}

    # Split sections
    lines = source.splitlines()
    lcn = len(lines)
    for lno, line in enumerate(lines):
        def process_whitespace(lines: list) -> None:
            if lines and isinstance(lines[-1], int):
                lines[-1] += 1

            else:
                lines.append(1)

        line, lines = line.strip(), data["sections"][data["active"]]["lines"]
        if (not line) or (line[:2] == "::"):
            process_whitespace(lines)
            continue

        elif line[0] == ":":
            sp = line.split(" ")
            sid = f"{filename}.{sp[0][1:]}"
            if sid in [s["sid"] for s in data["sections"]]:
                raise SectionConflict(f"section '{sid}' is already registered!")

            elif (len(data["sections"]) > 1) and (data["sections"][-1]["lines"][-1].split(" ")[0] != "ret"):
                raise InvalidSection(
                    f"section '{data['sections'][-1]['sid']}' is missing a return statement!",
                    stack = [Section(**data["sections"][-1])]
                )

            data["sections"].append({"sid": sid, "path": filepath, "lines": [], "start": lno + 2, "args": sp[1:]})
            data["active"] = len(data["sections"]) - 1
            continue

        else:
            lines = data["sections"][data["active"]]["lines"]
            if (line[-1] == "\\") and (lno == (lcn - 1)):
                lines.append(line)
                raise InvalidSyntax(
                    "multiline statement found, but this is the last line!",
                    stack = [Section(**data["sections"][-1])],
                    index = len(line) - 1
                )

            elif lines:
                index = -1 if (not isinstance(lines[-1], int)) or (len(lines) < 2) else -2
                if isinstance(lines[index], str) and lines[index][-1] == "\\":
                    lines[index] = lines[index][:-1] + line
                    process_whitespace(lines)
                    continue

            lines.append(line)
            if line.split(" ")[0] == "ret":
                data["active"] = 0

    if data["active"] > 0:
        raise InvalidSection(
            f"section '{data['sections'][-1]['sid']}' is missing a return statement!",
            stack = [Section(**data["sections"][-1])]
        )

    return data["sections"]
