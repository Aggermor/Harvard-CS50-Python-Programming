def main():
    x = input("Enter a number to square: ")
    print(f"{x} squared is {square(x)}")

def square(n):
    return int(n) ** 2 # `**` Exponentiation operator for powering

if __name__ == "__main__":
    # This block ensures that the main function is called only when the script is run directly.
    main()