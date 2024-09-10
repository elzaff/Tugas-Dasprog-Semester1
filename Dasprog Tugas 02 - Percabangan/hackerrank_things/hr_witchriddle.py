#input jumlah kucing
a = list(map(int, input().split()))

#jumlah kucing lompat ke depan
b = int(input())

#jumlah perulangan kucing melompat
c = int(input())

#indeks untuk pengeluaran
d, e, f = map(int, input().split())

# Lakukan rotasi sebanyak 'c' kali
for i in range(c):
    a = a[-b:] + a[:-b]

# Keluaran angka pada indeks d, e, f
print(a[d], a[e], a[f])
