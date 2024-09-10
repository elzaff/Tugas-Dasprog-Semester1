month = int(input("Masukkan bulan (1-12): "))
day = int(input("Masukkan hari (1-31): "))
year = int(input("Masukkan tahun: "))


if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    kabisat = True
else:
    kabisat = False


days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


if kabisat:
    days_in_month[1] = 29


if not (1 <= month <= 12):
    print("Bulan tidak valid")
elif not (1 <= day <= days_in_month[month - 1]):
    print("Hari tidak valid untuk bulan tersebut.")
else:
    day_number = sum(days_in_month[:month - 1]) + day
    print(f"Tanggal {month}/{day}/{year} adalah hari ke-{day_number} dalam tahun {year}.")
