# [x++](../../README.md) / [Documents](../documents.md) / Configurations

## Table of Contents

- [Home](../../README.md)
- [Tutorials](../tutorials.md)
- [Documents ▾](../documents.md)
    - [Table of Contents](../documents.md#table-of-contents)
    - [About](../documents.md#about)
    - [Documents ▾](../documents.md#documents)
        - [Comments](./comments.md)
        - [Comparators](./comparators.md)
        - **Configurations ▾**
            - [Table of Contents](#table-of-contents)
            - [Catalog](#catalog)
            - [About](#about)
            - [Documentation](#documentation)
        - [Data Types](./dataTypes.md)
        - [Operators](./operators.md)
        - [Packages](./packages.md)
        - [Sections](./sections.md)
        - [Variables](./variables.md)
- [Python API](../pythonAPI.md)
- [Standard Library](../standardLibrary.md)

## Catalog

### M

- [Main](#main)

## About

The configuration file defines what the project would do on execution. It is always placed in the `.xtconfig` file and should be written as if it is within a `*.json` file. If one is not found in the project, the default configuration is used internally instead:

```xconfig
{
    "main": "main.xpp"
}
```

The configuration file can also contain non-essential information, such as the author, version, or description of your project:

```xconfig
{
    "author": "my-name",
    "contributors": [
        "contributor A", "contributor B"
    ],
    "description": "This is my x++ project",
    "main": "main.xt",
    "name": "my-x++-project",
    "version": "1.0.0"
}
```

> This is part of the official .xconfig specification. In fact, `xpp --show <module>` will use this spec.

## Documentation

### Main

```xconfig
{
    "main": <path>
}
```

Defines the path of the main entry file.

| Parameter | Type | Default | Description |
| :-: | :-: | :-: | :-: |
| Path | String\<JSON> | "main.xpp" | Entrypoint relative to the current package (or cwd if it's a file) |

---

Last Updated: April 9th, 2023 by iiPython

[↑ Go To Top](#x--documents--configurations)