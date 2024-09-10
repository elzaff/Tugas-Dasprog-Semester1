boros = 15 #liter
hemat = 2 #liter
avgflush = 14 #kali per hari
orgtoilet = 3 #per toilet
biaya = 150

warga  = int(input("Masukkan jumlah warga: "))

totalbiaya = warga / orgtoilet * biaya
efisiensi = (warga / orgtoilet * avgflush * boros) - (warga / orgtoilet * avgflush * hemat)

print("Dengan menggunakan toilet yang baru, bisa menghemat", efisiensi, "liter per hari")   
print("Dengan total biaya pemasangan toilet baru sebesar", totalbiaya)