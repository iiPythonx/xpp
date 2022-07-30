# Copyright 2022 iiPython

# Modules
import sys
from typing import Any

from .sections import Section
from .tokenizer import tokenize
from .datastore import Memory, Datastore
from ..exceptions import UnknownSection, UnknownOperator

from ..modules.ops import opmap

# Context class
class Context(object):
    def __init__(self, args: list, mem: Memory) -> None:
        self.args, self.mem = args, mem

# Interpreter class
class Interpreter(object):
    def __init__(self, entrypoint: str, sections: list, **kwargs) -> None:
        self.entrypoint = entrypoint.replace("\\", "/").split("/")[-1].removesuffix(".x2")
        self.sections = sections

        self.stack, self.memory = [], Memory(**{"interpreter": self} | kwargs)
        self.operators = opmap

    def execute(self, line: str) -> Any:
        try:
            tokens = tokenize(line)
            if tokens[0] not in self.operators:
                raise UnknownOperator(tokens[0])

            return self.operators[tokens[0]](Context([Datastore(self.memory, t) for t in tokens[1:]], self.memory))

        except Exception as e:
            if isinstance(e, RecursionError):
                e = OverflowError("x2 overflow error")

            if len(self.stack) > 10:
                print(f"... last {len(self.stack) - 10} stack entries ommitted")

            for s in self.stack[-10:]:
                print(f"x2 file {s.path} in {s.sid} on line {s.current_line}:")
                print(f"  > {s.lines[s.current_line - s.start]}\n")

            print(f"{type(e).__name__}: {e}")
            if "-D" in sys.argv:
                print("\nPython traceback:")
                raise e

            return exit(1)

    def find_section(self, section: str) -> str:
        if "." not in section:
            file = self.stack[-1].path.split("/")[-1].removesuffix(".x2") if self.stack else self.entrypoint
            section = f"{file}.{section}"

        if section not in [s["sid"] for s in self.sections]:
            raise UnknownSection(f"no such section: '{section}'")

        return section

    def run_section(self, section: str) -> Any:
        section = Section(**[s for s in self.sections if s["sid"] == self.find_section(section)][0])
        section.initialize(self.memory)
        self.stack.append(section)
        for line in section.lines:
            if not line.strip() or line[:2] == "::":
                section.current_line += 1
                continue

            self.execute(line)
            section.current_line += 1

        self.stack.pop()
        return section.trash()
