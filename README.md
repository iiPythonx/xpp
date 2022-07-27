# x2

## Introduction

Welcome to the official documentation for x2! This documentation will get you started in the development of your first x2 project or will help you learn more about x2 in general with in-depth explanations and tutorials.  

If you're looking for a faster alternative to x2, check out [Calcium](https://github.com/Dm12332131mD/calcium). It's based around the same principles as x2, but written in C++ and fully OOP-compliant.

## Table of Contents

- **Home ▾**
    - [Introduction](#introduction)
    - [ToC](#table-of-contents)
    - [About](#about)
    - [Getting Started ▾](#getting-started)
        - [Step 1: Installation](#step-1-installation)
        - [Step 2: Set-Up](#step-2-set-up)
        - [Step 3: Execution](#step-3-execution)
    - [Frequently Asked Questions](#frequently-asked-questions)
    - [Credits and Links ▾](#credits--links)
        - [Contributors](#contributors)
        - [Resources](#resources)
- [Tutorials](./md/tutorials.md)
- [Documents](./md/documents.md)
- [Python API](./md/pythonAPI.md)
- [Standard Library](./md/standardLibrary.md)

***Please note: current x2 documentation is likely invalid due to the release of x2.3r1!**

## About

x2 (Pronounced "ex-two") is a high-level, interpreted language written in Python by [iiPython](https://github.com/iiPythonx) with low-level programming language syntax, similar to that of [x86 Assembly](https://en.wikipedia.org/wiki/X86_assembly_language) or [Batch](https://en.wikipedia.org/wiki/Batch_file).

x2 contains features such as:
- Automatic Garbage Collection
- Scoped/global Variables
- Sectioning/function system
- Python Integration
- Import/Export System
- Package Management System ([xpm](https://github.com/iiPythonx/xpm); coming soon!)
- ... many more!

## Getting Started

### Step 1: Installation

First and foremost, make sure you have [Python](https://python.org/downloads/) (Minimum Python 3.10 | Recommended Python 3.11) installed on your device. You can check if you have Python installed by opening up a terminal and typing:

```
python -V
```

It is extremely recommended to have a text editor or Integrated Development Environment, such as [Visual Studio Code](https://code.visualstudio.com/), as its built-in development tools and add-ons will speed up and facilitate your development process. However, a simple text editor like notepad is sufficient.

Next, visit our [github repository](https://github.com/iiPythonx/x2/) and download a clone of the repository by clicking on the green `Code ▾` button and the `Download ZIP` option. Optionally, if you have [git](https://git-scm.com/) installed on your device, you can also clone the repository by opening up a terminal and typing:

```
git clone https://github.com/iiPythonx/x2
```

If you are choosing Visual Studio Code as your Integrated Development Environment, you can also install the [x2 extension](https://marketplace.visualstudio.com/items?itemName=iiPython.x2) on the marketplace to get syntax highlighting on your x2 files.

### Step 2: Set-Up

Once you open up your x2 project, you should be able to find a file named `main.x2`. By default, this is your main entry file and is where you will be writing your x2 code. Within the file, you should see an example program similar to:

```xt
:: Main
prt "Hello, world!"
```

Any x2 files should always end in the `.x2` extension.

You can edit the main entry file by editing the configuration in `.x2config`. It is a JSON-like file that contains all the configurations for your x2 project. Within it, you should see:

```xtconfig
{
    "main": "main.x2"
}
```

> You can learn more about setting up your project in the [tutorials](./md/tutorials.md).

### Step 3: Execution

After you are done writing your x2 code, you can execute your x2 project immediately by opening up a terminal and typing:

```
python main.py .
```

Currently, you should see the terminal output:

```
"Hello, world!"
```

## Frequently Asked Questions

### Q: Why is it called x2?

It originally started as `x` because the name sounded cool. As development goes on, a second revision was published and the name was changed to `x2`.

### Q: Can I use x2 for data management, game design, or simply for fun?

You can pretty much do anything in vanilla x2, especially with the `evl` operator, which allows you to integrate Python into your project.

### Q: Where can I publish my games / packages?

You can publish your games and packages at [our website](https://x2.iipython.cf/)!

## Credits & Links

### Contributors

- [iiPython](https://github.com/iiPythonx) - Lead Developer
- [Dm123321_31mD](https://github.com/Dm12332131mD) - Developer + moral support

### Resources

- [Github Repository](https://github.com/iiPythonx/x2)
- [Visual Studio Code x2 Extension](https://marketplace.visualstudio.com/items?itemName=iiPython.x2)

---

Last Updated: April 22nd, 2022 by iiPython

[↑ Go To Top](#x2)
