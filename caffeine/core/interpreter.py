# Copyright 2023 iiPython

# Modules
from xpp.modules.ops import opmap
from xpp.core.datastore import Memory

from .datastore import Datastore
from ..modules.analysis import FlowTree

# Main interpreter class
class Interpreter(object):
    def __init__(self) -> None:
        self.mem = Memory()

    def run_tree(self, tree: FlowTree) -> None:
        for line in tree:
            opmap[line[0]](self.mem, [Datastore(self.mem, a) for a in line[1:]])
