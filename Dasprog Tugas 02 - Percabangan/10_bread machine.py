bread_type = input("Masukkan jenis roti (W untuk White, S untuk Sweet): ").strip().upper()
double_loaf = input("Apakah ukuran roti double? (yes/no): ").strip().lower()
manual_bake = input("Apakah baking manual? (yes/no): ").strip().lower()

if bread_type == 'W':
    knead_time1 = 15
    rise_time1 = 60
    knead_time2 = 18
    rise_time2 = 20
    shaping_time = 2 / 60  # 2 detik dalam menit
    final_rise_time = 75
    bake_time = 45
    cooling_time = 30
elif bread_type == 'S':
    knead_time1 = 20
    rise_time1 = 60
    knead_time2 = 33
    rise_time2 = 30
    shaping_time = 2 / 60  # 2 detik dalam menit
    final_rise_time = 75
    bake_time = 35
    cooling_time = 30
else:
    print("Jenis roti tidak valid. Gunakan 'W' untuk White atau 'S' untuk Sweet.")
    exit()


if double_loaf == 'yes':
    bake_time = int(bake_time * 1.5)

if manual_bake == 'no':
    bake_time = bake_time
else:
    bake_time = 0


print(f"\nInstruksi untuk roti jenis {'White' if bread_type == 'W' else 'Sweet'}:")
print(f"1. Knead pertama: {knead_time1} menit")
print(f"2. Rising pertama: {rise_time1} menit")
print(f"3. Knead kedua: {knead_time2} menit")
print(f"4. Rising kedua: {rise_time2} menit")
print(f"5. Loaf shaping: {shaping_time:.2f} menit")
print(f"6. Final rising: {final_rise_time} menit")

if manual_bake == 'yes':
    print("7. Baking manual: Stop setelah loaf-shaping cycle. Keluarkan adonan untuk baking manual.")
else:
    print(f"7. Baking: {bake_time} menit")

print(f"8. Cooling: {cooling_time} menit")


total_time = (knead_time1 + rise_time1 + knead_time2 + rise_time2 + shaping_time +
              final_rise_time + bake_time + cooling_time)

print(f"Total waktu yang dibutuhkan: {total_time:.2f} menit")
