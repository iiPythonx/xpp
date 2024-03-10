# Copyright 2023-2024 iiPython

# Modules
import os
import sys
import subprocess
from pathlib import Path
from shutil import copy, which
from tempfile import TemporaryDirectory

from . import __version__
from .modules.optimize import to_python

# Check for Python-Minifier
try:
    from python_minifier import minify

except ImportError:
    minify = None

# Initialization
def do_run(file: str) -> None:
    file = str(file)
    if "-r" not in sys.argv:
        return

    subprocess.run([sys.executable, file] if file.endswith(".py") else [file])

def main() -> None:
    args = [a for a in sys.argv[1:] if a[0] != "-"]
    if not args or "--help" in sys.argv or "-h" in sys.argv:
        print("\n".join([(ln.split(" " * 12)[1] if ln.strip() else ln) for ln in f"""
            caffeine {__version__} - an efficient x++ to python builder
            usage: {sys.executable} -m caffeine [options] <source file> [output file]

            options:
                -h: shows this message
                -o: overwrites the existing destination file (if it exists)
                -r: runs the output file after compilation is complete
                -<n>: sets the optimization level
                    -0: disables all optimizations
                    -1: minifies resulting python code
                -b: attempt to build using pyinstaller

            copyright (c) 2023-2024 iipython
            https://github.com/iiPythonx/xpp/tree/main/caffeine
        """.split("\n")[1:][:-1]]))
        sys.exit(0)

    # Load source file
    def ext(path: str, extension: str) -> str:
        return path if path.endswith(extension) else f"{path}.{extension}"

    source, destination = Path(ext(args[0], "xpp")), \
            Path(args[1] if len(args) > 1 else args[0].rstrip(".xpp"))

    if "." in str(destination).split(os.sep)[-1]:
        exit("error: destination must not have a file extension!")

    # Pre-compile sanity checks
    overwrite = "-o" in sys.argv
    if not source.is_file():
        exit("error: source file does not exist!")

    # Convert xpp into Python
    python_dest = destination.with_suffix(".py")
    if python_dest.is_file() and not overwrite:
        exit(f"error: {python_dest} exists! overwrite with the -o flag.")

    with open(python_dest, "w+") as fh:
        with open(source, "r") as sc:
            result = to_python(sc.read())

            # Minify file
            if "-1" in sys.argv:
                if minify is None:
                    print("warn: python-minifier is not installed, skipping minification step ...")

                else:
                    result = minify(result)

            # Send to file
            fh.write(result)

    # Convert to executable via pyinstaller
    if "-b" not in sys.argv:
        return do_run(python_dest)

    elif not which("pyinstaller"):
        exit("warn: pyinstaller is not installed, skipping build stage ...")

    with TemporaryDirectory() as temp:
        subprocess.run(["pyinstaller", python_dest, "-F", "--distpath", temp])
        copy(os.path.join(temp, destination), destination)

    os.remove(f"{destination}.spec")
    do_run(os.path.abspath(destination))

if __name__ == "__main__":
    main()
