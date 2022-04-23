# Copyright 2022 iiPython

# Modules
import os
import sys
from x2 import (
    load_sections, load_cli, config,
    Interpreter
)

# Initialization
cli = load_cli()  # Render CLI

# Load filepath
filepath = cli.filepath
if filepath is None:
    cli.show_help()

elif filepath == ".":
    filepath = config.get("main", "main.x2")

if not os.path.isfile(filepath):
    sys.exit("x2 Exception: no such file")

# Load file content
with open(filepath, "r") as f:
    data = f.read()

# Run file
sections = load_sections(data, filepath)
interpreter = Interpreter(
    filepath, sections,
    config = config,
    cli_vals = cli.vals
)
interpreter.run_section("main")
