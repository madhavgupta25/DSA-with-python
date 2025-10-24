def f(n:int)->list(int):
    result = []
    for i in range(n):
        result[i] = i
    
    odd_even =[]

    for i in range(n,-1,-1):
        if result[i]%2 != 0:
            result.append(result[i])
        else
            

n = int(input().strip())
f(n)