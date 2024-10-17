t = int(input())   

for _ in range(t):
    n, k = map(int, input().split())  
    a = list(map(int, input().split()))
    c = int(input())  
    
    if c == 1:  
        maks = min(a)
        for i in range(n):
            res = 0
            x = min(i+k, n)
            for j in range(i, x): 
                res += a[j]
                maks = max(maks, res)
        print(maks)
        
    elif c == 2: 
        mins = max(a)
        for i in range(n):
            res = 0
            x = min(i+k, n)
            for j in range(i, x):  
                res += a[j]
                mins = min(mins, res)
        print(mins)