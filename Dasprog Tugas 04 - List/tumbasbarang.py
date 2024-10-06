n, m = map(int,input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))
min_p = min(p)
max_p = max(p)
min_c = min(c)
max_c = max(c)

if(min_p > 0 and max_p > 0 and min_c > 0 and max_c > 0 ):
    hutang = min_c - sum(p)

elif(min_p < 0 and max_p < 0 and min_c < 0 and max_c < 0 ):
    hutang = sum(c) - max(p)

elif(min_p < 0 and max_p < 0 and min_c > 0 and max_c > 0 ):
    hutang = 0
    
else:
    belanja = 0
    bayar = 0
    for ambil_p in p:
        if(ambil_p > 0):
            belanja += ambil_p
    for ambil_c in c:
        if(ambil_c < 0):
            bayar += ambil_c
    hutang = bayar - belanja

print(hutang)
    