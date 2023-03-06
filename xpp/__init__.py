# Copyright 2022-2023 iiPython

__version__ = "x2.3r1"

from .extra.config import config
from .core.sections import load_sections
from .core.interpreter import Interpreter

# Handle CLI
def load_cli():
    from .extra.cli import CLI
    return CLI()
