# Copyright 2022 iiPython

# x2 Memory Handlers
class XTMemory(object):
    def __init__(self) -> None:
        self.vars = {"globals": {}, "file": {}, "local": {}}
