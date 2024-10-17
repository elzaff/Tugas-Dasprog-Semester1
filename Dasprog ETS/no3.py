n = int(input())

for i in range(n+2):
    for j in range(3 + 2 * n):
        if i == 0:
            if j == 0 or j == (2 + 2 * n):
                print("+", end="")
            else:
                print("-", end="")
        if i != 0 and i != n + 1:
            if j == 0 or j == (2 + 2 * n):
                print("|", end="")
            elif j > 0 and j % 2 == 1:
                print(" ", end="")
            else:
                if i % 2 == 1:
                    if j % 4 == 0:
                        print(".", end="")
                    else:
                        print("v", end="")
                if i % 2 == 0:
                    if j % 4 == 0:
                        print("v", end="")
                    else:
                        print(".", end="")
        if i == (n + 1):
            if j == 0 or j == (2 + 2 * n):
                print("+", end="")
            else:
                print("-", end="")
    print()