# Copyright 2022-2024 iiPython

# Modules
import os
import json

# Initialization
config = {}
if os.path.isfile(".xconfig"):
    try:
        with open(".xconfig", "r") as f:
            config = json.loads(f.read())

    except (OSError, json.JSONDecodeError):
        pass
