n, r, c = map(int, input().split())
posisi_chingu = []

for _ in range(n): 
    x, a, b = map(int, input().split())
    posisi_chingu.append((x, a, b))

for i in range(1, n + 1):  
    ada = False
    for chingu, a, b in posisi_chingu:  
        if chingu == i:
            for chingu_lain, a_lain, b_lain in posisi_chingu:  
                if a_lain == a and b_lain == b - 1:  
                    print(chingu_lain)
                    ada = True
                    break
                elif a_lain == a and b_lain == b + 1:  
                    print(chingu_lain)
                    ada = True
                    break
            break
    if not ada:
        print(0)
