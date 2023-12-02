# Copyright 2023-2024 iiPython

# Modules
import sys
import pathlib
sys.path.insert(1, str(pathlib.Path(__file__).parent.parent.resolve()))

# Start testing
from tests import start_tests
start_tests("Compare", [
    ("if (3 == 3) 'str 1' 'str 0'", "1"),
    ("if (2 == 5) 'str 1' 'str 0'", "0"),
    ("if (6 != 6) 'str 1' 'str 0'", "0"),
    ("if (6 != 7) 'str 1' 'str 0'", "1"),
    ("if (1 <= 6) 'str 1' 'str 0'", "1"),
    ("if (6 <= 1) 'str 1' 'str 0'", "0"),
    ("if (4 >= 3) 'str 1' 'str 0'", "1"),
    ("if (2 >= 7) 'str 1' 'str 0'", "0"),
    ("if (not 4) 'str 1' 'str 0'", "0"),
    ("if (not 0) 'str 1' 'str 0'", "1"),
])
