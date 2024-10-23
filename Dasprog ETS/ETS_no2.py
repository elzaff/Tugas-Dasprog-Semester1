n, m = map(int, input().split())
peta = []

for i in range(n):
    row = list(map(int, input()))
    peta.append(row)

korban = 0
for i in range(n):
    for j in range(m):
        if peta[i][j] == 1:
            if i-1 >= 0 and j-1 >= 0 and peta[i-1][j-1] == 0:
                korban += 1
            if j-1 >= 0 and peta[i][j-1] == 0:
                korban += 1
            if i+1 < n and j-1 >= 0 and peta[i+1][j-1] == 0:
                korban += 1
            if i-1 >= 0 and peta[i-1][j] == 0:
                korban += 1
            if i+1 < n and peta[i+1][j] == 0:
                korban += 1
            if i-1 >= 0 and j+1 < m and peta[i-1][j+1] == 0:
                korban += 1
            if j+1 < m and peta[i][j+1] == 0:
                korban += 1
            if i+1 < n and j+1 < m and peta[i+1][j+1] == 0:
                korban += 1
print(korban)