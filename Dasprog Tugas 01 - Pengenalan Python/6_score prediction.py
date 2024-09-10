grade = input("Masukkan nilai yang dimau: ")
min = float(input("Rata-rata minimum yang dibutuhkan: "))
avg = float(input("Rata-rata yang dimiliki sekarang: "))
percentage = float(input("Berapa persentase Final Exam: "))

butuhskor = (min - avg * (100 - percentage) / 100) * 100 / 25
butuhskor = round(butuhskor, 2)

print("Kamu butuh skor", butuhskor, "pada final exam untuk dapet", grade)

