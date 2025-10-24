def f(n:int)->list(int):
    result = []
    for i in range(n):
        result[i] = i
    
    odd =[]

    for i in range(n,-1,-1):
        if result[i]%2 != 0:
            odd.append(result[i])
        else:
            even.appen
            

n = int(input().strip())
f(n)