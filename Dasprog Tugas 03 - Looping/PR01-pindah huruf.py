kata = input()
angka = int(input())

for i in range(angka):
    kata = kata[1:] + kata[0]
    print(kata)
