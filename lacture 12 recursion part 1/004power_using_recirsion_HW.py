def f(n:int,pow:int)->int:
    # base case
    if pow == 0:
        return 1
    
    # recursion case:
    a = f(n,pow-1)
    return n*a
    
        
n , pow = map(int, input().split())
print(f(n,pow))