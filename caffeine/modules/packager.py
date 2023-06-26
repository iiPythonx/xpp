# Copyright 2023 iiPython

# Modules
import logging
from json import dumps

from .optimize import is_literal, string_block_starts
from .analysis import FlowTree

# package_tree
def package_tree(tree: FlowTree) -> str:
    new_tree = []
    for obj in tree:
        obj = list(obj)
        for idx, item in enumerate(obj[1:]):
            if isinstance(item, str):
                if item[0] == "(":
                    logging.error("caffeine does not support in-line execution")

                elif not is_literal(item):
                    obj[idx + 1] = (item,)
                    continue

                # Handle strings
                elif item[0] in string_block_starts:
                    obj[idx + 1] = item.strip("".join(string_block_starts))
                    continue

            # Handle floats/integers
            item = float(item)
            if item.is_integer():
                item = int(item)

            obj[idx + 1] = item

        new_tree.append(tuple([obj[0].__name__, *obj[1:]]))

    return dumps(new_tree, separators = (",", ""))
