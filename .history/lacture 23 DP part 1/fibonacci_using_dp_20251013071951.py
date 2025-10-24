def f(n:int)->int:
    a = f(n-1)

n = int(input)
print(f(n))