# To run this script, use the command: `python name.py <your_name>`
# sys.argv[0] is the script name
# sys.argv[1] is the first argument passed to the script
# sys.argv[2] is the second argument passed to the script etc...
# sys.argv returns a list of command line arguments passed to the script, including the script name.
# Command line arguments are passed as strings
# https://youtu.be/nLRL_NcnK-4?t=18657

from sys import argv # Importing argv from the sys module to handle command line arguments

# We can use try-except to handle the case where no command line argument is provided 
try:
    print(f"Hello, my name is {argv[1]}.")
except IndexError:
    print("Please provide your name as a command line argument.")

# We can also handle the case where both first and last names are provided
try:
    argv[1], argv[2] # This will raise an IndexError if there are not enough command line arguments
except IndexError:
    pass
else:
    print(f"Hello, my name is {argv[1]} {argv[2]}!")


""" # Implementation of cleaner code that handles command line arguments. It's Pythonic to handle errors rather than using if-else statements.
from sys import argv

if len(argv) == 1: # Check if no command line arguments are provided, `if not argv[1:]` would also work
    print("Please provide your name as a command line argument.")
else:
    full_name = " ".join(argv[1:])
    print(f"Hello, my name is {full_name}.")
"""