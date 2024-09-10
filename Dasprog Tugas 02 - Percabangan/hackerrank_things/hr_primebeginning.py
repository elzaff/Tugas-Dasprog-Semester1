angka = int(input("Masukkan angka: "))

if angka < 2:
    print(angka, "bukan bilangan prima.")
else:
    prima = True
    
    for i in range(2, angka):
        if angka % i == 0:
            prima = False
            break
    
    if prima:
        print(f"{angka} adalah bilangan prima")
    else:
        print(f"{angka} bukan bilangan prima")
