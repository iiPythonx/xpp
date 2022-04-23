# Copyright 2022 iiPython

# Modules
import os
import json

# Initialization
config = {}
if os.path.isfile(".x2config"):
    try:
        with open(".x2config", "r") as f:
            config = json.loads(f.read())

    except Exception:
        pass
