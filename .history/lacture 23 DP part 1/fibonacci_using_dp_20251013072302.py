def f(n:int)->int:
    
    if n == 0 or n == 1:
        return n
    
    a = f(n-1)
    b = f(n-2)
    return a+b

n = int(input().strip())
print(f(n))