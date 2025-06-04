# sys.argv[0] is the script name
# sys.argv[1] is the first argument passed to the script
# sys.argv[2] is the second argument passed to the script etc...
# sys.argv returns a list of command line arguments passed to the script
# To run this script, use the command: `python name.py <your_name>`
# Command line arguments are passed as strings
# [CMD args](https://youtu.be/nLRL_NcnK-4?t=18657)

from sys import argv

print(f"Hello, My name is {argv[1]}.") 