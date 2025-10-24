def f(n:int)->list(int):
    result = []
    for i in range(n):
        result[i] = i
    
    odd_even =[]

    for _ in result:
        if result%2 != 0:
            result.append(result)
            

n = int(input().strip())
f(n)