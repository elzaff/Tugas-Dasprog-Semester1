total = int(input())
angka = [0] * total
hasil = []

for i in range(total):
    angka[i] = int(input())
    angka[i] = format(angka[i], '032b')
#memisah angka[i] menjadi 4 bagian 
    angka[i] = [angka[i][0:8], angka[i][8:16], angka[i][16:24], angka[i][24:32]]
#mengubah biner menjadi desimal lalu ke karakter
    for j in range(4):
        desimal = int(angka[i][j], 2)
        karakter = chr(desimal)
#menggabungkan karakter yang awalnya berupa list
        hasil.append(karakter)

#menggabungkan karakter yang sudah digabungkan
kata = ''.join(hasil)
print(kata)