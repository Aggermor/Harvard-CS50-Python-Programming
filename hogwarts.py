def main():
    version_3()

# This will get long quickly...
students = {"Hermione": "Gryffindor", "Harry": "Gryffindor", "Ron": "Gryffindor"}

# You can create dictionaries on many lines for readability.
# Keys on the left, Values on the right.
students = {
    # "Key": "Value",
    "Hermione": "Gryffindor", 
    "Harry": "Gryffindor", 
    "Ron": "Gryffindor", 
    "Draco": "Slytherin"
}

def version_1():
    print (students["Hermione"])
    print (students["Harry"])
    print (students["Ron"])
    print (students["Draco"])

def version_2():
    for student in students:
        print(student, students[student], sep=", ")

def version_3():
    students = [
        {"name": "Hermione",    "house": "Gryffindor",      "petronus": "Otter"},
        {"name": "Harry",       "house": "Gryffindor",      "petronus": "Stag"},
        {"name": "Ron",         "house": "Gryffindor",      "petronus": "Jack Russel Terrier"},
        {"name": "Draco",       "house": "Slytherin",       "petronus": None}
        # `None` is a special keyword in Python to represent no value. 
        # `None` indicates that this is not an error, it's intended.
    ]

    for student in students:
        print(student["name"], student["house"], student["petronus"], sep=", ")

main()