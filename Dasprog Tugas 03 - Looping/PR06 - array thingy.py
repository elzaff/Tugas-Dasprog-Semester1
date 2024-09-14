n = int(input())

array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))

array1 = array1[:n]
array2 = array2[:n]

tof = []

m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    x = sum(array1[a:b+1])
    y = sum(array2[a:b+1])
    if x == y:
        tof.append(1)
    else:
        tof.append(0)

for i in range(len(tof)):
    if tof[i] == 1:
        print("YA")
    else:
        print("TIDAK")