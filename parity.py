def main():
    version_1()

def version_1():
    x = int(input("Enter a number for x: "))

    if x % 2 == 0:
        print(f"{x} is even")
    else:
        print(f"{x} is odd")

def version_2():
    x = int(input("Enter a number for x: "))

    if x % 2 == 0:
        print(f"{x} is even")
    elif x % 2 == 1:
        print(f"{x} is odd")
    else:
        print("This should never happen, but it's here just in case.")

def version_3():
    x = int(input("Enter a number for x: "))

    if is_even1(x):
        print(f"{x} is even")
    else:
        print(f"{x} is odd")

def is_even1(x):
    if x % 2 == 0:
        return True
    else:
        return False
    
def is_even2(x):
    # This notation is called a ternary operator
    # It is a shorthand for an if-else statement
    return True if x % 2 == 0 else False

def is_even3(x):
    # Returns the result of the expression directly
    return x % 2 == 0

main()