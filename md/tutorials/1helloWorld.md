# [x2](../../README.md) / [Tutorials](../tutorials.md) / 1. Hello, world!

## Table of Contents

- [Home](../../README.md)
- [Tutorials](../tutorials.md)
    - [Table of Contents](#table-of-contents)
    - [About](#about)
    - [Tutorials ▾](#tutorials)
        - **1. Hello, world! ▾**
            - [Table of Contents](#table-of-contents)
            - [Lesson](#lesson)
        - [2. User Input](./2userInput.md)
        - [3. Branches](./3branches.md)
        - [4. Calculator](./4calculator.md)
- [Documents](../documents.md)
- [Python API](../standardLibrary.md)
- [Standard Library](../pythonAPI.md)

## Lesson

Welcome to the first lesson of the tutorials! In this lesson, you will be learning how to write your first x2 project, how to define and use a variable, and how to print a value into the terminal.

First, make sure you properly installed x2 to your device if you haven't done so already. You can follow the guide in the [getting started](../../README.md#getting-started) section for additional help.

Once you are done, open up the `main.xt` file. Inside, you should find something like this:

```xt
:: Main
:main
    out "Hello, world!"
```

This is the default template when you first installed x2. It is important for you to know what the code is doing. Let's break it down.

The first line in the file is a comment. A comment is a text that provides information to the developer, such as you. It is ignored by the interpreter as it is intended for only developers to read.

The second line defines a section. A section is a region of code that will be executed upon being called. In this case, a section called `main` is being defined. In the main entry file, the `main` section is always required and is always called upon execution.

The third line prints out a string with the value `"Hello, world!"`. A string is a series of characters wrapped around by double-quotes (`"`). You can think of it like a character, word, phrase, or a sentence. The `out` is an operator, which means it takes arguments, processes them, and does a specific action based on what the arguments are. In the case, the `out` operator simply takes the arguments and prints them in the terminal.

Although indentations in x2 aren't necessary, it is a good practice to use indentation to group the statements, so you or other developers won't get confused.

Now that you understand what your code is doing, let's try it out. Using what you've learned, try printing out your name and age in the format `My name is <name> and I am <age> years old` in the terminal.

Did you get something similar to this:

```xt
:: Main
:main
    out "My name is Bob and I am 20 years old"
```

You can also store the name and the age in separate variables so you can reference it later. The `psh` operator takes in two arguments, the `value` and the `variable`. To define a value, you can use the following:

```xt
psh 5 myInteger
```

Let's put that in your code!

```xt
:: Main
:main
    psh "Bob" name
    psh 20 age
    out "My name is Bob and I am 20 years old"
```

Your can put your variables into your string using `string interpolation`. String interpolation is the process of inserting another statement within a string. This is usually done so by wrapping them in `$()`.

But here is the problem, you cannot reference the variable directly in a string interpolation. Your variable is not a statement and thus cannot be used on its own. You can fix this problem using the `pop` operator.

The pop operator parses a variable and returns its value like so:

```xt
"$(pop myInteger)
```

Let's try it!

```xt
:: Main
:main
    psh "Bob" name
    psh 20 age
    out "My name is $(pop name) and I am $(pop age) years old"
```

You did it! You made your first ever x2 project.

In the next lesson, you will learn how to get user inputs and how to manupulate strings and numbers.

---

Last Updated: February 6th, 2022 by Dm123321_31mD

[↑ Go To Top](#x2--tutorials--1-hello-world)