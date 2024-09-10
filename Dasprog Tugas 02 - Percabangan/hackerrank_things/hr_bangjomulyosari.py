#input mobil depan, belakan, dan waktu
M, N, T = map(int, input().split())

total_mobil = M + N + 1

#waktu bangjo
red = 20
yellow = 5
green = 60
satuperiode = red + yellow + green

mobil_persiklus = green // 5

#siklus dan sisa waktu
siklus = T // satuperiode
sisawaktu = T % satuperiode

mobillewat = mobil_persiklus * siklus

if sisawaktu > red + yellow:
    sisahijau = sisawaktu - (red + yellow)
    mobillewat += sisahijau // 5

mobillewat = min(mobillewat, total_mobil)
mobilsisa = total_mobil - mobillewat

if M <= mobilsisa:
    print(f"YES! {mobilsisa}")
else:
    print(f"NO! {mobilsisa}")