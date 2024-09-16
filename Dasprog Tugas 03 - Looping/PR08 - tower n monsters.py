lantai, energi_awal, kasus = map(int, input().split())
monster = list(map(int, input().split()))
energi = 0

for i in range(kasus):
    a, b= map(int, input().split())
    energi += sum(monster[a-1:b-1])

sisa = energi_awal - energi
if sisa >= 0:
    print(f"EZ banget, energiku sisa {sisa}!")
else:
    print(f"NT, kurang {abs(sisa)} energi sih")
