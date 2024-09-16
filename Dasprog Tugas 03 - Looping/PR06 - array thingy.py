n = int(input())

arrayA = list(map(int, input().split()))
arrayB = list(map(int, input().split()))

arrayA = arrayA[:n]
arrayB = arrayB[:n]

tof = []

m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    x = sum(arrayA[a:b+1])
    y = sum(arrayB[a:b+1])
    if x == y:
        tof.append(1)
    else:
        tof.append(0)

for i in range(len(tof)):
    if tof[i] == 1:
        print("YA")
    else:
        print("TIDAK")