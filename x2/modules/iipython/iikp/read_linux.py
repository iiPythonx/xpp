# Copyright 2022 iiPython

# Modules
import sys
import tty
import termios
from . import keys

# Readchar function
def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

        if ch == "\x1b":
            ch = sys.stdin.read(2)
            if ch == "[D":
                return keys.LEFT

            elif ch == "[C":
                return keys.RIGHT

            elif ch == "[A":
                return keys.UP

            elif ch == "[B":
                return keys.DOWN

        elif ch == "\r":
            return keys.ENTER

        elif ch == "\x7f":
            return keys.BACKSPACE

        elif ch == "\x03":
            return keys.CTRL_C

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return ch
