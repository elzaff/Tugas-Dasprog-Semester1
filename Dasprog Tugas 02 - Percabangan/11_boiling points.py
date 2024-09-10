boiling_point = float(input("Masukkan titik didih yang diamati dalam °C: "))

water = 100
mercury = 357
copper = 1187
silver = 2193
gold = 2660


tolerance = 0.05

if water * (1 - tolerance) <= boiling_point <= water * (1 + tolerance):
    print("Substansi adalah Air")
elif mercury * (1 - tolerance) <= boiling_point <= mercury * (1 + tolerance):
    print("Substansi adalah Merkuri")
elif copper * (1 - tolerance) <= boiling_point <= copper * (1 + tolerance):
    print("Substansi adalah Tembaga")
elif silver * (1 - tolerance) <= boiling_point <= silver * (1 + tolerance):
    print("Substansi adalah Perak")
elif gold * (1 - tolerance) <= boiling_point <= gold * (1 + tolerance):
    print("Substansi adalah Emas")
else:
    print("Substansi tidak diketahui")
