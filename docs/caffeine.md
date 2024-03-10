# [x++](README.md) / Caffeine

## Table of Contents

- [Home](README.md)
- [Tutorials](tutorials.md)
- [Documents](documents.md)
- [Python API](python-api.md)
- **Caffeine ▾**
    - [Introduction](#introduction)
    - [Basic Usage](#basic-usage)
    - [Notice](#notice)
- [Standard Library](stdlib.md)

## Introduction

Caffeine is a x++ to Python conversion module and CLI. It converts your existing code to Python for performance improvements or just general codebase migration.  
It's included with x++ since version 3.1.2 and is available globally as the Python package `caffeine`.  

It implements **all** features available in xpp except for imports.

## Basic Usage

If you had a file called `main.xpp` and wanted to convert it to Python, you could do something like this:

```sh
caffeine main.xpp
```

This will give you a  `main.py` file in the same directory.

---

Another feature is auto minification of the resulting Python code via the `-1` flag.  
To convert `main.xpp` to minified Python, you would run:

```sh
caffeine -o -1 main.xpp
```

Notice the `-o` in there? That stands for `overwrite`, so caffeine will write over the existing `main.py` file (if it exists).

---

Lastly, Caffeine supports automatic building via [pyinstaller](https://pyinstaller.org).  
To convert `main.xpp` to an exe (or binary, depending on your OS) and then run it automatically, you can do something like this:

```sh
caffeine -o -r -b main.xpp
```

This will give you a `main` file and will run it automatically after pyinstaller builds it.  
However, this obviouslly requires that you have pyinstaller installed and added to system PATH.

## Notice

Run `caffeine --help` for more up to date and accurate information then these docs can provide.  

---

Last Updated: March 9th, 2024 by iiPython

[↑ Go To Top](#x--caffeine)