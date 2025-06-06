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

# When you run this script directly, `__name__` will be "__main__".
# When you import this script as a module in another script, `__name__` will be the name of the module (in this case, "sayings").

# print(__name__)
# 'saysings' will print if the module is imported.          --> Demonstrating __name__ will == 'sayings'
# '__main__' will print if the module is run directly.      --> Demonstrating __name__ will == '__main__'
