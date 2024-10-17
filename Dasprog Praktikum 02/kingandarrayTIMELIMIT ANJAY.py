t = int(input())   

for _ in range(t):
    n, k = map(int, input().split())  
    a = list(map(int, input().split()))
    c = int(input())  
    res = []
    
    if c == 1:  
        for i in range(n):
            x = min(i+k, n)
            for j in range(i, x): 
                res.append(sum(a[i:j+1]))
        print(max(res))

    elif c ==2:  
        for i in range(n):
            x = min(i+k, n)
            for j in range(i, x): 
                res.append(sum(a[i:j+1]))
        print(min(res))
        