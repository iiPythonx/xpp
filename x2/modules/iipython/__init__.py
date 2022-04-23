__author__ = "iiPython"
__version__ = "1.1.2"
__license__ = "MIT"
__copyright__ = "Copyright 2022 iiPython"

from .term import color, clear, cprint, to_ansi, colormap
from .utils import (
    avg, find, findAll, findLast, filterAll, findIndex,
    parseBool, normalize, rangdict, reverse, now, prettyDict,
    xrange
)
from .iikp import keys, readchar
from .socket import Socket, Connection

from typing import List, Union

def keypress_prompt(accept: List[Union[str, int]]) -> Union[str, int]:
    """Infinitely waits until an acceptable key is pressed

    Parameters:
        accept (list): a list with allowed keys

    Returns:
        result (str, int): The pressed key
    """
    while True:
        key = readchar()
        if key in accept:
            return key

        elif key == keys.CTRL_C:
            raise KeyboardInterrupt
