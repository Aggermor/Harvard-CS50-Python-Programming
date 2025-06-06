# https://youtu.be/nLRL_NcnK-4?t=21757
# I created my own module named `sayings` used in the file `my_say.py` to demonstrate how to import and use functions from a custom module.

def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

if __name__ == "__main__":
    main()

# https://youtu.be/nLRL_NcnK-4?t=22013
# The `if __name__ == "__main__":` block is used to ensure that the `main()` function is only called when the script is run directly, not when it is imported as a module in another script.
# `__name__` is a special variable in Python that is set to "__main__" when the script is run directly.
