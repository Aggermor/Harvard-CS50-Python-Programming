def main():
    version_1()

def version_1():
    name = (input("Enter your name: "))
    if name == "Harry" or name == "Hermione" or name == "Ron":
    # if name in ["Harry", "Hermione", "Ron"]: # we havent learned about lists yet, but this is better.
        print("Gryffindor")
    elif name == "Draco":
        print("Slytherin")
    elif name == "Cedric":
        print("Hufflepuff")
    elif name == "Cho":
        print("Ravenclaw")
    else:
        print("Unknown house")

def version_2():
    name = (input("Enter your name: "))
    if name == "Harry" or "Hermione" or "Ron":
        print("Gryffindor")
    elif name == "Draco":
        print("Slytherin")
    elif name == "Cedric":
        print("Hufflepuff")
    elif name == "Cho":
        print("Ravenclaw")
    else:
        print("Unknown house")
        
def version_3():
    name = (input("Enter your name: "))
    match name:
        case "Harry" | "Hermione" | "Ron": 
            # The pipe | is used to match multiple patterns
            # This is called a match statement, introduced in Python 3.10
            # It is similar to a switch statement in other languages
            # It allows for more *complex* pattern matching
            print("Gryffindor")
        case "Draco":
            print("Slytherin")
        case "Cedric":
            print("Hufflepuff")
        case "Cho":
            print("Ravenclaw")
        case _: # The underscore _ is a wildcard that matches anything
            print("Unknown house")



main()