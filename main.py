# Copyright 2022-2023 iiPython

# Modules
import os
import sys
from xpp import (
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
    filepath = config.get("main", "main.xpp")

if not os.path.isfile(filepath):
    sys.exit("X++ Exception: no such file")

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
