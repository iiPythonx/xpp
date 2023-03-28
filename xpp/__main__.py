# Copyright 2022-2023 iiPython

# Modules
import os
import sys
from . import (
    __version__,
    load_sections, config, Interpreter
)

# CLI class
class CLI(object):
    def __init__(self) -> None:
        self.argv, self.vals = sys.argv[1:], {}
        self.flags = [
            {"args": ["-nx100", "--no-extra-params-warn"], "name": "no-extra-params-warn", "desc": "Hide warning produced by giving a function too many arguments"}
        ]
        self.options = [
            {"args": ["-h", "--help"], "fn": self.show_help, "desc": "Displays the help menu"},
            {"args": ["-hl", "--helplong"], "fn": self.show_help_long, "desc": "Displays a more detailed help menu"},
            {"args": ["-v", "--ver", "--version"], "fn": self.show_version, "desc": "Prints the x++ version"},
            {"args": ["-i", "--installation"], "fn": self.show_install_path, "desc": "Prints the installation path"}
        ]

        self.usage = f"""x++ ({__version__}) Interpreter
(c) 2021-23 iiPython; (c) 2022-23 Dm123321_31mD "DmmD" Gaming

Usage:
    xpp [options] [flags] <file>
    File can be replaced by a dot ('.'), using the 'main' value of .xconfig instead

See '{sys.executable} {os.path.abspath(sys.argv[0])} -hl' for more detailed usage."""

        # Register flag values
        for flag in self.flags:
            self.vals[flag["name"]] = any([a in self.argv for a in flag["args"]])

        # Handle options
        for opt in self.options:
            if any([a in self.argv for a in opt["args"]]):
                opt["fn"]()

        # Load filepath
        self.filepath = None
        if self.argv:
            self.filepath = ([a for a in self.argv if a[0] != "-"] or [None])[-1]

    def show_help(self) -> None:
        return sys.exit(self.usage)

    def show_help_long(self) -> None:
        print("\n".join(self.usage.split("\n")[:-1]))
        print("Flags:")
        for flag in self.flags:
            print(f"  {', '.join(flag['args'])}\n    {flag['desc']}")

        print("\nOptions:")
        for opt in self.options:
            print(f"  {', '.join(opt['args'])}\n    {opt['desc']}")

        return sys.exit(0)

    def show_version(self) -> None:
        return sys.exit(__version__)

    def show_install_path(self) -> None:
        return sys.exit(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

# Initialization
cli = CLI()

# Load filepath
filepath = cli.filepath
if filepath is None:
    cli.show_help()

elif filepath == ".":
    filepath = config.get("main", "main.xpp")

if not os.path.isfile(filepath):
    sys.exit("x++ Exception: no such file")

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
