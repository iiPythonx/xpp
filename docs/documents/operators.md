# [x++](../README.md) / [Documents](../documents.md) / Operators

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
        - **Operators ▾**
            - [Table of Contents](#table-of-contents)
            - [Catalog](#catalog)
            - [About](#about)
            - [Documentation](#documentation)
        - [Packages](packages.md)
        - [Sections](sections.md)
        - [Variables](variables.md)
- [Python API](../python-api.md)
- [Caffeine](../caffeine.md)
- [Standard Library](../stdlib.md)

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

- [Eval](#evaluate)
- [Exit](#exit)

### F

- [Float](#float)

### G

- [Get](#get)

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

### N

- [New](#new)

### P

- [Pop](#pop)
- [Power](#power)
- [Print](#print)
- [Push](#push)

### R

- [Random Number Generator](#random-number-generator)
- [Remove](#remove)
- [Repeat](#repeat)
- [Return](#return)
- [Round](#round)

### S

- [Save](#save)
- [Set](#set)
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

or:

```xpp
add 1 2 ?sum
```

A statement can also be wrapped around parentheses (`()`) to group them.

Some statements return values, which can be stored in a variable:

```xpp
var sum (add 1 2)
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

### Get

```xpp
get <object> <key> [?output]
```

Retrieves the specified key from the given object.  
If object is a list, retrieve the value at index `key`.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Object | **Dict** | | The source object |
| Key | **Any** | | The key to retrieve |
| Output | [Variable](./variables.md) | ✓ | The retrieved value |

Returns: **Any**

Example:

```xpp
flt "5" ?myFloat
prt myFloat
```

---

### If

```xpp
if <expr1> <branch1> [expr_n] [branch_n] [...] [else_branch]
```

Creates a branch based on whether or not the given expression(s) are true.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Expression 1 | [Expression](./comparators.md) | | The first expression |
| Branch 1 | [String](./dataTypes.md#string) | | Statement to execute if first branch is true |
| Expression N | [Expression](./comparators.md) | ✓ | The nth expression |
| Branch N | [String](./dataTypes.md#string) | ✓ | Statement to execute if nth branch is true |
| Else Branch | [String](./dataTypes.md#string) | ✓ | Statement to execute if all expressions were false |

Returns: [Null](./dataTypes.md#null)

Example:

```xpp
if (5 == 5) "jmp istrue" "jmp isfalse"

:istrue
    prt "5 is equal to 5"

:isfalse
    prt "5 is not equal to 5 somehow"
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

### New

```xpp
new <type> [?output]
```

Creates a new object of the specified type, returning it.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Type| [String](./dataTypes.md#string) | | 'list' or 'dict' |
| Output | [Variable](./variables.md) | ✓ | The new object |

Returns: **List** or **Dict**

Example:

```xpp
new "list" ?list
prt list
:: []
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

### Pop

```xpp
pop <list> [?output]
```

Removes the last item from a list and returns it.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| List | **List** | | The list to use |
| Output | [Variable](./variables.md) | ✓ | The last item |

Returns: **Any**

Example:

```xpp
new "list" ?list
psh list 5
pop list ?result
prt result list
:: 5 []
```

---

### Power

```xpp
pow <exp_1> <exp_2> <exp_n> <...> [result]
```

Takes all given exponents and powers them together in sequential order.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Exponent 1 | [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer) or [String](./dataTypes.md#string) | | The first exponent |
| Exponent 2 | [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer) | | The second exponent |
| Exponent N | [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer) | ✓ | The nth exponent |
| Result | [Variable](./variables.md) | ✓ | The result |

Returns: [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer)

Example:

```xpp
pow 2 2 ?result
prt result
:: 4
```

---

### Push

```xpp
psh <list> <value>
```

Pushes an item into a list's stack.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| List | **List** | | The list to use |
| Value | **Any** | | The item to push |

Returns: [Null](./dataTypes.md#null)

Example:

```xpp
new "list" ?list
psh list 5
prt list
:: [5]
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
rnd <number> [precision] [?output]
```

Rounds a number to a certain decimal point.  
If no precision is given, it is rounded to the nearest whole number instead.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Number | [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer) | | The number to round |
| Precision | [Integer](./dataTypes.md#integer) | ✓ | The precision to round to |
| Output | [Integer](./dataTypes.md#integer) | ✓ | The rounded number |

Returns: [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer)

Example:

```xpp
var myInteger 5.5
rnd myInteger
prt myInteger
:: 6
```

---

### Save

```xpp
save <path> <value> [encoding]
```

Writes the content into a file.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Path | [String](./dataTypes.md#string) | | The path of the file |
| Value | [String](./dataTypes.md#string) | | The content of the file |
| Encoding | [String](./dataTypes.md#string) | ✓ | The file encoding (utf8 is the default) |

Returns: [Null](./dataTypes.md#null)

Example:

```xpp
save "file.xpp" "Hello, world!" "utf8"
```

---

### Set

```xpp
set <dict> <key> <value>
```

Sets a key-value pair inside the given dictionary.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Dict | **Dict** | | The dict to update |
| Key | **Any** | | The key to use |
| Value | **Any** | | The value of the key |

Returns: [Null](./dataTypes.md#null)

Example:

```xpp
new "dict" ?dict
set dict "x" "Hello, world!"
prt (get dict "x")
:: Hello, world!
prt dict
:: { "x": "Hello, world!" }
```

---

### String

```xpp
str <value> [?output]
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
str 5 ?myString
prt myString
:: "5"
```

---

### Subtract

```xpp
sub <term_1> <term_2> <term_n> <...> [?result]
```

Subtracts all given terms from eachother in order.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Term 1 | [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer) | | The first value |
| Term 2 | [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer) | | The second value |
| Term N | [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer) | ✓ | The nth value |
| Result | [Variable](./variables.md) | ✓ | The difference of all given terms |

Returns: [Float](./dataTypes.md#float) or [Integer](./dataTypes.md#integer)

Example:

```xpp
sub 10 5 ?difference
prt difference
:: 5
```

---

### Throw

```xpp
thrw [message]
```

Throws an error message and exits the process.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Message | Any | ✓ | The message of the error |

Returns: [Null](./dataTypes.md#null)

Example:

```xpp
prt "Hello, world!"
thrw "Error message!"
prt "Haha! Can't see me!"
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
try "thrw 'Error message!'" "prt 'An error has occurred'"
:: An error has occured
```

---

### Uppercase

```xpp
upr <string> [?output]
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
upr "Hello, world!" ?output
prt output
```

---

### Wait

```xpp
wait <seconds>
```

Waits a certain number of seconds before executing the next statement.

| Parameter | Type | Optional | Description |
| :-: | :-: | :-: | :-: |
| Seconds | [Integer](./dataTypes.md#string) | | The number of seconds to wait |

Returns: [Null](./dataTypes.md#null)

Example:

```xpp
prt "Hello, world!"
wait 5
prt "Hello, world!"
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
:mySection a
    out a
    inc a
    ret a

var myInteger 0
whl (myInteger < 5) "jmp mySection myInteger ?myInteger"

:: 0
:: 1
:: 2
:: 3
:: 4
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

Last Updated: March 9th, 2024 by iiPython

[↑ Go To Top](#x--documents--operators)