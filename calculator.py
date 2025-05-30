# Harvard CS50 Python Programming Course 
# Lecture 0: Functions and Variables
# # This program performs basic arithmetic operations: addition, subtraction, multiplication, and division.

# Ask the user for two numbers
x = input("Enter the first number: ")
x = x.strip()   # Remove any leading or trailing whitespace
x = int(x)      # Convert the input string to an integer

y = int(input("Enter the second number: ").strip())

print(f"Addition: {x} + {y} = {x + y}")

print("\n--- Formatting Numbers [0000:,.2f] ---")
thousand = int(1000)
print(f"{thousand:,} is one thousand in comma-separated format.")
print(f"{thousand:_} is one thousand in underscore-separated format.")

pi = float(3.14159)
print(f"Pi is approximately {pi:.2f} in two decimal places.")
print(f"Pi is approximately {pi:.4f} in four decimal places.")
print(f"Pi is approximately {pi:.6f} in six decimal places.")

pi = round(pi, 2)  # Round pi to two decimal places
print(f"Rounded Pi: {pi}")  

num = 1234.5678
print(f"Formatted number: {num:,.2f}")  # Format with commas and two decimal places