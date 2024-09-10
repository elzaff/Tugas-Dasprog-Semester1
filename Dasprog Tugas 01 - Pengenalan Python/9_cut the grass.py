p_halaman = (float(input("Masukkan panjang halaman: ")))
l_halaman = (float(input("Masukkan lebar halaman: ")))
p_rumah = (float(input("Masukkan panjang rumah: ")))
l_rumah = (float(input("Masukkan lebar rumah: ")))

luas_halaman = p_halaman * l_halaman
luas_rumah = p_rumah * l_rumah

luas_sisa = luas_halaman - luas_rumah
rate = 2
ratem = rate * 0.3048
waktu = round(luas_sisa / ratem, 2)

print("Waktu yang dibutuhkan untuk memotong rumput dengan luas", luas_sisa, " adalah", waktu, "detik")