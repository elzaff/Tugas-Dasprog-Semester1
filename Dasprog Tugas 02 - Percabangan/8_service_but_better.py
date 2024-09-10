mobil = int(input("Masukkan berapa banyak mobil = "))

print("(1) First Free Service")
print("(2) Second Free Service")

jenis_servis = list(map(int, input(f"Masukkan jenis servis sesuai jumlah mobil (pisahkan dengan spasi) = ").split()))
miles = list(map(int, input(f"Masukkan miles tiap mobil (pisahkan dengan spasi) = ").split()))

if len(jenis_servis) != mobil or len(miles) != mobil:
    print("Jumlah input jenis servis atau miles tidak sesuai dengan jumlah mobil.")
else:
    for i in range(mobil):
        if jenis_servis[i] == 1:
            if 1500 < miles[i] <= 3000:
                print(f"Mobil {i+1}: Vehicle must be serviced")
            else:
                print(f"Mobil {i+1}: First Free Service are not available")   
        elif jenis_servis[i] == 2:
            if 3000 < miles[i] <= 4500:  # Rentang diperbaiki
                print(f"Mobil {i+1}: Vehicle must be serviced")
            else:
                print(f"Mobil {i+1}: Second Free Service are not available")
        else:
            print(f"Mobil {i+1}: Jenis servis tidak valid")
