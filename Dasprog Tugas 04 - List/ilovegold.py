r, c, m = map(int, input().split())
peta = []
posisi = [0, 0]

for i in range(r):
    peta.append(list(map(int, input().split())))
    
    if len(peta[i]) != c:
        print("Panjang baris tidak valid")
        exit()

gerak = input()
if len(gerak) != m:
    print("gerakanmu salah bung!")
    exit()

emas = peta[posisi[0]][posisi[1]]

for g in gerak:
    if g == 'U':
        emas += 3
        posisi[0] -= 1
    elif g == 'D':
        emas -= 2
        posisi[0] += 1
    elif g == 'L':
        emas -= 2
        posisi[1] -= 1
    elif g == 'R':
        emas += 3
        posisi[1] += 1
    if posisi[0] < 0 or posisi[0] >= r or posisi[0] < 0 or posisi[0] >= c:
        print("Gerakan keluar peta, tidak valid")
        exit()
    emas += peta[posisi[0]][posisi[1]]
print(f"total emas yang didapat adalah {emas}")

