# [x++](../../README.md) / [Documents](../documents.md) / Operators

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
        - **Operators ▾**
            - [Table of Contents](#table-of-contents)
            - [Catalog](#catalog)
            - [About](#about)
            - [Documentation](#documentation)
        - [Packages](./packages.md)
        - [Sections](./sections.md)
        - [Variables](./variables.md)
- [Python API](../pythonAPI.md)
- [Standard Library](../standardLibrary.md)

## Catalog

### A

- [Add](#add)

### C

- [Call](#call)
- [Character](#character)
- [Clear](#clear)
- [Compare](#compare)
- [Constant](#constant)

### D

- [Decrement](#decrement)
- [Divide](#divide)

### E

- [End](#end)
- [Evaluate](#evaluate)
- [Exit](#exit)

### F

- [Float](#float)

### I

- [Import](#import)
- [Index](#index)
- [Increment](#increment)
- [Is A Number](#is-a-number)
- [Is Any Number](#is-any-number)

### J

- [Jump](#jump)

### L

- [Length](#length)
- [Load](#load)
- [Lowercase](#lowercase)

### M

- [Multiply](#multiply)

### N

- [Number](#number)

### O

- [Output](#output)

### P

- [Pop](#pop)
- [Provoke](#provoke)
- [Push](#push)

### R

- [Random Number Generator](#random-number-generator)
- [Read](#read)
- [Remove](#remove)
- [Repeat](#repeat)
- [Return](#return)
- [Round](#round)

### S

- [Save](#save)
- [Skip](#skip)
- [Slice](#slice)
- [String](#string)
- [Subtract](#subtract)

### T

- [Throw](#throw)
- [Try](#try)

### U

- [Uppercase](#uppercase)

### W

- [Wait](#wait)
- [While](#while)

## About

Operators are keywords that process arguments.

A statement is a line of code that tells the interpreter what to do. They are always made up of two components: the `operator` and the `arguments`, and they are arranged like so:

```xpp
<operator> [...arguments]
```

For example:

```xpp
out "Hello, world!"
```

Or:

```xpp
add 1 2 sum
```

A statement can also be wrapped around parentheses (`()`) to group them.

Some statements return values, which can be stored in a variable:

```xpp
psh (add 1 2) sum
```

## Documentation

### Add

```xpp
add <addend A> <addend B> [sum]
```

Adds two addends together or concatenates two strings together.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Addend A | [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer) or [String](./dataTypes.md#string) | | The first addend |
| Addend B | [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer) or [String](./dataTypes.md#string) | | The second addend |
| Sum | [Variable](./variables.md) | ✓ | The sum of the two addend |

Returns: [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer) or [String](./dataTypes.md#string)

Example:

```xpp
add 5 10 sum
out sum
```

---

### Call

```xpp
call <section> [...arguments] <output>
```

Calls a section and stores the output in a variable.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Section | [Section](./sections.md) | | The target section |
| ...Arguments | ...Any | ✓ | The arguments passed to the target section |
| Output | [Variable](./variables.md) | | The output of the section |

Returns: Any

Example:

```xpp
call mySection 5 10 output
out output

:mySection a b
    add a b sum
    ret sum
```

---

### Character

```xpp
char <index> <string> [output]
```

Returns the character of a string at the specified index.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Index | [Integer](./dataTypes.md#integer) | | The index of the string |
| String | [String](./dataTypes.md#string) | | The target string |
| Output | [Variable](./variables.md) | ✓ | The character of the target string at the specified index |

Returns: [String](./dataTypes.md#string)

Example:

```xpp
char 3 "Hello, world!" output
out output
```

---

### Clear

```xpp
cls
```

Clears the terminal.

Returns: [Null](./dataTypes.md#null)

Example:

```xpp
out "Hello, world!"
cls
out "Hello, world!"
```

---

### Compare

```xpp
cmp <expression> <true branch> [false branch]
```

Creates a branch based on whether or not the expression is true.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Expression | [Expression](./comparators.md) | | The target expression |
| True Branch | [String](./dataTypes.md#string) | | The statement in string form that will be executed if the target expression is true |
| False Branch | [String](./dataTypes.md#string) | ✓ | The statement in string form that will be executed if the target expression is false |

Returns: [Null](./dataTypes.md#null)

Example:

```xpp
cmp 5 == 5 "jmp true" "jmp false"

:true
    out "5 is equal to 5"

:false
    out "5 is not equal to 5"
```

---

### Constant

```xpp
cnst <value> <variable>
```

Defines a constant variable.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Value | Any | | The value that will be stored in the variable |
| Variable | [Variable](./variables.md) | | The target variable |

Returns: [Null](./dataTypes.md#null)

Example:

```xpp
cnst 5 myInteger
out myInteger
```

---

### Decrement

```xpp
dec <value> [output]
```

Decreases a value by one.

If no output is given, the target value itself is decremented instead.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Value | [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer) | | The value that will be decremented |
| Output | [Variable](./variables.md) | ✓ | The decremented value |

Returns: [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer)

Example:

```xpp
psh 5 myInteger
dec myInteger
out myInteger
```

---

### Divide

```xpp
div <dividend> <divisor> [quotient]
```

Divides the dividend by the divisor.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Dividend | [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer) | | The value that is being divided |
| Divisor | [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer) | | The value that dividing the dividend |
| Quotient | [Variable](./variables.md) | ✓ | The quotient of the dividend and the divisor |

Returns: [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer)

Example:

```xpp
div 10 5 quotient
out quotient
```

---

### End

```xpp
end
```

Ends a section.

Returns: [Null](./dataTypes.md#null)

Example:

```xpp
:main
    out "Hello, world!"
    end
    out "Hello, world!"
```

---

### Evaluate

```xpp
evl <code>
```

Evaluate and execute the Python code.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Code | [String](./dataTypes.md#string) | | The Python code that is being evaluated and executed |

Returns: [Null](./dataTypes.md#null)

Example:

```xpp
evl "print('Hello, world!')"
```

---

### Exit

```xpp
expp
```

Exits the process.

Returns: [Null](./dataTypes.md#null)

Example:

```xpp
out "Hello, world!"
expp
out "Hello, world!"
```

---

### Float

```xpp
flt <string> [output]
```

Converts a string into a float.

If no output is given, the target string itself is converted instead.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| String | [String](./dataTypes.md#string) | | The target string |
| Output | [Variable](./variables.md) | ✓ | The converted float value |

Returns: [Float](./dataTypes.md#float)

Example:

```xpp
flt "5" myFloat
out myFloat
```

---

### Import

```xpp
imp <package/file> [as <name>]
```

Imports a package or file.

If no name is given, the package or file name is used instead.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Package / File | [String](./dataTypes.md#string) | | The relative path of package or file you want to import |
| Name | [String](./dataTypes.md#string) | ✓ | The name of the imported package of file |

Returns: [Null](./dataTypes.md#null)

Example:

```xpp
imp "myFile.xpp" as "myPackage"
```

---

### Index

```xpp
idx <substring> <string> [output]
```

Converts a string into a float.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Substring | [String](./dataTypes.md#string) | | The substring of the target string |
| String | [String](./dataTypes.md#string) | | The target string |
| Output | [Variable](./variables.md) | ✓ | The index of the substring in the target string |

Returns: [Integer](./dataTypes.md#integer)

Example:

```xpp
idx "ello" "Hello, world!" output
out output
```

---

### Increment

```xpp
inc <value> [output]
```

Increases a value by one.

If no output is given, the target value itself is incremented instead.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Value | [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer) | | The value that will be incremented |
| Output | [Variable](./variables.md) | ✓ | The incremented value |

Returns: [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer)

Example:

```xpp
psh 5 myInteger
inc myInteger
out myInteger
```

---

### Is A Number

```xpp
inm <value> [output]
```

Returns whether or not the value is a number.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Value | Any | | The target value |
| Output | [Variable](./variables.md) | ✓ | Whether or not the target value is a number |

Returns: [Integer](./dataTypes.md#integer)

Example:

```xpp
inm 5 output
out output
```

---

### Is Any Number

```xpp
inms <value> [output]
```

Returns whether or not the value is a number or a stringified number.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Value | Any | | The target value |
| Output | [Variable](./variables.md) | ✓ | Whether or not the target value is a number or a stringified number |

Returns: [Integer](./dataTypes.md#integer)

Example:

```xpp
inms "5" output
out output
```

---

### Jump

```xpp
jmp <section>
```

Jumps to another section.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Section | [Section](./sections.md) | | The target section |

Returns: [Null](./dataTypes.md#null)

Example:

```xpp
jmp mySection

:mySection
    out "Hello, world!"
```

---

### Length

```xpp
len <string> [output]
```

Returns the length of the string.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| String | [String](./dataTypes.md#string) | | The target string |
| Output | [Variable](./variables.md) | ✓ | The length of the target string |

Returns: [Integer](./dataTypes.md#integer)

Example:

```xpp
len "Hello, world!" output
out output
```

---

### Load

```xpp
load <path> [output]
```

Retrieves the content of a file.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Path | [String](./dataTypes.md#string) | | The path of the file |
| Output | [Variable](./variables.md) | ✓ | The content of the file |

Returns: [String](./dataTypes.md#string)

Example:

In `file.xpp`:

```xpp
:mySection
    out "Hello, world!"
```

In `main.xpp`:

```xpp
load "file.xpp" output
out output
```

---

### Lowercase

```xpp
lwr <string> [output]
```

Lowercases all the characters in a string.

If no output is given, the target value itself is lowercased instead.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| String | [String](./dataTypes.md#string) | | The target string |
| Output | [Variable](./variables.md) | ✓ | The lowercased string |

Returns: [String](./dataTypes.md#string)

Example:

```xpp
lwr "Hello, world!" output
out output
```

---

### Multiply

```xpp
mul <factor A> <factor B> [product]
```

Multiplies two factors together or repeats a string for a set amount of time.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Factor A | [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer) or [String](./dataTypes.md#string) | | The first factor |
| Factor B | [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer) | | The second factor |
| Product | [Variable](./variables.md) | ✓ | The product of the two factors |

Returns: [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer) or [String](./dataTypes.md#string)

Example:

```xpp
mul 5 10 product
out product
```

---

### Number

```xpp
num <string> [output]
```

Converts a string into a number.

If no output is given, the target string itself is converted instead.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| String | [String](./dataTypes.md#string) | | The target string |
| Output | [Variable](./variables.md) | ✓ | The converted number value |

Returns: [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer)

Example:

```xpp
num "5" myInteger
out myInteger
```

---

### Output

```xpp
out [...value]
```

Outputs a value into the terminal.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Value | Any | ✓ | The target values |

Returns: [Null](./dataTypes.md#null)

Example:

```xpp
out "Hello, world!"
```

---

### Pop

```xpp
pop <variable> [output]
```

Parses the variable and returns its value.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Variable | Any | | The target variable |
| Output | [Variable](./variables.md) | ✓ | The value of the parsed variable |

Returns: Any

Example:

```xpp
psh 5 myInteger
pop "myInterger" output
out output
```

---

### Provoke

```xpp
pvk <section> [...arguments]
```

Provokes a section.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Section | [Section](./sections.md) | | The target section |
| ...Arguments | ...Any | ✓ | The arguments passed to the target section |

Returns: Any

Example:

```xpp
pvk mySection 5 10

:mySection a b
    add a b sum
    out sum
```

---

### Push

```xpp
psh <value> <variable>
```

Defines a variable.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Value | Any | | The value that will be stored in the variable |
| Variable | [Variable](./variables.md) | | The target variable |

Returns: [Null](./dataTypes.md#null)

Example:

```xpp
psh 5 myInteger
out myInteger
```

---

### Random Number Generator

```xpp
rng <minimum> <maximum> [output]
```

Generates a random integer within the range. Both the minimum and maximum values are inclusive.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Minimum | [Integer](./dataTypes.md#integer) | | The minimum range |
| Maximum | [Integer](./dataTypes.md#integer) | | The maximum range |
| Output | [Variable](./variables.md) | ✓ | The randomized integer within the range |

Returns: [Integer](./dataTypes.md#integer)

Example:

```xpp
rng 0 5 myInteger
out myInteger
```

---

### Read

```xpp
read [prompt] [output]
```

Gets input from the user.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Prompt | Any | ✓ | The prompt outputted in the terminal |
| Output | Any | ✓ | The user input |

Returns: [Null](./dataTypes.md#null)

Example:

```xpp
read "What is your name: " name
out name
```

---

### Remove

```xpp
rem <variable>
```

Deletes a variable from the memory.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Variable | [Variable](./variables.md) | | The target variable |

Returns: [Null](./dataTypes.md#null)

Example:

```xpp
psh 5 myInteger
out myInteger
rem myInteger
out myInteger
```

---

### Repeat

```xpp
rep <amount> <statement>
```

Executes a statement for a set amount of times.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Amount | [Integer](./dataTypes.md#integer) | | The amount of times the statement will be executed |
| Statement | [String](./dataTypes.md#string) | | The statement in string form that will be executed |

Returns: [Null](./dataTypes.md#null)

Example:

```xpp
rep 5 "out \"Hello, world!\""
```

---

### Return

```xpp
ret <value>
```

Returns a value within a section.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Value | any | | The return value |

Returns: [Null](./dataTypes.md#null)

Example:

```xpp
:mySection
    ret 5
```

---

### Round

```xpp
rnd <number> [precision]
```

Rounds a number to a certain decimal point.

If no output is given, it is rounded to the nearest whole number instead.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Number | [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer) | | The return value |
| Precision | [Integer](./dataTypes.md#integer) | ✓ | The return value |

Returns: [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer)

Example:

```xpp
psh 5.5 myInteger
rnd myInteger
out myInteger
```

---

### Save

```xpp
save <path> [output]
```

Writes the content into a file.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Path | [String](./dataTypes.md#string) | | The path of the file |
| Value | [String](./dataTypes.md#string) | | The content of the file |

Returns: [Null](./dataTypes.md#null)

Example:

```xpp
save "file.xpp" "Hello, world!"
```

---

### Skip

```xpp
skp
```

Acts as a placeholder for a section.

Returns: [Null](./dataTypes.md#null)

Example:

```xpp
skp
```

---

### Slice

```xpp
slc <start> <end> <string> [output]
```

Returns the chunk of the string from the starting and ending index.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Start | [Integer](./dataTypes.md#integer) | | The starting index |
| End | [Integer](./dataTypes.md#integer) | | The ending index |
| String | [String](./dataTypes.md#string) | | The string that is being sliced |
| Output | [Variable](./variables.md) | ✓ | The chunk sliced from the target string |

Returns: [String](./dataTypes.md#string)

Example:

```xpp
slc 0 5 "Hello, world!" output
out output
```

---

### String

```xpp
str <value> [output]
```

Converts a value into a string.

If no output is given, the target value itself is converted instead.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Value | Any | | The target string |
| Output | [Variable](./variables.md) | ✓ | The converted string value |

Returns: [String](./dataTypes.md#string)

Example:

```xpp
str 5 myString
out myString
```

---

### Subtract

```xpp
sub <minuend> <subtrahend> [difference]
```

Subtracts the minuend from the subtrahend.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Minuend | [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer) | | The value that is being subtracted |
| Subtrahend | [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer) | | The value that subtracting the minuend |
| Difference | [Variable](./variables.md) | ✓ | The difference of the minuend and the subtrahend |

Returns: [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer)

Example:

```xpp
sub 10 5 difference
out difference
```

---

### Throw

```xpp
thrw <message>
```

Throws an error message and exits the process.

Even though the message parameter is required, if no message is provided, a RangeError is thrown instead.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Message | Any | | The message of the error |

Returns: [Null](./dataTypes.md#null)

Example:

```xpp
out "Hello, world!"
thrw "Error message!"
out "Hello, world!"
```

---

### Try

```xpp
try <statement> [error statement]
```

Executes the statement. If an error is thrown, the exception statement is executed instead.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Statement | [String](./dataTypes.md#string) | | The statement in string form that will be executed |
| Error Statement | [String](./dataTypes.md#string) | ✓ | The statement in string form that will be executed if an error is thrown |

Returns: [Null](./dataTypes.md#null)

Example:

```xpp
try "thrw \"Error message!\"" "out \"An error has occurred\""
```

---

### Uppercase

```xpp
upr <string> [output]
```

Uppercases all the characters in a string.

If no output is given, the target value itself is uppercased instead.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| String | [String](./dataTypes.md#string) | | The target string |
| Output | [Variable](./variables.md) | ✓ | The uppercased string |

Returns: [String](./dataTypes.md#string)

Example:

```xpp
upr "Hello, world!" output
out output
```

---

### Wait

```xpp
wait <seconds>
```

Waits a certain number of seconds before executing the nexpp statement.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Seconds | [Integer](./dataTypes.md#string) | | The number of seconds waited |

Returns: [Null](./dataTypes.md#null)

Example:

```xpp
out "Hello, world!"
wait 5
out "Hello, world!"
```

---

### While

```xpp
whl <expression> <statement>
```

Executes the statement until the expression is false.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Expression | [Expression](./comparators.md) | | The target expression |
| Statement | [String](./dataTypes.md#string) | | The statement in string form that will be executed while the expression is true |

Returns: [Null](./dataTypes.md#null)

Example:

```xpp
psh 0 @myInteger
whl @myInteger < 5 "jmp mySection"

:mySection
    out @myInteger
    inc @myInteger
```

---

Last Updated: February 6th, 2022 by Dm123321_31mD

[↑ Go To Top](#x--documents--operators)