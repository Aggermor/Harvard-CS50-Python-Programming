# https://youtu.be/nLRL_NcnK-4?t=22173
# Unit Tests
# Units are the smallest testable parts of an application, generally functions or methods.
# Unit tests are used to validate that each unit of the software performs as expected.
# Use pytest or unittest to write unit tests in Python. Explained further in this file.
# https://docs.pytest.org/en/stable/getting-started.html

# by Python convention, unit tests are placed in a file named `test_<module_name>.py`
# we will be testing the 'square.py' module

from square import square

def main():
    clunky()
    assert_square()
    test_square()

# Here's a clunky test to explain the concept of unit testing:
# If the tests pass, there will be no output.
def clunky():
    if square(2) != 4:
        print(f"Test failed: square(2) expected 4 and got {square(2)}.")
    if square(3) != 9:
        print(f"Test failed: square(3) expected 9 and got {square(3)}.")

# Use assertions to test the function with cleaner code.
def assert_square():
    assert square(1) == 1
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(0) == 0

    # If a test fails, an `AssertionError` will be raised.
    try:
        assert square(5) == 25
    except AssertionError:
        print("Test failed: square(5) expected 25 but got", square(5))
    # etc...

# by Python convention, unit tests are named `test_<function_name>.py`
# import pytest or unittest, we can define a test function that will be automatically discovered and run.
# `$ pytest test_square.py` run this command in the terminal to run the tests.
# This will automatically discover and run the test functions defined in this file. 
#   --> Which is why it's important to follow the naming conventions for test functions and files "test_".
# https://docs.pytest.org/en/stable/getting-started.html
# Usig pytest we do not need to write a main() function, pytest will automatically discover and run the test functions.

def test_square():
    assert square(1) == 1, f"Expected 1 and got {square(1)}"
    assert square(2) == 4, f"Expected 4 and got {square(2)}"
    assert square(3) == 9, f"Expected 9 and got {square(3)}"
    assert square(-2) == 4, f"Expected 4 and got {square(-2)}"
    assert square(0) == 0, f"Expected 0 and got {square(0)}"

# Ususally it's best to separate the tests into different functions for clarity and organization.
# This way all categories of tests can be run independently, and it's easier to see which tests pass or fail.
#   --> Otherwise, as before pytest would stop running tests after the first failure.

def test_positive_numbers():
    assert square(5) == 25
    assert square(10) == 100

def test_negative_numbers():
    assert square(-5) == 25
    assert square(-10) == 100

def test_zero():
    assert square(0) == 0

# https://youtu.be/nLRL_NcnK-4?t=24459
# `$ pip install pytest`
# import pytest in order to use pytest features like `raises` to test for exceptions.

import pytest

def test_str():
    with pytest.raises(TypeError):
        square("string")

if __name__ == "__main__":
    main()