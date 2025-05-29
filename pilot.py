def main():
    version_1()

def version_1():
    while True:
        n = int(input("Enter a the pilot's altitude: "))
        if n > 0:
            print("The pilot is flying.")
            continue
        else:
            print("The pilot should not be flying.")
            break

# https://youtu.be/nLRL_NcnK-4?t=11758

main()