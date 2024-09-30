n, m = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))
pbaru = []
cbaru = []

for i in range (len(p)):
    if p[i] > 0:
        pbaru.append(p[i])
for j in range (len(p)):
    if c[j] < 0:
        cbaru.append(c[j])
        
print(sum(cbaru) - sum(pbaru))