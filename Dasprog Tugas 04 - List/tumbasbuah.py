n, k = map(int, input().split())
harga = list(map(int, input().split()))
jenis = []

for i in range(n):
    if harga[i] <= k:
        jenis.append(i + 1)

bisa = len(jenis)
if bisa > 0:
    buah_jenis = ', '.join([f'jenis ke-{j}' for j in jenis[:-1]]) + f', dan jenis ke-{jenis[-1]}'
    print(f"Dengan uang {k} ia bisa membeli dengan kemungkinan {bisa} jenis buah yaitu buah {buah_jenis}")
else:
    print("uange ndak cukup, mulih sek")