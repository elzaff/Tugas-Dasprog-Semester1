n = int(input())  
tof = []  

bilangan = []
for i in range(n):
    q = int(input())
    bilangan.append(q)

for q in bilangan:
    found = False  
    batas = int(q**0.5) + 1 #batas karena akar kuadrat tidak akan lebih dari q 
    for x in range(batas):
        for y in range(batas):
            for z in range(batas):
                for w in range(batas):
                    if x**2 + y**2 + z**2 + w**2 == q:
                        tof.append("LEAVE")
                        found = True
                        break
                if found: break
            if found: break
        if found: break
    if not found:
        tof.append("ERASE")

for i in tof:
    print(i)


#SIMPLER VERSION
#KARENA MENURUT Lagrange's four-square theorem
#Setiap bilangan bulat positif dapat dipecah menjadi 
#jumlah dari 4 bilangan bulat positif kuadrat

# n = int(input())  
# tof = []

# for i in range(n):
#     q = int(input()) #MASUKKAN BILANGAN BULAT
#     if q >= 0: #SETIAP BILANGAN POSITIF DAPAT DIBENTUK DARI 
#         tof.append("LEAVE") # PENJUMLAHAN 4 BILANGAN BULAT KUADRAT
#     else:
#         tof.append("ERASE") #JADI HANYA BILANGAN NEGATIF YANG
#                             #TIDAK BISA
# for i in tof:
#     print(i)