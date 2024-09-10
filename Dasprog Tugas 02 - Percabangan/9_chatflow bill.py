freeminute = 600
flatrate = 3999 #dalam cent
tambahan = 0.40
tax = 0.0525

harikerja = int(input("Masukkan penggunaan di hari kerja dalam menit: "))
malam = int(input("Masukkan penggunaan di malam hari dalam menit: "))
akhirpekan = int(input("Masukkan penggunaan di akhir pekan dalam menit: "))

if harikerja > freeminute:
    ekstra = harikerja - freeminute
    biayatambahan = ekstra * tambahan
else:
    biayatambahan = 0

totalbiaya = flatrate + biayatambahan
totalmenit = harikerja + malam + akhirpekan
pajak = totalbiaya * tax

if totalmenit > 0:
    avgpermenit = totalbiaya / totalmenit
else:
    avgpermenit = 0
taxbiaya = totalbiaya + pajak

print("\nRincian tagihan: ")
print(f"Penggunaan di hari kerja: {harikerja} menit")
print(f"Penggunaan di malam hari: {malam} menit")
print(f"Penggunaan di akhir pekan: {akhirpekan} menit")
print(f"Flat rate: ${flatrate / 100:.2f}")
print(f"Biaya tambahan: ${biayatambahan / 100:.2f}")
print(f"Biaya sebelum pajak: ${totalbiaya / 100:.2f}")
print(f"Biaya per menit: ${avgpermenit / 100:.2f}")
print(f"Biaya pajak: ${pajak / 100:.2f}")
print(f"Biaya total: ${taxbiaya / 100:.2f}")