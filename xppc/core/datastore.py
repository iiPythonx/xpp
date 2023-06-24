# Copyright 2023 iiPython

# Modules
from xpp.core.datastore import Memory, Datastore as XDatastore

# Custom datastore class
class Datastore(XDatastore):
    def __init__(self, sec: str, mem: Memory, raw: str) -> None:
        self.mem, self.raw, self.id_ = mem, raw, raw.lstrip("@?")
        self.store = self.mem.variables["file"][sec.sid.split(".")[0]] if self.raw[0] == "@" else self.mem.variables["scope"][sec.sid]
        self.last_stack = sec
        if not raw:
            self._parse = lambda: None
        self.refresh()
