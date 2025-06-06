# https://youtu.be/nLRL_NcnK-4?t=20185
# Packages are a way to organize and distribute Python code. They can contain modules, which are files containing Python code, and can also include data files, documentation, and other resources.
# PyPI (Python Package Index), is a repository of software for Python.
# https://pypi.org/project/cowsay/
# 'cowsay' is a package that generates ASCII art of a cow with a speech bubble containing a message.
# pip is a program called a package manager for Python that allows you to install and manage Python packages.
# `$ pip install cowsay` This terminal command installs the cowsay package from PyPI.

# Module is a file containing Python code that can be imported and used in other Python programs.
# Package is a collection of modules that are organized in a specific way, usually with an __init__.py file to indicate that the directory is a package.
# Library is a collection of packages and modules that provide specific functionality, such as data manipulation, web development, or machine learning.

#! you cannot name your file `cowsay.py` because it will conflict with the `cowsay` package you are trying to import.
# `$ mv cowsay.py cow_say.py` This terminal command renames the file to avoid conflict with the `cowsay` package.

import cowsay
import sys

def main():
    v1()

def v1():
    if len(sys.argv) == 2:
        cowsay.cow("hello, " + sys.argv[1] + "!")

main()