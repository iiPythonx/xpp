# Copyright 2022 iiPython

# Modules
import string
import msvcrt
from . import keys

# String list
string_check = string.ascii_letters + string.digits + string.punctuation

# Main function
def readchar() -> str | int:

    # Grab a character
    ch = msvcrt.getch()
    ch_dc = ch.decode("mbcs")
    if ch_dc in string_check:
        return ch_dc

    ch = ord(ch)
    if ch == 0 or ch == 224:
        ch = ord(msvcrt.getch())

    # Character map
    if ch == keys.SPACE:
        return " "

    return ch
