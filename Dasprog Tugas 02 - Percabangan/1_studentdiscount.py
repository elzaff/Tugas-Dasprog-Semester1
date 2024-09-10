total_belanja = float(input("Masukkan total belanja: "))
mahasiswa = input("Apakah Anda mahasiswa? (ya/tidak): ").lower().strip()  

total_diskon = total_belanja
if mahasiswa == "ya":
    diskon = total_belanja * 0.2
    total_diskon -= diskon

pajak = round(total_diskon * 0.05,2)
total_akhir = total_diskon + pajak

print(f"Total belanjaan Rp{total_belanja:.2f}")
if mahasiswa == "ya":
    print(f"Diskon mahasiswa (20%) Rp{diskon:.2f}")
print(f"Total setelah diskon Rp{total_diskon:.2f}")
print(f"Pajak (5%) Rp{pajak:.2f}")
print(f"Total keseluruhan Rp{total_akhir:.2f}")
