def f(n:int)->int:
    # base case
    if n == 0 or n == 1:
        return n
    
    #recursive case
    a = f(n-1)
    b = f(n-2)
    return a+b

def f(n:int,)->int:
    # base case
    if n == 0 or n == 1:
        return n
    
    #recursive case
    a = f(n-1)
    b = f(n-2)
    return a+b

n = int(input().strip())
print(f(n))

dp = [-1]*(n+1)
print(f_topdown(n,dp))