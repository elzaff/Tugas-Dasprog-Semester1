print("Masukkan sejak kapan freezer mati")
jam = int(input("Jam: "))
menit = int(input("Menit: "))
convert_jam = jam + (menit / 60)
T = 4 * convert_jam ** 2 / (convert_jam + 2) - 20

print("Estimasi suhu freezer adalah", T, "derajat Celcius")