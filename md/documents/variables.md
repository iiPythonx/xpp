# [x2](../../README.md) / [Documents](../documents.md) / Variables

## Table of Contents

- [Home](../../README.md)
- [Tutorials](../tutorials.md)
- [Documents ▾](../documents.md)
    - [Table of Contents](../documents.md#table-of-contents)
    - [About](../documents.md#about)
    - [Documents ▾](../documents.md#documents)
        - [Comments](./comments.md)
        - [Comparators](./comparators.md)
        - [Configurations](./configurations.md)
        - [Data Types](./dataTypes.md)
        - [Operators](./operators.md)
        - [Packages](./packages.md)
        - [Sections](./sections.md)
        - **Variables ▾**
            - [Table of Contents](#table-of-contents)
            - [About](#about)
- [Python API](../pythonAPI.md)
- [Standard Library](../standardLibrary.md)

## About

A variable is a label that stores a value that can be referenced and modified at any time.

Even though a variable can contain any character besides spaces, it is recommended to use only alphabetical letters. A variable is defined using the `psh` operator:

```xt
psh 5 myInteger
```

A variable can then be referenced using the variable name:

```xt
out myInteger
```

By default, a variable is scoped, or local, which means it can only be referenced within the section it was defined in. Once the section is ended, the variables are garbage collected to save memory.

There are two other types of variables, `file variable` and `global variable`. A file variable can be referenced by any sections within the same file, while a global variable can be referenced anywhere in the project.

A file variable is defined by appending an at symbol (`@`) in front of the variable name:

```xt
psh 5 @myInteger
```

A global variable is defined by appending a hashtag (`#`) in front of the variable name:

```xt
psh 5 #myInteger
```

Both file and global are not garbage collected and must be manually deleted from the memory using the `rem` operator:

```xt
rem 5 @myInteger
```

Or:

```xt
rem 5 #myInteger
```

A variable can also be constant, which means it cannot be deleted using the `rem` operator. A constant variable can be defined using the `cnst` operator:

```xt
cnst 5 myInteger
```

Attempting to delete the variable will cause an error to be thrown. Note that even though a constant cannot be removed manually, it is still garbage collected if it is a local variable.

---

Last Updated: February 6th, 2022 by Dm123321_31mD

[↑ Go To Top](#x2--documents--variables)