r, c, m = map(int, input().split())
peta = []
posisi = [0, 0]

for i in range(r):
    peta.append(list(map(int, input().split())))
    
    if len(peta[i]) != c:
        print("Panjang baris tidak valid")
        exit()

gerak = input()

emas = peta[posisi[0]][posisi[1]]

for g in gerak:
    if g == 'U' and posisi[0] > 0:
        emas += 3
        posisi[0] -= 1
    elif g == 'D' and posisi[0] < r - 1:
        emas -= 2
        posisi[0] += 1
    elif g == 'L' and posisi[1] > 0:
        emas -= 2
        posisi[1] -= 1
    elif g == 'R' and posisi[1] < c - 1:
        emas += 3
        posisi[1] += 1
    else:
        break
    
    emas += peta[posisi[0]][posisi[1]]
    

print(emas)   
if len(gerak) != m:
    print("gerakanmu salah bung!")
    exit()

