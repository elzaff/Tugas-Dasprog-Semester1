data_used = float(input("Masukkan Penggunaan Data di Gbs: "))

if data_used < 0:
    charge = "Bad Data"
else:
    if data_used <= 1.0:
        charge = 250
    elif data_used <= 2.0:
        charge = 500
    elif data_used <= 5.0:
        charge = 1000
    elif data_used <= 10.0:
        charge = 1500
    elif data_used > 10.0:
        charge = 2000

if charge == "Bad Data":
    print("Bad Data")
else:
    print(f"Total biayanya adalah: {charge}")
