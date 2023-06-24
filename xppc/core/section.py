# Copyright 2023 iiPython

# Modules
from xpp.core.datastore import Memory
from xpp.core.sections import Section as XSection

# Main class
class Section(XSection):
    def __init__(self, sid: str, l: list, a: list) -> None:  # noqa
        self.active = True
        self.sid = sid
        self.lines = l
        self.args = a
        self.path = sid.split(".")[0]
        self.return_value = [None]

    def __repr__(self) -> str:
        return self.sid

    def initialize(self, mem: Memory) -> None:
        self._mem = mem
        if self.path not in self._mem.variables["file"]:
            self._mem.variables["file"][self.path] = {}

        self._mem.variables["scope"][self.sid] = {}
