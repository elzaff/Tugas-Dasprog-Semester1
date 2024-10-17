n, m = map(int, input().split())
peta = []

for i in range(n):
    row = list(map(int, input()))
    peta.append(row)

posisi = []
for i in range(n):
    for j in range(m):
        if peta[i][j] == 1:
            posisi.append((i,j))

korban = 0
for x, y in posisi:
    if x-1 >= 0 and y-1 >= 0 and peta[x-1][y-1] == 0:
        korban += 1
    if y-1 >= 0 and peta[x][y-1] == 0:
        korban += 1
    if x+1 < n and y-1 >= 0 and peta[x+1][y-1] == 0:
        korban += 1
    if x-1 >= 0 and peta[x-1][y] == 0:
        korban += 1
    if x+1 < n and peta[x+1][y] == 0:
        korban += 1
    if x-1 >= 0 and y+1 < m and peta[x-1][y+1] == 0:
        korban += 1
    if y+1 < m and peta[x][y+1] == 0:
        korban += 1
    if x+1 < n and y+1 < m and peta[x+1][y+1] == 0:
        korban += 1
print(korban)