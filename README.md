# x2

## Welcome

Welcome to the official documentation of x2! This documentation will get you started in the development of your first x2 project or will help you learn more about x2 in general with in-depth explanations and tutorials.

**! PLEASE NOTE: x2 development is currently on hold, check out [DmmD's OOP version](https://github.com/x2-dmmd/object) in the meantime. !**

## Table of Contents

- **Home ▾**
    - [Welcome](#welcome)
    - [Table of Contents](#table-of-contents)
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

## About

x2 (Pronounced "ex-two") is a high-level, interpreted language written in Python by [iiPython](https://github.com/ii-Python/) with low-level programming language syntax, such as [x86 Assembly](https://en.wikipedia.org/wiki/X86_assembly_language) or [Batch](https://en.wikipedia.org/wiki/Batch_file).

x2 contains features such as:
- Automatic Garbage Collection
- Scoped/Global Variables
- Public/Private Sections
- Functions and Methods
- Python Integration
- Working Import/Export System
- Package System
- ...And more!

## Getting Started

### Step 1: Installation

First and foremost, make sure you have [Python](https://python.org/downloads/) (Minimum Python 3.10 | Recommended Python 3.11) installed on your device. You can check if you have Python installed by opening up a terminal and typing:

```
python -V
```

It is extremely recommended to have a text editor or Integrated Development Environment, such as [Visual Studio Code](https://code.visualstudio.com/), as its built-in development tools and add-ons will speed up and facilitate your development process. However, a simple text editor like notepad is sufficient.

Next, visit our [github repository](https://github.com/ii-Python/x2/) and download a clone of the repository by clicking on the green `Code ▾` button and the `Download ZIP` option. Optionally, if you have [git](https://git-scm.com/) installed on your device, you can also clone the repository by opening up a terminal and typing:

```
git clone https://github.com/ii-Python/x2/
```

If you are choosing Visual Studio Code as your Integrated Development Environment, you can also install the [x2 extension](https://marketplace.visualstudio.com/items?itemName=iiPython.x2) on the marketplace to get syntax highlighting on your x2 files.

### Step 2: Set-Up

Once you open up your x2 project, you should be able to find a file named `main.xt`. By default, this is your main entry file and is where you will be writing your x2 code. Within the file, you should see:

```xt
:: Main
:main
    out "Hello, world!"
```

Any x2 files should always end in the `.xt` extension. The main entry file should also always contain a `:main` section.

You can edit the main entry file by editing the configuration in `.xtconfig`. It is a JSON-like file that contains all the configurations for your x2 project. Within it, you should see:

```xtconfig
{
    "main": "main.xt"
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

- [iiPython](https://github.com/ii-Python/) - Lead Developer
- [Dm123321_31mD](https://github.com/Dm12332131mD) - Contributor

### Resouces

- [Github Repository](https://github.com/ii-Python/x2)
- [Visual Studio Code x2 Extension](https://marketplace.visualstudio.com/items?itemName=iiPython.x2)
- [Website](https://x2.iipython.cf/)

---

Last Updated: February 6th, 2022 by Dm123321_31mD

[↑ Go To Top](#x2)
