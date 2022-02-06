# [x2](../../README.md) / [Documents](../documents.md) / Configurations

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

### Q

- [Quiet](#quiet)

## About

The configuration file defines what the project would do on execution. It is always placed in the `.xtconfig` file and should be written as if it is within a `*.json` file. If one is not found in the project, the default configuration is used internally instead:

```xtconfig
{
    "main": "main.xt",
    "quiet": false
}
```

If an essential field is missing, it is replaced with a default value internally instead:

```xtconfig
{
    "main": "main.xt"
}
```

> Because the `quiet` field is missing, its default value, `false`, is used instead.

The configuration file can also contain non-essential information, such as the author, version, or description of your project:

```xtconfig
{
    "author": "my-name",
    "contributors": [
        "contributor A", "contributor B"
    ],
    "description": "This is my x2 project",
    "main": "main.xt",
    "name": "my-x2-project",
    "version": "1.0.0"
}
```

## Documentation

### Main

```xtconfig
{
    "main": <path>
}
```

Defines the path of the main entry file.

| Parameter | Type | Default | Description |
| :-: | :-: | :-: | :-: |
| Path | String\<JSON> | "main.xt" | Main entry file path relative to the current working directory |

---

### Quiet

```xtconfig
{
    "quiet": <option>
}
```

Throws errors silently.

| Parameter | Type | Default | Description |
| :-: | :-: | :-: | :-: |
| Option | Boolean\<JSON> | false | Whether or not to throw error silently |

---

Last Updated: February 6th, 2022 by Dm123321_31mD

[↑ Go To Top](#x2--documents--configurations)