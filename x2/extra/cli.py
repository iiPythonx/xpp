# Copyright 2022-2023 iiPython

# Modules
import os
import sys
from .. import __version__

# CLI class
class CLI(object):
    def __init__(self) -> None:
        self.argv, self.vals = sys.argv[1:], {}
        self.flags = [
            {"args": ["-c", "--color"], "name": "color", "desc": "Colorize the print function where applicable"}
        ]
        self.options = [
            {"args": ["-h", "--help"], "fn": self.show_help, "desc": "Displays the help menu"},
            {"args": ["-hl", "--helplong"], "fn": self.show_help_long, "desc": "Displays a more detailed help menu"},
            {"args": ["-v", "--ver", "--version"], "fn": self.show_version, "desc": "Prints the x2 version"},
            {"args": ["-i", "--installation"], "fn": self.show_install_path, "desc": "Prints the installation path"}
        ]

        self.usage = f"""{__version__} Interpreter
(c) 2021-23 iiPython; (c) 2022-23 Dm123321_31mD "DmmD" Gaming

Usage:
    x2 [options] [flags] <file>
    File can be replaced by a dot ('.'), using the 'main' value of .x2config instead

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
