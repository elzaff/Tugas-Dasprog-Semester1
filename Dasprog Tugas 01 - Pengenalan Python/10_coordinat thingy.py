x1 = float(input("Masukkan x1: "))
y1 = float(input("Masukkan y1: "))
x2 = float(input("Masukkan x2: "))
y2 = float(input("Masukkan y2: "))

gradien = (y2 - y1) / (x2 - x1) #rumus gradien
xtengah = (x1 + x2) / 2 #rumus titik tengah x
ytengah = (y1 + y2) / 2 #rumus titik tengah y
gradien_tegaklurus = -1 / gradien #rumus gradien tegak lurus
#y = mx + b #rumus persamaan garis lurus
b = ytengah - gradien_tegaklurus * xtengah #rumus perpotongan dg garis y

print("Titik 1: (", x1, ",", y1, ")")
print("Titik 2: (", x2, ",", y2, ")")
print("Persamaan garis tegak lurus adalah y = ", gradien_tegaklurus, "x +", b)