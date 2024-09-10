galon = int(input("Masukkan banyak galon minyak: "))
efisiensi = int(input("Masukkan efisiensi: "))
btu = galon / 42 * 5800000 * efisiensi / 100
print("Btu yang dihasilkan adalah", btu, "Btu")