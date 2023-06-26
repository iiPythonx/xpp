# Copyright 2023 iiPython

# Modules
from typing import Any
from xpp.core.datastore import Memory

# Minimal datastore class
class Datastore(object):
    def __init__(self, mem: Memory, raw: Any) -> None:
        self.mem, self.raw, self.id_ = mem, str(raw), str(raw).lstrip("?")
        self.value = self.mem.variables.get(self.id_) if isinstance(raw, tuple) else raw

    def set(self, value: Any) -> None:
        self.mem.variables[self.id_] = value
        self.value = value

    def delete(self) -> None:
        if self.id_ in self.mem.variables:
            del self.mem.variables[self.id_]
