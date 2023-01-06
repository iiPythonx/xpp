# Copyright 2022-2023 iiPython

# Modules
import sys
from typing import Any, List

from .sections import Section
from .tokenizer import tokenize
from .datastore import Memory, Datastore
from ..exceptions import UnknownSection, UnknownOperator, MissingParameter

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

    def run_section(self, section: str, args: List[Datastore] = []) -> Any:
        section = Section(**[s for s in self.sections if s["sid"] == self.find_section(section)][0])
        section.initialize(self.memory)
        self.stack.append(section)
        try:
            for i, a in enumerate(section.args):
                self.memory.variables["scope"][section.sid][a] = args[i]

            if (len(args) > len(section.args)) and not self.memory.cli_vals["no-extra-params-warn"]:
                print(f"[WARN]: Section {section.sid} takes {len(section.args)} arguments and was given {len(args)}")

        except IndexError:
            raise MissingParameter(f"'{section.sid}' requires argument '{a}' which was not provided")

        for line in section.lines:
            if not line.strip() or line[:2] == "::":
                section.current_line += 1
                continue

            self.execute(line)
            section.current_line += 1

        self.stack.pop()
        return section.trash()
