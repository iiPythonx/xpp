# Copyright 2023 iiPython

# Modules
import logging
from types import FunctionType
from typing import List, Tuple
from xpp.modules.ops import opmap
from xpp.core.tokenizer import tokenize
from xpp.core.sections import load_sections

from .xpp_import import do_import

# Initialization
FlowTree = List[Tuple[FunctionType, ...]]

class Globals(object):
    sections = []

# Handle converting lines into a flow tree
def construct_flow_tree(source: str) -> FlowTree:
    g = Globals()
    g.sections, tree = load_sections(source, ""), []
    def insert_line(line: str) -> None:  # noqa: E306
        if not isinstance(line, str):
            return  # Skip included whitespace tracking

        tokens = tokenize(line)
        if tokens[0] not in opmap:
            logging.error(f"x++ operator '{tokens[0]}' not found")

        # If a line is a jump statement, load the specified section,
        # process it, and append it to the flow tree.
        elif tokens[0] == "jmp":
            if not tokens[1:]:
                logging.error("attempted to jmp with no specified section")

            tokens[1] = tokens[1] if "." in tokens[1] else "." + tokens[1]
            section_results = [s for s in g.sections if s["sid"] == tokens[1]]
            if not section_results:
                logging.error(f"attempted to jmp to non-existant section '{tokens[1]}'")

            # Process section arguments (first)
            for arg_idx, arg_name in enumerate([t for t in tokens[2:] if t[0] != "?"]):
                arg_replace = section_results[0]["args"][arg_idx]
                insert_line(f"var {arg_replace} {arg_name}")

            # Append all other section lines (next)
            section_lines = section_results[0]["lines"]
            [insert_line(ln) for ln in section_lines[:-1]]

            # Process return arguments (last)
            return_tokens = tokenize(section_lines[-1])
            if return_tokens[0] != "ret":
                logging.error(f"section '{tokens[1]}' ended without calling ret")

            for arg_idx, ret_arg in enumerate([t for t in tokens[2:] if t[0] == "?"]):
                arg_replace = return_tokens[arg_idx + 1]
                insert_line(f"var {ret_arg.lstrip('?')} {arg_replace}")

            return

        # If a line in an import statement, load the sections from
        # the specified file, and substitute where neccessary.
        elif tokens[0] == "imp":
            tkl = len(tokens)
            if tkl == 3:
                return logging.warn(f"provided '{tokens[2]}' to imp without providing an argument")

            path, namespace = tokens[1], tokens[3] if (tkl == 4 and tokens[2] == "as") else None

            # Merge sections with current list
            g.sections += do_import(path.strip("\"'"), namespace.strip("\"'"))
            return

        # Append the line to the tree
        tree.append((opmap[tokens[0]], *tokens[1:]))

    # Load the main section
    [insert_line(line) for line in g.sections[0]["lines"]]
    return tree
