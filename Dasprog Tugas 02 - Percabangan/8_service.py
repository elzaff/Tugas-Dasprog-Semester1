mobil = int(input("Masukkan berapa banyak mobil = "))

print("(1) First Free Service")
print("(2) Second Free Service")

jenis_servis = list(map(int, input(f"Masukkan jenis servis sesuai jumlah mobil = ").split()))
miles = list(map(int, input(f"Masukkan miles tiap mobil = ").split()))

for i in range(mobil):
    if jenis_servis[i] == 1:
        if 1500 < miles[i] <= 3000:
            print("Vehicle must be serviced")
        else:
            print("First Free Service are not available")   
    elif jenis_servis[i] == 2:
        if 3001 < miles[i] <= 4500:
            print("Vehicle must be serviced")
        else:
            print("Second Free Service are not available")