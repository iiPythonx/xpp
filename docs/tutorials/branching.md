# [x++](../README.md) / [Tutorials](../tutorials.md) / 3. Branches

## Table of Contents

- [Home](../README.md)
- [Tutorials](../tutorials.md)
    - [Table of Contents](../tutorials.md#table-of-contents)
    - [About](../tutorials.md#about)
    - [Tutorials ▾](../tutorials.md#tutorials)
        - [1. Hello, world!](hello-world.md)
        - [2. User Input](user-input.md)
        - **3. Branching ▾**
            - [Table of Contents](#table-of-contents)
            - [Lesson](#lesson)
        - [4. Calculator](calculator.md)
- [Documents](../documents.md)
- [Python API](../python-api.md)
- [Caffeine](../caffeine.md)
- [Standard Library](../stdlib.md)

## Lesson

In the previous lesson, you learned how to get a user input and modify them to get a certain result. In this lesson, you will be learning how to create a branch using the `if` operator.

The `if` operator takes 3 arguments, the `expression`, the `true` branch, and the `else` branch. An expression is an equation that evaluates the two sides. An expression is made up of 3 parts, the `source`, the `comparator`, and the `target`:

```xpp
<source> <comparator> <target>
```

For example, the `equal to` comparator looks like this:

```xpp
var myInteger 5
myInteger == 5
```

If the expression is true, the `if` operator will then trigger the `true` branch, else the `false` branch. Both branches must be a string and their contents must be a valid statement.

Because the branches are strings, if you want to use another (double-quoted) string within the branch, you have to escape it. This is done by appending a backslash (`\`) right before the double-quote.

Now let's put it together:

```xpp
var myAge 20
if (myAge == 20) { prt "I am 20 years old" } { prt "I am not 20 years old" }
```

When you run the code, you should see it outputs `"I am 20 years old"`. Try changing the value of `myAge` and see what happens.

The `else` branch is optional. If you only want to check if the expression is true, you can just use one branch instead:

```xpp
var myInteger 5
if (myInteger == 5) { prt "My integer is 5" }
```

With that knowledge, you can now output a special text if the user name matches yours:

```xpp
:: main.xpp
read "What is your name? " ?name
read "What is your age? " ?age

:: Keep a copy of their original string
var ogName name

:: Calculate birth year by using the current year
int age  :: Ensure it's an integer
sub 2024 age ?birthYear

:: Convert the name to lowercase (so we can check it)
if ((lwr name) == "bob") { prt "Welcome, Bob!" }

:: Show them their info
prt "Your name is $(ogName) and you were born in $(birthYear)."
```

There are many more comparators, such as the `greater than` (`>`) or `not equal` (`!=`). They work the same way as the `equal to` comparator.

Now's your turn. Check if the user's age is equal to or above 16 and output `"You can also drive a car"` after you output their name and their birth year if it is true.

Did you get something like this?

```xpp
:: main.xpp
read "What is your name? " ?name
read "What is your age? " ?age

:: Keep a copy of their original string
var ogName name

:: Calculate birth year by using the current year
int age  :: Ensure it's an integer
sub 2024 age ?birthYear

:: Convert the name to lowercase (so we can check it)
if ((lwr name) == "bob") { prt "Welcome, Bob!" }

:: Show them their info
prt "Your name is $(ogName) and you were born in $(birthYear)."
if (age >= 16) { prt "You can also drive a car." }
```

In the next lesson, you will be learning how to make a calculator using x++.

---

Last Updated: March 9th, 2024 by iiPython

[↑ Go To Top](#x--tutorials--3-branches)