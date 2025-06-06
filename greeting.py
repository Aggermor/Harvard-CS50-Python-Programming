# This program based on `hello.py` is for learning about testing entire directories of tests
# /test/ directory is a package because it contains an `__init__.py` file.
#   --> This allows us to run all tests in the directory with a single command.

def greeting(name="world"):
    return f"hello, {name}"