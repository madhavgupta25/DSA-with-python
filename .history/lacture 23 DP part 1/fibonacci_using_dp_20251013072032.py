def f(n:int)->int:
    a = f(n-1)
    b = f(n-2)
    return a+b

n = int(input().strip())
print(f(n))