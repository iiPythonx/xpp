# Copyright 2023 iiPython

# Modules
from typing import Any, List
from xpp import Interpreter as XInterpreter
from xpp.core.tokenizer import tokenize

from .section import Section
from .datastore import Datastore

# Initialization
class Interpreter(XInterpreter):
    def execute(self, tokens: List[str] | str, section: Section = None) -> Any:
        if isinstance(tokens, str):
            tokens = tokenize(tokens)

        return self.operators[tokens[0]](
            self.memory,
            [Datastore(section or self.stack[-1], self.memory, t) for t in tokens[1:]]
        )

    def run_section(self, section: str, args: List[Datastore] = []) -> List[Any]:
        sid = section if "." in section else self.entrypoint + "." + section
        section = Section(sid = sid, **self.sections[sid])
        section.initialize(self.memory)
        self.stack.append(section)
        for i, a in enumerate(section.args):
            self.memory.variables["scope"][section.sid][a] = args[i]

        for line in section.lines:
            if not section.active:
                break

            self.execute(line, section)

        self.stack.pop()
        return section.trash()
