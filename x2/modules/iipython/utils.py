# Copyright 2022 iiPython

# Modules
import math
from datetime import datetime
from typing import Any, Iterable, Union

# Functions
def avg(itrble: Iterable) -> float:
    """Returns the average number from the provided iterable

    Parameters:
        itrble (iterable): an iterable with only integers/floats

    Returns:
        average (float): The average of the iterable
    """
    return float(sum(itrble) / len(itrble))

def find(d: Iterable, func: Any) -> dict:
    """Finds dictionaries in a iterable with specific information

    Parameters:
        d (iterable): an iterable with only dictionaries; ie. [{"key": "value"}]
        func (any): a function that will return True/False if the dict has the right information

    Returns:
        result (dict): the dict matching the provided selector, else None

    Example:
        .find([{"Key1": "Value1"}, {"Key2": "Value2"}], lambda d: d["Key2"] == "Value2" if "Key2" in d else False)

        Returns:
            {"Key2": "Value2"}
    """
    ftype = [type(_).__name__ for _ in d if not isinstance(_, dict)]
    if ftype:
        raise ValueError("find needs a iterable with only dictionaries, got {}".format(ftype))

    for item in d:
        if func(item):
            return item

def findAll(d: Union[list, dict], func: Any) -> Any:
    """Finds items in the provided iterable matching the specification

    It works very similiarly to .find, although this finds all
    matches, and only passes the function the VALUE, rather than
    the entire item.

    Parameters:
        d (list, dict): either a list or a dictionary to be searched
        func (any): a function that will return True/False if the item has the right information

    Returns:
        result (Any): the matching data

    Example:
        .findAll({"Key1": "Value1", "Key2": "Value2", "Key3": "Value3"}, lambda d: d in ["Value1", "Value2"])

        Returns:
            {"Key1": "Value1", "Key2": "Value2"}

    """
    if isinstance(d, list):
        return [item for item in d if func(item) is True]

    return {item: d[item] for item in d if func(d[item])}

def findLast(d: Iterable, func: Any) -> Any:
    """Reverses the provided iterable, and calls .find(d, func)"""
    if hasattr(d, "reverse"):
        d.reverse()

    else:
        raise RuntimeError("provided iterable has no .reverse function")

    return find(d, func)

def filterAll(d: dict, func: Any) -> dict:
    """Filters the provided dictionary using the passed function

    Parameters:
        d (dict): a dictionary
        func (any): a function that returns a new value for the passed value

    Returns:
        result (dict): the filtered dictionary
    """
    for i in d:
        d[i] = func(d[i])

    return d

def findIndex(ls: list, idx: int) -> Any:
    """Returns the appropriate index from the provided list

    Parameters:
        ls (list): the list to use
        idx (int): the index to find

    Returns:
        rtem (any): the item at the provided index

    Specifically meant to be used with numbers larger than the list itself.
    In which case, built in indexing will fail, but this one works properly."""
    try:
        return ls[idx]

    except IndexError:
        return ls[idx - (len(ls) * math.floor(idx / len(ls)))]

def parseBool(v: str) -> bool:
    """Takes the provided string and converts it to a boolean
    - 1, 0
    - on, off
    - true, false
    - yes, no"""
    return v.lower() in ["true", "1", "yes", "on"]

def normalize(*args) -> list:
    """Takes the provided arguments, and attempts to replace all
    iterables with lists

    Non-iterable arguments will be ignored and kept in the list."""
    _normd = []
    for arg in args:
        try:
            _normd += list(arg)

        except ValueError:
            _normd.append(arg)

    return _normd

def rangdict(r: Iterable, value: Any = "") -> dict:
    """Constructs a dictionary with the given range

    Parameters:
        r (iterable): the range to use for keys
        value (any) -> "": the default value to use

    Returns:
        result (dict): a dict made using the range

    Example:
        .rangdict(range(5))

        Returns:
            {1: 1, 2: 2, 3: 3, 4: 4}

        If `value` is anything other than `""`, it
        will be used for the value of each key.
    """
    nd = {}
    for i in r:
        nd[i] = value.replace("%i", str(i)) or i

    return nd

def reverse(d: Iterable) -> Any:
    """Reverses the provided iterable, but also RETURNS it"""
    d.reverse()
    return d

def now() -> str:
    """Returns the current time in a neat way"""
    dt = datetime.now()
    return dt.strftime("%a. %B %-d{}, %Y".format("th" if 11 <= dt.day <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(dt.day % 10, "th")))

def prettyDict(d: dict) -> str:
    """Takes a dictionary and lays it out in "Key: Value" format, seperated by tabs."""
    return "".join("{}: {}\t".format(i, d[i]) for i in d)

def xrange(mn: int, mx: int = None) -> list:
    """Built-in range function, but actually gives you a range between mn and mx.

    Range: range(5) -> [0, 1, 2, 3, 4]
    XRange: xrange(5) -> [0, 1, 2, 3, 4, 5]"""
    return list(range(0 if mx is None else mn, mn + 1 if mx is None else mx + 1))
