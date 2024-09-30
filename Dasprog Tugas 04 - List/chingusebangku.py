n, r, c = map(int, input().split())
posisi_murid = {}

for _ in range(n):
    x, a, b = map(int, input().split())
    posisi_murid[(a, b)] = x

for i in range(1, n + 1):
    ada = False
    for (a, b), murid in posisi_murid.items():
        if murid == i:
            if (a, b - 1) in posisi_murid:
                print(posisi_murid[(a, b - 1)])
                ada = True
            elif (a, b + 1) in posisi_murid:
                print(posisi_murid[(a, b + 1)])
                ada = True
            break
    if not ada:
        print(0)
