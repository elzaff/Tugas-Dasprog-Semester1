awal_odometer = (float(input("Masukkan awal odometer: ")))
akhir_odometer = (float(input("Masukkan akhir odometer: ")))
jarak = akhir_odometer - awal_odometer
jarak = round(jarak, 2)
print("Kamu sudah menempuh", jarak, "miles")
tarif = 1.5
biaya = jarak * tarif
biaya = round(biaya, 2)
print("Tarifmu adalah $", biaya)