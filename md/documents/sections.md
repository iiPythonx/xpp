# [x2](../../README.md) / [Documents](../documents.md) / Sections

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
        - **Sections ▾**
            - [Table of Contents](#table-of-contents)
            - [About](#about)
        - [Variables](./variables.md)
- [Python API](../pythonAPI.md)
- [Standard Library](../standardLibrary.md)

## About

A section is a set of statements that get executed when using the operators `call`, `jmp`, or `pvk`. They are always loaded first when the file is executed or imported.

Sections always start with a colon `:`, and their name can only contain alphabetical letters:

```xt
:mySection
```

By default, a section is public, which means other files can import and use the section. To define a private section, append an at symbol (`@`) at the beginning of the section name. A private section can only be used by other sections within the file:

```xt
:@mySection
```

Statements that are not within a section are located in the global section predefined by the interpreter. The global section cannot be referenced, interacted with, or called, as it is deleted as soon as the file is executed or imported.

A section can also take arguments. Any variables separated by space and placed directly after the section name are considered arguments:

```xt
:myMethod argument0 argument1
```

> All arguments of a method or a function must be passed. An error is thrown if an argument is missing.

Three types of sections exist in x2.

A section that does not take any additional arguments nor return a value is considered a `section` and generally invoked using the `jmp` operator:

```xt
jmp mySection

:mySection
    out "Hello, world!"
```

A section that does take additional arguments but does not return a value is considered a `method` and generally invoked using the `pvk` operator.

```xt
pvk myMethod

:myMethod a b
    add a b c
    out c
```

A section that does take additional arguments and returns a value is considered a `function` and can be invoked using either the `pvk` or `call` operator. The `pvk` operator is used when the returned value is not wanted and the opposite is true for `call`:

```xt
call myFunction a b output
out output

:myFunction a b
    add a b c
    ret c
```

---

Last Updated: February 6th, 2022 by Dm123321_31mD

[↑ Go To Top](#x2--documents--sections)