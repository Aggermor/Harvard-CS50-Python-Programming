def main():
    version_4()

def version_1():
    for i in [0, 1, 5]:
        print("woof")

def version_2():
    for i in range(3):
        print("woof")

def version_3():
    for _ in range(3):
        # Pythonic convention
        # Using underscore to indicate that the loop variable is not used
        print("woof")

def version_4():
    print("woof\n" * 3, end='')

main()