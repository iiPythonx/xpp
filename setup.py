# Copyright 2023 iiPython

# Modules
import pathlib
from setuptools import setup, find_packages

# Initialization
top = pathlib.Path(__file__).parent.resolve()

# Setup call
setup(
    name = "xpp",
    description = "The x++ programming language.",
    long_description = (top / "README.md").read_text(encoding = "utf8"),
    long_description_content_type = "text/markdown",
    url = "https://github.com/iiPythonx/xpp",
    author = "iiPython",
    author_email = "ben@iipython.cf",
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
        "Topic :: Education :: Testing",
        "Topic :: Software Development",
    ],
    keywords = "xpp, parser, language, interpreter",
    packages = find_packages(),
    python_requires = ">=3.10, <4",
    extras_require = {
        "dev": ["twine"],
        "tests": ["rich"]
    },
    entry_points = {
        "console_scripts": [
            "xpp=xpp.__main__:main"
        ]
    },
    project_urls = {
        "Bug Reports": "https://github.com/iiPythonx/xpp/issues",
        "Source": "https://github.com/iiPythonx/xpp"
    }
)
