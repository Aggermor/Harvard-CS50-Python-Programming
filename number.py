# Syntax errors such as print("hello) are on the programmer to fix at the time of coding.
# Syntax error will not fix themselves.
# Runtime errors have a chance to be *caught* and handled before the program breaks.
# Programmers must predict how users might break the code.
# Write code with *error handling* in mind.

# How can you know what error might occure in future?
# --> sometimes documentation of a function might suggest what could go wrong.


input = input("Enter an intager for x: ")

try:
    x = int(input)
except ValueError:
    print(f"'{input}' is not an intager!") # cannot use {x} because it would throw an error before being assigned.
else:
    print(f"x is {x}")

print(f"I can still use x '{x}'") # you can still use {x} AFTER an else error handling. NOT BEFORE.