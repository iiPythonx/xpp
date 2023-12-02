# Copyright 2022-2024 iiPython

# Modules
import os
from typing import Any, List

from .sections import Section
from .tokenizer import tokenize
from .datastore import Memory, Datastore
from ..exceptions import (
    XPPException, MiscError, UnknownSection,
    UnknownOperator, MissingParameter
)
from ..modules.ops import opmap

# Interpreter class
class Interpreter(object):
    def __init__(self, entrypoint: str, sections: list, **kwargs) -> None:
        self.entrypoint = entrypoint.split(os.sep)[-1].removesuffix(".xpp")
        self.sections = sections

        self.stack, self.memory = [], Memory(**{"interpreter": self} | kwargs)
        self.operators = opmap

    def execute(self, line: str) -> Any:
        tokens = tokenize(line)
        if tokens[0] not in self.operators:
            raise UnknownOperator(tokens[0], index = range(0, len(tokens[0])))

        # Create datastores
        datastores = []
        for i, t in enumerate(tokens[1:]):
            try:
                datastores.append(Datastore(self.memory, t))

            except Exception as e:
                length = sum([len(t) + 1 for t in tokens[:i + 1]])

                # Ensure parenthesis aren't highlighted
                if t[0] == "(":
                    length, t = length + 1, t[:-2]  # -2 instead of -1 to bypass the length addition

                # Set the exception index
                if not isinstance(e, XPPException):
                    raise MiscError(str(e), index = range(length, length + len(t)))

                e.index = range(length, length + len(t))
                raise e

        return self.operators[tokens[0]](self.memory, datastores)

    def find_section(self, section: str) -> str:
        if "." not in section:
            file = self.stack[-1].path.split(os.sep)[-1].removesuffix(".xpp") if self.stack else self.entrypoint
            section = f"{file}.{section}"

        if section not in [s["sid"] for s in self.sections]:
            raise UnknownSection(f"no such section: '{section}'")

        return section

    def run_section(self, section: str, args: List[Datastore] = []) -> List[Any]:
        section = Section(**[s for s in self.sections if s["sid"] == self.find_section(section)][0])
        section.initialize(self.memory)
        self.stack.append(section)
        try:
            for i, a in enumerate(section.args):
                self.memory.variables["scope"][section.sid][a] = args[i]

        except IndexError:
            raise MissingParameter(f"'{section.sid}' requires argument '{a}' which was not provided")

        for line in section.lines:
            section.line_content = line
            if not section.active:
                break

            elif isinstance(line, int):  # This is whitespace
                section.current_line += line
                continue

            self.execute(line)
            section.current_line += 1

        self.stack.pop()
        return section.trash()
