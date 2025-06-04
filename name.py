# To run this script, use the command: `python name.py <your_name>`
# sys.argv[0] is the script name
# sys.argv[1] is the first argument passed to the script
# sys.argv[2] is the second argument passed to the script etc...
# sys.argv returns a list of command line arguments passed to the script, including the script name.
# Command line arguments are passed as strings
# https://youtu.be/nLRL_NcnK-4?t=18657

from sys import argv # Importing argv from the sys module to handle command line arguments

def main():
    v3()

def v1():
    # We can use try-except to handle the case where no command line argument is provided 
    try:
        print(f"Hello, my name is {argv[1]}.")
    except IndexError:
        print("Please provide your name as a command line argument.")

def v2():
    # We can also handle the case where both first and last names are provided
    try:
        argv[1], argv[2] # This will raise an IndexError if there are not enough command line arguments
    except IndexError:
        pass
    else:
        print(f"Hello, my name is {argv[1]} {argv[2]}!")

    """ # Implementation of cleaner code that handles command line arguments. It's Pythonic to handle errors rather than using if-else statements.
    if len(argv) == 1: # Check if no command line arguments are provided, `if not argv[1:]` would also work
        print("Please provide your name as a command line argument.")
    else:
        full_name = " ".join(argv[1:]) #? the `" ".` confuses me and also I've never used `join()` before
        print(f"Hello, my name is {full_name}.")
    """

# Seperate the logic to check for errors and print the greeting so that the "main logic" is not buried in the try-except block.
def v3():
    from sys import argv
    from sys import exit

    # Check for errors in command line arguments
    if len(argv) < 2:
        exit("No arguments provided. Please provide your first name.")
    elif len(argv) > 2:
        exit("Too many arguments provided. Please provide only your first name.")

    # Print the greeting with first and last name.
    print(f"Hello, my name is {argv[1]}.")

main()