def my_name(nama):
    print("Hello my name is", nama)
my_name("Fazle Mawla Wahyuhanda")

def jumlah_kuadrat(a, b):
    hasil = (a+b) ** (a-b)
    return hasil
print(jumlah_kuadrat(2, 3))
print("Hasilnya adalah " + str(jumlah_kuadrat(4, 2)))

def hari(*harinya):
  print("Hari ini adalah hari " + harinya[2])

hari("senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu")

def hari_bulan(**tanggalnya):
    print("Tanggal", tanggalnya["tanggal"], "Bulan", tanggalnya["bulan"])
hari_bulan(tanggal=12, bulan="Desember")

def negaraku(**negara):
    print("Negaraku adalah ", negara["negara"], "dengan ibukota", negara["ibukota"])
negaraku(negara="Indonesia", ibukota="IKN")

fruits = ["apel", "pisang", "anggur", "jeruk"]
def my_function(fruits):
    for x in fruits:
        print(x)
my_function(fruits)

def my_function(x):
  return 10 + x

for i in range(0, 5):
    print(my_function(i))

def my_function(a, b, /, *, c, d):
    print(int((a ** b + c) / d))

my_function(10, 2, c = 4, d = 4)

def cobarekursi(k):
    if(k > 0):
        result = k + cobarekursi(k - 1) - cobarekursi(k - 2)
        print(result)
    else:
        result = 0
    return result

print("Hasil Rekursi")
cobarekursi(5)