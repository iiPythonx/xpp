# [x2](../../README.md) / [Tutorials](../tutorials.md) / 3. Branches

## Table of Contents

- [Home](../../README.md)
- [Tutorials](../tutorials.md)
    - [Table of Contents](#table-of-contents)
    - [About](#about)
    - [Tutorials ▾](#tutorials)
        - [1. Hello, world!](./1helloWorld.md)
        - [2. User Input](./2userInput.md)
        - **3. Branches ▾**
            - [Table of Contents](#table-of-contents)
            - [Lesson](#lesson)
        - [4. Calculator](./4calculator.md)
- [Documents](../documents.md)
- [Python API](../standardLibrary.md)
- [Standard Library](../pythonAPI.md)

## Lesson

In the previous lesson, you learned how to get a user input and modify them to get a certain result. In this lesson, you will be learning how to create a branch using the `cmp` operator.

The `cmp` operator takes 3 arguments, the `expression`, the `true` branch, and the `false` branch. An expression is an equation that evaluates the two sides. An expression is made up of 3 parts, the `source`, the `comparator`, and the `target`:

```xt
<source> <comparator> <target>
```

For example, the `equal to` comparator looks like this:

```xt
psh 5 myInteger
myInteger == 5
```

If the expression is true, the `cmp` operator will then trigger the true branch, else the false branch. Both branches must be a string and their contents must be a valid statement.

Because the branches are strings, if you want to use another string within the branch, you have to escape it. This is done by appending a backslash (`\`) right before the double-quote.

Now let's put it together:

```xt
psh 20 myAge
cmp myAge == 20 "out \"I am 20 years old\"" "out \"I am not 20 years old\""
```

When you run the code, you should see it outputs `"I am 20 years old"`. Try changing the value of `myAge` and see what happens.

The `false` branch is optional. If you only want to check if the expression is true, you can just use one branch instead:

```xt
psh 5 myInteger
cmp myInteger == 5 "out \"My integer is 5\""
```

With that knowledge, you can now output a special text if the user name matches yours:

```xt
:: Main
:main
    read "What is your name? " name
    upr name
    read "What is your age? " age
    num age
    sub 2022 age birthYear
    cmp name == "BOB" "out \"Welcome, Bob!\""
    out "Your name is $(pop name) and you were born in $(pop birthYear)"
```

There are many more comparators, such as the `greater than` (`>`) or `not equal` (`!=`). They work the same way as the `equal to` comparator.

Now's your turn. Check if the user's age is above 16 and output `"You can also drive a car"` after you output their name and their birth year if it is true.

Did you get something like this:

```xt
:: Main
:main
    read "What is your name? " name
    upr name
    read "What is your age? " age
    num age
    sub 2022 age birthYear
    cmp name == "BOB" "out \"Welcome, Bob!\""
    out "Your name is $(pop name) and you were born in $(pop birthYear)"
    cmp age > 16 "out \"You can also drive a car\""
```

In the next lesson, you will be learning how to make a calculator using x2.

---

Last Updated: February 6th, 2022 by Dm123321_31mD

[↑ Go To Top](#x2--tutorials--3-branches)