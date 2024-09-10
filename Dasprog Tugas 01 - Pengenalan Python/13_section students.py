murid = int(input("Masukkan jumlah murid: "))
batch = 30
section = murid // batch
sisa = murid % batch

print("Jumlah murid yang terdaftar adalah", murid)
print("Jumlah section yang dibutuhkan adalah", section)
print("Jumlah murid yang tersisa adalah", sisa)