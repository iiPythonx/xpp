# Copyright 2022-2024 iiPython

# Modules
import json
from ..exceptions import InvalidSyntax

# Block handler
block_starts = ["(", "\"", "'", "{"]
block_ends = [")", "\"", "'", "}"]

# Tokenizer
def tokenize(line: str) -> list:
    dt = {"mode": None, "depth": 0, "val": "", "tokens": []}
    for char in line:
        dt["val"] += char
        if dt["mode"] is not None and char == block_ends[block_starts.index(dt["mode"])]:
            if dt["depth"] > 1:
                dt["depth"] -= 1

            else:
                if char == block_ends[0]:
                    dt["tokens"].append(dt["val"])
                    dt["val"] = ""

                dt["mode"] = None
                dt["depth"] = 0

        elif char in block_starts:
            if not dt["depth"]:
                dt["mode"] = char

            if char == dt["mode"]:
                dt["depth"] += 1

        elif dt["mode"] is None and char == " ":
            if dt["val"] == char:
                dt["val"] = ""
                continue  # Skip the space, it's just a seperator

            dt["val"] = dt["val"][:-1]  # :-1 to account for space
            if dt["val"] == "::":
                dt["val"] = ""
                break  # This is an in-line comment

            dt["tokens"].append(dt["val"])
            dt["val"] = ""

    if dt["val"]:
        if dt["mode"] is not None:
            closing_tag = block_ends[block_starts.index(dt["mode"])]
            if not dt["val"][-1].endswith(closing_tag):
                raise InvalidSyntax(f"expected a closing '{closing_tag}', found nothing.")

        dt["tokens"].append(dt["val"])
        dt["val"] = ""

    if dt["depth"] > 0:
        raise InvalidSyntax(f"unexpected depth value after tokenizing, did you close all open blocks?\nRaw token information: {json.dumps(dt, indent = 4)}")

    return dt["tokens"]
