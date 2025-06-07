# https://youtu.be/nLRL_NcnK-4?t=25229

def main():
    v3()

# This implementation doesn't save the locations to a file. Once the program ends, the locations will be lost.
def v1():
    locations = []

    for _ in range(3):
        location = input("Enter a location: ")
        locations.append(location)
    print("Locations entered:", locations)

    sorted_locations = sorted(locations)
    print("Sorted locations:", sorted_locations)

# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# This implementation saves the locations to a file called `locations.txt`.
def v2():
    location = input("Enter a location: ")
    
    # "w" mode opens the file for writing, overwriting any existing content. If the file doesn't exist, it will be created.
    # "a" mode would append to the file instead. If the file doesn't exist, it will be created.
    # "r" mode would open the file for reading, and raise an error if the file doesn't exist.
    file = open("locations.txt", "a") 
    file.write(location + "\n")
    file.close() # you need to close the file after writing to it to ensure that all data is saved properly.

    file = open("locations.txt", "r")
    locations = file.readlines() # read() will read the entire file as a single string, while readlines() reads the file line by line into a list.
    file.close() # you need to close the file after reading it to free up system resources.

    print("Locations in `locations.txt`: ", end="")
    for location in locations:
        print(location.strip(), end="") # strip() removes any leading or trailing whitespace, *including newlines*.
        
        if location != locations[-1]: # if it's not the last location in locations, print a comma for better formatting
            print(", ", end="")
    print()  # Print a newline for better formatting

# Pyhtonic convention is to use the `with` statement when working with files. This ensures that the file is properly closed after its suite finishes, even if an error is raised.
def v3():
    location = input("Enter a location: ")

    # you don't need to explicitly close the file when using `with`, it will automatically close the file when the block is exited.
    with open("locations.txt", "a") as file:  # Using `with` statement to handle file operations automatically
        file.write(location + "\n")

    locations = []
    with open("locations.txt") as file: # You don't need to specify the mode when opening a file for reading, as "r" is the default mode. 
        for line in file:
            locations.append(line.strip()) # this is appending to the list `locations`, not the file.
    
    locations.sort()  # Sort the locations in place

    print("Sorted locations in `locations.txt`: ", end="")
    for location in locations:
        if location != locations[-1]:
            print(location, end=", ")
        else:
            print(location, end="")
    print()

# --- main() function --- #
main()