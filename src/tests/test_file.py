# Copyright 2023-2024 iiPython

# Modules
import os
import sys
import pathlib
sys.path.insert(1, str(pathlib.Path(__file__).parent.parent.resolve()))

# Handle file checking
def check_file_content(content: str) -> bool:
    with open("test.txt", "r") as fh:
        return fh.read() == content

# Ascii/unicode tests
microsoft = "© 1998 Microsoft® Corporation"
half_life = "λ Black Mesa"
emojis = "❤️ 🔥 💀"

# Start testing
from tests import start_tests
start_tests("File", [
    ("save 'test.txt' '1234567890'", lambda: check_file_content("1234567890")),
    ("load 'test.txt'", "1234567890"),
    ("save 'test.txt' (128+64)", lambda: check_file_content("192")),
    ("load 'test.txt'", "192"),

    # Check that it's reading files properly
    (f"save 'test.txt' '{microsoft}'", lambda: check_file_content(microsoft)),
    ("load 'test.txt' ascii", microsoft),
    (f"save 'test.txt' '{half_life}'", lambda: check_file_content(half_life)),
    ("load 'test.txt' ascii", half_life),
    (f"save 'test.txt' '{emojis}'", lambda: check_file_content(emojis)),
    ("load 'test.txt' ascii", emojis)
])

if os.path.isfile("test.txt"):
    os.remove("test.txt")
