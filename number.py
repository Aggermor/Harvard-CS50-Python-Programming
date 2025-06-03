# Syntax errors such as print("hello) are on the programmer to fix at the time of coding.
# Syntax error will not fix themselves.
# Runtime errors have a chance to be *caught* and handled before the program breaks.
# Programmers must predict how users might break the code.
# Write code with *error handling* in mind.

# How can you know what error might occure in future?
# --> sometimes documentation of a function might suggest what could go wrong.

def main():
    version_2()

def version_1():
    usr_input = input("Enter an intager for x: ")   # put outside the try because we don't need to try this part.

    try:
        x = int(usr_input) #! this broke when the variable was named `input``, because input is a built-in function. Can I name varibles th same as built-in functions?
    except ValueError:
        print(f"'{input}' is not an intager!")      # cannot use {x} because it would throw an error before being assigned.
    else:
        print(f"x is {x}")

    print(f"I can still use x '{x}'")               # you can still use {x} AFTER an else error handling. NOT BEFORE.


def version_2():
    while True:                                     # This will loop until a valid integer is entered.
        usr_input = input("Enter an intager for n: ")
        
        try:
            n = int(usr_input)
        except ValueError:
            print(f"'{usr_input}' is NaN. Please enter a valid integer...")
            continue                                # continue to the next iteration of the loop
        else:
            print(f"{n} is a valid intager.")       # works here
            break                                   # break out of the loop if no error occurred        

    print(f"{n} is a valid intager.")               # works here too, after the loop has ended.

main()