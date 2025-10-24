def f(n:int)->int:
    # base case
    if n == 0 or n == 1:
        return n
    
    #recursive case
    a = f(n-1)
    b = f(n-2)
    return a+b

def f_topdown(n:int,dp:list[int])->int:
    # base case
    if n == 0 or n == 1:
        dp[n] = n
        return n
    
    #recursive case
    a = f_topdown(n-1)
    b = f_topdown(n-2)
    dp[n] = a+b
    return dp[n]

n = int(input().strip())
print(f(n))

dp = [-1]*(n+1)
print(f_topdown(n,dp))