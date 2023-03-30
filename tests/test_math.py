# Copyright 2023 iiPython

# Modules
import sys
import pathlib
sys.path.insert(1, str(pathlib.Path(__file__).parent.parent.resolve()))

# Start testing
from tests import start_tests
start_tests([

    # Addition testing
    ("add 2 3", 5),
    ("add 0.1 0.2", .1 + .2),
    ("add 0.25 (add 1 0.5)", 1.75),
    ("add 2 (8 + 10)", 20),
    ("add 1 (.1 + .2 + .3 + .4)", 2),
    ("add (7 + 4 + (2 + (5 + 2))) (8 + 9 + 2)", 39),

    # Subtraction testing
    ("sub 2 3", -1),
    ("sub 0.1 0.2", -.1),
    ("sub 0.25 (sub 1 0.5)", -.25),
    ("sub 2 (8 - 10)", 4),
    ("sub 1 (.1 - .2 - .3 - .4)", 1.8),
    ("sub (7 - 4 - (2 - (5 - 2))) (8 - 9 - 2)", 7),

    # Multiplication testing
    ("mul 2 3", 6),
    ("mul 0.1 0.2", .1 * .2),
    ("mul 0.25 (mul 1 0.5)", .125),
    ("mul 2 (8 * 10)", 160),
    ("mul 1 (.1 * .2 * .3 * .4)", .1 * .2 * .3 * .4),
    ("mul (7 * 4 * (2 * (5 * 2))) (8 * 9 * 2)", 80640),

    # Division testing
    ("div 2 3", 2 / 3),
    ("div 0.1 0.2", .1 / .2),
    ("div 0.25 (div 1 0.5)", .125),
    ("div 2 (8 / 10)", 2.5),
    ("div 1 (.1 / .2 / .3 / .4)", .24),
    ("div (7 / 4 / (2 / (5 / 2))) (8 / 9 / 2)", 4.921875),
])
