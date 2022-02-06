# [x2](../../README.md) / [Documents](../documents.md) / Data Types

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
        - **Data Types ▾**
            - [Table of Contents](#table-of-contents)
            - [Catalog](#catalog)
            - [About](#about)
            - [Documentation](#documentation)
        - [Operators](./operators.md)
        - [Packages](./packages.md)
        - [Python API](./pythonAPI.md)
        - [Sections](./sections.md)
        - [Variables](./variables.md)
- [Python API](../pythonAPI.md)
- [Standard Library](../standardLibrary.md)

## Catalog

### B

- [Boolean](#boolean)

### F

- [Float](#float)

### I

- [Integer](#integer)

### N

- [Null](#null)

### S

- [String](#string)

## About

Data types are classifications of variables or values. Each data type can only store a specific type of value. For example, a string cannot contain an integer value, or a boolean cannot contain a string value.

Because x2 is a dynamic programming language, you can change the data type of a variable or a value during run-time.

x2 is also a weakly-typed programming language. You do not (and cannot) directly specify what the data type of a variable or value is. The interpreter will read the value and determine the data type during run-time.

Strongly-typed language, such as [Java](https://en.wikipedia.org/wiki/Java_(programming_language)):

```java
int myInteger = 5;
```

Weakly-typed language, such as [JavaScript](https://en.wikipedia.org/wiki/JavaScript):

```javascript
let myInteger = 5;
```

Similarly, in x2, you define a variable with a data type of an integer like so:

```xt
psh 5 myInteger
```

## Documentation

### Boolean

A boolean value represents either `true` or `false`.

Currently, it is impossible to get a boolean value within vanilla x2. Because of that, integers are used instead to represent a true or false value, where `1` represents `true` and `0` represents `false`.

---

### Float

A float is a signed number value with decimal points:

```xt
5.0
```

```xt
-5.0
```

It can be compared using mathematical comparators or be modified using certain operators.

Unlike integers, a decimal point is required to define a float.

Because floats are not accurate representations of the values, inaccuracies can occur similar to other programming languages:

```xt
psh 0.1 a
psh 0.2 b
add a b c
out c
```

---

### Integer

An integer is a signed number value with no decimal points:

```xt
5
```

```xt
-5
```

It can be compared using mathematical comparators or be modified using certain operators.

Unlike Python, integer does allow leading `0`s to exist:

```xt
psh 05 myInteger
out myInteger
```

In vanilla x2, it can also be used as a boolean value, where `1` represents `true` and `0` represents `false`:

```xt
psh 0 hamburgerIsEaten
evl hamburgerIsEaten == 1 "out \"Someone ate my hamburger\""
```

---

### Null

Null is a data type that represents nothing.

It cannot be defined normally in x2 and acts as the default value to undefined variables:

```xt
out nonexistingVariable
```

It cannot be modified using any operators, but it can be used as a source or target within an expression:

```xt
cmp nonexistingVariable == anotherNonExistingVariable "out \"true\""
```

---

### String

A string is a combination of characters, numbers, spaces, and other symbols wrapped around by double-quotes (`"`):

```xt
"string"
```

```xt
"Hello, world!"
```

```xt
"My favorite number is 5."
```

Some sets of characters, called escape codes or escape sequences, have special meanings within a string, and they always start with a backslash (`\`):

```xt
"\t Indentation"
```

```xt
"\n New Line"
```

Below is a list of all the escape codes for reference:

| Escape Code | Description | Example | Result | Widely-Supported |
| :-: | :-: | :-: | :-: | :-: |
| | Normal | `out "Hello, world!"` | `Hello, world!` | ✓ |
| `\\` | Backslash character | `out "Hello,\\world!"` | `Hello,\world!` | ✓ |
| `\'` | Single-quote character | `out "\'Hello, world!\'"` | `'Hello, world!'` | ✓ |
| `\"` | Double-quote character | `out "\"Hello, world!\""` | `"Hello, world!"` | ✓ |
| `\a` | Triggers Notification Sound | `out "\a"` | | |
| `\b` | Backspace | `out "Hello,\bworld!"` | `Helloworld!` | ✓ |
| `\f` | Form Feed | `out "Hello,\fworld!"` | `Hello,`<br>`world!` | |
| `\n` | Line Feed | `out "Hello,\nworld!"` | `Hello,`<br>`world!` | ✓ |
| `\r` | Carriage Return | `out "Hello,\rworld!"` | `world!` | ✓ |
| `\t` | Horizontal Tab | `out "Hello,\tworld!"` | `Hello,`&nbsp;&nbsp;`world!` | ✓ |
| `\v` | Verticle Tab | `out "Hello,\vworld!"` | `Hello,`<br>`world!` | |
| `\ooo` | Octal Value | `out "\110\145\154\154\157\54\40\167\157\162\154\144\41"` | `Hello, world!` | ✓ |
| `\xhh` | Hex Value | `out "\x48\x65\x6C\x6C\x6F\x2C\x20\x77\x6F\x72\x6C\x64\x21"` | `Hello, world!` | ✓ |
| `\N{name}` | [Unicode Name](https://unicode.org/) | `out "Hello,\N{grinning face}world!"` | `Hello,😀world!` | ✓ |
| `\uhhhh` | [16-Bit Unicode Escape](https://home.unicode.org/) | `out "\u0048\u0065\u006c\u006c\u006f\u002c\u0020\u0077\u006f\u0072\u006c\u0064\u0021"` | `Hello, world!` | ✓ |
| `\Uhhhhhhhh` | [32-Bit Unicode Escape](https://unicode.org/) | `out "Hello,\U0001F600world!"` | `Hello,😀world!` | ✓ |
| `\033[` | [ANSI Escape](https://en.wikipedia.org/wiki/ANSI_escape_code) | `out "\033[31mHello, world!\033[0m"` | `Hello, world!` in red | ✓ |

> Source: [Python DS - Python 3 Escape Sequences](https://www.python-ds.com/python-3-escape-sequences)

You can also string interpolation within an x2 string. All string interpolations must be a valid x2 statement and be surrounded by `$()`:

```xt
psh 5 myInteger
out "My favorite integer: $(pop myInteger)"
```

Any non-string data type within a string interpolation will automatically be converted into a string data type.

When being compared against using mathematical comparators, it is compared lexicographically:

```xt
cmp "abc" < "cba" "out \"true\""
```

---

Last Updated: February 6th, 2022 by Dm123321_31mD

[↑ Go To Top](#x2--documents--data-types)