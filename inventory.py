# Saw this in a youtube short
# all() returns True if *all* elements are truthy
# any() returns True if *any* element is truthy

inventory = ["Sword", None, None]

if all(inventory):
    print("You have everything in your inventory!")
elif any(inventory):
    print("You have something in your inventory!")
else:
    print("You have nothing in your inventory!")
