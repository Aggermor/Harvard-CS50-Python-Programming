def main():
    x = input("Enter a number to square: ")
    print(f"{x} squared is {square(x)}")

def square(n):
    return int(n) ** 2 # `**` Exponentiation operator for powering

main()

# Notice we definined main() and square() functions and then called main() at the end of the script.  
# This is a common pattern in Python scripts to ensure that the code is written in a top-down manner.

def version_1():
    x = input("Enter a number to square: ")
    print("x squared is ")
    print(square(x))

def version_2():
    # I can make several iterations of my code that improve it and add complexity.
    pass

def version_3():
    pass # This is a placeholder for future parts of the program.