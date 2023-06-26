# Copyright 2023 iiPython

# Modules
import os
import pathlib
from typing import List
from setuptools import setup

# Initialization
top = pathlib.Path(__file__).parent.resolve()

# Custom implementation of find_packages()
def find_packages(directories: List[str]) -> List[str]:
    packages = []
    for directory in directories:
        for path, _, __ in os.walk(directory):
            if path.split(os.sep)[-1][:2] == "__":  # Ignore pycache
                continue

            packages.append(path.replace(os.sep, "."))

    return packages

# Setup call
setup(
    name = "xpp",
    description = "The x++ programming language.",
    long_description = (top / "README.md").read_text(encoding = "utf8"),
    long_description_content_type = "text/markdown",
    url = "https://github.com/iiPythonx/xpp",
    author = "iiPython",
    author_email = "ben@iipython.dev",
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Topic :: Education :: Testing",
        "Topic :: Software Development",
    ],
    keywords = "xpp, parser, language, interpreter",
    packages = find_packages(["xpp", "caffeine"]),
    python_requires = ">=3.10, <4",
    extras_require = {
        "dev": ["twine"],
        "tests": ["rich"]
    },
    entry_points = {
        "console_scripts": [
            "xpp=xpp.__main__:main",
            "caffeine=caffeine.__main__:main"
        ]
    },
    project_urls = {
        "Bug Reports": "https://github.com/iiPythonx/xpp/issues",
        "Source": "https://github.com/iiPythonx/xpp"
    }
)
