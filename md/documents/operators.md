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

- [Character](#character)
- [Clear](#clear)

### D

- [Decrement](#decrement)
- [Divide](#divide)

### E

- [Eval](#eval)
- [Exit](#exit)

### F

- [Float](#float)

### I

- [If](#if)
- [Increment](#increment)
- [Index](#index)
- [Integer](#integer)
- [Import](#import)

### J

- [Jump](#jump)

### L

- [Length](#length)
- [Load](#load)
- [Lowercase](#lowercase)

### M

- [Multiply](#multiply)

### P

- [Power](#power)
- [Print](#print)

### R

- [Random Number Generator](#random-number-generator)
- [Remove](#remove)
- [Repeat](#repeat)
- [Return](#return)
- [Round](#round)

### S

- [Save](#save)
- [String](#string)
- [Subtract](#subtract)

### T

- [Throw](#throw)
- [Try](#try)

### U

- [Uppercase](#uppercase)

### V

- [Variable](#variable)

### W

- [Wait](#wait)
- [While](#while)

## About

Operators are keywords that process arguments.

A statement is a line of code that tells the interpreter what to do. They are always made up of two components: the `operator` and the `arguments`, and they are arranged like so:

```xpp
<operator> [...arguments] [...?outputs]
```

For example:

```xpp
prt "Hello, world!"
```

Or:

```xpp
add 1 2 ?sum
```

A statement can also be wrapped around parentheses (`()`) to group them.

Some statements return values, which can be stored in a variable:

```xpp
var (add 1 2) sum
```

## Documentation

### Add

```xpp
add <addend A> <addend B> [?sum]
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
add 5 10 ?sum
prt sum
```

---

### Character

```xpp
chr <string> <index> [stop] [?output]
```

Returns a substring of `string` from index `index` to `stop`. If `stop` is not provided, `chr` will return the character at `index`.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| String | [String](./dataTypes.md#string) | | The target string |
| Index | [Integer](./dataTypes.md#integer) | | The index of the string |
| Stop | [Integer](./dataTypes.md#integer) | ✓ | The index of the string |
| Output | [Variable](./variables.md) | ✓ | The resulting substring or character |

Returns: [String](./dataTypes.md#string)

Example:

```xpp
chr "Hello, world!" 3 5 ?output
chr "Hello, world!" 3 ?output2
prt output output2
:: "lo," "l"
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
prt "Hello, world!"
cls
prt "Why hello there!"
```

---

### If

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

### Decrement

```xpp
dec <value> <value_2> <...> [?output]
```

Decreases all given values by one.

If no output is given, the target value itself is decremented instead.  
If output is specified, but multiple values are decremented. The result will be [null](./dataTypes.md#null).

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Value(s) | [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer) | | The value that will be decremented |
| Output | [Variable](./variables.md) | ✓ | The decremented value |

Returns: [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer)

Example:

```xpp
var myInteger 5
dec myInteger
prt myInteger
:: 4
```

---

### Divide

```xpp
div <dividend> <divisor> <divisor_2> <...> [?quotient]
```

Divides the dividend by the divisor (in sequential order, if multiple given).

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Dividend | [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer) | | The value that is being divided |
| Divisor(s) | [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer) | | The value that is dividing the dividend |
| Quotient | [Variable](./variables.md) | ✓ | The quotient of the dividend and the divisor |

Returns: [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer)

Example:

```xpp
div 10 5 ?quotient
prt quotient
:: 2
```

---

### Evaluate

```xpp
evl <code>
```

Evaluate and execute Python code.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Code | [String](./dataTypes.md#string) | | The Python code that is being evaluated |

Returns: [Null](./dataTypes.md#null)

Example:

```xpp
evl "print('Hello, world!')"
```

---

### Exit

```xpp
exit
```

Exits the process.

Returns: [Null](./dataTypes.md#null)

Example:

```xpp
prt "Hello, world!"
exit
prt "You'll never see me! Aha!"
```

---

### Float

```xpp
flt <string> <?output>
```

Converts a string into a float.

Output is **not** required, however the operator call will do nothing if no output is provided.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| String | [String](./dataTypes.md#string) | | The target string |
| Output | [Variable](./variables.md) | ✓ | The converted float value |

Returns: [Float](./dataTypes.md#float)

Example:

```xpp
flt "5" ?myFloat
prt myFloat
```

---

### Import

```xpp
imp <package/file/python file> [as <name>]
```

Imports a package, file, or Python script.

If no name is given, the package or file name is used instead. For example, `imp "extras"` will require you to use `jmp extras.section`; but `imp "extras" as "hi"` will allow you to use `jmp hi.section` instead.  
If `path` does not begin with `./`, the path will be assumed to be `pkgs/<module>/<module>.xpp` if there isn't a `.xconfig` file in the module directory stating another file to load.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Package / File | [String](./dataTypes.md#string) | | The path of package or file you want to import |
| Name | [String](./dataTypes.md#string) | ✓ | The name of the imported package of file |

Returns: [Null](./dataTypes.md#null)

Example:

```xpp
imp "myFile.xpp" as "myPackage"
```

---

### Index

```xpp
idx <string> <substring> [?output]
```

Converts a string into a float.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| String | [String](./dataTypes.md#string) | | The target string |
| Substring | [String](./dataTypes.md#string) | | The substring of the target string |
| Output | [Variable](./variables.md) | ✓ | The index of the substring in the target string |

Returns: [Integer](./dataTypes.md#integer)

Example:

```xpp
idx "Hello, world!" "ello" ?output
prt output
:: 1
```

---

### Increment

```xpp
inc <value> <value_2> <...> [?output]
```

Increases all given values by one.

If no output is given, the target value itself is incremented instead.  
If output is specified, but multiple values are incremented. The result will be [null](./dataTypes.md#null).

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Value(s) | [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer) | | The value that will be incremented |
| Output | [Variable](./variables.md) | ✓ | The incremented value |

Returns: [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer)

Example:

```xpp
var myInteger 5
inc myInteger
prt myInteger
:: 6
```

---

### Jump

```xpp
jmp <section> [...arguments] [?output1] [?output_n] [?...]
```

Jumps to a section, provides it with arguments, and stores the output(s) in a variable (or multiple, depending on how many the section returns).

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Section | [Section](./sections.md) | | The target section |
| ...Arguments | ...Any | ✓ | The arguments passed to the target section |
| ...Outputs | [Variable](./variables.md) | ✓ | The output(s) of the section |

Returns: Any

Example:

```xpp
:mySection a b
    add a b ?sum
    ret ?sum

jmp mySection 5 10 ?output
prt output
:: 15
```

---

### Length

```xpp
len <string> [?output]
```

Returns the length of the string.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| String | [String](./dataTypes.md#string) | | The target string |
| Output | [Variable](./variables.md) | ✓ | The length of the target string |

Returns: [Integer](./dataTypes.md#integer)

Example:

```xpp
len "Hello, world!" ?output
prt output
:: 13
```

---

### Load

```xpp
load <path> <output>
```

Retrieves the content of a file.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Path | [String](./dataTypes.md#string) | | The path of the file |
| Output | [Variable](./variables.md) | | The content of the file |

Returns: [String](./dataTypes.md#string)

Example:

In `file.xpp`:

```xpp
:mySection
    prt "Hello, world!"
```

In `main.xpp`:

```xpp
load "file.xpp" ?output
prt output
:: :mySection
::     prt "Hello, world!"
```

---

### Lowercase

```xpp
lwr <string> [?output]
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
lwr "Hello, world!" ?output
prt output
:: hello, world!
```

---

### Multiply

```xpp
mul <factor_1> <factor_2> <factor_n> <...> [product]
```

Multiples all given factors together in sequential order.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Factor 1 | [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer) or [String](./dataTypes.md#string) | | The first factor |
| Factor 2 | [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer) | | The second factor |
| Factor N | [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer) | ✓ | The nth factor |
| Product | [Variable](./variables.md) | ✓ | The product of the factors |

Returns: [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer) or [String](./dataTypes.md#string)

Example:

```xpp
mul 5 10 ?product
prt product
:: 50
```

---

### Integer

```xpp
int <string> [?output]
```

Converts a string into an integer.  
If no output is given, the target string itself is converted instead.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| String | [String](./dataTypes.md#string) | | The target string |
| Output | [Variable](./variables.md) | ✓ | The converted number value |

Returns: [Integer](./dataTypes.md#integer)

Example:

```xpp
int "5" ?myInteger
prt myInteger
:: 5
```

---

### Print

```xpp
prt [...value]
```

Prints value(s) into the terminal.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Value | Any | ✓ | The target value(s) |

Returns: [Null](./dataTypes.md#null)

Example:

```xpp
prt "Hello, world!"
```

---

### Variable

```xpp
var <value> <variable>
```

Defines a variable.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Value | Any | | The value that will be stored in the variable |
| Variable | [Variable](./variables.md) | | The target variable |

Returns: [Null](./dataTypes.md#null)

Example:

```xpp
var 5 myInteger
prt myInteger
```

---

### Read

```xpp
read [prompt] [?output]
```

Gets input from the user.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Prompt | Any | ✓ | The prompt outputted in the terminal |
| Output | Any | ✓ | The user input |

Returns: [Null](./dataTypes.md#null)

Example:

```xpp
read "What is your name: " ?name
prt name
```

---

### Random Number Generator

```xpp
rng <minimum> <maximum> [?output]
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
rng 0 5 ?myInteger
prt myInteger
```

---

### Remove

```xpp
rem <variable>
```

Deletes a variable from memory.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Variable | [Variable](./variables.md) | | The target variable |

Returns: [Null](./dataTypes.md#null)

Example:

```xpp
var 5 myInteger
prt myInteger
rem myInteger
prt myInteger
```

---

### Repeat

```xpp
rep <amount> <statement>
```

Executes a statement a set amount of times.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Amount | [Integer](./dataTypes.md#integer) | | The amount of times the statement will be executed |
| Statement | [String](./dataTypes.md#string) | | The statement in string form that will be executed |

Returns: [Null](./dataTypes.md#null)

Example:

```xpp
rep 5 "prt 'Hello, world!'"
```

---

### Return

```xpp
ret [value_1] [value_2] [value_n] [...]
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