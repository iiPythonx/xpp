# [x++](../README.md) / [Documents](../documents.md) / Data Types

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
        - **Data Types ▾**
            - [Table of Contents](#table-of-contents)
            - [Catalog](#catalog)
            - [About](#about)
            - [Documentation](#documentation)
        - [Operators](operators.md)
        - [Packages](packages.md)
        - [Sections](sections.md)
        - [Variables](variables.md)
- [Python API](../python-api.md)
- [Caffeine](../caffeine.md)
- [Standard Library](../stdlib.md)

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

Because x++ is a dynamic programming language, you can change the data type of a variable or a value during run-time.

x++ is also a weakly-typed programming language. You do not (and cannot) directly specify what the data type of a variable or value is. The interpreter will read the value and determine the data type during run-time.

Strongly-typed language, such as [Java](https://en.wikipedia.org/wiki/Java_(programming_language)):

```java
int myInteger = 5;
```

Weakly-typed language, such as [JavaScript](https://en.wikipedia.org/wiki/JavaScript):

```javascript
let myInteger = 5;
```

Similarly, in x++, you define a variable with a data type of an integer like so:

```xpp
var myInteger 5
```

## Documentation

### Boolean

A boolean value represents either `true` or `false`.

Currently, it is impossible to get a boolean value within vanilla x++. Because of that, integers are used instead to represent a true or false value, where `1` represents `true` and `0` represents `false`.

> You can however, use Python integration to create booleans on demand. The x++ interpreter supports this functionality natively.

---

### Float

A float is a signed number value with decimal points:

```xpp
5.0
```

```xpp
-5.0
```

It can be compared using mathematical comparators or be modified using certain operators.

Unlike integers, a decimal point is required to define a float.

Because floats are not accurate representations of the values, inaccuracies can occur similar to other programming languages:

```xpp
var a 0.1
var b 0.2
prt (a + b)
```

---

### Integer

An integer is a signed number value with no decimal points:

```xpp
5
```

```xpp
-5
```

It can be compared using mathematical comparators or be modified using certain operators.

Unlike Python, integers do allow leading `0`s to exist:

```xpp
var myInteger 05
prt myInteger  :: 5
```

In vanilla x++, it can also be used as a boolean value, where `1` represents `true` and `0` represents `false`:

```xpp
var hamburgerIsEaten 1
if (hamburgerIsEaten == 1) { prt "Someone ate my hamburger" }
```

---

### Null

Null is a data type that represents nothing.

It cannot be defined normally in x++ and acts as the default value to undefined variables:

```xpp
prt nonexistingVariable
```

It cannot be modified using any operators, and it cannot be used as a source or target within an expression:

```xpp
:: This will throw a parsing exception
if (nonexistingVariable == anotherNonExistingVariable) { prt "true" }
```

---

### String

A string is a combination of characters, numbers, spaces, and other symbols wrapped around by double-quotes (`"`):

```xpp
"string"
```

```xpp
"Hello, world!"
```

```xpp
"My favorite number is 5."
```

Some sets of characters, called escape codes or escape sequences, have special meanings within a string, and they always start with a backslash (`\`):

```xpp
"\t Indentation"
```

```xpp
"\n New Line"
```

Below is a list of all the escape codes for reference:

| Escape Code | Description | Example | Result | Widely-Supported |
| :-: | :-: | :-: | :-: | :-: |
| | Normal | `prt "Hello, world!"` | `Hello, world!` | ✓ |
| `\\` | Backslash character | `prt "Hello,\\world!"` | `Hello,\world!` | ✓ |
| `\'` | Single-quote character | `prt "\'Hello, world!\'"` | `'Hello, world!'` | ✓ |
| `\"` | Double-quote character | `prt "\"Hello, world!\""` | `"Hello, world!"` | ✓ |
| `\a` | Triggers Notification Sound | `prt "\a"` | | |
| `\b` | Backspace | `prt "Hello,\bworld!"` | `Helloworld!` | ✓ |
| `\f` | Form Feed | `prt "Hello,\fworld!"` | `Hello,`<br>`world!` | |
| `\n` | Line Feed | `prt "Hello,\nworld!"` | `Hello,`<br>`world!` | ✓ |
| `\r` | Carriage Return | `prt "Hello,\rworld!"` | `world!` | ✓ |
| `\t` | Horizontal Tab | `prt "Hello,\tworld!"` | `Hello,`&nbsp;&nbsp;`world!` | ✓ |
| `\v` | Verticle Tab | `prt "Hello,\vworld!"` | `Hello,`<br>`world!` | |
| `\ooo` | Octal Value | `prt "\110\145\154\154\157\54\40\167\157\162\154\144\41"` | `Hello, world!` | ✓ |
| `\xhh` | Hex Value | `prt "\x48\x65\x6C\x6C\x6F\x2C\x20\x77\x6F\x72\x6C\x64\x21"` | `Hello, world!` | ✓ |
| `\N{name}` | [Unicode Name](https://unicode.org/) | `prt "Hello,\N{grinning face}world!"` | `Hello,😀world!` | ✓ |
| `\uhhhh` | [16-Bit Unicode Escape](https://home.unicode.org/) | `prt "\u0048\u0065\u006c\u006c\u006f\u002c\u0020\u0077\u006f\u0072\u006c\u0064\u0021"` | `Hello, world!` | ✓ |
| `\Uhhhhhhhh` | [32-Bit Unicode Escape](https://unicode.org/) | `prt "Hello,\U0001F600world!"` | `Hello,😀world!` | ✓ |
| `\033[` | [ANSI Escape](https://en.wikipedia.org/wiki/ANSI_escape_code) | `prt "\033[31mHello, world!\033[0m"` | `Hello, world!` in red | ✓ |

> Source: [Python DS - Python 3 Escape Sequences](https://www.python-ds.com/python-3-escape-sequences)

You can also string interpolation within an x++ string. All non-string interpolations must be a valid x++ statement and be surrounded by `()`:

```xpp
:: If you are interpolating two strings:
var secondString "world!"
prt ("Hello, " + secondString)  :: "Hello, world!"

:: If you have other datatypes:
var myInteger 5
prt "My favorite integer:" (myInteger)
```

Any non-string data type within a string interpolation will require the use of `()`.

When being compared against using mathematical comparators, it is compared lexicographically:

```xpp
if ("abc" < "cba") { prt "true" }
```

---

Last Updated: March 9th, 2024 by iiPython

[↑ Go To Top](#x--documents--data-types)