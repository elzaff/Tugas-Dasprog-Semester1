n = int(input())
baris = list(map(int, input().split()))

hasil = 1
for i in range(n):
    for j in range(i + 1, n):
        hasil *= baris[i] ^ baris[j]
        print(hasil)
        if hasil == 0:
            print(0)
            exit()

print(hasil)
