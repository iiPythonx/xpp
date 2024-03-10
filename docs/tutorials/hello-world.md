# [x++](../README.md) / [Tutorials](../tutorials.md) / 1. Hello, world!

## Table of Contents

- [Home](../README.md)
- [Tutorials](../tutorials.md)
    - [Table of Contents](../tutorials.md#table-of-contents)
    - [About](../tutorials.md#about)
    - [Tutorials ▾](../tutorials.md#tutorials)
        - **1. Hello, world! ▾**
            - [Table of Contents](#table-of-contents)
            - [Lesson](#lesson)
        - [2. User Input](user-input.md)
        - [3. Branching](branching.md)
        - [4. Calculator](calculator.md)
- [Documents](../documents.md)
- [Python API](../python-api.md)
- [Caffeine](../caffeine.md)
- [Standard Library](../stdlib.md)

## Lesson

Welcome to the first lesson of the tutorials! In this lesson, you will be learning how to write your first x++ project, how to define and use a variable, and how to print a value into the terminal.

First, make sure you properly installed x++ to your device if you haven't done so already. You can follow the guide in the [getting started](../../README.md#getting-started) section for additional help.

Once you are done, open up the `main.xpp` file. Inside, you should find something like this:

```xpp
:: main.xpp
prt "Hello world!"
```

This is the default template when you first installed x++. It is important for you to know what the code is doing. Let's break it down.

The first line in the file is a comment. A comment is a text that provides information to the developer, such as you. It is ignored by the interpreter as it is intended for only developers to read.

The second line prints out a string with the value `"Hello, world!"`. A string is a series of characters wrapped around by double-quotes (`"`). You can think of it like a character, word, phrase, or a sentence. The `prt` is an operator, which means it takes arguments, processes them, and does a specific action based on what the arguments are. In the case, the `prt` operator simply takes the arguments and prints them in the terminal.

Although indentations in x++ aren't necessary, it is a good practice to use indentation to group the statements, so you or other developers won't get confused.

Now that you understand what your code is doing, let's try it out. Using what you've learned, try printing out your name and age in the format `My name is <name> and I am <age> years old` in the terminal.

Did you get something similar to this:

```xpp
:: main.xpp
prt "My name is Bob and I am 20 years old"
```

You can also store the name and the age in separate variables so you can reference it later. The `var` operator takes in two arguments, the `variable` and the `value`. To define a value, you can use the following:

```xpp
var myInteger 5
```

Let's put that in your code!

```xpp
:: main.xpp
var name "Bob"
var age 20
prt "My name is Bob and I am 20 years old."
```

Your can put your variables into your string using `string interpolation`. String interpolation is the process of inserting another statement within a string. This is usually done so by wrapping them in `$()`.

The statement you can wrap inside of `$()` can be any valid x++ syntax, however it has another key feature: you can directly reference variables from inside this environment. This means you can do something like the following:

```xpp
var x 5
prt "$(x) should be 5."
:: 5 should be 5.
```

Let's try it!

```xpp
:: main.xpp
var name "Bob"
var age 20
prt "My name is $(name) and I am $(age) years old."
```

You did it! You made your first ever x++ project.

In the next lesson, you will learn how to get user input and manipulate strings or numbers.

---

Last Updated: March 9th, 2024 by iiPython

[↑ Go To Top](#x--tutorials--1-hello-world)