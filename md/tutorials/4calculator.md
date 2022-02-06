# [x2](../../README.md) / [Tutorials](../tutorials.md) / 4. Calculator

## Table of Contents

- [Home](../../README.md)
- [Tutorials](../tutorials.md)
    - [Table of Contents](#table-of-contents)
    - [About](#about)
    - [Tutorials ▾](#tutorials)
        - [1. Hello, world!](./1helloWorld.md)
        - [2. User Input](./2userInput.md)
        - [3. Branches](./3branches.md)
        - **4. Calculator ▾**
            - [Table of Contents](#table-of-contents)
            - [Lesson](#lesson)
- [Documents](../documents.md)
- [Python API](../standardLibrary.md)
- [Standard Library](../pythonAPI.md)

## Lesson

From the last three lessons, you learned how to print values into the terminal, get user inputs, modify strings and numbers, and create branches. In this lesson, you will be using all of this knowledge to construct a calculator using x2. Even though it may seem difficult at first, it is just made up of simple components. Let's break it down.

Let's introduce the program and get some inputs from the user using the `out` and `read` operators:

```xt
:: Main
:main
    out "Welcome to the x2 calculator!"
    out "-----"
    read "Please enter your first number: " a
    read "Please enter your second number: " b
    out "-----"
```

You can also use escape codes to format your texts, such as `\t` to indent your text:

```xt
:: Main
:main
    out "Welcome to the x2 calculator!"
    out "-----"
    read "Please enter your first number: " a
    read "Please enter your second number: " b
    out "-----"
    out "Operators"
    out "\t[A] Addition"
    out "\t[S] Subtraction"
    out "\t[M] Multiplication"
    out "\t[D] Division"
    read "Please enter your operator by typing the letter within the bracket: " o
    out "-----"
```

Currently, the numbers you got from the user are a string. You need to parse it into a number using the `num` operator so you can use mathematical operators on it. You can also uppercase your operator using the `upr` operator so you can allow both lowercase and uppercase answers:

```xt
:: Main
:main
    out "Welcome to the x2 calculator!"
    out "-----"
    read "Please enter your first number: " a
    read "Please enter your second number: " b
    out "-----"
    out "Operators"
    out "\t[A] Addition"
    out "\t[S] Subtraction"
    out "\t[M] Multiplication"
    out "\t[D] Division"
    read "Please enter your operator by typing the letter within the bracket: " o
    out "-----"
    num a
    num b
    upr o
```

Now we can use the `cmp` operator to check what operator the user selected and act accordingly. Currently, there are four types of mathematical operators: `add`, `sub`, `mul`, and `div`. Let's use them:

```xt
:: Main
:main
    out "Welcome to the x2 calculator!"
    out "-----"
    read "Please enter your first number: " a
    read "Please enter your second number: " b
    out "-----"
    out "Operators"
    out "\t[A] Addition"
    out "\t[S] Subtraction"
    out "\t[M] Multiplication"
    out "\t[D] Division"
    read "Please enter your operator by typing the letter within the bracket: " o
    out "-----"
    num a
    num b
    upr o
    cmp o == "A" "add a b c"
    cmp o == "S" "sub a b c"
    cmp o == "M" "mul a b c"
    cmp o == "D" "div a b c"
```

Since you defined `c` as the answer to the equation, you can simply output it to the terminal. Using string interpolation and the `pop` operator, you can also use variables within your strings:

```xt
:: Main
:main
    out "Welcome to the x2 calculator!"
    out "-----"
    read "Please enter your first number: " a
    read "Please enter your second number: " b
    out "-----"
    out "Operators"
    out "\t[A] Addition"
    out "\t[S] Subtraction"
    out "\t[M] Multiplication"
    out "\t[D] Division"
    read "Please enter your operator by typing the letter within the bracket: " o
    out "-----"
    num a
    num b
    upr o
    cmp o == "A" "add a b c"
    cmp o == "S" "sub a b c"
    cmp o == "M" "mul a b c"
    cmp o == "D" "div a b c"
    out "The answer to that equation is $(pop c)"
```

Tada! You got a working calculator. How cool is that!

In the next lesson, you will be learning how to define and jump into another section.

---

Last Updated: February 6th, 2022 by Dm123321_31mD

[↑ Go To Top](#x2--tutorials--4-calculator)