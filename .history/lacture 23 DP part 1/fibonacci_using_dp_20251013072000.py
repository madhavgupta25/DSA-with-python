def f(n:int)->int:
    a = f(n-1)
    b = f(n-2)
    

n = int(input)
print(f(n))