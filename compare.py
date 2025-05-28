def main():
    version_1()

def version_1():
    x = int(input("Enter a number for x: "))
    y = int(input("Enter a number for y: "))

    if x > y:
        print(f"{x} is greater than {y}")
    if x < y:
        print(f"{x} is less than {y}")
    if x == y:
        print(f"{x} is equal to {y}")

def version_2():
    # elif to reduce unnecessary checks
    x = int(input("Enter a number for x: "))
    y = int(input("Enter a number for y: "))

    if x > y:
        print(f"{x} is greater than {y}")
    elif x < y:
        print(f"{x} is less than {y}")
    elif x == y:
        print(f"{x} is equal to {y}")

def version_3():
    # else is a catch-all, but logically, x == y is the only case left over.
    x = int(input("Enter a number for x: "))
    y = int(input("Enter a number for y: "))

    if x > y:
        print(f"{x} is greater than {y}")
    elif x < y:
        print(f"{x} is less than {y}")
    else: # x == y is the only case left over, so no need to check.
        print(f"{x} is equal to {y}")

def version_4():
    # or 
    x = int(input("Enter a number for x: "))
    y = int(input("Enter a number for y: "))

    if (x > y) or (x < y):
        print(f"{x} is not equal to {y}")
    else:
        print(f"{x} is equal to {y}")




main()