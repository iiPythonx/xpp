# x2

## Table of Contents
- [**About**](#about)
- [**Installation**](#installation)
- [**Basics**](#basics)
- [**Configuration**](#configuration)
- [**Syntax**](#syntax)
    - [Operators](#operators)
    - [Sections](#sections)
    - [Data Types](#data-types)
    - [Expressions](#expressions)
    - [Other](#other)
- [**Packages**](#packages)
- [**Links**](#links)
    - [Github](https://github.com/ii-Python)
    - [Syntax Highlighter](https://github.com/Dm12332131mD/x2-theme)
    - [Syntax Highlighter Extension](https://marketplace.visualstudio.com/items?itemName=iiPython.x2)
    - [Repository](https://github.com/ii-Python/x2)
    - [Website](https://x2.iipython.cf/)

## About

x2 is a miniminalistic, open-source programming language created by [**iiPython**](https://github.com/ii-Python), inspired by [**x86 assembly**](https://en.wikipedia.org/wiki/X86_assembly_language) and [**batch**](https://en.wikipedia.org/wiki/Batch_file). It is a [**high-level language**](https://en.wikipedia.org/wiki/High-level_programming_language) with low-level, easy-to-remember syntax, similar to [**assembly**](https://en.wikipedia.org/wiki/X86_assembly_language).

An x2 file can have any name and should end with the extension `.xt`. It uses a [**Python**](https://python.org) interpreter to execute the x2 code.  
Check out [**how to install x2**](#installation) and [**the basics**](#basics) to get started with x2.

## Installation

To get started, you must have an installation of [**Python**](https://python.org).  
[**Python 3.11**](https://www.python.org/downloads/release/python-3110a5/) or above is recommended, but the minimal requirement is [**Python 3.10**](https://www.python.org/downloads/release/python-3100/).

You can check the version of your [**Python**](https://python.org) installation by opening up a terminal and typing:

```
python -V
```

Next, go to the [**x2 repository**](https://github.com/ii-Python/x2) and clone it onto your device.  
or, if you have [**git**](https://git-scm.com/) installed on your device, you can type the following into your terminal instead:

```
git clone https://github.com/ii-Python/x2
```

If you are using [**Visual Studio Code**](https://code.visualstudio.com/) as your text editor, you can also install the [**x2 syntax highlighter extension**](https://marketplace.visualstudio.com/items?itemName=iiPython.x2).

## Basics

Once you finish installing the x2 interpreter, you should be able to find a file named `main.xt`. This is your default entry point for your project. You can edit the entry point by following the [**configuration guide**](#configuration).

Inside the `main.xt` file is the Hello World example for the x2 language.

```
:main
    out "Hello World"
```

You can begin editing the `main.xt` file to start programming in x2.

Once you are done editing the file, open up a terminal in the folder and execute the `main.py` interpreter by typing:

```
python main.py
```

In the example above, you should see the following output when executing the interpreter

```
Hello World
```

## Configuration

Inside the x2 interpreter, you should also find a file called `.xtconfig`. Inside is your configuration for the x2 interpreter.  
Below is the default configurations of the x2 interpreter:

```json
{
    "main": "main.xt",
    "quiet": false
}
```

The `main` field is the default entry point when executing the `main.py` file. The path is relative to the current working directory of your terminal.

Optionally, you can also type the following to ignore the default entry point:

```
python main.py <file>.xt
```

For example:

```
python main.py test.xt
```

## Syntax

The syntax of the x2 language is fairly simple. Below you can find a list of all the operators and techniques with examples attached.

---

### Table of Contents

- [Operators](#operators)
- [Sections](#sections)
- [Data Types](#data-types)
- [Expressions](#expressions)
- [Other](#other)

---

### Operators

An operator defines an action in which the x2 interpreter would execute. The operator always comes at the beginning of the line. It is then followed by its arguments.

---

#### - **add**

The `add` operator adds two numbers together and appends two strings together.

Syntax:

```
add <a> <b> <output>
```

Example:

```
:main
    psh 5 a
    psh 10 b
    add a b output
    out output
    :: 15
```

```
:main
    psh "Hello " a
    psh "World" b
    add a b output
    out output
    :: "Hello World"
```

---

#### - **call**

The `call` operator calls and passes arguments to a section. It is usually used with the operator `ret`.

See [**sections**](#sections) in the sections guide for more information.

Syntax: 

```
call <section> <_a1> <_a2> <_a...> <output>
```

Example:

```
:main
    call appendString "Hello " "World" output
    out output
    :: "Hello World"

:appendString a b
    ret (add a b)
```

---

#### - **cmp**

The `cmp` operator compares two variables and executes a branch.

See [**expressions**](#expressions) in the expressions guide for more information.

Syntax:

```
cmp <expression> <branch true> [branch false]
```

Example:

```
:main
    psh 5 a
    psh 10 b
    cmp a == b "jmp true" "jmp false"
    :: "The values are different!"

:true
    out "The values are equal!"

:false
    out "The values are different!"
```

#### - **cls**

The `cls` operator clears the screen.

Syntax:

```
cls
```

Example:

```
:main
    out "Hello World"
    cls
    out "Oh no! I am alone!"
```

---

#### - **dec**

The `dec` operator decreases a number by 1.

Syntax:

```
dec <variable>
```

Example:

```
:main
    psh 5 number
    dec number
    out number
    :: 4
```

---

#### - **div**

The `div` operator divides a number by another number.

Syntax:

```
div <a> <b> <output>
```

Example:

```
:main
    div 6 2 output
    out output
    :: 3
```

---

#### - **evl**

The `evl` operator executes Python code in the context of the x2 interpreter.  
It is recommended to not be used as it can be unreliable.

Syntax:

```
evl <expression>
```

Example:

```
:main
    evl "x2.setvar('a', 'b')"
    out b  :: a
```

---

#### - **ext**

The `ext` operator exits the x2 interpreter.

Syntax:

```
ext [status_code]
```

Example:

```
:main
    out "Hello World"
    ext
    out "What about me??? :C"
```

---

#### - **inc**

The `inc` operator increases a number by 1.

Syntax:

```
inc <variable>
```

Example:

```
:main
    psh 5 number
    inc number
    out number
    :: 6
```

---

#### - **inm**

The `inm` operator checks if a variable is a number and outputs a 1 if it is true or 0 if it is not.

See [**data types**](#data-types) in the data types guide for more information.

Syntax:

```
inm <variable> <output>
```

Example:

```
:main
    psh "Hello World" number
    inm number output
    cmp output == 1 "out \"It is a number!\"" "out \"It is NOT a number!\""
    :: "It is NOT a number!"
```

---

#### - **inms**

The `inms` operator is similar to the `inm` operator.  
It checks if a variable or a string is a number and outputs a 1 if it is true or 0 if it is not.

See [**data types**](#data-types) in the data types guide for more information.

Syntax:

```
inms <variable> <output>
```

Example:

```
:main
    psh "5" number
    inms number output
    cmp output == 1 "out \"It is a number!\"" "out \"It is NOT a number!\""
    :: "It is a number"
```

---

#### - **imp**

The `imp` operator imports another x2 file to the current workspace.

See [**importing packages from another file**](#packages) in the packages guide for more information.

Syntax:

```
imp <path>
```

Example:

```
imp "stdlib"

:main
    out "Hello World"
```

---

#### - **jmp**

The `jmp` operator allows the x2 interpreter to jump to another section.  
See [**sections**](#sections) in the sections guide for more information.

Syntax:

```
jmp <section>
```

Example:

```
:main
    jmp print
    :: "Hello World"

:print
    out "Hello World"
```

---

#### - **lwr**

The `lwr` operator turns the given string into all lowercase letters.

Syntax:

```
lwr <variable>
```

Example:

```
:main
    psh "Hello World" string
    lwr string
    out string
    :: "hello world"
```

---

#### - **mul**

The `mul` operator multiplies two numbers together.

Syntax:

```
mul <a> <b> <output>
```

Example:

```
:main
    psh 5 a
    psh 10 b
    mul a b output
    out output
    :: 50
```

---

#### - **num**

The `num` operator turns the variable into a number.

See [**data types**](#data-types) in the data types guide for more information.

Syntax:

```
num <variable>
```

Example:

```
:main
    psh "5" number
    num number
    out number
    :: 5
```

---

#### - **out**

The `out` operator prints a variable or a string into the terminal.

Syntax:

```
out [argument(s)]
```

Example:

```
:main
    out "Hello World"
    :: "Hello World"
```

---

#### - **pop**

The `pop` operator pops a value from a variable. This is especially useful when used inside a string template literal.

Syntax:

```
pop <variable> [output]
```

Example:

```
:main
    psh "Hello World" string
    out "$(pop string)"
    :: "Hello World"
```

---

#### - **psh**

The `psh` operator stores a value as a variable.

Syntax:

```
psh <value> <variable>
```

Example:

```
:main
    psh "Hello World" variable
```

---

#### - **read**

The `read` operator waits for an input and stores it as a variable.

Syntax:

```
read [prompt] [output]
```

Example:

```
:main
    out "What is your name?"
    read "> " name
    out "Your name is $(name)"
    :: "Your name is <name>"
```

---

#### - **rem**

The `rem` operator removes a variable from the memory.

Syntax:

```
rem <variable>
```

Example:

```
:main
    psh "Hello World" string
    out string
    :: "Hello World"
    rem string
    out string
    :: None
```

---

#### - **rep**

The `rep` operator repeats a section.

See [**sections**](#sections) from the sections guide for more information.

Syntax:

```
rep <amount> <section>
```

Example:

```
:main
    rep 5 print
    :: "Hello World"
    :: "Hello World"
    :: "Hello World"
    :: "Hello World"
    :: "Hello World"

:print
    out "Hello World"
```

---

#### - **ret**

The `ret` operator returns a value. It is usually used with the `call` operator.  
See [**sections**](#sections) in the sections guide for more information.

Syntax:

```
ret <variable>
```

Example:

```
:main
    call appendString "Hello " "World" output
    out output
    :: "Hello World"

:appendString a b
    add a b result
    ret result
```

---

#### - **rnd**

The `rnd` operator rounds a number to the nearest whole number.

Syntax:

```
rnd <variable> [precision]
```

Example:

```
:main
    psh 5.5 number
    rnd number
    out number
    :: 6
```

---

#### - **rng**

The `rng` operator picks a random whole number from a range.

Syntax:

```
rng <a> <b> <output>
```

Example:

```
:main
    rng 0 5 number
    out number
    :: 3 (Any number from 0 - 5)
```

---

#### - **sub**

The `sub` operator subtracts a number from another.

Syntax:

```
sub <a> <b> <output>
```

Example:

```
:main
    psh 5 a
    psh 10 b
    sub a b output
    out output
    :: -5
```

---

#### - **str**

The `str` operator turns a variable into a string.  
See [**data types**](#data-types) in the data types guide for more information.

Syntax:

```
tstr <variable>
```

Example:

```
:main
    psh 5 number
    str number
    out number
    :: "5"
```

---

#### - **upr**

The `upr` operator turns the given string into all uppercase letters.

Syntax:

```
upr <variable>
```

Example:

```
:main
    psh "Hello World" string
    upr string
    out string
    :: "HELLO WORLD"
```

---

#### - **whl**

The `whl` operator will continuously call a section until the expression is false.

See [**expressions**](#expressions) in the expressions guide for more information.  
See [**sections**](#sections) in the sections guide for more information.

Syntax:

```
whl <expression> <section>
```

Example:

```
:main
    psh 0 @number
    whl @number != 5 print
    :: "Hello World"
    :: "Hello World"
    :: "Hello World"
    :: "Hello World"
    :: "Hello World"
    :: "Hello World"

:print
    out "Hello World"
    inc @number
```

---

### Sections

A section defines a chunk of code where it can then be executed separately multiple times.  
To define a section, simply append a colon (`:`) at the beginning of the section name:

```
:<name>
```

For example:

```
:print
```

The entry section is always called `main` and is necessary in all entry points.  
It is a good practice to always put your `main` section at the top with any user-defined sections at the bottom:

```
:main
    jmp print

:print
    out "Hello World"
```

A section may be blank:

```
:main

:print
    out "Hello World"
```

If a section is merged with another section, only the first one would be valid. The other sections would be ignored and not defined in memory. 

```
:main :print
    out "Hello World"
```

In the example above, only `main` would be defined properly. Even though the section `print` is also present in the code, it is ignored by the interpreter, thus does not exist when attempting to jump into the section.

A section may take arguments when it is used with the `call-ret` pair. It then returns a value and stores it in the last argument.

A proper `call` operator should look like this:

```
call <section> <_a1> <_a2> <_a...> <output>
```

And a proper `ret` operator should look like this:

```
ret <variable>
```

Note that a `ret` operator is not always necessary in a `call-ret` pair if the section does not return a value. However, a return variable is still mandatory in that situation.

Arguments in a section are defined after the section name, for example: `:hello arg1 arg2 arg3`. These arguments are in the local scope and garbage collected upon section end.

Below is an example of a proper `call-ret` section.

```
:main
    call addExclamationMark "Hello World" output
    out output
    :: "Hello World!"

:addExclamationMark text
    ret "$(pop text)!"
```

---

### Data Types

There are a total of 3 data types in the x2 language.

---

#### - **str**

The `str` data type is a string value that can represent a character, a word, a phrase, or a sentence. It is always wrapped around with double quotes (`"`):

```
"<string>"
```

For example:

```
"Hello World"
```

Strings can be compared using the following comparators:

```
==
!=
in
xin
```

See [**expressions**](#expressions) in the expressions guide for more information.

Some characters have special meanings, that means if you want to use these characters as a literal form in a string, you need to escape them. This is done by adding a back-slash `\` immediately in front of the character:

```
"\<character>"
```

For example:

```
"\t"
"\r"
"\n"
"\\"
"\""
"\033["
"\"Hello World\""
```

You can also use what is called a `string template literal` to wrap other variables inside a string:

```
"$(<variable>)"
```

Inside a `string template literal`, you can insert another instruction or variable inside. For example:

```
"$(pop number)"
```

Note that a nested `string template literal` is not allowed. See [**how to get values from variable names**](#others) in the technieques guide for more information.

---

#### - **int**

The `int` data type is an number that can represent any integers. It, however, cannot store any decimal points. An integer can be positive or negative, and is not wrapped around double quotes (`"`):

```
<integer>
-<integer>
```

For example:

```
5
-5
```

All numbers, including integers, can be increased or decreased using mathematical [**operators**](#operators):

```
inc 5
dec 5
add 5 10 output
sub 5 10 output
mul 5 10 output
div 5 10 output
```

See [**operators**](#operators) in the operators guide for more information.

Integers can also be used a booleans, where 0 represents a false value and 1 represents a true value.  
All numbers, including integers, can also use the following comparators:

```
==
<
<=
>
=>
!=
```

See [**expressions**](#expressions) in the expressions guide for more information.

---

#### - **float**

The `float` data type is an number that can represent any decimal numbers. It must have a decimal place, or it will be considered as an integer otherwise. A floating point number can be positive or negative, and is not wrapped around double quotes (`"`):

```
<float>
-<float>
```

For example:

```
5.0
-5.0
```

All numbers, including floating point numbers, can be increased or decreased using mathematical [**operators**](#operators):

```
inc 5.0
dec 5.0
add 5.0 10.0 output
sub 5.0 10.0 output
mul 5.0 10.0 output
div 5.0 10.0 output
```

It can also be rounded to an integer:

```
rnd 5.4  :: 5
```

See [**operators**](#operators) in the operators guide for more information.

All numbers, including floating point numbers, can also use the following comparators:

```
==
<
<=
>
=>
!=
```

See [**expressions**](#expressions) in the expressions guide for more information.

---

### Expressions

An expression compares two values and returns a boolean. It cannot be used on its own and must be paired with [**operators**](#operators) that accepts expressions:

```
evl <a> <comparator> <b> <branch true> [branch false]
whl <a> <comparator> <b> <section>
```

An expression takes 3 arguments:

```
<a> <comparator> <b>
```

The expression takes the two values on the side, `a` and `b`, and compares them with the comparator provided in the middle.

For example:

```
"foo" != "bar"
5.5 == 5.5
5 <= 10
```

There are 9 different comparators in the x2 language.

---

#### - **==**

The `==` comparator checks if the two values are equal. It can take any [**data type**](#data-types) on each side. When comparing, it checks if the two sides have the same [**data type**](#data-types) and have the same value. The comparator returns true if both sides are equal or false if they are not.

Syntax:

```
<a> == <b>
```

Example:

```
5 == 10
:: false
```

---

#### - **<**

The `<` comparator checks if the value on the left side is less than the value on the right side. It can take any [**data type**](#data-types), but both [**data type**](#data-types) must be the same. When both sides are numbers, it compares if the number on the left side is less than the number on the right side. When both sides are strings, it is compared [**lexicographically**](https://en.wikipedia.org/wiki/Lexicographical_order). The comparator returns true of the value on the left side is less than the value on the right side or false if they are not.

Syntax:

```
<a> < <b>
```

Example:

```
5 < 10
:: true
```

---

#### - **<=**

The `<` comparator checks if the value on the left side is less than or equal to the value on the right side. It can take any [**data type**](#data-types), but both [**data type**](#data-types) must be the same. When both sides are numbers, it compares if the number on the left side is less than or equal to the number on the right side. When both sides are strings, it is compared [**lexicographically**](https://en.wikipedia.org/wiki/Lexicographical_order). The comparator returns true of the value on the left side is less than or equal the value on the right side or false if they are not.

Syntax:

```
<a> <= <b>
```

Example:

```
5 <= 10
:: true
```

---

#### - **>**

The `>` comparator checks if the value on the left side is greater than the value on the right side. It can take any [**data type**](#data-types), but both [**data type**](#data-types) must be the same. When both sides are numbers, it compares if the number on the left side is greater than the number on the right side. When both sides are strings, it is compared [**lexicographically**](https://en.wikipedia.org/wiki/Lexicographical_order). The comparator returns true of the value on the left side is greater than the value on the right side or false if they are not.

Syntax:

```
<a> > <b>
```

Example:

```
5 > 10
:: false
```

---

#### - **>=**

The `>=` comparator checks if the value on the left side is greater than or equal to the value on the right side. It can take any [**data type**](#data-types), but both [**data type**](#data-types) must be the same. When both sides are numbers, it compares if the number on the left side is greater than or equal to the number on the right side. When both sides are strings, it is compared [**lexicographically**](https://en.wikipedia.org/wiki/Lexicographical_order). The comparator returns true of the value on the left side is greater than or equal the value on the right side or false if they are not.

Syntax:

```
<a> >= <b>
```

Example:

```
5 >= 10
:: false
```

---

#### - **!=**

The `!=` comparator checks if the two values are not equal. It can take any [**data type**](#data-types) on each side. When comparing, it checks if the two sides have different [**data type**](#data-types) or have different values. The comparator returns true if both sides are different or false if they are the same.

Syntax:

```
<a> != <b>
```

Example:

```
5 != 10
:: true
```

---

#### - **in**

The `in` comparator checks if a string exists in another string. It can only take the string [**data type**](#data-types) on both sides. When comparing, it checks if the string on the left is included in the string on the right, whether it is equal to the string on the right side or it is only a part of the string on the right side. The comparator returns true if the string on the left side appears in the string on the right side.

Syntax:

```
<a> in <b>
```

Example:

```
"Hello" in "Hello World"
:: true
```

---

#### - **xin**

The `xin` comparator checks if a string doesn't exist in another string. It can only take the string [**data type**](#data-types) on both sides. When comparing, it checks if the string on the left is not included in the string on the right. The comparator returns true if the string on the left side doesn't appear in the string on the right side.

Syntax:

```
<a> xin <b>
```

Example:

```
"Hello" xin "Hello World"
:: false
```

---

#### - **is**

The `is` comparator checks if a value is a certain [**data type**](#data-types). It can take in any [**data type**](#data-types) on the left side, but it can only take the string [**data type**](#data-types) on the right side. When comparing, the data type of value on the left side is checked against the string on the right side. The comparator returns true if the [**data type**](#data-types) of the value on the left side matched the [**data type**](#data-types) on the right side.

Syntax:

```
<variable> is <data type>
```

Example:

```
"Hello World" is "str"
:: true
```

#### - **from**

The `from` comparator checks if a value's type descends from another [**data type**](#data-types). This operator is very similar to `is`, however the second value is the datatype you wish to check, allowing for custom datatypes to be created by `evl` and checked using `cmp`.

Syntax:

```
<variable> from <data type>
```

Example:

```
evl "x2.setvar('bool', bool)"
evl "x2.setvar('areGeesEpik', True)"

areGeesEpik from bool
:: true
```

---

### Other

Here are some techniques and other core features of the x2 language.

---

#### - **Comments**

You can define a comment by adding two colons (`::`) in front of any line, for example:

```
:: Hello, world!
```

You can also have an inline comment by adding the `::` after the line.  
Currently, it is not possible to have a block comment.

---

#### - **Getting Values From Variable Names**

Because it is impossible to have nested string template literals, it may seem challenging to obtain a value from a variable name. However, this can be done by having a separate `pop` [**operator**](#operators):

```
pop <variable name> output
```

For example:

```
psh 5 number
psh 10 number5Times2
pop "number$(pop number)Times2" output
out output
:: 10
```

The string template literal within the string grabs the `5` from the variable `number`. It then appends it with the rest of the string. The combined variable name is then popped out and stored in the variable `output`.

This method can be useful when you have an unknown variable in your variable name.

## Packages

You can import packages from other files. This allows you to use other people's code within your own workspace. Only files ending with the extension `.xt` can be imported correctly.

You can import a package by typing the following at the top of your files:

```
imp <path>
```

For example:

```
imp "stdlib/system"
```
will attempt to import `pkg/stdlib/system/main.xt` automatically.

Note that the file extension is unnecessary when importing a package, however it is required to indicate you are importing a relative file.

It is a common practice to have a separate folder called `pkg/`. When first initializing your x2 interpreter, a `pkg/` folder should already be created with a `stdlib/` folder within it. These packages inside the `stdlib/` folder are the standard libraries of the x2 language. They are pre-made packages created by the developers of the x2 language. Documentations of these standard libraries can be found on the [**official website**](https://x2.iipython.cf/) of x2.

Additional packages can be downloaded from the [**x2 marketplace**](https://x2.iipython.cf/list?id=packages).

## Links

Here are some useful links for x2:
- [**Repository**](https://github.com/ii-Python/x2) - Repository for x2
- [**Website**](https://x2.iipython.cf/) - Official Website of x2
- [**Syntax Highlighter**](https://github.com/Dm12332131mD/x2-theme) - Syntax Highlighter for x2 on Visual Studio Code
Extension on Visual Studio Code
- [**Syntax Highlighter Extension**](https://marketplace.visualstudio.com/items?itemName=iiPython.x2) - Syntax Highlighter
- [**Github**](https://github.com/ii-Python) - iiPython's Github Profile
