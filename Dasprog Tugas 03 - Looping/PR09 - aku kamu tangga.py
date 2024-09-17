N,M = input().split()
M = str(M).lower().strip()
N = int(N)

if M == "aku" :
    for i in range(1, N + 1):
       if i % 2 == 1:
           print("I U " * (i // 2) + "I")
       else:
           print("U I " * (i // 2)) 

if M == "kamu" :
    for i in range(1, N + 1):
        if i % 2 == 1:
           print("  " * (N - i) + "I U " * (i // 2) + "I")
        else:
           print("  " * (N - i) + "I U " * (i // 2))