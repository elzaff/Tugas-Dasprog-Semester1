N, C = map(int, input().split())

if N % 4 == 0:
    if C == 1:
      winner = 2
    else: 
        winner = 1
else:
    winner = C

if winner == 1:
    print("Lala")
else:
    print("Lili")
