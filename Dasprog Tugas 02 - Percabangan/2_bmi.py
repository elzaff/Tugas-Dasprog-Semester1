jenisberat = input("Apa jenis beratnya (kg/pounds): ").lower().strip()  
jenistinggi = input("Apa jenis tingginya (cm/inch): ").lower().strip()

berat = float(input("Masukkan berat badan: "))
tinggi = float(input("Masukkan tinggi badan: "))

if jenisberat == "kg":
    berat = berat * 2.20462
if jenistinggi == "cm":
    tinggi = tinggi * 0.393701

bmi = berat * 703 / (tinggi * tinggi) 

if bmi < 18.5:
    status = "Underweight"
elif bmi < 25:
    status = "Normal"
elif bmi < 30:
    status = "Overweight"
else:
    status = "Obese"

print(f"BMI Anda: {bmi:.2f}, dengan status: {status}")