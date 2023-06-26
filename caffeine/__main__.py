# Copyright 2023 iiPython

# Modules
import sys
import subprocess
from pathlib import Path
from .modules.optimize import optimize
from .modules.packager import package_tree
from .modules.analysis import construct_flow_tree

# Initialization
def main() -> None:
    args = [a for a in sys.argv[1:] if a[0] != "-"]
    if not args:
        exit("\n".join([(ln.split(" " * 12)[1] if ln.strip() else ln) for ln in f"""
            caffeine - an efficient x++ compiler
            usage: {sys.executable} -m caffeine [-o -r] <source file> [output file]

            options:
                -o: overwrites the existing destination file (if it exists)
                -r: runs the output file after compilation is complete

            copyright (c) 2023 iipython
            https://github.com/iiPythonx/xpp/tree/main/caffeine
        """.split("\n")[1:][:-1]]))

    # Load source file
    def ext(path: str, extension: str) -> str:
        return path if path.endswith(extension) else f"{path}.{extension}"

    source, destination = Path(ext(args[0], "xpp")), \
        Path(ext((args[1] if len(args) > 1 else args[0]).rstrip(".xpp"), "py"))

    # Pre-compile sanity checks
    if destination.is_file() and ("-o" not in sys.argv):
        exit("error: destination file exists! overwrite with the -o flag.")

    elif not source.is_file():
        exit("error: source file does not exist!")

    # Compile everything
    with open(destination, "w+") as fh:
        with open(source, "r") as sc:
            tree = package_tree(optimize(construct_flow_tree(sc.read())))

        fh.write(f"from caffeine import Interpreter as i;t=i();t.run_tree({tree})")

    # Handle running
    if "-r" in sys.argv:
        subprocess.run([sys.executable, destination])

if __name__ == "__main__":
    main()
