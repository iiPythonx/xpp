# Copyright 2022 iiPython

# Modules
import re
import os

# Color map
def to_ansi(code: int) -> str:
    return f"\033[{code}m"

colormap_ = {
    "black": 30, "red": 31, "green": 32,
    "yellow": 33, "blue": 34, "magenta": 35,
    "cyan": 36, "white": 37, "bright": 1,
    "dim": 2, "norm": 22, "reset": 39
}
colormap = {}
for color, code in colormap_.items():
    colormap[color] = to_ansi(code)
    if color not in ["bright", "dim", "norm"]:
        colormap["l" + color] = to_ansi(code + 60)
        colormap["bg" + color] = to_ansi(code + 10)
        colormap["bgl" + color] = to_ansi(code + 70)

# Initialization
_tagregex = re.compile(r"\[\/?\w*\]")
_clear_command = "cls" if os.name == "nt" else "clear"

# Terminal functions
def clear() -> None:
    """Clears the terminal screen"""
    os.system(_clear_command)

def color(text: str, dry: bool = False) -> str:
    """Colorizes text using bbcode-like markup

    Parameters:
        text (str): the text to colorize
        dry (bool): dry run, only strip tags

    Returns:
        text (str): the colorized text

    Example:
        .color("[red]Hello, red world![/red]")
        Returns:
            \033[31mHello, red world!\033[39m

        For more examples, see the Python rich library:
        https://github.com/willmcgugan/rich
    """
    text = str(text)

    # Process tags
    text += ("[reset]" if not text.endswith("[reset]") else "")
    tags = []
    for tag in _tagregex.findall(text):
        tag = tag.strip("[]")
        if tag == "/":
            isbg, tags = tags[-1][:2] == "bg", tags[:-1]
            text = text.replace(f"[/{tag[1:]}]", (colormap["bgreset"] if isbg else "") + (colormap[tags[-1] if tags else "reset"]) if not dry else "", 1)

        else:
            if tag not in colormap:
                continue

            text = text.replace(f"[{tag}]", colormap[tag] if not dry else "", 1)
            tags.append(tag)

    return text

def cprint(*args, **kwargs) -> None:
    """A wrapper for print() which calls .color() on each argument"""
    return print(*[color(a) for a in args], **kwargs)
