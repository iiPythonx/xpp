# [x++](../README.md) / [Tutorials](../tutorials.md) / 4. Calculator

## Table of Contents

- [Home](../README.md)
- [Tutorials](../tutorials.md)
    - [Table of Contents](../tutorials.md#table-of-contents)
    - [About](../tutorials.md#about)
    - [Tutorials ▾](../tutorials.md#tutorials)
        - [1. Hello, world!](hello-world.md)
        - [2. User Input](user-input.md)
        - [3. Branching](branching.md)
        - **4. Calculator ▾**
            - [Table of Contents](#table-of-contents)
            - [Lesson](#lesson)
- [Documents](../documents.md)
- [Python API](../python-api.md)
- [Caffeine](../caffeine.md)
- [Standard Library](../stdlib.md)

## Lesson

From the last three lessons, you learned how to print values into the terminal, get user inputs, modify strings and numbers, and create branches. In this lesson, you will be using all of this knowledge to construct a calculator using x++. Even though it may seem difficult at first, it is just made up of simple components. Let's break it down.

Let's introduce the program and get some inputs from the user using the `prt` and `read` operators:

```xpp
:: main.xpp
prt "Welcome to the x++ calculator!"
prt "-----"
read "Please enter your first number: " ?a
read "Please enter your second number: " ?b
prt "-----"
```

You can also use escape codes to format your texts, such as `\t` to indent your text:

```xpp
:: main.xpp
prt "Welcome to the x++ calculator!"
prt "-----"
read "Please enter your first number: " ?a
read "Please enter your second number: " ?b
prt "-----"
prt "Operators"
prt "\t[A] Addition"
prt "\t[S] Subtraction"
prt "\t[M] Multiplication"
prt "\t[D] Division"
read "Please enter your operator by typing the letter within the bracket: " ?o
prt "-----"
```

Currently, the numbers you got from the user are a string. You need to parse it into a number using the `int` operator so you can use mathematical operators on it. You can also uppercase your operator using the `upr` operator so you can allow both lowercase and uppercase answers:

```xpp
:: main.xpp
prt "Welcome to the x++ calculator!"
prt "-----"
read "Please enter your first number: " ?a
read "Please enter your second number: " ?b
prt "-----"
prt "Operators"
prt "\t[A] Addition"
prt "\t[S] Subtraction"
prt "\t[M] Multiplication"
prt "\t[D] Division"
read "Please enter your operator by typing the letter within the bracket: " ?o
prt "-----"
int a
int b
upr o
```

Now we can use the `if` operator to check what operator the user selected and act accordingly. Currently, there are four types of mathematical operators: `add`, `sub`, `mul`, and `div`. Let's use them:

```xpp
:: main.xpp
prt "Welcome to the x++ calculator!"
prt "-----"
read "Please enter your first number: " ?a
read "Please enter your second number: " ?b
prt "-----"
prt "Operators"
prt "\t[A] Addition"
prt "\t[S] Subtraction"
prt "\t[M] Multiplication"
prt "\t[D] Division"
read "Please enter your operator by typing the letter within the bracket: " ?o
prt "-----"
int a
int b
upr o
if (o == "A") { add a b ?c } \
   (o == "S") { sub a b ?c } \
   (o == "M") { mul a b ?c } \
   (o == "D") { div a b ?c }
```

Since you defined `c` as the answer to the equation, you can simply output it to the terminal. Using string interpolation, you can also use variables within your strings:

```xpp
:: main.xpp
prt "Welcome to the x++ calculator!"
prt "-----"
read "Please enter your first number: " ?a
read "Please enter your second number: " ?b
prt "-----"
prt "Operators"
prt "\t[A] Addition"
prt "\t[S] Subtraction"
prt "\t[M] Multiplication"
prt "\t[D] Division"
read "Please enter your operator by typing the letter within the bracket: " ?o
prt "-----"
int a
int b
upr o
if (o == "A") { add a b ?c } \
   (o == "S") { sub a b ?c } \
   (o == "M") { mul a b ?c } \
   (o == "D") { div a b ?c }
prt "The answer to that equation is $(c)."
```

Tada! You got a working calculator. How cool is that?

---

Last Updated: March 9th, 2024 by iiPython

[↑ Go To Top](#x--tutorials--4-calculator)