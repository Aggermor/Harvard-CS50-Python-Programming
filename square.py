# This script demonstrates function
# I will also use this script to demonstrate unit testing.

def main():
    x = input("Enter a number to square: ")
    print(f"{x} squared is {square(x)}")

def square(n):
    introduce_bug = True  # Set to True to introduce a bug for testing purposes

    if introduce_bug:
        return n + n
    else:
        return int(n) ** 2 # `**` Exponentiation operator for powering
    

if __name__ == "__main__":
    # This block ensures that the main function is called only when the script is run directly.
    main()