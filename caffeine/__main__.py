# Copyright 2023 iiPython

# Modules
import sys
import subprocess
from pathlib import Path

from . import __version__
from .modules.optimize import optimize
from .modules.analysis import construct_flow_tree
from .modules.packager import package_tree, tree_to_xpp

# Initialization
def main() -> None:
    args = [a for a in sys.argv[1:] if a[0] != "-"]
    if not args:
        print("\n".join([(ln.split(" " * 12)[1] if ln.strip() else ln) for ln in f"""
            caffeine {__version__} - an efficient x++ compiler
            usage: {sys.executable} -m caffeine [options] <source file> [output file]

            options:
                -o: overwrites the existing destination file (if it exists)
                -r: runs the output file after compilation is complete
                -x: output an x++ file instead of Python
                -<n>: sets the optimization level
                    -0: disables all optimizations
                    -1: optimizes common x++ operations
                    -2: optimizes everything possible (default)

            copyright (c) 2023 iipython
            https://github.com/iiPythonx/xpp/tree/main/caffeine
        """.split("\n")[1:][:-1]]))
        exit(0)

    # Load source file
    def ext(path: str, extension: str) -> str:
        return path if path.endswith(extension) else f"{path}_out.{extension}"

    source, destination = Path(ext(args[0], "xpp")), \
        Path(ext((args[1] if len(args) > 1 else args[0]).rstrip(".xpp"), "py" if "-x" not in sys.argv else "xpp"))

    # Pre-compile sanity checks
    if destination.is_file() and ("-o" not in sys.argv):
        exit("error: destination file exists! overwrite with the -o flag.")

    elif not source.is_file():
        exit("error: source file does not exist!")

    # Handle optimization level
    level = 2
    for opt in sys.argv:
        if (len(opt) != 2) or (opt[0] != "-") or (not opt[1].isdigit()):
            continue

        level = int(opt[1])
        if level not in range(0, 3):
            exit("error: optimization level not in range 0-2")

    # Compile everything
    with open(destination, "w+") as fh:
        with open(source, "r") as sc:
            flowtree = construct_flow_tree(sc.read())
            tree = optimize(flowtree, level) if level else flowtree
            if "-x" in sys.argv:
                fh.write(tree_to_xpp(tree))

            else:
                fh.write(f"from caffeine import Interpreter as i;t=i();t.run_tree({package_tree(tree)})")

    # Handle running
    if "-r" in sys.argv:
        xpp_args = ["-m", "xpp"]
        subprocess.run([sys.executable, *(xpp_args if "-x" in sys.argv else []), destination])

if __name__ == "__main__":
    main()
