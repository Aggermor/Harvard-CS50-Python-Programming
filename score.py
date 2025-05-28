def main():
    version_4()

def version_1():
    score = int(input("Enter your score: "))

    # Laying the foundation of the grading system logic
    if score >= 90 and score <= 100:
        print("You got an A!")
    elif score >= 80 and score < 90:
        print("You got a B!")
    elif score >= 70 and score < 80:
        print("You got a C!")
    elif score >= 60 and score < 70:
        print("You got a D!")
    else:
        print("You got an F!")

def version_2():
    score = int(input("Enter your score: "))

    # Changing the order of conditions to improve readability
    if 90 <= score and score <= 100:
        print("You got an A!")
    elif 80 <= score and score < 90:
        print("You got a B!")
    elif 70 <= score and score < 80:
        print("You got a C!")
    elif 60 <= score and score < 70:
        print("You got a D!")
    else:
        print("You got an F!")

def version_3():
    score = int(input("Enter your score: "))
    
    # Feature of Python: Chained comparisons
    if 90 <= score <= 100:
        print("You got an A!")
    elif 80 <= score < 90:
        print("You got a B!")
    elif 70 <= score < 80:
        print("You got a C!")
    elif 60 <= score < 70:
        print("You got a D!")
    else:
        print("You got an F!")

def version_4():
    score = int(input("Enter your score: "))
    # Assumes score is always a valid integer between 0 and 100!
    
    # Using a single comparison for each grade
    if score >= 90:
        print("You got an A!")
    elif score >= 80:
        print("You got a B!")
    elif score >= 70:
        print("You got a C!")
    elif score >= 60:
        print("You got a D!")
    else:
        print("You got an F!")

main()