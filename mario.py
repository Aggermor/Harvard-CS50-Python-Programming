def main():
    print_square3(3)

# --- Version 1 --- #
def version_1():
    def print_column(height):
        for _ in range(height):
            print("#")

# --- Draw Screen --- #
def print_column(height):
        print("#\n" * height, end="")

def print_row(width):
    print("?" * width)

# --- Versions of `print_square()` --- #
def print_square(size):
    for i in range(size):               # outer loop: to start a new row
        for j in range(size):           # inner loop: to draw the row
            print("#", end="")          
        print("")                       # prints a new line at the end of each inner loop.

def print_square2(size):
    for i in range(size):
        print("#" * size)          

def print_square3(size):
    for i in range(size):
        print_row(size)                 # abstract the code so that it's easier to maintin and read.

# --- MAIN --- #
main()