#input dalam km/jam
kec_takeoff = int(input("Masukkan kecepatan jet takeoff: "))
jarak = int(input("Masukkan jarak takeoff: "))

#convert dari km/jam ke m/s
kec_takeoff = round(kec_takeoff * 1000 / 3600, 2)
#rumus akselerasi a=v^2/2s
akselerasi = round(kec_takeoff**2 / (2 * jarak), 2)
waktu = round(kec_takeoff / akselerasi, 2)

print("Kecepatan jet takeoff adalah", kec_takeoff, "m/s")
print("Akselerasi jet takeoff adalah", akselerasi, "m/s^2")
print("Waktu yang dibutuhkan jet takeoff adalah", waktu, "detik")