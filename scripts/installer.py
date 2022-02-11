# Copyright 2022 iiPython
# x2 Installer

# Modules
import os
import sys
import shutil
import zipfile
import subprocess
from typing import Any
from datetime import datetime

from iipython import readchar, keys

from rich.live import Live
from rich.align import Align
from rich.panel import Panel
from rich.console import Console
from rich.progress import Progress

# Initialization
rcon = Console()
rprint = rcon.print

options = {"install_docs": True, "install_stdlib": True, "change_dir": False}

def close(code: int, message: str = None) -> None:
    if message is not None:
        rprint(message)

    return sys.exit(code)

def read(accept: list) -> Any:
    while True:
        kp = readchar()
        if kp in accept:
            break

        elif kp == keys.CTRL_C:
            rcon.clear()
            close(0)

    return kp

def show_slide(content: str) -> None:
    rcon.clear()
    rprint("\n" * (round((rcon.size.height - content.count("\n")) / 2) - 1), end = "")  # Vertically center
    rprint(Panel(content, title = "%%V Installer"), justify = "center")

def make_menu(opts: list) -> dict:
    idx = 0
    def construct() -> str:  # noqa
        ml = len(max(opts, key = lambda d: len(d["name"]))["name"])
        return "\n".join([f"{'[ ]' if not opt['checked'] else '[[green]X[/]]'} {opt['name']}{' ' * (ml - len(opt['name']))} {'[yellow]:[/]' if i == idx else ':'}" for i, opt in enumerate(opts)])

    while True:
        show_slide("\n" + construct() + "\n\nPress [yellow][SPACE][/] to toggle options, [yellow][ENTER][/] to confirm.")

        # Handle keypresses
        kp = readchar()
        if kp == keys.UP and idx > 0:
            idx -= 1

        elif kp == keys.DOWN and idx < (len(opts) - 1):
            idx += 1

        elif kp in [" ", keys.SPACE]:
            opts[idx]["checked"] = not opts[idx]["checked"]

        elif kp == keys.ENTER:
            return {opt["ref"]: opt["checked"] for opt in opts}

        elif kp == keys.CTRL_C:
            break

def select_menu(opts: list) -> str:
    idx = 0
    def construct() -> str:  # noqa
        ml = len(max(opts, key = lambda d: len(d["name"]))["name"])
        return "\n".join([f"{opt['name']}{' ' * (ml - len(opt['name']))} {'[yellow]:[/]' if i == idx else ':'}" for i, opt in enumerate(opts)])

    while True:
        show_slide("\n" + construct() + "\n\nPlease select an option and press [yellow][ENTER][/].")

        # Handle keypresses
        kp = readchar()
        if kp == keys.UP and idx > 0:
            idx -= 1

        elif kp == keys.DOWN and idx < (len(opts) - 1):
            idx += 1

        elif kp == keys.ENTER:
            return opts[idx]["ref"]

        elif kp == keys.CTRL_C:
            rcon.clear()
            close(0)

# File checks
if not os.path.isfile("package.zip"):
    close(1, "Missing critical file: package.zip")

# Input handler
def get_path_input() -> str:
    rcon.clear()
    directory = ""
    while True:
        show_slide(f"[cyan]Enter a path to install x2 to:[/]\n[yellow]>[/] {directory}")
        kp = readchar()
        if isinstance(kp, str):
            directory += kp

        elif kp == keys.ENTER and directory:
            return directory

        elif kp == keys.BACKSPACE and directory:
            directory = directory[:-1]

# Install handler
def install() -> None:
    path = os.path.abspath(os.path.expanduser("~"))
    if options["change_dir"]:
        path = get_path_input()

    path = os.path.join(path, "x2")
    if os.path.isdir(path):
        show_slide(f"\n[red]The directory {path} already exists!\nRemove it and overwrite [/][yellow][Y/N][/][red]?[/]\n")
        kp = read(["y", "n"])
        if kp == "n":
            return

        shutil.rmtree(path)

    rcon.clear()
    start = datetime.now()

    # Extract zip
    with zipfile.ZipFile("package.zip", "r") as zf:

        # Create progress bar
        prg = Progress()
        ext_task = prg.add_task("[yellow]Extracting...", total = len(zf.infolist()))

        # Extract files
        rprint("\n" * (round((rcon.size.height - 1) / 2) - 1), end = "")  # Vertically center
        with Live(Align(Panel(prg, title = "%%V Installer"), align = "center"), refresh_per_second = 1 if os.name == "nt" else 10) as lv:
            for file in zf.infolist():
                root = file.filename.split("/")[0]
                if root == "md" and not options["install_docs"]:
                    continue

                elif root == "pkg" and not options["install_stdlib"]:
                    continue

                # Attempt to extract
                try:
                    zf.extract(file.filename, path)

                except PermissionError:
                    lv.stop()
                    show_slide("[red]Failed to write to folder: permission denied\nPress any key to return to the main menu.")
                    return readchar()

                prg.update(ext_task, advance = 1)

    # Handle launcher + path
    show_slide("\n[cyan]Creating launcher and PATH entries ...\n")
    if os.name == "nt":
        with open(os.path.join(path, "x2.bat"), "w+") as f:
            f.write("@echo off\n\"%~dp0python\python.exe\" \"%~dp0x2.py\" %*")  # noqa

        shutil.move(os.path.join(path, "main.py"), os.path.join(path, "x2.py"))

        userpath = subprocess.Popen(
            "for /f \"usebackq tokens=2,*\" %A in (`reg query HKCU\Environment /v PATH`) do echo %B",  # noqa
            stdout = subprocess.PIPE,
            shell = True
        ).communicate()[0].decode().strip("\r\n").split("\n")[1]
        if path not in userpath:
            os.system(f"setx PATH \"{userpath};{path}\"")

    # We're done
    elapsed = round((datetime.now() - start).total_seconds(), 2)
    show_slide(f"\n[green]Install completed in [yellow]{elapsed}s[/].\nPress any key to exit the installer.[/]")
    readchar()
    close(0)

# Main menu
while True:
    opt = select_menu([
        {"name": "Install now", "ref": "install"},
        {"name": "Install options", "ref": "options"},
        {"name": "Exit installer", "ref": "exit"}
    ])
    if opt == "exit":
        rcon.clear()
        close(0)

    elif opt == "options":
        options = make_menu([
            {"name": "Install documentation", "ref": "install_docs", "checked": options["install_docs"]},
            {"name": "Install standard library", "ref": "install_stdlib", "checked": options["install_stdlib"]},
            {"name": "Change install directory", "ref": "change_dir", "checked": options["change_dir"]}
        ])

    elif opt == "install":
        install()
