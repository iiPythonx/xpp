# [x++](README.md) / Python API

## Table of Contents

- [Home](README.md)
- [Tutorials](tutorials.md)
- [Documents](documents.md)
- **Python API ▾**
    - [Introduction](#introduction)
    - [Definitions](#definitions)
    - [Inline statements](#inline-statements)
    - [Python modules](#python-modules)
    - [Python inside .xconfig](#python-inside-xconfig)
- [Caffeine](caffeine.md)
- [Standard Library](stdlib.md)

## Introduction

Welcome to the x++ Python API documentation.  
This page will cover how to integrate the [Python](https://python.org) programming language into your x++ projects.

## Definitions

Before attempting to integrate Python with your x++ project, please ensure you **never** install (and **especially don't import**) untrusted or random Python modules. Code inside these modules will have unrestricted access to the host computer and can do everything from adding you to a botnet to completely destroying your PC.  

With that being said, here's some loose terms that will be used throughout this document:
- **Module**
    - A Python file that is being imported using the `imp` operator
- **Packages Folder**
    - This will normally be the `pkgs` folder inside your current working directory.


## Inline statements

x++ comes with the built-in `evl` operator, which will execute the given Python code with access to all internal classes and methods. This makes it easy to execute small amounts of Python code in an x++ program.  

> If you need custom operators, newlines, or large pieces of Python, please see [Python modules](#python-modules).

The most basic syntax for an evaluation statement is as follows:
```py
prt "the following statement will be executed by python:"

:: actually run our code
evl "print('hello, world! this is python')"
```  

This "live" Python environment has access to the following globals:
- `mem` (see [datastore.py](https://github.com/iiPythonx/xpp/blob/main/xpp/core/datastore.py))
- `interpreter` (the x++ interpreter; see [interpreter.py](https://github.com/iiPythonx/xpp/blob/main/xpp/core/interpreter.py))
- `vars` (all current variables; see [datastore.py](https://github.com/iiPythonx/xpp/blob/main/xpp/core/datastore.py))
- `version` (current x++ version)

These globals, in theory, should allow you to customize the x++ runtime as much as desired.

## Python modules

The built-in `imp` operator not only allows you to import x++ files, but also allows the importing of modules inside the packages folder. For example, if you have the following inside `example.py`:
```py
# example.py
print("Hello from example.py!")
```

Then you can do the following from inside x++:
```xpp
imp "example.py"
:: example.py will of ran by now, so the terminal should say hello
```

However, this is a very bad usage of Python importing. For something this small, it is recommended to just use [inline statements](#inline-statements).  

---

Now for the fun stuff.  
Python modules imported via the `imp` operator are loaded using the x++ operator loader. This means you have the ability to create custom operators at runtime and use them in your x++ code.  

Take the following Python module:
```py
# example.py
class XOperators:
    def some_operator(mem, args):
        print("Hello! some_operator is running!")
        print(mem)  # Contains cli_vals, variables, and other things
        print(args)  # List of Datastore() objects
```

You can now use `some_operator` inside x++:
```xpp
imp "example.py"
some_operator "some arguments" 1 2 3 4 5
```

Additionally, arguments can be processed via `ctx.args`.

## Python inside .xconfig

If your x++ module has a `.xconfig` file (as it should), you can set the `main` argument to a Python file and use it as your entrypoint. An example `.xconfig` file is as follows:
```json
{
    "main": "example.py"
}
```

Assuming you had that `.xconfig` file located at `pkgs/example/.xconfig` and moved `example.py` to `pkgs/example/example.py` then you could do the following from within x++:
```xpp
:: since .xconfig says to run example.py from inside pkgs/example
:: this will load any operators from inside the file
imp "example"
some_operator

:: it should of printed hello to the screen again
```

---

Last Updated: July 5th, 2023 by iiPython

[↑ Go To Top](#x--python-api)