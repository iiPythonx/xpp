# [x2](../../README.md) / [Tutorials](../tutorials.md) / 2. User Input

## Table of Contents

- [Home](../../README.md)
- [Tutorials](../tutorials.md)
    - [Table of Contents](#table-of-contents)
    - [About](#about)
    - [Tutorials ▾](#tutorials)
        - [1. Hello, world!](./1helloWorld.md)
        - **2. User Input ▾**
            - [Table of Contents](#table-of-contents)
            - [Lesson](#lesson)
        - [3. Branches](./3branches.md)
        - [4. Calculator](./4calculator.md)
- [Documents](../documents.md)
- [Python API](../standardLibrary.md)
- [Standard Library](../pythonAPI.md)

## Lesson

In the previous lesson, you learned how to write your first x2 project, define and use a variable, and output a value into the terminal. In this lesson, you will learn how to get a user input and how to manipulate strings and numbers.

So far, you should've gotten this in your `main.xt` file:

```xt
:: Main
:main
    psh "Bob" name
    psh 20 age
    out "My name is $(pop name) and I am $(pop age) years old"
```

What if you want to ask what the user's name is instead of yours? You can use the `read` operator to get a user input from the terminal. The `read` operator takes in two arguments, the `prompt` and the `output`. The prompt is what the user will see when you get a user input. You can think of it as asking a question. The output is the answer from the user input.

Let's see it:

```xt
read "What is your favorite color? " favoriteColor
```

You can replace your `psh` operators and use the `read` operators instead:

```xt
:: Main
:main
    read "What is your name? " name
    read "What is your age? " age
    out "Your name is $(pop name) and you are $(pop age) years old"
```

You can also make the name more standout from the rest of the string by making it all capitalized. You can uppercase all the letters in a string by using the `upr` operator:

```xt
psh "Hello, world!" myString
upr myString
out myString :: Outputs: "HELLO, WORLD!"
```

Let's try it:

```xt
:: Main
:main
    read "What is your name? " name
    upr name
    read "What is your age? " age
    out "Your name is $(pop name) and you are $(pop age) years old"
```

You can also use mathematical operators to calculate the user's birth year. By subtracting the user's age from the current year, you get their birth year. You can use the `sub` operator for this purpose:

```xt
sub 5 10 output
out output :: Outputs: -5
```

However, because the user input always gives us a string, you need a way to convert it into a number. You can use the `num` operator for this:

```xt
psh "5" myInteger
num myInteger
out myInteger :: Outputs: 5
```

Let's give it a shot:

```xt
:: Main
:main
    read "What is your name? " name
    upr name
    read "What is your age? " age
    num age
    sub 2022 age birthYear
    out "Your name is $(pop name) and you were born in $(pop birthYear)"
```

Now it will ask the user their name and age and output their name and birth year. Incredible isn't it.

In the next lesson, you will learn how to make branches using the `cmp` operator.

---

Last Updated: February 6th, 2022 by Dm123321_31mD

[↑ Go To Top](#x2--tutorials--2-user-input)