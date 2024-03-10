<div align = "center">
    <h1>xpp</h1>
    <hr>
    <p>an interpreted, minimalistic programming language</p>
    <img alt="License" src="https://img.shields.io/github/license/iiPythonx/xpp?color=c3e7ff&style=flat-square">
    <img alt="Downloads" src="https://img.shields.io/github/downloads/iiPythonx/xpp/total.svg?color=c3e7ff&style=flat-square">
    <img alt="Last commit" src="https://img.shields.io/github/last-commit/iiPythonx/xpp?color=c3e7ff&style=flat-square">
    <img alt="Repo size" src="https://img.shields.io/github/repo-size/iiPythonx/xpp?color=c3e7ff&style=flat-square">
    <img alt="Stars" src="https://img.shields.io/github/stars/iiPythonx/xpp?color=c3e7ff&style=flat-square">
    <hr>
</div>

<!-- ---- Introduction ---- -->
<h2 align = "center" id = "introduction">
    Introduction
</h2>

Welcome to the official documentation for x++! This documentation will get you started in the development of your first x++ project or will help you learn more about x++ in general with in-depth explanations and tutorials.  

<!-- ---- TOC ---- -->
<h2 align = "center" id = "table-of-contents">
    Table of Contents
</h2>

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
- [Tutorials](tutorials.md)
- [Documents](documents.md)
- [Python API](python-api.md)
- [Standard Library](stdlib.md)

<!-- ---- About ---- -->
<h2 align = "center" id = "about">
    About
</h2>

x++ (Pronounced "ex-plus-plus") is a high-level, interpreted language written in Python by [iiPython](https://github.com/iiPythonx) with low-level syntax, similar to that of [x86 Assembly](https://en.wikipedia.org/wiki/X86_assembly_language) (and additionally inspired by [Batch](https://en.wikipedia.org/wiki/Batch_file)).

x++ contains features such as:
- Automatic garbage collection
- Scoped/file/global variables
- Sectioning/function system
- Mature python integration
- Import/export/module system
- Object-oriented programming through the use of files
- ... much more!

<!-- ---- Getting started ---- -->
<h2 align = "center" id = "getting-started">
    Getting Started
</h2>

### Step 1: Installation

First and foremost, make sure you have [Python](https://python.org/downloads/) (Python 3.10 is required, however we recommend 3.11+) installed on your device. You can check if you have Python installed by opening up a terminal and typing:

```
python3 -V
```
(on NT* platforms, replace `python3` with `py`)

It is highly recommended to have a text editor or Integrated Development Environment, such as [Visual Studio Code](https://code.visualstudio.com/), as its built-in development tools and add-ons will speed up and facilitate your development process. However, a simple text editor like notepad is sufficient.

Next, visit our [github repository](https://github.com/iiPythonx/xpp/) and download a clone of the repository by clicking on the green `Code ▾` button and the `Download ZIP` option. Optionally, if you have [git](https://git-scm.com/) installed on your device, you can also clone the repository by opening up a terminal and typing:

```
git clone https://github.com/iiPythonx/xpp
```

To install xpp system-wide, run the following:
```
pip install .
```

You will now have the `xpp` command available for use.  

If you are choosing Visual Studio Code as your Integrated Development Environment, you can also install the [x++ extension](https://marketplace.visualstudio.com/items?itemName=iiPython.xpp) on the marketplace to get syntax highlighting on your x++ files.

### Step 2: Set-Up

Once you open up your x++ project, you should be able to find a file named `main.xpp`. By default, this is your main entry file and is where you will be writing your x++ code. Within the file, you should see an example program similar to:

```xpp
:: Main
prt "Hello, world!"
```

Any x++ files should always end in the `.xpp` extension.

You can edit the main entry file by editing the configuration in `.xconfig`. It is a JSON-like file that contains all the configurations for your x++ project. Within it, you should see:

```json
{
    "main": "main.xpp"
}
```

> You can learn more about setting up your project in the [tutorials](tutorials.md).

### Step 3: Execution

After you are done writing your x++ code, you can execute your x++ project immediately by opening up a terminal and typing:

```
python main.py .
```

Currently, you should see the terminal output:

```
"Hello, world!"
```
> You can also compile your xpp code into Python using [caffeine](caffeine.md).

<!-- ---- FAQ ---- -->
<h2 align = "center">
    Frequently Asked Questions
</h2>

### Q: Why is it called x++?

The language originally started as the "X Programming Language" because the name sounded cool. As development went on, a second revision was published and the name was changed to `x2`.  
Starting on March 6th, 2023, x2 was deprecated in favor of x++ as the language was beginning to undergo major changes.

### Q: Can I use x++ for data management, game design, or simply for fun?

Most of the things you could think of making are able to be created within x++. However, you can also supercharge xpp with the power of Python; [see here](python-api.md).

<!-- ---- Contrib + resources ---- -->
<h2 align = "center">
    Credits & Links
</h2>

### Contributors

- [iiPython](https://github.com/iiPythonx) - Developer, Documentation
- [DmmD Gaming](https://github.com/DmmDGM) - Original Documentation, Ideas, & Standard Library

### Resources

- [Github Repository](https://github.com/iiPythonx/xpp)
- [Visual Studio Code x++ Extension](https://marketplace.visualstudio.com/items?itemName=iiPython.xplusplus)

---

Last Updated: December 2nd, 2023 by iiPython

[↑ Go To Top](#introduction)
