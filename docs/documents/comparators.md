# [x++](../README.md) / [Documents](../documents.md) / Comparators

## Table of Contents

- [Home](../README.md)
- [Tutorials](../tutorials.md)
- [Documents ▾](../documents.md)
    - [Table of Contents](../documents.md#table-of-contents)
    - [About](../documents.md#about)
    - [Documents ▾](../documents.md#documents)
        - [Comments](comments.md)
        - **Comparators ▾**
            - [Table of Contents](#table-of-contents)
            - [Catalog](#catalog)
            - [About](#about)
            - [Documentation](#documentation)
        - [Configuration](configuration.md)
        - [Data Types](datatypes.md)
        - [Operators](operators.md)
        - [Packages](packages.md)
        - [Sections](sections.md)
        - [Variables](variables.md)
- [Python API](../python-api.md)
- [Caffeine](../caffeine.md)
- [Standard Library](../stdlib.md)

## Catalog

### E

- [Equal To](#equal-to)

### F

- [From](#from)

### G

- [Greater Than](#greater-than)
- [Greater Than or Equal To](#greater-than-or-equal-to)

### I

- [In](#in)
- [Is](#is)

### L

- [Less Than](#less-than)
- [Less Than or Equal To](#less-than-or-equal-to)

### N

- [Not Equal To](#not-equal-to)
- [Not In](#not-in)

## About

Comparators are symbols or keywords that compare two different variables or values and trigger a branch in the x++ thread. Each comparator has its functionality.

Expressions are segments in the code that creates a branch in the x++ thread. They are always made up of three components: the `source`, the `comparator`, and the `target`, and they are arranged like so:

```xpp
<source> <comparator> <target>
```

For example:

```xpp
5 == 5
```

Or:

```xpp
"hello" in "hello world"
```
 
An expression cannot be used on its own, as it is not considered as an operator and thus not a valid statement. It is always accompanied by operators that take an expression as an argument. A classic example of this is the `if` operator:

```xpp
if (5 == 5) "prt 'true'"
```

Any operator that uses an expression creates a branch, with `true` being the first branch and the second acts as an `else`. For example, the `if` operator creates a branch based on whether or not the expression is true:

```xpp
if (5 == 10) "prt 'same'" "prt 'different'"
```

## Documentation

### Equal To

```xpp
<source> == <target>
```

Checks if the two variables or values are equal to each other.

| Parameter | Type | Description |
| :-: | :-: | :-: |
| Source | Any | The variable or value that is being compared against |
| Target | Any | The variable or value being compared to |

Example:

```xpp
if (5 == 5) "prt 'true'"
```

---

### Not Equal To

```xpp
<source> != <target>
```

Checks if the two variables or values are different from each other.

| Parameter | Type | Description |
| :-: | :-: | :-: |
| Source | Any | The variable or value that is being compared against |
| Target | Any | The variable or value being compared to |

Example:

```xpp
if (5 != 10) "prt 'true'"
```

---

### Less Than

```xpp
<source> < <target>
```

Checks if the source is less than the target.

| Parameter | Type | Description |
| :-: | :-: | :-: |
| Source | [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer) or [String](./dataTypes.md#string) | The variable or value that is being compared against |
| Target | [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer) or [String](./dataTypes.md#string) | The variable or value being compared to |

Example:

```xpp
if (5 < 10) "prt 'true'"
```

---

### Less Than or Equal To

```xpp
<source> <= <target>
```

Checks if the source is less than or equal to the target.

| Parameter | Type | Description |
| :-: | :-: | :-: |
| Source | [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer) or [String](./dataTypes.md#string) | The variable or value that is being compared against |
| Target | [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer) or [String](./dataTypes.md#string) | The variable or value being compared to |

Example:

```xpp
if (5 <= 10) "prt 'true'"
```

---

### Greater Than

```xpp
<source> > <target>
```

Checks if the source is greater than the target.

| Parameter | Type | Description |
| :-: | :-: | :-: |
| Source | [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer) or [String](./dataTypes.md#string) | The variable or value that is being compared against |
| Target | [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer) or [String](./dataTypes.md#string) | The variable or value being compared to |

Example:

```xpp
if (10 > 5) "prt 'true'"
```

---

### Greater Than or Equal To

```xpp
<source> >= <target>
```

Checks if the source is greater than or equal to the target.

| Parameter | Type | Description |
| :-: | :-: | :-: |
| Source | [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer) or [String](./dataTypes.md#string) | The variable or value that is being compared against |
| Target | [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer) or [String](./dataTypes.md#string) | The variable or value being compared to |

Example:

```xpp
if (10 >= 5) "prt 'true'"
```

---

### In

```xpp
<source> in <target>
```

Checks if the source is in the target.

| Parameter | Type | Description |
| :-: | :-: | :-: |
| Source | Any | The variable or value that is being compared against |
| Target | Any | The variable or value being compared to |

Example:

```xpp
if ("ello" in "Hello, world!") "prt 'true'"
```

---

### Not In

```xpp
<source> not in <target>
```

Checks if the source is not in the target.

| Parameter | Type | Description |
| :-: | :-: | :-: |
| Source | Any | The variable or value that is being compared against |
| Target | Any | The variable or value being compared to |

Example:

```xpp
if ("bye" not in "Hello, world!") "prt 'true'"
```

---

### Is

```xpp
<source> is <target>
```

Checks if the source is a type of the target.

| Parameter | Type | Description |
| :-: | :-: | :-: |
| Source | Any | The variable or value that is being compared against |
| Target | [String](./dataTypes.md#string) | The variable or value being compared to |

Example:

```xpp
if (5 is "int") "prt 'true'"
```

---

Last Updated: March 9th, 2024 by iiPython

[↑ Go To Top](#x--documents--comparators)