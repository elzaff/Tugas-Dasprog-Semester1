#input dalam km/jam
kec_takeoff = int(input("Masukkan kecepatan jet takeoff: "))
jarak = int(input("Masukkan jarak takeoff: "))

#convert dari km/jam ke m/s
kec_takeoff = kec_takeoff * 1000 / 3600
#rumus akselerasi a=v^2/2s
akselerasi = kec_takeoff**2 / (2 * jarak)
waktu = kec_takeoff / akselerasi

print("Kecepatan jet takeoff adalah", kec_takeoff, "m/s")
print("Akselerasi jet takeoff adalah", akselerasi, "m/s^2")
print("Waktu yang dibutuhkan jet takeoff adalah", waktu, "detik")