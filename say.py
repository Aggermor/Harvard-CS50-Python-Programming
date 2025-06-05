# https://youtu.be/nLRL_NcnK-4?t=20185
# Packages are a way to organize and distribute Python code. They can contain modules, which are files containing Python code, and can also include data files, documentation, and other resources.
# PyPI (Python Package Index), is a repository of software for Python.
# cowsay is a package that generates ASCII art of a cow with a speech bubble containing a message.
# pip is a program called a package manager for Python that allows you to install and manage Python packages.
# `$ pip install cowsay` This terminal command installs the cowsay package from PyPI.

#! you cannot name your file `cowsay.py` because it will conflict with the `cowsay` package you are trying to import.
# `$ mv cowsay.py say.py` This terminal command renames the file to avoid conflict with the `cowsay` package.

import cowsay as say
import sys

def main():
    v1()

def v1():
    if len(sys.argv) == 2:
        say.cow("hello, " + sys.argv[1] + "!")

main()