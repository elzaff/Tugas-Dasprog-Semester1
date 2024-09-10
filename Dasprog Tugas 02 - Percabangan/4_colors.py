color = input("Enter the first letter of the cylinder's color = ").lower().strip()

if color == "y":
    print("Contents: Hydrogen")
elif color == "o":
    print("Contents: Ammonia")
elif color == "b":
    print("Contents: Carbon Monoxide")
elif color == "g":
    print("Contents: Oxygen")
else:
    print("Contents unknown")