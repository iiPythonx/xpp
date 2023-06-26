# Copyright 2023 iiPython

# Modules
from typing import Any
from xpp.core.datastore import Memory

# Minimal datastore class
class Datastore(object):
    def __init__(self, mem: Memory, raw: Any) -> None:
        self.raw = raw[0] if isinstance(raw, list) else str(raw)
        self.mem, self.id_ = mem, self.raw.lstrip("?")
        self.value = self.mem.variables.get(self.id_) if isinstance(raw, list) else self.raw

    def set(self, value: Any) -> None:
        self.mem.variables[self.id_] = value
        self.value = value

    def delete(self) -> None:
        if self.id_ in self.mem.variables:
            del self.mem.variables[self.id_]
