# A Python library is also called a module. A module is a file that contains Python code.
# A module can define functions, classes, and variables that can be used in other Python programs.
# `import` a module to load the code into the current namespace.
# You can also use `from <module> import <function>` to import a specific function from a module.
# You can also use `from <module> import *` to import all functions from a module, but this is not recommended as it can lead to name conflicts.
# You can also use `import <module> as <alias>` to import a module with an alias. like 
# You can also use `from <module> import <function> as <alias>` to import a specific function with an alias.

import random

coin = random.choice(['heads', 'tails'])  # Randomly choose between heads and tails
print(coin)

# ----------------------------------- #
from random import choice

coin = choice(['heads', 'tails'])  # Randomly choose between heads and tails
print(coin)

# ----------------------------------- #
from random import choice as c

coin = c(['heads', 'tails'])  # Randomly choose between heads and tails
print(coin)

# ----------------------------------- #
from random import randint

generator = randint(1, 10)  # Randomly generate a number between 1 and 10, 10% probability of getting any number.
print(generator)

# ----------------------------------- #