# [x++](../README.md) / [Tutorials](../tutorials.md) / 2. User Input

## Table of Contents

- [Home](../README.md)
- [Tutorials](../tutorials.md)
    - [Table of Contents](../tutorials.md#table-of-contents)
    - [About](../tutorials.md#about)
    - [Tutorials ▾](../tutorials.md#tutorials)
        - [1. Hello, world!](./hello-world.md)
        - **2. User Input ▾**
            - [Table of Contents](#table-of-contents)
            - [Lesson](#lesson)
        - [3. Branching](branching.md)
        - [4. Calculator](calculator.md)
- [Documents](../documents.md)
- [Python API](../python-api.md)
- [Caffeine](../caffeine.md)
- [Standard Library](../stdlib.md)

## Lesson

In the previous lesson, you learned how to write your first x++ project, define and use a variable, and output a value into the terminal. In this lesson, you will learn how to get a user input and how to manipulate strings and numbers.

So far, you should've gotten this in your `main.xpp` file:

```xpp
:: main.xpp
var name "Bob"
var age 20
prt "My name is $(name) and I am $(age) years old."
```

What if you want to ask what the user's name is instead of yours? You can use the `read` operator to get user input from the terminal. The `read` operator takes in two arguments, the `prompt` and the `output`. The prompt is what the user will see when you get a user input. You can think of it as asking a question. The output is the answer from the user input.

Let's see it:

```xpp
read "What is your favorite color? " ?favoriteColor
```

You can replace your `var` operators and use the `read` operators instead:

```xpp
:: main.xpp
read "What is your name? " ?name
read "What is your age? " ?age
prt "Your name is $(name) and you are $(age) years old."
```

You can also make the name more standout from the rest of the string by making it all capitalized. You can uppercase all the letters in a string by using the `upr` operator:

```xpp
var myString "Hello, world!"
upr myString
prt myString  :: Outputs: "HELLO, WORLD!"
```

Let's try it:

```xpp
:: main.xpp
read "What is your name? " ?name
upr name
read "What is your age? " ?age
prt "Your name is $(name) and you are $(age) years old."
```

You can also use mathematical operators to calculate the user's birth year. By subtracting the user's age from the current year, you get their birth year. You can use the `sub` operator for this purpose:

```xpp
sub 5 10 ?output
prt output  :: Outputs: -5
```

However, because the user input always gives us a string, you need a way to convert it into a number. You can use the `int` operator for this:

```xpp
var myInteger "5"
int myInteger
prt myInteger  :: Outputs: 5
```

Let's give it a shot:

```xpp
:: main.xpp
read "What is your name? " ?name
upr name
read "What is your age? " ?age
int age
sub 2024 age ?birthYear
prt "Your name is $(name) and you were born in $(birthYear)."
```

Now it will ask the user their name and age and output their name and birth year. Incredible isn't it?

In the next lesson, you will learn how to make branches using the `if` operator.

---

Last Updated: March 9th, 2024 by iiPython

[↑ Go To Top](#x--tutorials--2-user-input)