# Copyright 2022 iiPython

# Modules
from ..exceptions import InvalidSyntax

# Block handler
block_starts = ["(", "\"", "'"]
block_ends = [")", "\"", "'"]

# Tokenizer
def tokenize(line: str) -> list:
    dt = {"mode": None, "depth": 0, "val": [], "tokens": []}
    for block in line.split(" "):
        dt["val"].append(block)
        if block[0] in block_starts:
            if not dt["depth"]:
                dt["mode"] = block[0]

            if block[0] == dt["mode"]:
                dt["depth"] += 1

        elif dt["mode"] is not None and block[-1] == block_ends[block_starts.index(dt["mode"])]:
            if dt["depth"] > 1:
                dt["depth"] -= 1

            else:
                dt["mode"], dt["depth"] = None, 0
                dt["tokens"].append(" ".join(dt["val"]))
                dt["val"] = []

        elif dt["mode"] is None:
            dt["val"] = []
            dt["tokens"].append(block)

    if dt["val"]:
        closing_tag = block_ends[block_starts.index(dt["mode"])]
        if not dt["val"][-1].endswith(closing_tag):
            raise InvalidSyntax(f"expected a closing '{closing_tag}', found nothing")

        dt["tokens"].append(" ".join(dt["val"]))
        dt["val"] = []

    return dt["tokens"]
