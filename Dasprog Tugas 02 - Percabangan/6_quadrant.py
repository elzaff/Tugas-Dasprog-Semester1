
x, y = input("Masukkan koordinat x dan y (pisahkan dengan spasi): ").split()


x = float(x)
y = float(y)


if x == 0 and y == 0:
    print("Titik berada di titik pusat")
elif x == 0:
    print("Titik berada di sumbu y")
elif y == 0:
    print("Titik berada di sumbu x")
else:
    if x > 0 and y > 0:
        print(f"({x}, {y}) Titik berada di kuadran I")
    elif x < 0 and y > 0:
        print(f"({x}, {y}) Titik berada di kuadran II")
    elif x < 0 and y < 0:
        print(f"({x}, {y}) Titik berada di kuadran III")
    elif x > 0 and y < 0:
        print(f"({x}, {y}) Titik berada di kuadran IV")
