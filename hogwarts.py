def main():
    version_3()

def version_1(): 
    students = ["Hermione", "Harry", "Ron"]

    # Pyhton lists are 0 indexed.
    print(students)

def version_2():
    students = ["Hermione", "Harry", "Ron"]

    # Access elements in a list.
    print(students[0])
    print(students[1])
    print(students[2])

def version_3():    
    students = ["Hermione", "Harry", "Ron"]

    # Print all students in a list
    for student in students:
        print(student)

    total_students = len(students)
    for i in range(total_students):
        print(i + 1, students[i])


main()