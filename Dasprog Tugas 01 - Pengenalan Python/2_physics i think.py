height = int(input("Masukkan tinggi bendungan: "))  
density_air = 1000
flow = 1.3 * 10**3
massa = density_air * flow
print("Massa air per detik adalah", massa, "kg per detik")
g = 9.8
potensial = massa * g * height
print("Energi potensial adalah", potensial, "Joule")
efisiensi = 0.9 * potensial
megawatt = efisiensi / 10**6

print("90% dari energi potensial air di bendungan adalah", megawatt, "megawatt")