# Input waktu streaming di GMT+2 (jam, menit, detik)
HH, MM, SS = map(int, input("Input waktu streaming dengan format jam:menit:detik = ").split(':'))

# Input waktu saat ini di GMT+7 (jam, menit, detik)
CH, CM, CS = map(int, input("Input waktu sekarang dengan format jam:menit:detik = ").split(':'))

# ubah waktu stream ke GMT+7
HH = HH + 5

# konversi waktu streaming dan waktu saat ini ke detik
waktustream = HH * 3600 + MM * 60 + SS
waktuskrg = CH * 3600 + CM * 60 + CS

# perbedaan waktu
beda = waktustream - waktuskrg

# kalo negatif, udah kelewatan
if beda <= 0:
    print("See you on the next Pear Event!")
else:
    # Menghitung sisa jam, menit, detik
    jam = beda // 3600
    beda %= 3600
    menit = beda // 60
    detik = beda % 60

    print(f"{jam:02}:{menit:02}:{detik:02}")
