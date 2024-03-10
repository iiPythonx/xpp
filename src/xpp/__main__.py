# Copyright 2022-2024 iiPython

# Modules
import os
import sys
import json
from . import (
    __version__,
    load_sections, config, Interpreter
)

# CLI class
class CLI(object):
    def __init__(self) -> None:
        self.argv, self.vals = sys.argv[1:], {}
        self.options = [
            {"args": ["-h", "--help"], "fn": self.show_help, "desc": "Displays the help menu"},
            {"args": ["-hl", "--helplong"], "fn": self.show_help_long, "desc": "Displays a more detailed help menu"},
            {"args": ["-v", "--ver", "--version"], "fn": self.show_version, "desc": "Prints the x++ version"},
            {"args": ["-i", "--installation"], "fn": self.show_install_path, "desc": "Prints the installation path"},
            {"args": ["-s", "--show"], "fn": self.show_module, "desc": "Provides information about an installed x++ module"}
        ]
        self.install_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))

        self.usage = f"""x++ (x{__version__}) Interpreter
(c) 2021-24 iiPython; (c) 2022-23 Dm123321_31mD "DmmD" Gaming

Usage:
    xpp [options] [flags] <file>
    File can be replaced by a dot ('.'), using the 'main' value of .xconfig instead

See '{sys.executable} -m xpp -hl' for more detailed usage."""

        # Load filepath
        self.filepath = None
        if self.argv:
            self.filepath = ([a for a in self.argv if a[0] != "-"] or [None])[-1]

        # Handle options
        for opt in self.options:
            if any([a in self.argv for a in opt["args"]]):
                opt["fn"]()

    def show_help(self) -> None:
        print(self.usage)
        return sys.exit(0)

    def show_help_long(self) -> None:
        print("\n".join(self.usage.split("\n")[:-1]))
        print("\nOptions:")
        for opt in self.options:
            print(f"  {', '.join(opt['args'])}\n    {opt['desc']}")

        return sys.exit(0)

    def show_version(self) -> None:
        return sys.exit(__version__)

    def show_install_path(self) -> None:
        return sys.exit(self.install_path)

    def show_module(self) -> None:
        if self.filepath is None:
            return exit("usage: xpp -s <module>")

        module_path = os.path.join(self.install_path, "pkgs", self.filepath.replace(".", os.sep))
        if not os.path.isdir(module_path):
            return exit("no such module: " + self.filepath)

        # Load .xconfig
        xconfig = os.path.join(module_path, ".xconfig")
        if not os.path.isfile(xconfig) and "." in self.filepath:
            xconfig = os.path.join(self.install_path, "pkgs", self.filepath.split(".")[-1], ".xconfig")

        metadata = {}
        if os.path.isfile(xconfig):
            with open(xconfig, "r") as fh:
                metadata = json.loads(fh.read())

        # Print out information
        exit(f"""Name: {self.filepath}
Version: {metadata.get('version', 'N/A')}
Summary: {metadata.get('summary', 'N/A')}
Author: {metadata.get('author', 'N/A')}
License: {metadata.get('license', 'N/A')}
Location: {module_path}""")

# Initialization
cli = CLI()

# Main handler
def main() -> None:

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
    from .exceptions import handle_exception
    interpreter = Interpreter(filepath, [], config = config)
    try:
        interpreter.sections = load_sections(data, filepath)
        interpreter.run_section("main")

    except Exception as e:
        handle_exception(e, interpreter.stack)

if __name__ == "__main__":  # Don't run twice from setup.py import
    main()
