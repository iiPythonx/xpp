# [x++](../README.md) / [Documents](../documents.md) / Sections

## Table of Contents

- [Home](../README.md)
- [Tutorials](../tutorials.md)
- [Documents ▾](../documents.md)
    - [Table of Contents](../documents.md#table-of-contents)
    - [About](../documents.md#about)
    - [Documents ▾](../documents.md#documents)
        - [Comments](comments.md)
        - [Comparators](comparators.md)
        - [Configuration](configuration.md)
        - [Data Types](datatypes.md)
        - [Operators](operators.md)
        - [Packages](packages.md)
        - **Sections ▾**
            - [Table of Contents](#table-of-contents)
            - [About](#about)
        - [Variables](variables.md)
- [Python API](../python-api.md)
- [Caffeine](../caffeine.md)
- [Standard Library](../stdlib.md)

## About

A section is a set of statements that get executed when using the `jmp` operator. They are always loaded first when the file is executed or imported.

Sections always start with a colon `:`, and their name can only contain alphabetical letters:

```xpp
:mySection
```

Statements that are not within a section are located in the global section predefined by the interpreter. The global section cannot be referenced, interacted with, or called, as it is deleted as soon as the file is executed or imported.

A section can also take arguments. Any variables separated by space and placed directly after the section name are considered arguments:

```xpp
:myMethod argument0 argument1
```

> All arguments of a method or a function must be passed. An error is thrown if an argument is missing.

Since the release of x2.3, only one type of section exists in x++.

A section that takes (or doesn't take) additional arguments and (may or may not) return a value is considered a `function` and can be invoked using the `jmp` operator.

```xpp
jmp myFunction 1 2 ?output
prt output  :: 3

:myFunction a b
    add a b c
    ret c
```

---

Last Updated: March 9th, 2024 by iiPython

[↑ Go To Top](#x--documents--sections)