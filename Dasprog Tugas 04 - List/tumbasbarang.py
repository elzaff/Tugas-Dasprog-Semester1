n, m = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))

p_pos = [harga for harga in p if harga > 0]
p_neg = [harga for harga in p if harga < 0]

c_pos = [uang for uang in c if uang > 0]
c_neg = [uang for uang in c if uang < 0]

if p_pos and c_neg:
    hutang_skenario1 = sum(c_neg) - sum(p_pos)
else:
    hutang_skenario1 = 0  

if p_neg and c_pos:
    hutang_skenario2 = sum(p_neg) - sum(c_pos)
else:
    hutang_skenario2 = 0  

hutang_terbesar = min(hutang_skenario1, hutang_skenario2)

print(hutang_terbesar)