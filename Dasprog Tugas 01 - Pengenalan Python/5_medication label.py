vbti = int(input("Masukkan kuantitas cairan: "))
menit = int(input("Masukkan menit penginfusan: "))

print("VBTI = ", vbti, "mL")

rate = vbti / menit * 60

print("Rate infus = ", rate, "mL")
