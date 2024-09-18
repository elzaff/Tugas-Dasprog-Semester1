x1, y1 = map(int, input().split())  
xs, ys = map(int, input().split())
xf, yf = map(int, input().split()) 

jarak_king = ((xs - xf)**2 + (ys - yf)**2)**0.5 

jarak_lingkaran_ke_akhir = ((x1 - xf)**2 + (y1 - yf)**2)**0.5 

if int(jarak_lingkaran_ke_akhir) > int(jarak_king):
    print("Yes")
else:
    print("No")

