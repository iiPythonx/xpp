# Copyright 2022 iiPython
# x2 Installer

# Modules
import os
import shutil
import zipfile
import subprocess
from typing import Any
from datetime import datetime

from iipython import readchar, keys

from rich.live import Live
from rich.panel import Panel
from rich.console import Console
from rich.progress import Progress

# Initialization
rcon = Console()
rprint = rcon.print

def close(code: int, message: str = None) -> None:
    if message is not None:
        rprint(message)

    return exit(code)

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
def install(path: str) -> None:
    path = os.path.join(path, "x2")
    if os.path.isdir(path):
        show_slide(f"\n[red]The directory {path} already exists!\nRemove it and overwrite [/][yellow][Y/N][/][red]?[/]\n")
        kp = read(["y", "n"])
        if kp == "n":
            rcon.clear()
            close(0, "[yellow]Please make the appropriate directory changes then rerun the installer.")

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
        with Live(Panel(prg, title = "%%V Installer"), refresh_per_second = 1):
            for file in zf.infolist():
                zf.extract(file.filename, path)
                prg.update(ext_task, advance = 1)

    # Handle launcher + path
    show_slide("\n[cyan]Creating launcher and PATH entries ...\n")
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
show_slide("""[blue bold]Welcome to the x2 Installer![/]

This executable will install x2 on your computer.
Press [yellow][ENTER][/] to install now, or [yellow][E][/] to change the installation directory.

[red]Press [yellow][Q][/] or [yellow][^C][/] to quit the installer.""")
kp = read([keys.ENTER, keys.CTRL_C, "e", "q"])
if kp == keys.ENTER:
    install(os.path.abspath(os.path.expanduser("~")))

elif kp == "e":
    install(get_path_input())

elif kp == "q":
    rcon.clear()
    close(0)
