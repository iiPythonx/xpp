import os
from . import keys

if os.name == "nt":
    import msvcrt
    from .read import readchar

elif "nix" in os.name or os.name == "posix":
    from .read_linux import readchar

else:
    raise OSError("unsupported OS '{}'".format(os.name))
