# [x++](../README.md) / [Documents](../documents.md) / Packages

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
        - **Packages ▾**
            - [Table of Contents](#table-of-contents)
            - [About](#about)
        - [Sections](sections.md)
        - [Variables](variables.md)
- [Python API](../python-api.md)
- [Caffeine](../caffeine.md)
- [Standard Library](../stdlib.md)

## About

Packages are x++ files written by other people that can be imported to your x++ project using the `imp` operator:

```xpp
imp "examplePackage"
```

All packages are located in the `pkgs/` folder. If one is not found, the interpreter will automatically create one. When attempting to import a package, the interpreter will look for the `pkgs/<package>/main.xpp` file. If one is not found, an error is thrown.

Imported packages are only available in that one specific file. When attempting to use the package elsewhere, an error is thrown.

You can use an imported package by referencing the package name and then followed by a dot and the section name like so:

```xpp
imp "examplePackage"

examplePackage.mySection
```

The same applies to importing files.

To import a file from the x++ project, the path must contain the `.xpp` extension. The interpreter will then attempt to find the file from the current working directory. If one is not found, an error is thrown.

Currently, the [standard library](../stdlib.md) is built into the x++ interpreter. You can install more packages from GitHub.

---

Last Updated: March 9th, 2024 by iiPython

[↑ Go To Top](#x--documents--packages)