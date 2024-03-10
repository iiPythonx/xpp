# [x++](../README.md) / [Documents](../documents.md) / Configuration

## Table of Contents

- [Home](../README.md)
- [Tutorials](../tutorials.md)
- [Documents ▾](../documents.md)
    - [Table of Contents](../documents.md#table-of-contents)
    - [About](../documents.md#about)
    - [Documents ▾](../documents.md#documents)
        - [Comments](comments.md)
        - [Comparators](comparators.md)
        - **Configuration ▾**
            - [Table of Contents](#table-of-contents)
            - [Catalog](#catalog)
            - [About](#about)
            - [Documentation](#documentation)
        - [Data Types](datatypes.md)
        - [Operators](operators.md)
        - [Packages](packages.md)
        - [Sections](sections.md)
        - [Variables](variables.md)
- [Python API](../python-api.md)
- [Caffeine](../caffeine.md)
- [Standard Library](../stdlib.md)

## Catalog

### M

- [Main](#main)

## About

The configuration file defines what the project would do on execution. It is always placed in the `.xconfig` file and should be written as if it is within a `*.json` file. If one is not found in the project, the default configuration is used internally instead:

```json
{
    "main": "main.xpp"
}
```

The configuration file can also contain non-essential information, such as the author, version, or description of your project:

```json
{
    "author": "my-name",
    "contributors": [
        "contributor A", "contributor B"
    ],
    "description": "This is my x++ project",
    "main": "main.xpp",
    "name": "my-xpp-project",
    "version": "1.0.0"
}
```

> This is part of the official .xconfig specification. In fact, `xpp --show <module>` will use this spec.

## Documentation

### Main

```json
{
    "main": <path>
}
```

Defines the path of the main entry file.

| Parameter | Type | Default | Description |
| :-: | :-: | :-: | :-: |
| Path | String\<JSON> | "main.xpp" | Entrypoint relative to the current package (or cwd if it's a file) |

---

Last Updated: March 9th, 2024 by iiPython

[↑ Go To Top](#x--documents--configurations)