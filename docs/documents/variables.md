# [x++](../README.md) / [Documents](../documents.md) / Variables

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
        - [Sections](sections.md)
        - **Variables ▾**
            - [Table of Contents](#table-of-contents)
            - [About](#about)
- [Python API](../python-api.md)
- [Caffeine](../caffeine.md)
- [Standard Library](../stdlib.md)

## About

A variable is a label that stores a value that can be referenced and modified at any time.

Even though a variable can contain any character besides spaces, it is recommended to use only alphabetical letters. A variable is defined using the `var` operator:

```xpp
var myInteger 5
```

A variable can then be referenced using the variable name:

```xpp
prt myInteger
```

By default, a variable is scoped, or local, which means it can only be referenced within the section it was defined in. Once the section is ended, the variables are garbage collected to save memory.

There are two other types of variables, `file variable` and `global variable`. A file variable can be referenced by any sections within the same file, while a global variable can be referenced anywhere in the project.

A file variable is defined by appending an at symbol (`@`) in front of the variable name:

```xpp
var @myInteger 5
```

A global variable is unable to be defined using x++ syntax. However, you can use [Python Integration](../python-api.md) to do so.

Both local and file variables are automatically garbage collected, but they can also be manually deleted from RAM using the `rem` operator:

```xpp
:: Removes BOTH myInteger AND @myInteger
rem myInteger @myInteger
```

---

Last Updated: March 9th, 2024 by iiPython

[↑ Go To Top](#x--documents--variables)