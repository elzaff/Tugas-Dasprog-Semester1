n = int(input())
results = []

for _ in range(n):
    m = int(input())
    angka = list(map(int, input().split()))
    if m == 1:
        results.append('-1')
        continue
    wadah = [0]*10
    for i in angka:
        wadah[i] += 1
    jumlah_angka_terbesar_yang_muncul = max(wadah)
    simpan_modus = []
    for i in range(len(wadah)):
        if wadah[i] == max(wadah):
            simpan_modus.append(i)
    if len(simpan_modus) == 1:
        result = f"{jumlah_angka_terbesar_yang_muncul} * {simpan_modus[0]} = {simpan_modus[0] * jumlah_angka_terbesar_yang_muncul}"
        results.append(result)
    else:
        p = 1
        s = ''
        for i in range(len(simpan_modus)):
            s += str(simpan_modus[i])
            if i != len(simpan_modus)-1:
                s += ' * '
        s += ' = '
        for i in simpan_modus:
            p *= i
        result = s + str(p)
        results.append(result)

for result in results:
    print(result)