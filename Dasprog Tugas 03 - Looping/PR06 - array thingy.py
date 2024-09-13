n = int(input())

array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))

array1 = array1[:n]
array2 = array2[:n]


m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    x = sum(array1[a:b+1])
    y = sum(array2[a:b+1])
    if x == y:
        print("YA")
    else:
        print("TIDAK")