m = int(input("Masukkan value dari m: "))
n = int(input("Masukkan value dari n: "))

#mencari sisi 1
sisi1 = abs(m**2 - n**2)
#mencari sisi 2
sisi2 = 2 * m * n
#mencari sisi 3
sisi3 = m**2 + n**2

print("Triple Pythagoras dari value di atas adalah", sisi1, sisi2, sisi3)