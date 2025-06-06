import sys
from sayings import hello

if len(sys.argv) == 2:
    name = sys.argv[1]
    hello(name)
else:
    print("Usage: `$ python my_say.py <name>`")
    sys.exit(1) # exit(1) is used to indicate that the program has terminated with an error.
