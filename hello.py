# Harvard CS50 Python Programming Course 
# Lecture 0: Functions and Variables
# This program asks the user for their name and greets them.

# Ask the user for their name
name = input("What's your name? ").strip().title()

# string methods that can be used on the `name` variable:
# strip()           # Remove any leading or trailing whitespace
# lower()           # Convert the name to lowercase
# upper()           # Convert the name to UPPERCASE
# title()           # Convert the name to Title Case
# capitalize()      # Capitalize the first letter of the name
# len()             # Get the length of the name

# Say hello to the user
print("Hello, " + name + "!")

# Improved using f-string for better readability
print(f"Hello, {name}!")