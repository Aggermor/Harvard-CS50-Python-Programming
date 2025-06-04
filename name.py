# sys.argv[0] is the script name
# sys.argv[1] is the first argument passed to the script
# sys.argv[2] is the second argument passed to the script etc...
# sys.argv returns a list of command line arguments passed to the script
# Command line arguments are passed as strings
# [CMD args](https://youtu.be/nLRL_NcnK-4?t=18657)

# To run this script, use the command: `python name.py <your_name>`
from sys import argv

# We can use try-except to handle the case where no command line argument is provided 
try:
    print(f"Hello, my name is {argv[1]}.")
except IndexError:
    print("Please provide your name as a command line argument.")

