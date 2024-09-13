batu = input()
listbatu = []
hancur = 0
rugi = 0

for i in batu:
    if listbatu and listbatu[-1] == i:
        listbatu.pop()
        hancur += 1
        rugi += ord(i) * 1000 * 2 #batu
    else:
        listbatu.append(i)

sisa = len(listbatu)    
print(f"Di gudang tersisa {sisa} batu")

if hancur > 0:
    print(f"Total Kerugian : {rugi} Dolar Imbu")
else:
    print(" Wah, Jotaro Joemama tidak jadi dipecat")








