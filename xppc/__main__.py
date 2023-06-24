# Copyright 2023 iiPython

# Modules
import os
import sys
import json
import pathlib
from typing import List, Tuple

from xpp import load_sections
from xpp.core.tokenizer import tokenize
from xpp.core.datastore import Memory, Datastore
from xpp.modules.ops.stdlib.import_ import XOperators as imp_

# Initialization
imp = imp_.imp
args, usage = sys.argv[1:], "xppc - the x++ compiler\n" +\
                            f"usage: {sys.executable} -m xppc [-p] [-r] [-j] <source file.xpp> [output file.xppc/py]\n\n" +\
                            "copyright (c) 2023 iiPython"

# Load the input file
infile = None
for i in args:
    if i[0] != "-":
        infile = i
        break

if infile is None:
    exit(usage)

# Sanity checks
fp, of = pathlib.Path(infile), pathlib.Path("out")
if not fp.is_file():
    exit("xppc: file does not exist")

elif args[-1] != infile:
    of = pathlib.Path(args[-1].split(".")[0])
    if of.is_dir():
        exit("xppc: cannot output to a directory")

# Load source content
with open(fp, "r") as fh:
    source = fh.read()

# Compile all sections
class Fakepath(object):
    def __init__(self) -> None:
        self.path = pathlib.Path(os.getcwd()) / infile

class FakeInterpreter(object):
    def __init__(self) -> None:
        self.sections = []
        self.stack = [Fakepath()]

    def run_section(*args, **kwargs) -> None:
        pass

class FakeDatastore(Datastore):
    def __init__(self, data: str) -> None:
        self.raw = data
        self.value = self._parse()

tempmem = Memory(interpreter = FakeInterpreter())
def process_lines(lines: List[str | int]) -> Tuple[List[str], List[dict]]:
    [lines.remove(ln) for ln in lines if not (isinstance(ln, str) and ln.strip())]
    tokenized_lines, sections = [tokenize(ln) for ln in lines], []
    for line in tokenized_lines:
        if line[0] != "imp":
            continue

        imp(tempmem, [FakeDatastore(t) for t in line[1:]])
        for sec in tempmem.interpreter.sections:
            if not [a for a in sec["lines"] if isinstance(a, str) and a.strip()]:
                continue

            sections.append(sec)

        tokenized_lines.remove(line)

    return tokenized_lines, sections

def find_sections(seclist: List[dict] = load_sections(source, fp.name)) -> dict:
    sections = {}
    for obj in seclist:
        lines, sec2 = process_lines(obj["lines"])
        sections[obj["sid"]] = {"l": lines, "a": obj["args"]}
        sections = sections | (find_sections(sec2) if sec2 else {})

    return sections

sections = find_sections() | {"ep": fp.name.split(".")[0]}

# Handle -p (print)
if "-p" in args:
    try:
        from rich import print as pprint

    except ImportError:
        from pprint import pprint

    pprint(sections)

# Handle -j (json)
dumped = json.dumps(sections, separators = (",", ":"))
if "-j" in args:
    with open(of.name + ".xppc", "w+") as fh:
        fh.write(dumped)

    exit()

# Construct normal Python file
with open(of.name + ".py", "w+") as fh:
    fh.write(f"from xppc import Interpreter;d={dumped};ep=d['ep'];del d['ep'];i=Interpreter(ep,d);i.run_section('main')")

# Handle -r (run)
if "-r" in args:
    import subprocess
    subprocess.run([sys.executable, of.name + ".py"])
