# [x2](../../README.md) / [Documents](../documents.md) / Packages

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
        - **Packages ▾**
            - [Table of Contents](#table-of-contents)
            - [About](#about)
        - [Sections](./sections.md)
        - [Variables](./variables.md)
- [Python API](../pythonAPI.md)
- [Standard Library](../standardLibrary.md)

## About

Packages are x2 files written by other people that can be imported to your x2 project using the `imp` operator:

```xt
imp "examplePackage"
```

All packages are located in the `pkg/` folder. If one is not found, the interpreter will automatically create one. When attempting to import a package, the interpreter will look for the `pkg/<package>/main.xt` file. If one is not found, an error is thrown.

Imported packages are only available in that one specific file. When attempting to use the package elsewhere, an error is thrown.

You can use an imported package by referencing the package name and then followed by a dot and the section name like so:

```xt
imp "examplePackage"

examplePackage.mySection
```

The same applies to importing files.

To import a file from the x2 project, the path must contain the `.xt` extension. The interpreter will then attempt to find the file from the current working directory. If one is not found, an error is thrown.

Currently, the [standard library](../standardLibrary.md) is built into the x2 interpreter. You can install more packages at the [official website](https://x2.iipython.cf/).

---

Last Updated: February 6th, 2022 by Dm123321_31mD

[↑ Go To Top](#x2--documents--packages)