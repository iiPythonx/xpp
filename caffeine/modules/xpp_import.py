# Copyright 2023 iiPython

# Modules
import logging
from typing import List
from pathlib import Path
from xpp.core.sections import load_sections

# do_import
def do_import(path: str, namespace: str = None) -> List[dict]:
    if (len(path) < 2) or (path[:2] != "./"):
        return logging.error("caffeine does not support importing non-relative files")

    fp = Path(path[2:]).absolute()
    if not fp.is_file():
        return logging.error(f"could not locate module at '{fp.resolve()}'")

    with open(fp, "r") as fh:
        return load_sections(fh.read(), path.rstrip(".xpp"), namespace = namespace)
